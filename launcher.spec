# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Marcos Serpa\\Documents\\GitHub\\Sistema-de-moedas-GOTY-RPG\\launcher.py'],
    pathex=['SRC','SRC/CORE', 'SRC/MODELS', 'SRC/SERVICES', 'SRC/VIEWS'],
    binaries=[],
    datas=[('C:\\Users\\Marcos Serpa\\Documents\\GitHub\\Sistema-de-moedas-GOTY-RPG\\.venv\\Lib\\site-packages/customtkinter', 'customtkinter/')],
    hiddenimports=['SRC','SRC.CORE', 'SRC.MODELS', 'SRC.SERVICES', 'SRC.VIEWS'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='launcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='launcher',
)
