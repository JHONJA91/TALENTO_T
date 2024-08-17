from random import * #Con * se imoprta todas las funciones de la libreria random

aleatorio = randint(1,50)


aleatorio = round(uniform(1,5),2)

aleatorio = random() # Devuelve un decimal entre 0 y 1


lista_colores = ["Azul", "Verde", "Rojo", "Amarillo"]
aleatorio = choice(lista_colores) #Devuelve un elemento de la lista aleatoreamente

lista_numeros = list(range(1,50,5))
shuffle(lista_numeros) #Modifica el orden de la lista
print(lista_numeros)





