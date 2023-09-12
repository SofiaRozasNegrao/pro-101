import random

roll= str(input("Quer girar o dado: "))

def roll2():
    roll_A= str(input("Se quiser jogar novamente digite 'S', senão digite 'N': "))

def roll_the_dice(): 
    while roll=="sim":
        dice=random.randint(1,6)
        print(dice)
        print(roll2())

if roll=="sim":
    roll_the_dice()
elif roll=="não":
    print("Ok")

def roll_again():
    roll2()
    if roll2=="S":
        roll_the_dice()
    elif roll2=="N":
        print("Ok")
       