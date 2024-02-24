from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import time

def booting_driver():
    # Setando as configurações
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=500,500', '--incognito'] # '--headless' para rodar em background
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

    # Inicializando o webdriver 
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

def accessing_website(site):
    driver.get(site)


def finishing_connection():
    driver.quit()
    
    
booting_driver()
accessing_website('https://www.google.com')
time.sleep(5)
finishing_connection()