import os
import platform
import sys

def libs():
    # os.system("pip install --upgrade pip")
    os.system(r"pip install .\Data\PySide6-6.4.2-cp37-abi3-win_amd64.whl")
    os.system(r"pip install .\Data\peewee-3.15.4.tar.gz")
    os.system(r"pip install .\Data\docxtpl-0.16.5-py2.py3-none-any.whl")
    os.system(r"pip install .\Data\docx2pdf-0.1.8-py3-none-any.whl")


version = platform.win32_ver()

libs()
# if version[0] in ['8', '8.1', '10', '11']:

#     if sys.version_info.major == 3 and sys.version_info.minor == 11:
#         libs()
#     else:
#         os.startfile(r"\LR BD new\Data\python-3.11.2-amd64.exe", "open")
# else:
#     if sys.version_info.major == 3 and sys.version_info.minor == 7:
#         libs()
#     else:
#         os.startfile(r"\LR BD new\Data\python-3.8.1-amd64.exe", "open")
