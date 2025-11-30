import json
import os

from datetime import datetime

from SRC.UTILS.Logger import Logger

class ManagerJsonService:

    def __init__(self, logger: Logger, base_dir: str | None = None) -> None:
        if not isinstance(logger, Logger): raise ValueError("logger deve ser uma instância de Logger")
        self.__log = logger
        self.__log.log_info(f"Inicializando ManagerJsonService com Logger: {logger}")
        self.__base_dir = base_dir if base_dir else os.path.join("DATABASE", "JSON")
        self.__entity_to_file = {
            "salas": os.path.join(self.__base_dir, "salas.json"),
            "agendamentos": os.path.join(self.__base_dir, "agendamentos.json"),
        }

        for path in self.__entity_to_file.values(): self.__ensure_file(path)

    #? ------------------ Métodos utilitários internos ------------------

    def __ensure_file(self, path: str) -> None:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if not os.path.exists(path) or os.path.getsize(path) == 0:
                with open(path, "w", encoding="utf-8") as f: json.dump([], f, ensure_ascii=False, indent=2)
        except Exception as e: self.__log.log_error(f"Falha ao garantir arquivo '{path}': {e}")

    def __get_file_path(self, entity: str) -> str:
        if entity not in self.__entity_to_file: raise ValueError("Entidade inválida. Use 'salas' ou 'agendamentos'.")
        return self.__entity_to_file[entity]

    def __read_all(self, entity: str) -> list[dict]:
        path = self.__get_file_path(entity)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    self.__log.log_warning(f"Conteúdo inesperado em '{path}'. Recriando como lista vazia.")
                    return []
                return data
        except json.JSONDecodeError as e:
            self.__log.log_error(f"JSON inválido em '{path}': {e}. Recriando como lista vazia.")
            try:
                with open(path, "w", encoding="utf-8") as f: json.dump([], f, ensure_ascii=False, indent=2)
            except Exception as inner: self.__log.log_error(f"Falha ao restaurar '{path}': {inner}")
            return []
        except FileNotFoundError:
            self.__log.log_warning(f"Arquivo '{path}' não encontrado. Criando novo.")
            self.__ensure_file(path)
            return []
        except Exception as e:
            self.__log.log_error(f"Erro ao ler '{path}': {e}")
            return []

    def __write_all(self, entity: str, items: list[dict]) -> bool:
        path = self.__get_file_path(entity)
        try:
            with open(path, "w", encoding="utf-8") as f: json.dump(items, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            self.__log.log_error(f"Erro ao escrever em '{path}': {e}")
            return False

    def __reindex_ids(self, entity: str, items: list[dict]) -> None:
        if entity != "agendamentos": return
        for idx, item in enumerate(items, start=1):
            item["id"] = idx

    def __generate_next_id(self, items: list[dict]) -> int:
        try:
            current_max = max((int(item.get("id", 0)) for item in items), default=0)
            return current_max + 1
        except Exception: return 1

    def __coerce_to_int(self, value, default: int | None) -> int | None:
        try:
            return int(value)
        except Exception: return default

    def __find_index_by_id(self, items: list[dict], item_id: int) -> int:
        alvo = int(item_id)
        for idx, item in enumerate(items):
            existente = self.__coerce_to_int(item.get("id"), None)
            if existente is not None and existente == alvo: return idx
        return -1

    def __normalize_if_agendamento(self, entity: str, dados: dict) -> dict:
        if entity == "agendamentos":
            if isinstance(dados.get("data_inicio"), datetime):  dados["data_inicio"] = dados["data_inicio"].isoformat()
            if isinstance(dados.get("data_fim"), datetime):     dados["data_fim"] = dados["data_fim"].isoformat()
        return dados

    #? ---------------------- API Pública ----------------------

    def listar(self, entity: str) -> list[dict]:
        data = self.__read_all(entity)
        self.__log.log_info(f"Listados {len(data)} registro(s) de '{entity}'.")
        return data

    def obter_por_id(self, entity: str, item_id: int) -> dict | None:
        items = self.__read_all(entity)
        alvo = int(item_id)
        for item in items:
            existente = self.__coerce_to_int(item.get("id"), None)
            if existente is not None and existente == alvo:
                self.__log.log_info(f"Registro '{entity}' com id={item_id} encontrado.")
                return item
        self.__log.log_warning(f"Registro '{entity}' com id={item_id} não encontrado.")
        return None

    def criar(self, entity: str, dados: dict) -> dict | None:
        items = self.__read_all(entity)
        current_id = self.__coerce_to_int(dados.get("id"), None)
        if current_id in (None, 0):                             dados["id"] = self.__generate_next_id(items)
        if entity == "agendamentos":
            if isinstance(dados.get("data_inicio"), datetime):  dados["data_inicio"] = dados["data_inicio"].isoformat()
            if isinstance(dados.get("data_fim"), datetime):     dados["data_fim"] = dados["data_fim"].isoformat()
        novo_id = self.__coerce_to_int(dados.get("id"), None)
        if novo_id is not None and any(self.__coerce_to_int(x.get("id"), None) == novo_id for x in items):
            self.__log.log_error( f"Falha ao criar em '{entity}': id={dados['id']} já existe.")
            return None
        items.append(dados)
        if self.__write_all(entity, items):
            self.__log.log_success(f"Criado registro em '{entity}' com id={dados['id']} com sucesso.")
            return dados
        self.__log.log_error(f"Falha ao salvar novo registro em '{entity}'.")
        return None

    def atualizar(self, entity: str, item_id: int, novos_dados: dict) -> dict | None:
        items = self.__read_all(entity)
        idx = self.__find_index_by_id(items, item_id)
        if idx == -1:
            self.__log.log_warning(f"Registro '{entity}' id={item_id} não encontrado para atualizar.")
            return None
        atual = {**items[idx], **novos_dados, "id": item_id}
        atual = self.__normalize_if_agendamento(entity, atual)
        items[idx] = atual
        if self.__write_all(entity, items):
            self.__log.log_success(f"Atualizado registro '{entity}' id={item_id} com sucesso.")
            return atual
        self.__log.log_error(f"Falha ao salvar atualização de '{entity}' id={item_id}.")
        return None

    def excluir(self, entity: str, item_id: int) -> bool:
        items = self.__read_all(entity)
        alvo = int(item_id)
        novo = [x for x in items if self.__coerce_to_int(x.get("id"), None) != alvo]
        if len(novo) == len(items):
            self.__log.log_warning(f"Registro '{entity}' id={item_id} não encontrado para exclusão.")
            return False
        self.__reindex_ids(entity, novo)
        if self.__write_all(entity, novo):
            self.__log.log_success(f"Excluído registro '{entity}' id={item_id} com sucesso.")
            return True
        self.__log.log_error(f"Falha ao salvar exclusão em '{entity}' id={item_id}.")
        return False

    #? ---------------------- Atalhos específicos ----------------------

    def listar_salas         ( self                                   ) -> list[dict] : return self.listar      ( "salas" )
    def obter_sala           ( self,        sala_id: int              ) -> dict | None: return self.obter_por_id( "salas", sala_id)
    def criar_sala           ( self,          dados: dict             ) -> dict | None: return self.criar       ( "salas", dados)
    def atualizar_sala       ( self,        sala_id: int, dados: dict ) -> dict | None: return self.atualizar   ( "salas", sala_id, dados)
    def excluir_sala         ( self,        sala_id: int              ) -> bool       : return self.excluir     ( "salas", sala_id)

    def listar_agendamentos  ( self                                   ) -> list[dict] : return self.listar      ( "agendamentos"                        )
    def obter_agendamento    ( self, agendamento_id: int              ) -> dict | None: return self.obter_por_id( "agendamentos", agendamento_id        )
    def criar_agendamento    ( self,          dados: dict             ) -> dict | None: return self.criar       ( "agendamentos",          dados        )
    def atualizar_agendamento( self, agendamento_id: int, dados: dict ) -> dict | None: return self.atualizar   ( "agendamentos", agendamento_id, dados )
    def excluir_agendamento  ( self, agendamento_id: int              ) -> bool       : return self.excluir     ( "agendamentos", agendamento_id        )

Manager_json_service = ManagerJsonService