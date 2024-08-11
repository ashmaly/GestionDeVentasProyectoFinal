from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

# Abrir la web
driver = webdriver.Firefox()

# Maximizar la ventana del navegador
driver.maximize_window()

url = 'http://127.0.0.1/CantinAPP'
driver.get(url)

# Abrir el formulario de registro presionando el botón de Registro
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "cargaFormRegistro"))
    ).click()

# Obtener los inputs 
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.ID, "nombre"
    ))
)

email = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.ID, "email"
    ))
)

password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.ID, "password"
    ))
)

# Limpiar los inputs y escribir en ellos
username.clear()
username.send_keys("Ashanty")

email.clear()
email.send_keys('ashanty@gmail.com')

password.clear()
password.send_keys("test")


# Presionar el botón para registrar el nuevo usuario
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "BT_Registrar"))
    ).click()

# Esperar 5 segundos y cerrar el navegador
time.sleep(5)
driver.quit()





