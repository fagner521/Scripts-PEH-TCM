#!/bin/python3

#Listas tem []

filmes = ["Harry potter", "it a coisa"]
print(filmes[0])
print(filmes[1])
print(filmes[0:1])
print(filmes[:1])
print(filmes[0:])
print(filmes[-1])

print(len(filmes))
filmes.append("Exorcista")
print(filmes)

filmes.pop()
print(filmes)

filmes.pop(0)
print(filmes)