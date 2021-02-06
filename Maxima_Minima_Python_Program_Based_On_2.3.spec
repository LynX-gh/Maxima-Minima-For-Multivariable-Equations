# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Maxima_Minima_Python_Program_Based_On_2.3.py'],
             pathex=['C:\\Users\\lynx2\\Desktop\\Indus\\Sem 1\\Subjects\\Calc\\Maxima_Minima_Python Program Based On 2.3'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Maxima_Minima_Python_Program_Based_On_2.3',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
