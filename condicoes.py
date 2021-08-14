#!/bin/python3

def drink(money):
    if money >= 2:
        print( "Tome um drink")
    else:
        print( "Sem grana")
drink(3)
drink(1)

def alcool(anos, dinheiro):
    if (anos >= 18) and (dinheiro >= 5):
        print( "Pode dar um gole")
    elif (anos >= 18) and (dinheiro < 5):
        print( "Sem grana")
    elif (anos < 18) and (dinheiro >= 5):
        print( "Menor n bebe")
    else:
        print( "De menor e sem grana")

dinheiro = input("Quanto vc tem ?")
anos = input("Qual sua idade ?")
try:
    alcool(int(anos), int(dinheiro))
except Exception as e:
    print (str(e))
    print("Digite numeros")
