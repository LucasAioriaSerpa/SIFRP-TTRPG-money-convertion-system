import os
import py2exe
import customtkinter

ctk_path = os.path.dirname(customtkinter.__file__)

py2exe.freeze(
    console=['launcher.py'],
    options={
        'py2exe': {
            'includes': ['customtkinter'],
            'packages': [
                'SRC.CORE',
                'SRC.DATABASE',
                'SRC.MODELS',
                'SRC.SERVICES',
                'SRC.UTILS',
                'SRC.VIEWS'
            ],
            'bundle_files': 3,
            'optimize': 2
        }
    },
    data_files=[
        ('customtkinter/assets/themes', [
            os.path.join(ctk_path, 'assets', 'themes', 'blue.json'),
            os.path.join(ctk_path, 'assets', 'themes', 'dark-blue.json'),
            os.path.join(ctk_path, 'assets', 'themes', 'green.json')
        ])
    ]
)
