mi_lista = ["a","b","c","d"]
mi_lista2 = ["e","f","g","h"]
print(type(mi_lista))
print(len(mi_lista))
resultado = mi_lista[2]
print(resultado)
resultado = mi_lista[0:2] # fragmenta la lista
print(resultado)

print(mi_lista+mi_lista2) #concatena listas

mi_lista[0]="A" #Reemplaza el valor de la lista en el posicionamiento [0]
print(mi_lista)

mi_lista.append("E") #append adiciona valores a la lista
print(mi_lista)

mi_lista.insert(2,"Hola") #Insert permite adicionar valores en una posicióin exacta de la lista
print(mi_lista)

mi_lista.pop()#pop sin parametro elimina el primer elemento de la lista
print(mi_lista)

mi_lista.pop(0)#pop con parametro elimina la posicion de la lista especifada
print(mi_lista)

lista3 = ["z","a","j"]
lista3.sort() #La funcion sort() ordena la lista
print(lista3)

lista4 = [100,50,200,15]
lista4.sort() #La funcion sort() ordena la lista de menor a mayor
print(lista4)

lista4.reverse() #La funcion reverse() ordena la lista de mayor a menor
print(lista4)

