# 1 importar Biblioteca
from selenium.webdriver.common.by import By
from selenium.webdriver.wpewebkit import webdriver
import pytest


# 2 Classe


class Test_selenium_webdriver:
    # Definição de Inicio - Executa antes do teste

    def setup_method(self):
        # Declarar o obejto do Selenium e instanciar como o navegador  desejado
        self.driver = webdriver.Chrome('C:/Users/55119/PycharmProjects/pythonProject/fts132_inicial1/driver/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    #Definição de fim = Executa depois do teste
    def teardown_method(self):
        # Destruir o objeto do Selenium
        self.driver.quit()


        # definição do teste
    def testar_comprar_curso_mantis(self):
        # O selenium abre a url  indicada - site alvo do teste
        self.driver.get('https://iterasys.com.br/plataforma/home/index.php?action=initial')
        # O selenium escreve  "Mantis" na caixa de pesquisa
        self.driver.find_element(By.ID, "searchtext").send_keys('mantis')
        # O selenium clica no botão da lupa
        self.driver.find_element(By.ID,'btn_form_search').click()
        # O selenium  clica em Matricule-se
        self.driver.find_element(By.CSS_SELECTOR, ".span.comprar").click()
        # O selenium valida o nome do curso  no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, ".span.item-title").text == "Mantis"
        # O selenium valida  o prço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, "span.new-price").text == "R$ 59,99"
