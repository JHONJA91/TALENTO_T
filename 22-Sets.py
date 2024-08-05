mi_set = set([1,2,3,4,5,6]) #Forma 1 de implementar un set o conjunto
mi_set = set({1,2,3,4,5,6}) #Forma 2 de implementar un set o conjunto
mi_set = set((1,2,3,4,5,6,)) #Forma 3 de implementar un set o conjunto

mi_set = {1,2,3,4,5} #Forma 4 de implementar un set o conjunto, es la mas utilizada
print(type(mi_set))
print(mi_set)

print(len(mi_set)) #Obterner la longitud del conjunto

conjunto = {1,2,3,4,5,6,7,8,9,1,1} #Al imprimir un set se omiten los elementos duplicados
print(conjunto) 

print(2 in conjunto) #Buscar el 2 en nusetro conjunto devuelve un valor booleno

s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1.union(s2) #Unir 2 conjuntos con la funcion union()
print(s3)

s1.add(4) #Se adiciona el valor 4 al set S1
print(s1)

s1.remove(3) #Eliminar un elemento del set en este caso se elimina el  valor 3
print(s1)

s1.clear() #Limpia el set y queda un conjunto vacio