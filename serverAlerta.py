import socket
import threading

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"

END = "\033[0m"

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(("0.0.0.0", 5000))

servidor.listen()

print(CYAN + "Servidor iniciado!" + END)
print(YELLOW + "Esperando conexões..." + END)
print()

clientes=[]
contador_mensagem={}
LIMITE_MEDIO=5
LIMITE_ALTO=10

PALAVRAS_ALERTA=[
    "senha",
    "password",
    "dados",
    "inform"
]