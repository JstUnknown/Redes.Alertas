from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"

END = "\033[0m"
EMAIL= "email@gmail.com"
URL=""


senhas=[
    "123456",
    "admin",
    "senha123",
    "qwerty",
    "wasd",
    "olivia2011",
    "naoseimminhasenha",
    "senha",
    "naoseioqescrever",
    "nao.entre.na.minha.conta"
]

print(RED + "=====================================================" + END)
print(RED + "             SIMULAÇÃO DE AUTENTICAÇÃO               " + END)
print(RED + "==================================================" + END)
opcoes=Options()
navegador=webdriver.Chrome(options=opcoes)
print(RED+"[INFO]abrindo o navegador..."+END)
navegador.get(URL)
time.sleep(2)
print(RED+"[INFO]pagina de login carregada"+END)
print(RED+"[INFO]EMAIL:{EMAIL}"+END)
for senha in senhas:
    campo_email=navegador.find_element(By.ID,"email")
    campo_senha=navegador.find_element(By.ID,"senha")
    campo_email.clear()
    campo_senha.clear()
    campo_email.send_keys(EMAIL)
    campo_senha.send_keys(senha)
    print(f"[TESTE]" 
    f"tentando: {senha}")
    botao=navegador.find_element(By.TAG_NAME,"buttom")
    botao.click()
    time.sleep(0.7)
    mensagem=navegador.find_element(By.ID,"mensagem").text
    if mensagem=="acesso concedido":
        print(f"[ACESSO CONCEDIDO]")
        print(f"senha encontrada: {senha}")
        break
    else:
        print("negado")
    time.sleep(0.5)
else:
    print("senha não encontrada")
time.sleep(3)
navegador.quit()