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
    "information"
]

def analisar_dados(endereco,dados):
    ip=endereco[0]
    porta=endereco[1]
    try:
        mensagem=dados.decode()
    except:
        mensagem="[os dados não puderam ser decodficados]"

    if ip not in contador_mensagem:
        contador_mensagem[ip]=0
    contador_mensagem[ip]+=1
    quantidade=contador_mensagem[ip]
    if quantidade>LIMITE_ALTO:
        nivel="ALTO"
    elif quantidade>LIMITE_MEDIO:
        nivel="MÉDIO"
    else:
        nivel="NORMAL"
    
    print()
    print(RED + "==================== MONITOR DE REDE ====================" + END)
    print(
        WHITE +
        "IP de origem:" +
        END,
        ip
    )

    print(
        WHITE +
        "PORTA de origem:" +
        END,
        endereco[1]
    )

    print(
        WHITE +
        "PROTOCOLO:" +
        END,
        "TCP"
    )

    print(
        WHITE +
        "TAMANHO:" +
        END,
        len(dados),
        "bytes"
    )

    print(
        WHITE +
        "mensagem deste ip:" +
        END,
        quantidade
    )

    print(
        WHITE +
        "NIVEL:" +
        END,
        nivel
    )

    print(
        WHITE +
        "conteudo" +
        END,
        mensagem
    )

    print(RED + "==========================================================" + END)
    
    if quantidade>LIMITE_ALTO:
        print()
        print(RED + "================= ALERTA DE SEGURANÇA ================" + END)
        print(RED + "            COMPORTAMENTO ANORMAL DETECTADO           " + END)
        
        print(
            WHITE +
            "IP de origem:" +
            END,
            ip
        )  
        print(
            WHITE +
            "quantidade" +
            END,
            quantidade
        )
        print(RED + "NÍVEL ALTO" + END)
        print()
   
    elif quantidade>LIMITE_MEDIO:
        print()
        print(RED + "================= ALERTA DE SEGURANÇA ================" + END)
        print(RED + "              MUITAS MENSAGENS RECEBIDAS              " + END)
        
        print(
            WHITE +
            "IP de origem:" +
            END,
            ip
        )  
        print(
            WHITE +
            "quantidade" +
            END,
            quantidade
        )
        print(RED + "NÍVEL MEDIO" + END)
        print()
    mensagem_minuscula=mensagem.lower()
    for palavra in PALAVRAS_ALERTA:
        if palavra in mensagem_minuscula:
            print()
            print(RED + "================= ALERTA DE SEGURANÇA ================" + END)
            print(
                WHITE +
                "palavra detectada" +
                END,
                palavra
            )
            print(
                WHITE +
                "IP de origem:" +
                END,
                ip
            )
            print(
                WHITE +
                "mensagem" +
                END,
                mensagem
            )    