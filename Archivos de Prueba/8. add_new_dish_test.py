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

loginAsAdmin("Admin", "CantinAPP")


# Ir al apartado de Nuevo Plato
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "newComposicion"))
).click()


# Obtener los inputs para añadir un nuevo plato 
nombreComposicion = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.ID, "nombreComposicion"
    ))
)

descripcionComposicion = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.ID, "descripcionComposicion"
    ))
)

nombreComposicion.clear()
nombreComposicion.send_keys("Pasta con pechuga a la plancha")

descripcionComposicion.clear()
descripcionComposicion.send_keys("Pasta con trozos de pechuga de pollo a la plancha")


# Seleccionar una opción de tipo de composición
tipoComposicion = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "tipoComposicion"))
)

select = Select(tipoComposicion)    
select.select_by_visible_text("Plato")


# Hacer click sobre el botón Añadir a la carta
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "agregarComposicion"))
).click()


# Esperar 5 segundos y cerrar el navegador
time.sleep(5)
driver.quit()