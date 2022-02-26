import random
import os


erros=0
sorteado=random.randrange(0,100)
print("\033[1;30;40m JOGO DE ADIVINHAÇÃO ")
jogador=int(input("\033[1;34;40m Digite seu numero: ")) 

while(sorteado!=jogador):
    os.system("cls")
    if(sorteado>jogador):
        print('ERRO, o numero e maior')
    elif(sorteado<jogador):
        print("ERRO,o numero e menor")
    erros+=1
    jogador=int(input("Digite seu numero: ")) 
print('Numero ', jogador, ', voce acertou em ', erros+1 , ' tentativas' )

