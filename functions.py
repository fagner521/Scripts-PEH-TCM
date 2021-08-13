#!/bin/python3

#Alguns exemplos de função

def Quem_Sou_Eu(): #isso é uma função
    nome = "Fagner"
    anos = 86
    print("Meu nome é %s eu tenho %s anos" %(nome, anos))

Quem_Sou_Eu()

#passando parametros para função

def Soma_Cem(numero):
    print(int(numero) + 100)

Soma_Cem(150)