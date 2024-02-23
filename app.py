from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Inicializando o webdriver 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Acessando o site
driver.get('https://www.google.com')

input('Pressione ENTER para fechar o navegador...')