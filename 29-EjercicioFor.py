alumnos_clase = ["Maira", "Jose", "Carlos", "Martina", "Isabel", "Tomas", "Daniela"]

for i in alumnos_clase:
    print(f"Hola {i}")
    

numeros = [1,5,8,7,6]
sum_numeros = 0

for x in numeros:
    sum_numeros = sum_numeros+x
    #sum_numeros += x #Otra forma de aculular la suma en la variable
   

print(f" La suma total es {sum_numeros}")


pares = 0
impares = 0
for y in numeros:
    if y%2==0:
        pares += y
    else:
        impares += y
        
print(f"La suma de pares es {pares}")
print(f"La suma de impares es {impares}")




