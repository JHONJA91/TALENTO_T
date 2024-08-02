mi_dic = {
    "nombre":"Karen",
    "apellido":"Jurgens",
    "edad":35,
    "ocupacion":"Periodista",
}

print(mi_dic)

mi_dic["ocupacion"]="Editora"
mi_dic["pais"]="Colombia"

print(mi_dic)

#Pruebas deportivas con diccionarios

prueba_deportiva = {
    'Jhon':1200,
    'Julian':1108,
    'Mario':989,
    'Alex':1058,
    'Luis':1289,
    'Area': ['Futbol','Baloncesto','Boleybol']
    }

puntaje = prueba_deportiva
area_dep = prueba_deportiva["Area"][1]

print(f"Esta es la prueba de Julian: {puntaje["Julian"]}")
print(f"El Area deportiva es: {area_dep}")