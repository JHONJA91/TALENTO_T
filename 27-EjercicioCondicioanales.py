num1 = int(input("Por favor ingrese un número"))
num2 = int(input("Por favor ingrese otro número"))

if num1 > num2: 
    print(f"{num1} es mayor que {num2}") 
elif num2 > num1:
    print(f"{num2} es mayor que {num1}") 
else:
    print(f"{num1} y {num2} Son iguales")