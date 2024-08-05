mi_texto = input("Por favor Ingrese un Texto: ").lower()
letras = input("Por favor Ingrese 3 letras a su elección: ").lower()

lista = list(letras)


print(f"La letra {lista[0]} se encuentra {mi_texto.count(lista[0])} Veces en el Texto ingresado")
print(f"La letra {lista[1]} se encuentra {mi_texto.count(lista[1])} Veces en el Texto ingresado")
print(f"La letra {lista[2]} se encuentra {mi_texto.count(lista[2])} Veces en el Texto ingresado")

print(f"El texto ingresado tiene {len(mi_texto.split())} Palabras")

print(f"La primera letra del texto es: {mi_texto[0]} y la ultima es: {mi_texto[-1]}")

print(f"El texto invertido es: {mi_texto[::-1]}")


consulta = ("python" in mi_texto)


diccionario = {True:"SI", False:"NO"}

print(f" La palabra Python {diccionario[consulta]} Se encuentra en el texto digitado")