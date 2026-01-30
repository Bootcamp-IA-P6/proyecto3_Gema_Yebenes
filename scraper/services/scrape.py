# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Para Chrome
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# def scrape_website():
#     # Configurar Selenium
#     options = Options()
#     options.add_argument('--headless')  # Ejecutar en modo headless
#     options.add_argument('--no-sandbox')  # Requerido para algunos servidores
#     options.add_argument('--disable-dev-shm-usage')  # Para evitar errores de memoria

#     # 🔹 Aquí inicializamos correctamente `service`
#     service = Service(ChromeDriverManager().install())

#     # Para Chrome
#     # Selenium Manager se encargará de descargar y gestionar el WebDriver
#     #service = Service()  # No es necesario especificar el ejecutable
#     driver = webdriver.Chrome(service=service, options=options)

#     # Navegar al sitio web
#     url = "https://jorgebenitezlopez.com"
#     driver.get(url)
#     print(driver.title)  
# # Esperar a que los elementos estén presentes
#     try:
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1"))
#         )
#         titles = driver.find_elements(By.CSS_SELECTOR, "h1")
#         urls = driver.find_elements(By.CSS_SELECTOR, "a")
#     except Exception as e:
#         print("Error al encontrar los elementos:", e)
#         driver.quit()
#         return []

#     scraped_data = []
#     for title, link in zip(titles, urls):
#         scraped_data.append({
#             "title": title.text,
#             "url": link.get_attribute("href"),
#         })

#     print("Scraped data:", scraped_data)  # Para depuración
#     driver.quit()
#     return scraped_data
## ESTO SE COMENTA PORQUE AL HACER EL DOCKERFILE DOCKER NO ES COMPATIBLE CON CHROME Y HAY QUE CONFIGURAE PARA FIREFOX
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
# from webdriver_manager.firefox import GeckoDriverManager

def scrape_website():
    # Configurar directorio para screenshots - Usar ruta absoluta al volumen
    screenshots_dir = "/app/screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
        
    # Configurar Selenium
    options = Options()
    options.add_argument('--headless')  # Ejecutar en modo headless
    options.add_argument('--no-sandbox')  # Requerido para algunos servidores
    options.add_argument('--disable-dev-shm-usage')  # Para evitar errores de memoria

    # Configurar el servicio de GeckoDriver
    service = Service("/usr/local/bin/geckodriver")
    
    # En vez de poner la ruta a mano, dejamos que el manager lo instale solo
    # service = Service(GeckoDriverManager().install())
    
    # Crear el WebDriver de Firefox
    driver = webdriver.Firefox(service=service, options=options)

    # Navegar al sitio web
    url = "http://books.toscrape.com/"
    driver.get(url)
    # print(driver.title)  
    print(f"Navegando a: {url}")
    
# Esperar a que los elementos estén presentes
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.product_pod"))
        )
        # 2. ### NUEVO: HACER LA FOTO ###
        # Creamos un nombre con la fecha y hora para que no se repita
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshots_dir, f"captura_{timestamp}.png")
        
        # ¡Click! Guardamos la foto
        driver.save_screenshot(screenshot_path)
        print(f"Captura de pantalla guardada en: {screenshot_path}")
        
        titles = driver.find_elements(By.CSS_SELECTOR, "h1")
        urls = driver.find_elements(By.CSS_SELECTOR, "a")
    except Exception as e:
        print("Error al encontrar los elementos:", e)
        driver.quit()
        return []

    scraped_data = []
    for title, link in zip(titles, urls):
        scraped_data.append({
            "title": title.text,
            "url": link.get_attribute("href"),
        })

    print("Scraped data:", scraped_data)  # Para depuración
    driver.quit()
    return scraped_data