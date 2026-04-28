import random
import time

vida_vc = 100
vida_Eivor = 150

print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")


                      JOGO JOGAVEL MUITO GAME GAYMOSO JOGO DE JOGADOR NATO                     




                                      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
                                      █--------MENU---------█
                                      █-------1. JOGAR------█
                                      █-------2. SAIR-------█
                                      █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█




░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n""")



escolha1 = input()

if escolha1 == "1":
    print(""" ... Iniciando ... """)
    time.sleep(2)
else:

    print(""" ... Encerrando ... """)
    exit()





# sempre 16 linhas de espaço

print(
    """░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    
         *    .--.                  *                *                     *                        .--.
          _..(    ).                                                                          . (    ).._
      .:  '.___.__)__)                        *                                                 (___.__)__.'  :.
     *       *               *                       *  *                     *           * 
    
    
                                                  O grande Eivor - 100% hp                                                                   
                                                                                                [   ]                          
                                                                                                  |                         
                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                 /|              
                                                                                      /   /     / |                           
                                                                                     ( * )     /                                                                                                            
                                                                                       _|_ --                                  
                                                                                      / |                                                                                                                  
                                                                                     /  |\\                                    
                                                                                    /   |                                                                                                
                               O —|)                                                   / \\                                   
                              /|                                                      |   |                                   
    __________________________/_\\____________________________________________________|___|__________________________________                                                 
      __            --                      --                     -              --                  -             -                 
    -    -                    --                     --         -                            -                     --    -           
                    -                       -                               -                                   -               
    -
    
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n""")

while vida_Eivor > 0 and vida_vc > 0:

    print(f"\n--- STATUS: Você [HP: {vida_vc}] | Eivor [HP: {vida_Eivor}] ---")

    print("""
                             |=================================================|                                                                              
                             |                                                 |
                             |                   1. Atacar                     |
                             |                   2. Fugir                      |
                             |                   3. Defender                   |
                             |                                                 |
                             |=================================================|
                             """)

    escolha = input("Ação: ")

    eivor_vai_atacar = False
    dano_recebido_reduzido = False

    if escolha == "1":
        dano = random.randint(10, 25)
        vida_Eivor -= dano
        print(f"\n Você atacou O grande Eivor e causou {dano} de dano")
        eivor_vai_atacar = True
        time.sleep(2)

    elif escolha == "3":
        print("\nVocê se prepara para o golpe, levantando seu escudo!")
        time.sleep(2)
        dano_recebido_reduzido = Trues
        if random.randint(1, 6) == 2:
            eivor_vai_atacar = True
        else:
            print("Eivor hesitou e não te atacou neste turno!")
            time.sleep(2)

    elif escolha == "2":
        print("Covardão betinha!")
        break
    else:
        print("Escolha inválida!")
        continue

    if eivor_vai_atacar and vida_Eivor > 0:
        danoE = random.randint(0, 40)

        if dano_recebido_reduzido:
            danoE //= 3
            vida_vc -=danoE
            print(f"Sua defesa foi solida, porem eivor e muito forte você sofreu {danoE} de dano")
            time.sleep(2)
        else:
            vida_vc -= danoE
            print(f"Eivor balança seu machado e causou {danoE} de dano!")
            time.sleep(2)

if vida_vc <= 0:
    print("\nVocê foi derrotado por Eivor... Valhalla espera por ele, não por você.")
elif vida_Eivor <= 0:
    print("\n você se ergueu contra Eivor e voltou Vitorioso Parabens!!.")
    print(
        """░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

             *    .--.                  *                *                     *                        .--.
              _..(    ).                                                                          . (    ).._
          .:  '.___.__)__)                        *                                                 (___.__)__.'  :.
         *       *               *                       *  *                     *           * 


                                                      Você Venceu                                                                  
                                                                                                                            
                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                  
                                                                                                                                                                                                   
                                                                                                        |                       
                                                                                                        |                                                                                 
                                   O |                                                                  |                      
                                  /|                                     /  /                           |                      
        __________________________/_\\__________________________________( @ )_________________________[   ]____________________                                                 
          __            --                      --                     -              --                  -             -                 
        -    -                    --                     --         -                            -                     --    -           
                        -                       -                               -                                   -               
        -

        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n""")





