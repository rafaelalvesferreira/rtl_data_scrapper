# -*- coding: utf-8 -*-
"""
Script para baixar os dados atualizados do Promax para o acompanhamento de
volume


"""

import time
import datetime
import os
import random
import logging
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

logging.basicConfig(level=logging.INFO,
                    filename='3-16-1.log',
                    format='%(asctime)s; %(levelname)s; %(message)s')


def Relatorio3_16_1(branch, branch_code, login, password):
    """
    Função que automatiza a geração dos dados do relatório 3.16.1
    variáveis de entrada:
    Branch - número do branch de 1 a 4
    Branch_code - código do branch no promax 132000, 61913, 85789, 63785
    Login - Login do usuário no Promax
    Password - Senha

    retorna o arquivo csv baixado na pasta final_donwnload_path
    """
    # Constantes utilizada
    logging.info('Inicio da rotina da filial %s', branch_code)
    random.seed()

    driver_path = 'chromedriver.exe'

    profile_path = os.path.join('C:\\Users',
                                os.getlogin(),
                                'AppData\\Local\\Google\\Chrome SxS',
                                'User Data\\Profile 1')

    day = str(datetime.datetime.now().date())

    final_data_path = os.path.join('C:\\Users',
                                   os.getlogin(),
                                   'Downloads',
                                   day)

    # criar uma pasta para o download com nome aleatório
    random_folder = str(random.randint(0, 1000))
    download_path = os.path.join(final_data_path, random_folder)
    os.makedirs(download_path)

    logging.info(download_path)
    # branch_code = branch_code_number
    # branch = branch_number

    chrome_Options = Options()
    chrome_Options.add_argument(f"user-data-dir={profile_path}")
    chrome_Options.add_argument("--start-maximized")
    chrome_Options.add_argument("--disable-popup-blocking")
    chrome_Options.add_argument("--safebrowsing-disable-download-protection")
    chrome_Options.add_argument('--disable-extensions')
    chrome_Options.add_argument('--safebrowsing-disable-extension-blacklist')
    chrome_Options.add_argument('--log-level=3')
    chrome_Options.add_argument('--disable-extensions')
    chrome_Options.add_argument('test-type')
    chrome_Options.add_experimental_option('excludeSwitches',
                                           ['enable-logging'])
    chrome_Options.add_experimental_option("prefs", {
        "profile.default_content_settings.popups": 0,
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True,
        "extensions_to_open": "inf"
    })

    # chrome_Options.binary_location =
    # r'C:\Users\rafael.ferreira\AppData
    # Local\Google\Chrome SxS\Application\chrome.exe'

    chrome_Options.binary_location = os.path.join('C:\\Users',
                                                  os.getlogin(),
                                                  'AppData\\Local\\Google\\',
                                                  'Chrome SxS\\Application\\',
                                                  'chrome.exe')

    driver = webdriver.Chrome(options=chrome_Options,
                              executable_path=driver_path)

    driver.get('http://rotele.promaxcloud.com.br/pw/')

    # mudar para o frame 'top'
    driver.switch_to.frame(driver.find_element_by_name("top"))

    # preencher usuário e senha na primeira página
    driver.find_element_by_name('Usuario').send_keys(login)
    driver.find_element_by_name('Senha').send_keys(password)
    driver.find_element_by_name('cmdConfirma').click()

    # selecionar a filial referente ao relatório
    element_addr = '/html/body/form/table/tbody[1]/tr[3]/td[2]/select'
    select = Select(driver.find_element_by_xpath(element_addr))
    select.select_by_value(f"015000{branch}")
    driver.find_element_by_name('cmdConfirma').click()

    wait = WebDriverWait(driver, 40)

    # testar os popups que aparecem no login, como são variáveis
    # usaremos os blocos try except para tratar os erros
    try:
        wait.until(EC.alert_is_present())
    except TimeoutException:
        logging.warning('Erro de popup 1')
    else:
        driver.switch_to.alert.accept()

    try:
        wait.until(EC.alert_is_present())
    except TimeoutException:
        logging.warning('Erro de popup 2')
    else:
        driver.switch_to.alert.accept()

    try:
        wait.until(EC.alert_is_present())
    except TimeoutException:
        logging.warning('Erro de popup 3')
    else:
        driver.switch_to.alert.accept()

    try:
        wait.until(EC.alert_is_present())
    except TimeoutException:
        logging.warning('Erro de popup 4')
    else:
        driver.switch_to.alert.accept()

    # esperar o frame principal aparecer e mudar para ele
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID,
                                                          'iFrameMenu')))

    # encontrar e clicar no menu novo siv
    element_addr = '//*[@id="out2000000000t"]'
    wait.until(EC.element_to_be_clickable((By.XPATH, element_addr)))
    element = driver.find_element_by_xpath(element_addr)
    driver.execute_script("arguments[0].click();", element)

    # aguardar a janela abrir
    # time.sleep(10)
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])

    # encontrar e clicar no menu 3.16.1
    time.sleep(10)
    element_addr = '//*[@id="treeMenu"]/ul/li[2]/ul/li[16]/ul/li[1]/a'
    wait.until(EC.invisibility_of_element_located((By.XPATH, element_addr)))
    element = driver.find_element_by_xpath(element_addr)
    driver.execute_script("arguments[0].click();", element)

    # clicar na lista no nome do GV
    element_addr = '//*[@id="listaEquipeVendas"]/ul/li[1]/a/ins[1]'
    wait.until(EC.element_to_be_clickable((By.XPATH, element_addr)))
    element = driver.find_element_by_xpath(element_addr)
    driver.execute_script("arguments[0].click();", element)

    # se for Campo Grande clicar no VDI
    if branch == '1':
        element_addr = '//*[@id="listaEquipeVendas"]/ul/li[2]/a/ins[1]'
        element = driver.find_element_by_xpath(element_addr)
        driver.execute_script("arguments[0].click();", element)

    # seleciona a opção analítico
    element_addr = "input[type='radio'][name='tpRelatorio'][value='A']"
    element = driver.find_element_by_css_selector(element_addr)
    driver.execute_script("arguments[0].click();", element)

    # clicar no botão exportar
    #  wait
    element = driver.find_element_by_xpath('//*[@id="botExportar"]')
    driver.execute_script("arguments[0].click();", element)

    logging.info('Baixando Analítico da filial %s', branch_code)
    WebDriverWait(driver, 150).until(EC.number_of_windows_to_be(3))

    # monitorar o tempo de download
    start_download = time.time()

    # verifica se o download está concluído
    loop_status = True
    loop_file_size = True
    while loop_status:
        while loop_file_size:
            time.sleep(1)
            for file in os.listdir(download_path):
                if file.endswith('.crdownload'):
                    file_size = os.stat(os.path.join(download_path,
                                                     file)).st_size
                    time.sleep(1)
                    file_size_after = os.stat(os.path.join(download_path,
                                                           file)).st_size
                    if file_size_after == file_size:
                        logging.info('Analitico File Size %2f', file_size)
                        driver.switch_to.window(driver.window_handles[2])
                        logging.info('Analitico Windows Handles')
                        time.sleep(1)
                        pyautogui.press('tab')
                        pyautogui.press('enter')
                        loop_file_size = False
        for file in os.listdir(download_path):
            if file.endswith('.inf'):
                arquivo = os.listdir(download_path)
                old_file = os.path.join(download_path, arquivo[0])
                new_file = os.path.join(final_data_path,
                                        f"3.16.1_{branch_code} Analítico.csv")
                os.rename(old_file, new_file)
                download_time = time.time() - start_download
                loop_status = False

    logging.info('Tempo de Download da Analítico da filial %2f', download_time)

    # fecha a janela do download e volta para o Novo SIV
    # WebDriverWait(driver, 50).until(EC.number_of_windows_to_be(3))
    logging.info(driver.window_handles)
    driver.switch_to.window(driver.window_handles[2])
    driver.close()

    # volta para a pagina do novo siv
    driver.switch_to.window(driver.window_handles[1])

    # seleciona a opção sintético
    element_addr = "input[type='radio'][name='tpRelatorio'][value='S']"
    element = driver.find_element_by_css_selector(element_addr)
    driver.execute_script("arguments[0].click();", element)

    # clica no botão exportar
    element = driver.find_element_by_xpath('//*[@id="botExportar"]')
    driver.execute_script("arguments[0].click();", element)

    # procedimento de download igual o anterior
    logging.info('Baixando Sintético da filial %s', branch_code)
    WebDriverWait(driver, 150).until(EC.number_of_windows_to_be(3))

    # monitorar o tempo de download
    start_download = time.time()

    loop_status = True
    loop_file_size = True
    while loop_status:
        while loop_file_size:
            time.sleep(1)
            for file in os.listdir(download_path):
                if file.endswith('.crdownload'):
                    file_size = os.stat(os.path.join(download_path,
                                                     file)).st_size
                    time.sleep(1)
                    file_size_after = os.stat(os.path.join(download_path,
                                                           file)).st_size
                    if file_size_after == file_size:
                        logging.info('Sintetico File Size: %2f', file_size)
                        driver.switch_to.window(driver.window_handles[2])
                        logging.info('Sintetico Windows Handles')
                        time.sleep(1)
                        pyautogui.press('tab')
                        pyautogui.press('enter')
                        loop_file_size = False
        for file in os.listdir(download_path):
            if file.endswith('.inf'):
                arquivo = os.listdir(download_path)
                old_file = os.path.join(download_path, arquivo[0])
                new_file = os.path.join(final_data_path,
                                        f"3.16.1_{branch_code} Sintetico.csv")
                os.rename(old_file, new_file)
                download_time = time.time() - start_download
                loop_status = False

    logging.info('Tempo de Download da Analítico da filial %2f', download_time)

    # vai fechando progressivamente as janelas download -> novo siv -> promax

    driver.switch_to.window(driver.window_handles[2])
    driver.close()
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()

    for raiz, diretorios, _ in os.walk(final_data_path):
        for diretorio in diretorios:
            os.rmdir(os.path.join(raiz, diretorio))

    logging.info('Final da rotina da filial %s', branch_code)

    with open(f'3-16-1 - {branch_code}.success', 'w'):
        pass

    return
