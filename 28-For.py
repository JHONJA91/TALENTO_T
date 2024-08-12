lista = ["a","b","c","d"]

for i in lista:
    print(f"Letra: {i}") 
    
    
for i in lista:
    numero_letra = lista.index(i)+1
    print(f"letra {numero_letra}: {i}")
    
lista2 = ["Pablo","Juan","Andrea","Lucia"]

for nombre in lista2:
    if nombre.startswith("L"):
        print(nombre)
    else:
        print(f"{nombre} no inicia con L")
    
for letra in "Python":
    print(letra)
    
    
for numero in [1,2,3,4]:
    print(numero)
    
    
for numero in (1,2,3,4,5):
    print(numero)
    
    
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
    
print("___________________")
    
dic = {"clave1":"a","clave2":"b","clave3":"c"}

for item in dic.values():
    print(item)
    
    
for item in dic.items():
    print(item)
    
for a,b in dic.items():
    print(a,b)
    