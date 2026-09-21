def calcular_area(base, altura ):
    area = base * altura 
    return area

base_input = int(input("Ingrese la base del rectangulo:"))
altura_input = int(input("Ingrese la altura del rectangulo:"))

resultado = calcular_area(base_input, altura_input);

print(f"El area del rectangulo es:{resultado}")