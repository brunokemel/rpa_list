from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# abrir navegador em full size
navegador.maximize_window()

# acessar o site
navegador.get("https://cremesp.org.br/?siteAcao=cid10")

#timer teste
# time.sleep(1)

wait = WebDriverWait(navegador, 20)

# navegador.switch_to.default_content()
#entrada do iframe
iframes = navegador.find_elements(By.TAG_NAME, "iframe")
navegador.switch_to.frame(iframes[0])

selecet_element = wait.until(
    EC.element_to_be_clickable((By.NAME, "tbCategorias_length"))
    )

select = Select(selecet_element).select_by_value("100")

time.sleep(2)










# print(len(iframes))


# for i in range(len(iframes)):
#     navegador.switch_to.default_content()
#     navegador.switch_to.frame(iframes[i])
    
#     elementos = navegador.find_elements(By.NAME, "tbCategorias_length")
#     print(f"Iframe {i} -> encontrados: {len(elementos)}")


# print(len(navegador.find_elements(By.TAG_NAME, "iframe")))
