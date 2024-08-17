palabra = "Python"

lista = []

for i in palabra:
    lista.append(i)
print(lista)


lista = [i for i in palabra]
print(lista)

lista2 = [pares for pares in range(0,21,2)]
print(lista2)

lista2 = [pares  if pares*2 > 10 else "No" for pares in range(0,21,2)]
print(lista2)