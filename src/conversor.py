def conversor(cantidad_a_cambiar, valor_dolar):
    conversor = round(cantidad_a_cambiar/valor_dolar,2)
    print("Tienes " + str(conversor)+ " $")



menu = """
    Bienvenido al conversor de monedas a dolares
    1 - Bolivares
    2 - Pesos Argentinos
    3 - Pesos argentinos

    Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor(5.7, 400)
elif opcion == 2:
   conversor(3.7, 400)
elif opcion == 3:
    conversor(5.7, 400)
else:
    print("Elige una opción correcta")
