#!/bin/python3

#Relações com booleanos

maiorque = 7 > 5
menorque = 5 < 7
maiorouigualque = 7 >= 7
menorouigualque = 7 <= 7

teste_and = (7>5) and (5<8)
teste_and2 = (7>5) and (5 > 8)
teste_or = (7>5) or (5 > 8)
teste_or2 = (7 < 5) or (5 > 8)
teste_not = not True

print(maiorque, menorque,maiorouigualque,menorouigualque)
print(teste_and,teste_and2,teste_or,teste_or2,teste_not)