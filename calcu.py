# Función para calcular el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Función para obtener recomendaciones de salud
def obtener_recomendaciones(imc):
    if imc < 18.5:
        return "Peso insuficiente. Se recomienda una dieta equilibrada y ejercicio regular."
    elif imc < 24.9:
        return "Peso saludable. Mantén una dieta equilibrada y ejercicio regular."
    elif imc < 29.9:
        return "Sobrepeso. Consulta a un médico y considera cambios en tu dieta y estilo de vida."
    else:
        return "Obesidad. Es importante buscar atención médica y hacer cambios significativos en tu estilo de vida."

# Pedir información de la persona
nombre = input("Nombre completo: ")
edad = int(input("Edad: "))
peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))

# Calcular el IMC
imc = calcular_imc(peso, altura)

# Obtener recomendaciones de salud
recomendaciones = obtener_recomendaciones(imc)

# Mostrar resultados
print("\nResultados:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"IMC: {imc:.2f}")
print("Recomendaciones de salud:")
print(recomendaciones)



