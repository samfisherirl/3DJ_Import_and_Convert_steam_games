# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/def.css', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/css.html', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/render.html', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/render_post_style.html', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/render_pre_style.html', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/webview_test2.html', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/service_account.json', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/service_account1.json', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/desktop_icons.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/evaluate_js.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/evaluate_js_async.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/GSHEET.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/GSHEET_old.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/import requests.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/main.py', '.'), ('C:/Users/dower/OneDrive/PYTHON/X PYTHON SCRIPTS/NEUTRON EEL PYTHON justlikeahk/UPLOAD TABLE PYWEBVIEW/examples/test.py', '.')],
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
    name='import_from_api',
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
    name='import_from_api',
)
