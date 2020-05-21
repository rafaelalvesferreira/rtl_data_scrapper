import time
import datetime
import os
import random
import logging
import shutil
from func_timeout import func_set_timeout
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# logging.basicConfig(level=logging.INFO,
#                     filename='5-7-1.log',
#                     format='%(asctime)s; %(levelname)s; %(message)s')


@func_set_timeout(300)
def Relatorio5_12_2(branch, branch_code, login, password):
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
    logging.info('20-5-12-2-Inicio da rotina da filial %s', branch_code)
    random.seed()

    branchs = {'132000': 'CG', '61913': 'AQ', '85789': 'CB', '63785': 'CX'}

    driver_path = 'chromedriver.exe'

    day = str(datetime.datetime.now().date())
    first_day = datetime.date.today().strftime('01/%m/%Y').replace('/', '')

    lastday = (datetime.date.today() - datetime.timedelta(days=1))
    if lastday.strftime('%a') == 'Sun':
        lastday = (datetime.date.today() - datetime.timedelta(days=2))

    lastday = lastday.strftime('%d/%m/%Y').replace('/', '')

    final_data_path = os.path.join('C:\\Users',
                                   os.getlogin(),
                                   'Downloads',
                                   day)
    try:
        # criar uma pasta para o download com nome aleatório
        random_folder = str(random.randint(0, 1000))
        download_path = os.path.join(final_data_path, random_folder)
        os.makedirs(download_path)

        logging.info('20-5-12-2-%s', download_path)
        # branch_code = branch_code_number
        # branch = branch_number

        chrome_Options = Options()
        # chrome_Options.add_argument(f"user-data-dir={profile_path}")
        chrome_Options.add_argument("--start-maximized")
        chrome_Options.add_argument("--disable-popup-blocking")
        chrome_Options.add_argument(
            "--safebrowsing-disable-download-protection")
        chrome_Options.add_argument('--disable-extensions')
        chrome_Options.add_argument(
            '--safebrowsing-disable-extension-blacklist')
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

        wait = WebDriverWait(driver, 20)

        # testar os popups que aparecem no login, como são variáveis
        # usaremos os blocos try except para tratar os erros
        try:
            wait.until(EC.alert_is_present())
        except TimeoutException:
            logging.warning('20-5-12-2-Erro de popup 1')
        else:
            driver.switch_to.alert.accept()

        try:
            wait.until(EC.alert_is_present())
        except TimeoutException:
            logging.warning('20-5-12-2-Erro de popup 2')
        else:
            driver.switch_to.alert.accept()

        try:
            wait.until(EC.alert_is_present())
        except TimeoutException:
            logging.warning('20-5-12-2-Erro de popup 3')
        else:
            driver.switch_to.alert.accept()

        try:
            wait.until(EC.alert_is_present())
        except TimeoutException:
            logging.warning('5-7-1-Erro de popup 4')
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

        # encontrar e clicar no menu 5.7.1
        time.sleep(3)
        element_addr = '//*[@id="treeMenu"]/ul/li[4]/ul/li[12]/ul/li/a'
        wait.until(EC.invisibility_of_element_located((By.XPATH,
                                                       element_addr)))
        element = driver.find_element_by_xpath(element_addr)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        # clicar na lista no nome do GV
        element_addr = '//*[@id="listaEquipeVendas"]/ul/li[1]/a/ins[1]'
        wait.until(EC.element_to_be_clickable((By.XPATH, element_addr)))
        element = driver.find_element_by_xpath(element_addr)
        driver.execute_script("arguments[0].click();", element)

        # clicar na data final
        element_addr = '//*[@id="dtFim"]'
        wait.until(EC.element_to_be_clickable((By.XPATH, element_addr)))
        time.sleep(2)
        element = driver.find_element_by_xpath(element_addr).click()
        time.sleep(1)
        #print(f'Ultimo dia: {lastday}')
        element = driver.find_element_by_xpath(element_addr).send_keys(
            lastday)
        driver.find_element_by_xpath(
            '//*[@id="formPH070111"]/div[1]/div[3]/div[1]').click()
        time.sleep(1)

        # clicar na data inicial
        element_addr = '//*[@id="dtInicio"]'
        wait.until(EC.element_to_be_clickable((By.XPATH, element_addr)))
        #element = driver.find_element_by_xpath(element_addr).click()
        #print(f'Primeiro dia: {first_day}')
        element = driver.find_element_by_xpath(element_addr).send_keys(
            first_day)

        time.sleep(1)

        # clicar no botão exportar
        element = driver.find_element_by_xpath('//*[@id="botExportar"]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        loop_status = True
        while loop_status:
            for file in os.listdir(download_path):
                if file.endswith(f'{branch_code}.csv'):
                    old_file = os.path.join(download_path, file)
                    new_file = os.path.join(
                        final_data_path,
                        f"20.5.12.2_{branchs.get(branch_code)}.csv")
                    os.rename(old_file, new_file)
                    loop_status = False

        shutil.rmtree(download_path, ignore_errors=True)

        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()

    except (TimeoutException,
            NoSuchElementException,
            StaleElementReferenceException,
            WebDriverException) as error:
        logging.warning('20-5-12-2-%s', error)
        with open(os.path.join(final_data_path,
                               f'20-5-12-2-{branch_code}.fail'), 'w'):
            pass
        shutil.rmtree(download_path, ignore_errors=True)
        for window in driver.window_handles:
            driver.switch_to.window(window)
            driver.close()
        Relatorio5_12_2(branch, branch_code, login, password)

    shutil.rmtree(download_path, ignore_errors=True)

    logging.info('20-5-12-2-Final da rotina da filial %s', branch_code)

    with open(os.path.join(final_data_path,
                           f'20-5-12-2-{branch_code}.success'), 'w'):
        pass

    return

# lg = 'RAFAELFERRE'
# pwd = 'Rafa001*el'
# Relatorio5_12_2("2", "61913", lg, pwd)