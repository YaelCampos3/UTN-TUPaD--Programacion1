#Solicitud de nombre y se verifica que sean caracteres válidos
nombre = input("Ingrese su nombre: ")

while not nombre.isalpha():
    nombre = input("Caracteres incorrectos. Ingrese su nombre: ")

#Se solicita la cantidad de productos y se verifica que sean números positivos
cantidad = input("Ingrese la cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Error, debe ingresar una cantidad válida: ")

cantidad = int(cantidad)

#Se definen las variables contadores
total_con_descuento = 0
total_sin_descuento = 0
total_ahorro = 0

#Generamos el bucle para cada producto
for producto in range(cantidad):

    #Solicitamos el precio para cada producto, validamos que sean dígitos y lo convertimos en entero
    while True:
        precio = input("Ingrese el precio: ")
        if precio.isdigit():
            precio = int(precio)
            break
        print("Error. Debe ingresar un número válido ")

    #definimos precio base (para los precios sin descuento) y contador de porcentaje de descuento
    precio_base = precio
    porcentaje = 0

    #Se consulta para cada producto si se debe o no aplicar descuento
    while True:
        descuento = input(f"Producto {producto +1} ¿Tiene descuento? (S/N): ").lower()        

        if descuento == "s":
            porcentaje = (precio * 10 /100)
            precio -= porcentaje
            break

        elif descuento == "n":
            break
        else:
            print("Error. Debe ingresar una opción válida 'S' o 'N'")

    #Se actualizan los contadores 
    total_con_descuento += precio
    total_sin_descuento += precio_base
    total_ahorro += porcentaje
    
promedio = total_con_descuento / cantidad

print(f"""
Cliente: {nombre.capitalize()}
Cantidad de productos: {cantidad}
El total con descuentos es: ${total_con_descuento:.2f}
El total sin descuento es: ${total_sin_descuento:.2f}
El total ahorrado es de: ${total_ahorro:.2f}
El promedio por producto es: ${promedio:.2f}
""")





    