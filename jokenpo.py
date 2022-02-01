import random
import pandas as pd
import time
import sys
from colorama import Fore, Style

def placar(ponto_usario, ponto_oponente):
    df = pd.DataFrame({'# -- USER':[int(ponto_usuario)], 'PC -- #':[int(ponto_oponente)]})
                       
    print(Fore.BLUE + df.to_string(index=False))
    print(Style.RESET_ALL)
    
    time.sleep(1)
    
ponto_usuario = 0
ponto_oponente = 0

escolhas = dict({'A':'Pedra', 'B':'Papel', 'C':'Tesoura'})


while True:
    escolhaUsuario = (input("Escolha sua jogada! [A]Pedra, [B]Papel, [C]Tesoura")).upper()
    
    if escolhaUsuario == 'SAIR':
        print('Vamos ver o placar final!')
        placar(ponto_usuario, ponto_oponente)
        if ponto_usuario<ponto_oponente:
            print("Poxa vida, não foi dessa vez. Tente novamente")
            sys.exit()
        else:
            print("Parabéns, voce brocou!")
            sys.exit()
            
    escolhaOponente = random.choice(list(escolhas.keys()))
    
    if escolhaOponente == escolhaUsuario:
            print("Empate! ")
            placar(ponto_usuario, ponto_oponente)
        
        # Caso contrário...
    elif escolhaOponente == 'A' and escolhaUsuario == 'C':
        print("Tesoura é mais forte que Pedra! Eu ganhei!")
        ponto_oponente += 1
        placar(ponto_usuario, ponto_oponente)
        
    
    elif escolhaOponente == 'C' and escolhaUsuario == 'B':
        print("Tesoura é mais forte que Papel! Eu ganhei! ")
        ponto_oponente += 1
        placar(ponto_usuario, ponto_oponente)
        
    
    elif escolhaOponente == 'B' and escolhaUsuario == 'A':
        print("Pedra é mais forte que Papel! Eu ganhei! ")
        ponto_oponente += 1
        placar(ponto_usuario, ponto_oponente)
        
    
    else:
        print("Você ganhou!")
        ponto_usuario += 1
        placar(ponto_usuario, ponto_oponente)
    
    
    
            