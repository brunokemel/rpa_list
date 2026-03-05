from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
navegador.maximize_window()
navegador.get("https://cremesp.org.br/?siteAcao=cid10")

wait = WebDriverWait(navegador, 20)

# entra no iframe pelo id
iframe = wait.until(
    EC.presence_of_element_located((By.ID, "fraIncludePaginaResponsivel"))
)
navegador.switch_to.frame(iframe)

# espera o select aparecer
wait.until(
    EC.presence_of_element_located((By.NAME, "tbCategorias_length"))
)

# altera o select para 3000 registros
navegador.execute_script("""
var select = document.getElementsByName('tbCategorias_length')[0];
var option = select.querySelector("option[value='100']");
option.value = "3000";
option.text = "3000";
select.value = "3000";
select.dispatchEvent(new Event('change'));
""")

# espera carregar todas as linhas
wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="tbCategorias"]/tbody/tr')))
linhas = navegador.find_elements(By.XPATH, '//*[@id="tbCategorias"]/tbody/tr')
print(f"Total de linhas: {len(linhas)}")

dados_tabela = []

for i, linha in enumerate(linhas, start=1):
    codigo = linha.find_element(By.XPATH, './td[1]').text.strip()
    descricao = linha.find_element(By.XPATH, './td[2]').text.strip()
    
    # botão da linha atual
    botao_visualizar = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f'//*[@id="tbCategorias"]/tbody/tr[{i}]/td[3]/button')
        )
    )

    # rola até o botão antes de clicar
    navegador.execute_script("arguments[0].scrollIntoView(true);", botao_visualizar)

    # tenta clicar e esperar a tabela de derivações
    try:
        navegador.execute_script("arguments[0].click();", botao_visualizar)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="tabela_body"]/tr')))
    except TimeoutException:
        print(f"Falha ao carregar derivações da linha {i}, tentando novamente...")
        navegador.execute_script("arguments[0].click();", botao_visualizar)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="tabela_body"]/tr')))

    # coleta os detalhes
    linhas_detalhe = navegador.find_elements(By.XPATH, '//*[@id="tabela_body"]/tr')
    derivacoes = []
    for detalhe in linhas_detalhe:
        deriv_codigo = detalhe.find_element(By.XPATH, './td[1]').text.strip()
        deriv_desc = detalhe.find_element(By.XPATH, './td[2]').text.strip()
        derivacoes.append(f"{deriv_codigo} - {deriv_desc}")
    
    registro = f"{codigo} - {descricao}\n    Derivações:\n    " + "\n    ".join(derivacoes)
    dados_tabela.append(registro)
    print(registro)
    
    # botão voltar
    botao_voltar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnVoltarTbListCategorias"]')))
    botao_voltar.click()
    
    # recarrega tabela principal
    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="tbCategorias"]/tbody/tr')))
    linhas = navegador.find_elements(By.XPATH, '//*[@id="tbCategorias"]/tbody/tr')

# Agora 'dados_tabela' é uma lista de strings
resultado_final = "\n\n".join(dados_tabela)
print(resultado_final)

time.sleep(5)


##try Cat

# for letra in string.ascii_uppercase:  # A até Z
#     for numero in range(100):         # 00 até 99
#         codigo = f"{letra}{numero:02d}"  # Formata 00, 01, 02...

#         try:
#             elemento = navegador.find_element(By.ID, codigo)  # exemplo
#             print(f"Encontrado: {codigo}")
            
#             # Aqui você faz a raspagem
            
#         except:
#             continue