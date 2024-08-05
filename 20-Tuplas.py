mi_tupla = (1,2,3,4)
print(type(mi_tupla))


print(mi_tupla[0])

#mi_tupla[0] = 7 # Las tuplas no permiten asignar valores

mi_tupla2 = (1,2,(2,4),6)
print(mi_tupla2[2][1])

mi_tupla = list(mi_tupla) #Castear de tupla a lista


t = (1,"Hola",1.2)

x,y,z = t

print (x,y,z)

print(len(t))

print(t.count(1)) #Cuenta cuantas veces esta el 1 denttro de la tupla

