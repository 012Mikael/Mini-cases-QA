# importar o webdriver do selenium
from selenium import webdriver
# importar Options() para configurar o navegador
from selenium.webdriver.chrome.options import Options
# importar By() para selecionar coisas no site
from selenium.webdriver.common.by import By
# importar Keys() para mandar comandos para o navegador
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('https://www.jogajuntoinstituto.org/')

'''
qual a importância e os benefícios da automação de testes.? 
    agilizar e ganhar tempo em tarefas diarias.

pesquisa: 
    A automação de testes é fundamental para entregar softwares com mais qualidade e rapidez, pois executa validações repetitivas de forma automática e integra-se a fluxos de entrega contínua (CI/CD)

ferramentas mais usadas: 
    • Web: Selenium, Cypress e Playwright.
    • Mobile: Appium.
    • APIs e comportamento (BDD): Postman e Cucumber.
    • Suítes completas e em nuvem: Katalon Studio, TestComplete, Ranorex Studio e TestMu AI.
'''