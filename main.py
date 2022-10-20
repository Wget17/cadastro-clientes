import sys
import time
import os

while True:


    def banner():

        print("""

    ____          _           _               ____              _   ___  
    / ___|__ _  __| | __ _ ___| |_ _ __ ___   |  _ \ _ __ ___   / | / _ \ 
    | |   / _` |/ _` |/ _` / __| __| '__/ _ \  | |_) | '__/ _ \  | || | | |
    | |__| (_| | (_| | (_| \__ \ |_| | | (_) | |  __/| | | (_) | | || |_| |
    \____\__,_|\__,_|\__,_|___/\__|_|  \___/  |_|   |_|  \___/  |_(_)___/ 
                                                                        

        """)

    banner()
    #Banner pode ser modificado ou apagado..vai da sua escolha


    digite = input("Digite o nome do cliente: ") 
    #Aqui vai pegar o nome do cliente


    cpf = input("Digite o CPF do cliente: ")
    #Aqui vai pegar o CPF 


    cep = input("Digite aqui o endereço do cliente: ")
    #Aqui vair pegar o CEP


    nome_sair_txt = input("Digite o nome do arquivo final desse cliente: ")
    #Aqui vc vai digitar o nome do arquivo de saida do cliente > ele vai ser jogado pra um TXT


    gravar = open(f"{nome_sair_txt}.txt", "w")
    #Aqui vai escrever o aequivo TXT


    gravar.write(f"{digite}\n{cpf}\n{cep}")
    #Aqui vai gravar todo os dados do cliente no TXT


    gravar.close()
    #Aqui vai fechar o arquivo TXT


    print("Òtimo, os dados do cliente está sendo salvo no banco de dados....")
    time.sleep(3)
    print("Blz, dados salvo....até mais")
    #Mensagem final

    
    maquina = (sys.platform)
    if maquina == "linux":
        os.system("clear")

    elif maquina == "windows":
        os.system("cls")

    
   #Esse bloco de código vai fazer a lempeza no terminal, conforme o seu sistema operacional



