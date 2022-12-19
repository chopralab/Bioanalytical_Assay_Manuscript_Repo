# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['GUI_dev.py'],
             pathex=['/Users/armenbeck/Desktop/0003_Merck/Scripts/GUI_APP_PYINSTALLER'],
             binaries=[],
             datas=[('~/plate_2_score.py','.'),
                    ('~/reverse_screen.py','.'),
                    ('~/AF00.png','.'),
                    ('~/AF01.png','.'),
                    ('~/AF10.png','.'),
                    ('~/AF11.png','.'),
                    ('~/Formats.jpg','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

#for d in a.datas:
#    if 'pyconfig' in d[0]:
#        a.datas.remove(d)
#        break

#a.datas += [('AF00.png','.'),('AF01.png','.'),('AF10.png','.'),('AF11.png','.'),('Formats.jpg','.')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='GUI_dev',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
