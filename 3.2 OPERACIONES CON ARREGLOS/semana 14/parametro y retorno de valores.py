# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=20):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
def main():
    # Llamada a la función solo con el monto total (usando el valor predeterminado de 10%)
    monto_total_1 = 100  # Ejemplo de monto
    descuento_1 = calcular_descuento(monto_total_1)
    monto_final_1 = monto_total_1 - descuento_1
    print(f"Monto Total: ${monto_total_1}, Descuento: ${descuento_1}, Monto Final: ${monto_final_1}")

    # Llamada a la función con el monto total y un porcentaje de descuento específico
    monto_total_2 = 500  # Otro ejemplo de monto
    porcentaje_descuento_2 = 20  # Ejemplo de porcentaje de descuento
    descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
    monto_final_2 = monto_total_2 - descuento_2
    print(f"Monto Total: ${monto_total_2}, Descuento: ${descuento_2}, Monto Final: ${monto_final_2}")

if __name__ == "__main__":
    main()