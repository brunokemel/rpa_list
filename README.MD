🐍 Web Scraping CID-10 (CREMESP)

Script em Python que utiliza Selenium para realizar a raspagem de dados da tabela de Categorias CID-10 disponível no site do CREMESP.

O robô acessa a página, carrega todas as categorias disponíveis, entra em cada item da tabela e coleta suas derivações, retornando os dados estruturados no terminal.

📌 Objetivo

Automatizar a coleta de informações da tabela CID-10, incluindo:

Código da categoria

Descrição da categoria

Lista de derivações relacionadas

O script percorre todas as linhas da tabela (mais de 2000 registros) e coleta os dados de forma automatizada.

⚙️ Tecnologias utilizadas

Python 3

Selenium

WebDriver Manager

ChromeDriver

Bibliotecas principais:

selenium
webdriver-manager
🚀 Como executar o projeto
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2️⃣ Criar ambiente virtual (opcional)
python -m venv venv

Ativar:

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
3️⃣ Instalar dependências
pip install selenium webdriver-manager
4️⃣ Executar o script
python main.py
🔎 Como o script funciona

O fluxo da automação é:

Abre o site do CREMESP contendo a tabela CID-10

Entra no iframe onde a tabela está localizada

Altera o seletor de paginação para carregar até 3000 registros

Percorre cada linha da tabela

Clica no botão visualizar de cada categoria

Coleta todas as derivações associadas

Retorna à tabela principal

Repete o processo até finalizar todas as linhas

📊 Estrutura dos dados coletados

O script gera uma saída semelhante a:

A00 - Cólera
    Derivações:
    A00.0 - Cólera devido a Vibrio cholerae 01, biótipo cholerae
    A00.1 - Cólera devido a Vibrio cholerae 01, biótipo eltor
    A00.9 - Cólera não especificada
⚠️ Observações

O site possui carregamento dinâmico e estrutura limitada, por isso foi utilizado Selenium para interação com a interface.

O script utiliza esperas curtas (WebDriverWait) para melhorar a velocidade da raspagem.

Como o processo envolve milhares de registros, a execução pode levar alguns minutos.



👨‍💻 Autor

Projeto desenvolvido por Bruno Kemel 