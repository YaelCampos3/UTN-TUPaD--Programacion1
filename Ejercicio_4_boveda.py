energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

#Pedir nombre del agente y validar que solo contenga letras
nombre = input("Ingrese su nombre:")

while not nombre.isalpha():
    nombre = input("Datos no válidos. Ingrese su nombre: ")

#Se asignan variables para las forzadas continuas y el bloqueo
forzadas_seguidas = 0 
bloqueado = False

#Iniciamos el bucle del estado y menu del juego. Validamos la continuidad del juego.
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print(f"""
----Estado----
Agente: {nombre}
Energía: {energia}
Tiempo: {tiempo} 
Cerraduras abiertas: {cerraduras_abiertas}/3
Alarma activada: {alarma}

----Menú----
1. Forzar cerradura
2. Hackear panel
3. Descansar

""")
    #Se solicita la opción del menú y se valida que sea un dígito, se convierte a entero y se corrobora que sea una opción válida.
    opcion = input("Ingrese la opción deseada: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            opcion = input("Error. Debe ingresar un número válido.")
            
        
    opcion_int = int(opcion)  

    #Definimos la opción 1 del menú y se modifican las variables iniciales.
    if opcion_int == 1:
        energia -= 20
        tiempo -= 2
        forzadas_seguidas += 1

        #Se implementa la regla antispam de forzadas continuas.
        if forzadas_seguidas == 3:
            alarma = True
            print("Alarma activada. La cerradura se trabó")

        else:
            #Se valida la energía y el riesgo de alarma
            if energia < 40:
                print("Riesgo de alarma.")
                numero = input("Ingrese un número del 1 al 3: ")

                #Se valida que el número ingresado sea un dígito y que esté entre 1 y 3, caso contrario se pide nuevamente.
                while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                    numero = input("Error. Debe ingresar un número del 1 al 3.")

                numero_int = int(numero)

                #Se activa la alarma si el usuario ingresa el número 3.
                if numero_int == 3:
                    alarma = True
                    print("Alarma activada. La cerradura se trabó.")

            #Si no se activa la alarma, se incrementa las cerraduras abiertas.
            if not alarma:
                cerraduras_abiertas += 1

    #Definimos la opción 2 y se modifican las variables iniciales.
    elif opcion_int == 2:
        energia -= 10
        tiempo -= 3
        #Se reinician las forzadas seguidas
        forzadas_seguidas = 0

        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso} de 4: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Se ha abierto una cerradura.")

    #Se define la opción 3 y se modifican las variables iniciales
    elif opcion_int == 3:
        #Se reinician nuevamente las forzadas seguidas
        forzadas_seguidas = 0
        energia += 15
        #La energía no puede ser mayor a 100.
        if energia > 100:
            energia = 100
            print("Energía máxima.")
        tiempo -= 1
        #La energía disminuye si la alarma está activa.
        if alarma:
            energia -= 10
    #Se corrobora el bloqueo
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True

#Se evaluan los resultados finales del juego
if cerraduras_abiertas == 3:
    print(f"¡Felicidades {nombre}! Has logrado abrir la bóveda.")

elif bloqueado:
    print("Derrota. No ha logrado abrir la bóveda.")

elif energia <= 0 or tiempo <= 0:
    print("Derrota. Se han agotado los recursos para abrir la bóveda.")
