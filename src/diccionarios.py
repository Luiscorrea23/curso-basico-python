my_diccionarios = {
    "Luis": 27,
    "Genesis": 25,
    "Carla" :16
}

#Accder a los valores
my_diccionarios["Carla"]

#Agregar a diccionario 
my_diccionarios["Clave"] = "Valor"

#iterar en "Claves"
for i in my_diccionarios.keys():
    print(i)


#iterar sobre los valores

for i in my_diccionarios.values():
    print(i)

#iterar sobre valores y claves

for nombre, edad in my_diccionarios.items():
    print(nombre, edad)