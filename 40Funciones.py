def saludar_persona():
    '''  Esta funcion saluda a una persona
    '''
    print("Hola buenos días")
    
    
saludar_persona()

num1 = 0
num2 = 0

def sumar_enteros(num1,num2):
    num1 = int(input("Ingrea número 1: "))
    num2 = int(input("Ingrea número 2: "))
    
    return num1+num2
    #print (f"La suma de {num1} + {num2} es {num1+num2}")
    
resutado = sumar_enteros(num1,num2)
print (resutado)

def mult(num1,num2):
    num1 = int(input("Ingrea número 1: "))
    num2 = int(input("Ingrea número 2: "))
    
    return num1*num2
    #print (f"La suma de {num1} + {num2} es {num1+num2}")
    
resutado = mult(num1,num2)
print (resutado)

def analizar_3_cifras(numero):
    return numero in range(100,1000)

resultado2 = analizar_3_cifras(258)
print(resultado2)

def analizar_3_cifras2(lista):
    lista_3cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3cifras.append(n)
        else:
            pass
    
    return lista_3cifras

resultado3 =analizar_3_cifras2([580,22,1000,457])
print(resultado3)


    