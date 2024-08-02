texto = "Esto es un texto en Python"
resultado = texto.upper() # Mayúsculas
print(resultado)

resultado = texto.lower() #Minúsculas
print(resultado)

resultado = texto[3].upper()
print(resultado)

resultado = texto[11:16].upper()
print(resultado)

resultado = texto.split() #Separa por defecto con espacios 
print(resultado)

resultado = texto.split("t") #Con separador especifico
print(resultado)

palabra1 = "Aprender"
palabra2 = "Python"
palabra3 = "es"
palabra4 = "genial"

frase = "_".join([palabra1,palabra2,palabra3,palabra4]) #Concatenar palabras, al inicio se antepone el separador entre palabras
print(frase)

resultado = texto.find("j") #Find muestra el posicionamiento y cuando no lo encuentra muestra -1 a diferencia de index que muestra error
print(resultado)

vari = texto.replace("texto", "Text")
print(vari)
