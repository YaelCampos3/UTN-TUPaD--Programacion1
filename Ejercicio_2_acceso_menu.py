# Se definen las variables para el acceso
usuario_correcto = "alumno"
clave_correcta = "python123"

# Se inicia contador y variable bandera
intentos = 0
salir = False

# Se valida el correcto inicio de sesión y posteriormente se muestra el menú
while intentos < 3 and salir == False:
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        
        print("""
-----Menú-----
1. Estado de inscripción.
2. Cambiar clave.
3. Mensaje motivacional.
4. Salir
""")    
        # Se solicita seleccionar opción del menú, se valida que se ingrese un dígito que esté en el menú.
        while True:
            opcion = input("Seleccione una opción: ")
            if not opcion.isdigit():
                print("Error. Debe ingresar un número válido.")
                continue
            else:
                opcion_int = int(opcion)

            if opcion_int < 1 or opcion_int > 4:
                print("Error. Opción fuera de rango.")
                continue

            # Se define la opción 1
            elif opcion_int == 1:
                print("Inscripto.")

            # Se define la opción 2, se solicita nueva clave validando que tenga mínimo 6 caracteres y su confirmación coincida
            elif opcion_int == 2:
                while True:
                    nueva_clave = input("Ingrese nueva clave: ")
                    

                    if len(nueva_clave) < 6:
                        print("La nueva clave debe tener mínimo 6 caracteres.")
                        continue

                    confirmacion = input("Confirme la nueva clave: ")

                    if nueva_clave == confirmacion:
                        clave_correcta = nueva_clave
                        print("Cambio de clave confirmado.")
                        break
                    else:
                        print("La clave no coincide. Ingrese nuevamente la clave y su confirmación")
                        continue

            # Se define opción 3
            elif opcion_int == 3:
                print("El esfuerzo de hoy es tu éxito de mañana.")

            # Se define opción 4 y finalización del programa
            elif opcion_int == 4:
                print("Gracias por usar el sistema. ¡Hasta pronto!")
                salir = True
                break

                
    # Se incrementa el contador para los errores en el inicio de sesión
    else:
        intentos +=1
        print("Usuario y/o contraseña incorrecta.")

# Se define la condición del bloqueo de cuenta
if intentos == 3:
    print("Cuenta bloqueada.")

