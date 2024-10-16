from biblioteca import *

while True:
    x = int(input("Digite 1 para Gravar um Texto\n"
                  "Digite 2 para ler o texto gravado\n"
                  "Digite 3 para sair do sistema\n"
                  "Escolha uma opção: "))
    if x == 1:
        with open("registro.txt", "a") as arquivo:
            texto = input("Digite um texto: ")
            arquivo.write(f"{texto}\n")
    if x == 2:
        with open("registro.txt", "r") as arquivo2:
            texto = arquivo2.read()
            print(texto)
    if x == 3:
        break
