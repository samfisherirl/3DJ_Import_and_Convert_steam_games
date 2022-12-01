# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/EXAMPLE2.PY'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/import_gspread_table.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/test.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/EXAMPLE2.PY', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/pyairtable_real_test_december - Copy.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/python pygsheetrs.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/EXAMPLE2 - Copy.PY', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/pyairtable_real_test_december.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/service_account.json', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/web', 'web/'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/gsheetmain.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE/input_gui.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='EXAMPLE2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='EXAMPLE2',
)
