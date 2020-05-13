from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from faker import Faker
import random, string
import requests, os
from time import sleep
from itertools import cycle
from datetime import datetime, timedelta
import sys
from flask import Flask, render_template, request

# app = Flask(__name__)

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))
    
def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

class Killer:
    def __init__(self):
        # self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        # self.driver.add_argument('headless')
        self.initAction()
        

    def initAction(self):
        self.counter = 0
        while True:
            self.driver.get("https://pyme.apanotupyme.cl/index.php?p=signup")
            newUser = FakeUsuario(fake) 
            nombre =newUser.nombre
            email = newUser.email
            password = newUser.password
            rut = newUser.rut
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/form/div/div/div[2]/div/div[1]/div[1]/input").send_keys(nombre)
            sleep(0.1)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/form/div/div/div[2]/div/div[1]/div[2]/input").send_keys(email)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/form/div/div/div[2]/div/div[1]/div[3]/input").send_keys(password)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/form/div/div/div[2]/div/div[1]/div[4]/input").send_keys(password)
            sleep(0.1)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/form/div/div/div[2]/div/div[1]/div[5]/input").send_keys(rut)
            element = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/form/div/div/div[2]/div/div[1]/div[6]/div/label/span[2]")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.driver.execute_script("arguments[0].click();", element)
            sleep(0.3)
            print("email: {} \t pass: {}".format(email,password))
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/form/div/div/div[2]/div/div[2]/button").click()
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/nav/div[2]/div[2]/div/ul/li[2]/a").click() # LOGOUT
            sleep(0.5)
            self.counter +=1
            print("Counter: ",self.counter)
            
        

class FakeUsuario:
    def __init__(self, fake):
        self.data = fake.profile()
        self.nombre = self.data["name"]
        self.email = self.data["mail"]
        self.pyme = self.data["company"]
        self.generatePassword()
        self.generateRut()

    def generatePassword(self):
        num = random.randint(8,15)
        self.password = get_random_alphaNumeric_string(num)
    
    def generateRut(self):
        num = random.randint(6500000,81000000)
        verificador = digito_verificador(num)
        self.rut = str(num) + "-" + str(verificador)

def hack(fake):
    Killer()

# @app.route('/')
# def index_page():
#     fake = Faker(['es_MX'])
#     hack(fake)
#     return render_template('index.html')

if __name__ == "__main__":
    fake = Faker(['es_MX'])
    hack(fake)
    