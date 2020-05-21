import subprocess
import sys
import importlib


def install_and_import(package):
    '''
    Instala os pacotes necessários para rodar as rotinas
    '''
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m",
                               "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('func_timeout')
install_and_import('selenium')
install_and_import('pyautogui')
