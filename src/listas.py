objetos = [1,"hola", True, ["Que tal"]]

#Agregar 
objetos.append("Claro")

#Borrar
objetos.pop(2)

for elemento in objetos:
    print(elemento)

#obtener lista al reves 
print(objetos[::-1])

# sumar listas
objetos2 = [1,2,"L", True]
resultado = objetos + objetos2
print(resultado)