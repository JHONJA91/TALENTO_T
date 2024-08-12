lista = ["a","b","c"]

for i in enumerate(lista): #Enumerar los elementos de la lista y los muetra en la tupla
    print (i)
    
    
for indice,elemento in enumerate(lista):
    print(indice,elemento)
    
for indice,elemento in enumerate(range(1,10)):
    print(indice,elemento)
    
mis_tuplas = list(enumerate(lista))

print(mis_tuplas)

tuplas = list(enumerate("Python"))
print(tuplas)


lista_nombres = ["Mario","juan","Maria","Pedro"]

for i,nombre in enumerate(lista_nombres): #Enumerate devuelve los indices y los nombres 
    if nombre[0] == "M":
        print(f"{i} {nombre}")
    

