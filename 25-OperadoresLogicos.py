a,b,c = (10,5,15)

comparacion = 4 <5 <6
comparacion = 4 < 5 and 5 < 6
print(comparacion) 

comparacion = 55 == 55 and "Perro" == "Perro" #Verdadesro
print(comparacion) 

comparacion = 55 != 55 and "Perro" == "Perro" # Falso
print(comparacion)

comparacion = 55 != 55 or "Perro" == "Perro" # Verdadero
print(comparacion)

texto = "Esta frase es breve"

comparacion = ("frase" in texto) and ("python" in texto) #Falso
comparacion = ("frase" in texto) or ("python" in texto) #Verdadero

comparacion = not "a" == "a" #Falso con la negacion antepuesta

