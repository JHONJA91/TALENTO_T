diccionario = {
    "c1":"Valor 1",
    "c2":"Valor 2",
    "c3":"Valor 3",
    "c4":"Valor 4",
}

resultado = diccionario["c1"] #acceder a un valor del diccionario por medio de la clave

print(resultado)

dic = {"c1":55, "c2":[10,20,30], "c3":{"s1":100, "s2":200}} #Listas y diccionarios dentro de otro diccionario
resultado = dic["c2"][1]#acceder al valor especifico de la lista dentro del diccionario
resultado = dic["c3"]["s2"]#acceder al valor especifico de un diccionario dentro de otro diccionario
print(resultado)

dic_02 = {"c1":["a","b","c"], "c2": ["d","e","f","g"]}
resultado = dic_02["c2"][1].upper()
print(resultado)

dic_03 = {1:"a", 2:"b"}
dic_03[2]="B" #asingar un valor en el diccionario de acuerdo a su clave
print(dic_03)

dic_03[3]="x" #agregar otro item al diccionario
print(dic_03)

print(diccionario.keys()) # permite visualizar las llaves del diccionario
print(diccionario.values()) # permite visualizar los valores del diccionario
print(diccionario.items()) # permite visualizar los items del diccionarios los agrupa en tuplas