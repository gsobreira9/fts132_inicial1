# 1 - importar bibliotecas /pacotes

import pytest   #framework de teste unidad/ engine /motor

import time     # Controle do tempo
import json     # Ler e Escrever no formato Json


from selenium import webdriver             #Bibliotecas do Selenium WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

 # 2 Classe e Definições
class TestConsultaMantis():
    def setup_method(self, method):
        #Instanciar o obejto do Selenium WebDriver como Chrome
        self.driver = webdriver.Chrome('C:/Users/55119/PycharmProjects/pythonProject/fts132_inicial1/driver/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait(3) # o robô irá esperar por até 30 segundos pelo elementos
        self.driver.maximize_window() #Maximizar a janela do navegador
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_consultaMantis(self):
        self.driver.get("https://iterasys.com.br/plataforma/home/index.php?action=initial")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.ID, "searchtext").click()
        self.driver.find_element(By.ID, "searchtext").send_keys("MANTIS")
        self.driver.find_element(By.ID, "btn_form_search").click()
        #time.sleep(3) # pausa forçada / "alfine' /sempre deve remover antes de salvar no repositorio
        self.driver.find_element(By.CSS_SELECTOR, ".comprar").click()
        self.driver.find_element(By.CSS_SELECTOR, ".item-title").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".item-title").text == "Mantis"
        assert self.driver.find_element(By.CSS_SELECTOR, ".new-price").text == "R$ 59,99"