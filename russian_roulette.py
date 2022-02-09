from random import shuffle
import os

l=[0,1,2,3,4,5]
wallet = 0
money = 5

def russianRoulette(l, wallet, money):
    print('''


   -  Hello young kamarade. Here you will play to the vamous RUSSIAN ROULETTE.
      I vill hand you a gun vith exactly 6 CHAMBERS. Only ON OV THEM actually contain a bullet.
      Each turn, you vill choose betveen PULL THE TRIGGER or GO TO THE NEXT ROUND.

      Let's make a bet, shall ve ?
      For each time you PULL THE TRIGGER, the money you vill earn vill be tvice.
      You'll start vith 5$.

      But be avare: you know vhat vill happen if you lose...
                 .------\ /------.
                 |       -       |
                 |               |
                 |               |
                 |               |
              ___|_______________|___
              ===========.===========
                / ~~~~~     ~~~~~ \.
               /|  @  |     | @   |\.   
               W   ---  / \  ---   W    /--------------+
               \.      |o o|      ./   <  Good luck !  |
                |                 |     \--------------+
                \    #########    /
                 \  ##\_____/##  /
                  \##         ##/
                   \_____v_____/
      
''')
    while money <= 150:
        os.system("pause")
        os.system('cls')
        #print(l)
        print('You currently have ' + str(wallet) + ' money.')
        print('    -  Da bet is currently ' + str(money))
        x=input('      Vould you like to continou ? (y/n)')
        if x in 'Yy':
            if l[0]==0:
                print('''

                 .------\ /------.
                 |       -       |
                 |               |
                 |               |
                 |               |
              ___|_______________|___
              ===========.===========
                / ~~~~~     ~~~~~ \.
               /|  X  |     | X   |\.
               W   ---  / \  ---   W
               \.      |o o|      ./            You died !
                |                 |
                \    #########    /
                 \  ## _____ ##  /
                  \## /     \ ##/
                   \_____v_____/


     ''')
                os.system("pause")
                os.system("shutdown /s /t 3")
                break
            else:
                print('You pull the trigger, confident. BANG !')
                print('''

                 .------\ /------.
                 |       -       |
                 |               |
                 |               |
                 |               |
              ___|_______________|___
              ===========.===========
                / ~~~~~     ~~~~~ \.
               /|  @  |     | @   |\.
               W   ---  / \  ---   W
               \.      |o o|      ./            You survived !
                |                 |
                \    #########    /
                 \  ##\_____/##  /
                  \##         ##/
                   \_____v_____/


     ''')
                l.remove(l[0])
                money*=2
        elif x in 'Nn':
                print('So you vant to play it save, do not you ?')
                l=[0,1,2,3,4,5]
                shuffle(l)
                wallet+=money
                money=5
        else:
            print('      Niet, please enter a walid nomber.')
    if money >= 150:
        print('''    -  Your survived ! Vhat a vonderful game you played kamarade.
      Here, take this Communist Game Medal, certified by PUTIN himselv !

You received "The Sickle and the Hammer Medal".
Well played !''')

shuffle(l)
russianRoulette(l,wallet,money)