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


#entrada do iframe
iframes = navegador.find_elements(By.TAG_NAME, "iframe")
navegador.switch_to.frame(iframes[0])

#espera explicita do elemnto
wait.until(
    EC.presence_of_element_located((By.NAME, "tbCategorias_length"))
    )

# altera a option 100 para 1000
#var select puxa no primeiro iframe o elemento select que contem "name=tbCategorias_length"
navegador.execute_script("""
var select = document.getElementsByName('tbCategorias_length')[0];
var option = select.querySelector("option[value='100']");

option.value = "1000";
option.text = "1000";

select.value = "1000";
select.dispatchEvent(new Event('change'));
""")



time.sleep(2)










# print(len(iframes))


# for i in range(len(iframes)):
#     navegador.switch_to.default_content()
#     navegador.switch_to.frame(iframes[i])
    
#     elementos = navegador.find_elements(By.NAME, "tbCategorias_length")
#     print(f"Iframe {i} -> encontrados: {len(elementos)}")


# print(len(navegador.find_elements(By.TAG_NAME, "iframe")))
