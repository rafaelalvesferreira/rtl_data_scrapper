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
from func_timeout import func_set_timeout
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

logging.basicConfig(level=logging.INFO,
                    filename='3-16-2.log',
                    format='%(asctime)s; %(levelname)s; %(message)s')


@func_set_timeout(300)
def Relatorio3_16_2(branch, branch_code, login, password):
    """
    Função que automatiza a geração dos dados do relatório 3.16.2
    variáveis de entrada:
    Branch - número do branch de 1 a 4
    Branch_code - código do branch no promax 132000, 61913, 85789, 63785
    Login - Login do usuário no Promax
    Password - Senha

    retorna o arquivo csv baixado na pasta final_donwnload_path
    """
    # Constantes utilizada
    logging.info('3-16-2-Inicio da rotina da filial %s', branch_code)
    random.seed()

    driver_path = 'chromedriver.exe'

    # profile_path = os.path.join('C:\\Users',
    #                             os.getlogin(),
    #                             'AppData\\Local\\Google\\Chrome SxS',
    #                             'User Data\\Profile 1')

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

    driver_path = 'chromedriver.exe'

    # profile_path = os.path.join('C:\\Users',
    #                             os.getlogin(),
    #                             'AppData\\Local\\Google\\Chrome SxS',
    #                             'User Data\\Profile 1')

    chrome_Options = Options()
    # chrome_Options.add_argument(f"user-data-dir={profile_path}")
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
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False
    })

    chrome_Options.binary_location = os.path.join('C:\\Users',
                                                  os.getlogin(),
                                                  'AppData\\Local\\Google\\',
                                                  'Chrome SxS\\Application\\',
                                                  'chrome.exe')

    driver = webdriver.Chrome(options=chrome_Options,
                              executable_path=driver_path)
    try:
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
            logging.warning('3-16-2-Erro de popup 1')
        else:
            driver.switch_to.alert.accept()

        try:
            wait.until(EC.alert_is_present())
        except TimeoutException:
            logging.warning('3-16-2-Erro de popup 2')
        else:
            driver.switch_to.alert.accept()

        try:
            wait.until(EC.alert_is_present())
        except TimeoutException:
            logging.warning('3-16-2-Erro de popup 3')
        else:
            driver.switch_to.alert.accept()

        try:
            wait.until(EC.alert_is_present())
        except TimeoutException:
            logging.warning('3-16-2-Erro de popup 4')
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
        wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])

        # encontrar e clicar no menu 3.16.2
        element_addr = '//*[@id="treeMenu"]/ul/li[2]/ul/li[16]/ul/li[2]/a'
        wait.until(EC.invisibility_of_element_located((By.XPATH,
                                                       element_addr)))
        element = driver.find_element_by_xpath(element_addr)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        # clicar no dropdown gerente de vendas
        element_addr = 'tpGv'
        wait.until(EC.element_to_be_clickable((By.NAME, element_addr)))
        select = Select(driver.find_element_by_name(element_addr))
        select.select_by_index(1)
        time.sleep(2)

        # clicar no dropdown gerente de vendas
        element_addr = 'tpArea'
        wait.until(EC.element_to_be_clickable((By.NAME, element_addr)))
        select = Select(driver.find_element_by_name(element_addr))
        select.select_by_index(1)
        time.sleep(2)

        # clicar no botão exportar
        element = driver.find_element_by_xpath('//*[@id="botGerarCSV"]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        # clicar em gerar CSV
        element_addr = '//*[@id="botGerarDiv"]'
        wait.until(EC.element_to_be_clickable((By.XPATH, element_addr)))
        element = driver.find_element_by_xpath(element_addr)
        driver.execute_script("arguments[0].click();", element)
        # time.sleep(5)

        try:
            wait.until(EC.alert_is_present())
        except TimeoutException:
            logging.warning('3-16-2-Erro de popup 1')
        else:
            driver.switch_to.alert.accept()

        # aguardar o download do arquivo, mudar o nome e salvar no
        # final_download_path
        # o driver do Chrome está causando um bug no download, portanto estamos
        # buscando o arquivo incopleto na pasta de download_path
        logging.info('3-16-2-Baixando Diário da filial %s', branch_code)

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
                            logging.info('3-16-2-Diario File Size %2f',
                                         file_size)
                            driver.switch_to.window(driver.window_handles[2])
                            logging.info('3-16-2-Diario Windows Handles')
                            time.sleep(1)
                            pyautogui.press('tab')
                            pyautogui.press('enter')
                            loop_file_size = False
            for file in os.listdir(download_path):
                if file.endswith('.inf'):
                    arquivo = os.listdir(download_path)
                    old_file = os.path.join(download_path, arquivo[0])
                    new_file = os.path.join(final_data_path,
                                            f"Diario_{branch_code}.csv")
                    os.rename(old_file, new_file)
                    download_time = time.time() - start_download
                    loop_status = False

        logging.info('3-16-2-Tempo de Download do Diario da filial %2f',
                     download_time)

        # vai fechando progressivamente as janelas download ->
        # novo siv -> promax
        WebDriverWait(driver, 50).until(EC.number_of_windows_to_be(3))
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()

        with open(os.path.join(final_data_path,
                               f'3_16_2-{branch_code}.success'), 'w'):
            pass

    except Exception as error:
        logging.warning(error)
        with open(os.path.join(final_data_path,
                               f'3_16_2-{branch_code}.fail'), 'w'):
            pass
        Relatorio3_16_2(branch, branch_code, login, password)

    os.rmdir(download_path)

    logging.info('3-16-2-Final da rotina da filial %s', branch_code)

    # with open(os.path.join(final_data_path,
    #                        f'3_16_2-{branch_code}.success'), 'w'):
    #     pass

    return
