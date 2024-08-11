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

loginAsAdmin("Admin", "CantinAPP")


# Ir al apartado de Resumen de caja
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "cashSummary"))
).click()


# Obtener el input de busqueda
searchField = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[aria-controls='tablaCashSummary']")
    )
)

searchField.clear()
searchField.send_keys("2021")


# Esperar 8 segundos y cerrar el navegador
time.sleep(8)
driver.quit()