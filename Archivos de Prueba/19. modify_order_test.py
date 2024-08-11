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

loginAsAdmin("Ashanty", "test")

# Ir al apartado Mis Pedidos
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "miPedido"))
).click()

time.sleep(1)

# Click en Modificar
btModificarPedido = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "btModificarPedido"))
)

# Desplazar hacia abajo
driver.execute_script("arguments[0].scrollIntoView(true);", btModificarPedido)
time.sleep(2)

btModificarPedido.click()

tablaMenuHoy = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "tablaMenuHoy"))
)

tablaMenuHoy.find_element(By.XPATH, "//table[@id='tablaMenuHoy']/tbody/tr[5]").click()
tablaMenuHoy.find_element(By.XPATH, "//table[@id='tablaMenuHoy']/tbody/tr[6]").click()


# Click en Actualizar Pedido
btAgregarPedido = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "btAgregaPedido"))
).click()


# Esperar 5 segundos y cerrar el navegador
time.sleep(5)
driver.quit()