from selenium import webdriver
from selenium.webdriver.common.by import By ###localiza o elemento
from webdriver_manager.chrome import ChromeDriverManager ###abre e controla o navegador
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument("--start-maximized")
service = Service("C:\\chromedriver\\chromedriver.exe") ###configurar o navegador e o caminho do driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user") ### find element busca o campo pelo seletor by.id
    driver.find_element(By.ID, "password").send_keys("secret_sauce") ### simula digitacao
    driver.find_element(By.ID, "login-button").click() ### simula o clique

    time.sleep(10)

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products", f"Título incorreto: {title}"
    print("Login realizado")

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert "Backpack" in item_name, "Item nao encontrado"
    print("item adicionado ao carrinho")

finally:
    time.sleep(10)
    driver.quit()