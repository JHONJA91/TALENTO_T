#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("Señor Usuario escriba una palabra: ")
#Solución N 1 
print((palabra+"\n")*10)

#Solución N 2
i = 10
while i <= 10 and i > 0:
    print(palabra)
    i -= 1
    
#Solución N 3
for x in range(10):
    print(f"Palabra en la posición {x+1} : {palabra}")
    

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Por Favor Ingrese su edad: "))
#Solución N 1 
for años in range(edad):
    print(f"Has cumplido {años+1} años")
    
print("________________________________________")
 #Solución N 2   
while edad > 0:
    print(f"Año: {edad}")
    edad -=1
    
    
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

num_positivo = int(input("Por favor ingrese un número entero Positivo: "))

 #Solución N 1
for i in range(1,num_positivo+1,2):
    if i != num_positivo:
        print(f"Número impar: {i}", end=", ")
    else:
        print(f"Número impar: {i}", end="")#Evita imprimir la coma al final
        
print()
        
 #Solución N 2  
for i in range(1,num_positivo+1,2):
    if i %2 == 1 and i != num_positivo:
        print(i, end=", ")
    else:
        print(i, end="") #Evita imprimir la coma al final
        
###Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
       
num_positivo = int(input("Por favor ingrese un número entero Positivo: "))

 #Solución N 1 
while num_positivo >= 0:
    print(num_positivo,end=",")
    num_positivo -=1
    
print()   

 #Solución N 2 
for i in range(num_positivo,-1,-1):
     print(num_positivo,end=",")