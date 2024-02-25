from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pathlib import Path
import time


def botting_driver():
    # Setando as configurações
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1200,1000', '--incognito'] # '--headless' para rodar em background
    for argument in arguments:
        chrome_options.add_argument(argument)

    # Setando as configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': str(Path().home() / "Downloads"),
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    global driver
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    return None

def accessing_website(site):
    driver.get(site)

def find_element(type_of_selection, value):
    if type_of_selection == 'id':
        return driver.find_element(By.ID, value)
    elif type_of_selection == 'class':
        return driver.find_element(By.CLASS_NAME, value)
    elif type_of_selection == 'name':
        return driver.find_element(By.NAME, value)
    elif type_of_selection == 'xpath':
        return driver.find_element(By.XPATH, value)
    elif type_of_selection == 'css':
        return driver.find_element(By.CSS_SELECTOR, value)
    elif type_of_selection == 'link':
        return driver.find_element(By.LINK_TEXT, value)
    elif type_of_selection == 'partial_link':
        return driver.find_element(By.PARTIAL_LINK_TEXT, value)
    elif type_of_selection == 'tag':
        return driver.find_element(By.TAG_NAME, value)
    else:
        return None

def find_elements(type_of_selection, value):
    if type_of_selection == 'id':
        return driver.find_elements(By.ID, value)
    elif type_of_selection == 'class':
        return driver.find_elements(By.CLASS_NAME, value)
    elif type_of_selection == 'name':
        return driver.find_elements(By.NAME, value)
    elif type_of_selection == 'xpath':
        return driver.find_elements(By.XPATH, value)
    elif type_of_selection == 'css':
        return driver.find_elements(By.CSS_SELECTOR, value)
    elif type_of_selection == 'link':
        return driver.find_elements(By.LINK_TEXT, value)
    elif type_of_selection == 'partial_link':
        return driver.find_elements(By.PARTIAL_LINK_TEXT, value)
    elif type_of_selection == 'tag':
        return driver.find_elements(By.TAG_NAME, value)
    else:
        return None

botting_driver()
accessing_website('https://cursoautomacao.netlify.app/desafios.html')

botao1 = find_element('id', 'btn1')
botao2 = find_element('class', 'btn2.btn.btn-dark')
botao3 = find_element('class', 'btn2.btn.btn-warning')

if botao1.is_enabled():
    print('botão 1 está habilitado')
else:
    print('botão 1 está desabilitado')

if botao2.is_enabled():
    print('botão 2 está habilitado')
else:
    print('botão 2 está desabilitado')

if botao3.is_enabled():
    print('botão 3 está habilitado')
else:
    print('botão 3 está desabilitado')


input('')
driver.close()