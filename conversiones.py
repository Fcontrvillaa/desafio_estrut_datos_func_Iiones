import sys

if len(sys.argv) != 5:
    print(" El comando necesita la siguiente estructura: python conversiones.py <tasa_sol> <tasa_peso_arg> <tasa_dolar_usd> <cantidad_peso_cl>")
    sys.exit(1)


try:
    # Captura las tasas de conversión
    sol = float(sys.argv[1])
    peso_argentino = float(sys.argv[2])
    dolar_americano = float(sys.argv[3])
    # captura monto en Pesos Chilenos a convertir
    peso_cl = float(sys.argv[4])

    #print(f"sol : {sol}, Peso Argentino : {peso_argentino}, Dolar Americano : {dolar_americano}, peso Cl : {peso_cl}")

    print(f"Los {peso_cl:.0f} pesos, equivalen a: ")

    print(f"{sol*peso_cl:.2f} Soles")
    print(f"{peso_argentino*peso_cl:.2f} Pesos Argentinos")
    print(f"{dolar_americano*peso_cl:.2f} Dolares Americanos")

except ValueError:
    print("Error: Asegúrate de que todos los valores sean números válidos.")
    sys.exit(1)