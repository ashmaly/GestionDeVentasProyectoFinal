from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

# Abrir la web
driver = webdriver.Firefox()

# Maximizar la ventana del navegador
driver.maximize_window()

url = 'http://127.0.0.1/CantinAPP'
driver.get(url)

# Iniciar sesión como el usuario Admin
def loginAsAdmin(user, passwd):
    # Abrir el formulario de registro presionando el botón de Login
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "cargaFormLogin"))
        ).click()

    # Obtener los inputs 
    username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.ID, "nombre"
        ))
    )

    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.ID, "password"
        ))
    )

    # Limpiar los inputs y escribir en ellos
    username.clear()
    username.send_keys(user)

    password.clear()
    password.send_keys(passwd)

    # Presionar el botón para registrar el nuevo usuario
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "BT_Login"))
    ).click()

loginAsAdmin("Ashanty", "test")

time.sleep(1)

# Click en Ayer para ver el menú del día anterior
yesterday = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "yesterday"))
)

# Desplazar hacia abajo
driver.execute_script("arguments[0].scrollIntoView(true);", yesterday)
time.sleep(2)

yesterday.click()

time.sleep(1)

# Click en Ayer para ver el menú de hoy
today = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "today"))
)

# Desplazar hacia abajo
driver.execute_script("arguments[0].scrollIntoView(true);", today)
time.sleep(2)

today.click()

time.sleep(1)

# Click en Ayer para ver el menú del día anterior
tomorrow = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "tomorrow"))
)

# Desplazar hacia abajo
driver.execute_script("arguments[0].scrollIntoView(true);", tomorrow)
time.sleep(2)

tomorrow.click()


# Esperar 5 segundos y cerrar el navegador
time.sleep(5)
driver.quit()