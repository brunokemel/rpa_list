from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
from selenium.common.exceptions import NoSuchElementException
import re 



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

# altera a option 100 para 3000
#var select puxa no primeiro iframe o elemento select que contem "name=tbCategorias_length"
navegador.execute_script("""
var select = document.getElementsByName('tbCategorias_length')[0];
var option = select.querySelector("option[value='100']");

option.value = "3000";
option.text = "3000";

select.value = "3000";
select.dispatchEvent(new Event('change'));
""")

#acessa o botao de visualizar variacoes de cada categoria
botao = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-round.btn-sm.btn-success"))
    )

botao.click()

padrao_categoria = r"^[A-Z]\d{2}$"
padrao_subcategoria = r"^[A-Z]\d{3}$"

linhas = navegador.find_elements(By.CSS_SELECTOR, "table tbody tr")

for linha in linhas:
    colunas = linha.find_elements(By.TAG_NAME, "td")

    if len(colunas) >= 2:
        codigo = colunas[0].get_attribute("innerText").strip()
        descricao = colunas[1].get_attribute("innerText").strip()

        classes = colunas[0].get_attribute("class")
    
    # Se tiver classe dtr-control → é categoria (A00)
        if classes and "dtr-control" in classes:

            print(f"\nCódigo: {codigo}")
            print(f"Descrição: {descricao}")
            print("-" * 40)

        # Senão → é subcategoria (A000)
        else:

            print(f"   Código: {codigo}")
            print(f"   Descrição: {descricao}")
            print("   " + "-" * 36)
    

time.sleep(10)


# for letra in string.ascii_uppercase:  # A até Z
#     for numero in range(100):         # 00 até 99
#         codigo = f"{letra}{numero:02d}"  # Formata 00, 01, 02...

#         try:
#             elemento = navegador.find_element(By.ID, codigo)  # exemplo
#             print(f"Encontrado: {codigo}")
            
#             # Aqui você faz a raspagem
            
#         except:
#             continue