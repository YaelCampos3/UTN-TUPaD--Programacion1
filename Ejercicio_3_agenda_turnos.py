#Pedir nombre de operador
nombre = input("Ingrese su nombre: ")

while not nombre.isalpha():
    nombre = input("Datos no válidos. Ingrese su nombre: ")

#Se definen las variables de los turnos por cada día.
lunes_1 = ""
lunes_2 = ""
lunes_3 = ""
lunes_4 = ""

martes_1 = ""
martes_2 = ""
martes_3 = ""

#Menú
while True:
    print("""
----Menú----
1. Reservar turno
2. Cancelar turno (por nombre)
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema
""")
    #Solicitamos seleccionar opción del menú y se valida que sean dígitos.
    opcion = input("Ingrese la opción deseada: ")
    if not opcion.isdigit():
        print("Error. Debe ingresar un número válido")
        continue

    #Validado el dígito se convierte en entero y se verifica la opción ingresada
    opcion_int = int(opcion)  

    if opcion_int < 1 or opcion_int > 5:
        print("Error. Debe seleccionar una opción entre 1 y 5")
        continue
    
    #Se solicita seleccionar el día y se corrobora que se ingresen dígitos dentro del rango correcto
    if opcion_int == 1:
        while True:
            dia = input("""
                    Seleccione el día:
                    1. Lunes
                    2. Martes
                    """)
            if not dia.isdigit():
                print("Error, debe ingresar 1 o 2.")
                continue

            
            dia_int = int(dia)

            if dia_int < 1 or dia_int > 2:
                print("Error. Debe ingresar 1 para Lunes o 2 para Martes.")
                continue
            break
        
        paciente = input("Ingrese el nombre del paciente: ")

        while not paciente.isalpha():
            paciente = input("Error. Sólo se admiten letras. Ingrese el nombre del paciente: ")

        paciente = paciente.title()

        #Se verifica si el paciente ya está asignado a un turno por cada día, caso contrario se le asigna el turno.
        if dia_int == 1:

            if paciente == lunes_1 or paciente == lunes_2 or paciente == lunes_3 or paciente == lunes_4:
                print("El paciente ya tiene un turno reservado para el día Lunes.")

            elif lunes_1 == "":
                lunes_1 = paciente
                print(f"Turno reservado para {paciente} el día Lunes en el horario 1.")

            elif lunes_2 == "":
                lunes_2 = paciente
                print(f"Turno reservado para {paciente} el día Lunes en el horario 2.") 

            elif lunes_3 == "":
                lunes_3 = paciente
                print(f"Turno reservado para {paciente} el día Lunes en el horario 3.")

            elif lunes_4 == "":
                lunes_4 = paciente
                print(f"Turno reservado para {paciente} el día Lunes en el horario 4.") 

            else:
                print("No hay turnos disponibles para el día Lunes.")

        elif dia_int == 2:

            if paciente == martes_1 or paciente == martes_2 or paciente == martes_3:
                print("El paciente ya tiene un turno reservado para el día Martes.")

            elif martes_1 == "":
                martes_1 = paciente
                print(f"Turno reservado para {paciente} el día Martes en el horario 1.")

            elif martes_2 == "":
                martes_2 = paciente
                print(f"Turno reservado para {paciente} el día Martes en el horario 2.") 

            elif martes_3 == "":
                martes_3 = paciente
                print(f"Turno reservado para {paciente} el día Martes en el horario 3.")

            else:
                print("No hay turnos disponibles para el día Martes.")

    #Se valida que el usuario ingrese un carácter numéricos y que esté dentro de las opciones disponibles
    elif opcion_int == 2:
        while True:
            cancelar_dia = input("""
Seleccione el día:
1. Lunes
2. Martes
""")
            if not cancelar_dia.isdigit():
                print("Error, debe ingresar 1 o 2.")
                continue

            cancelar_dia_int = int(cancelar_dia)

            if cancelar_dia_int < 1 or cancelar_dia_int > 2:
                print("Error. Debe ingresar 1 para Lunes o 2 para Martes.")
                continue
            break
        # Se corrobora que el usuario ingrese correctamente letras 
        cancelar_paciente = input("Ingrese el nombre del paciente a cancelar turno: ")

        while not cancelar_paciente.isalpha():
            cancelar_paciente = input("Error. Sólo se admiten letras. Ingrese el nombre del paciente a cancelar turno:")
        cancelar_paciente = cancelar_paciente.title()

        # Se verifica que el paciente tenga turno asignado, de ser así se procede a cancelar.
        if cancelar_dia_int == 1:
            if cancelar_paciente == lunes_1:
                lunes_1 = ""
                print(f"Turno 1 del Lunes para {cancelar_paciente} cancelado.")

            elif cancelar_paciente == lunes_2:
                lunes_2 = ""
                print(f"Turno 2 del Lunes para {cancelar_paciente} cancelado.")

            elif cancelar_paciente == lunes_3:
                lunes_3 = ""
                print(f"Turno 3 del Lunes para {cancelar_paciente} cancelado.")

            elif cancelar_paciente == lunes_4:
                lunes_4 = ""
                print(f"Turno 4 del Lunes para {cancelar_paciente} cancelado.")

            else:
                print(f"No se encontró un turno reservado para {cancelar_paciente} el día Lunes.")

        elif cancelar_dia_int == 2:
            if cancelar_paciente == martes_1:
                martes_1 = ""
                print(f"Turno 1 del Martes para {cancelar_paciente} cancelado.")

            elif cancelar_paciente == martes_2:
                martes_2 = ""
                print(f"Turno 2 del Martes para {cancelar_paciente} cancelado.")

            elif cancelar_paciente == martes_3:
                martes_3 = ""
                print(f"Turno 3 del Martes para {cancelar_paciente} cancelado.")

            else:
                print(f"No se encontró un turno reservado para {cancelar_paciente} el día Martes.")

    elif opcion_int == 3:

        while True:
            ver_dia = input("""
Seleccione el día:
1. Lunes
2. Martes
""")
            # Se valida que se ingresen dígitos dentro de las opciones disponibles
            if not ver_dia.isdigit():
                print("Error, debe ingresar 1 o 2.")
                continue

            
            ver_dia_int = int(ver_dia)

            if ver_dia_int < 1 or ver_dia_int > 2:
                print("Error. Debe ingresar 1 para Lunes o 2 para Martes.")
                continue
            
            break

        # Se definen los turnos ocupados y libres a mostrar por día
        if ver_dia_int == 1:

            mostrar_lunes_1 = lunes_1
            mostrar_lunes_2 = lunes_2
            mostrar_lunes_3 = lunes_3
            mostrar_lunes_4 = lunes_4

            if mostrar_lunes_1 == "":
                mostrar_lunes_1 = "Libre"
            if mostrar_lunes_2 == "":
                mostrar_lunes_2 = "Libre"
            if mostrar_lunes_3 == "":
                mostrar_lunes_3 = "Libre"
            if mostrar_lunes_4 == "":
                mostrar_lunes_4 = "Libre"

            print(f"""
Agenda del día Lunes:
Turno 1: {mostrar_lunes_1}
Turno 2: {mostrar_lunes_2}
Turno 3: {mostrar_lunes_3}
Turno 4: {mostrar_lunes_4}
""")
        if ver_dia_int == 2:
            mostrar_martes_1 = martes_1
            mostrar_martes_2 = martes_2
            mostrar_martes_3 = martes_3

            if mostrar_martes_1 == "":
                mostrar_martes_1 = "Libre"
            if mostrar_martes_2 == "":
                mostrar_martes_2 = "Libre"
            if mostrar_martes_3 == "":
                mostrar_martes_3 = "Libre"

            print(f"""
Agenda del día Martes:
Turno 1: {mostrar_martes_1}
Turno 2: {mostrar_martes_2}
Turno 3: {mostrar_martes_3}
""")

    
    elif opcion_int == 4:
        #Se generan contadores para ver los turnos ocupados y libres por día
        lunes_ocupados = 0
        martes_ocupados = 0

        if lunes_1 != "":
            lunes_ocupados += 1
        if lunes_2 != "":
            lunes_ocupados += 1
        if lunes_3 != "":
            lunes_ocupados += 1
        if lunes_4 != "":
            lunes_ocupados += 1

        if martes_1 != "":
            martes_ocupados += 1
        if martes_2 != "":
            martes_ocupados += 1
        if martes_3 != "": 
            martes_ocupados += 1

        lunes_libres = 4 - lunes_ocupados
        martes_libres = 3 - martes_ocupados

        print(f"""
Resumen general:

Día Lunes:
Turnos ocupados: {lunes_ocupados}
Turnos libres: {lunes_libres}

Día Martes:
Turnos ocupados: {martes_ocupados}
Turnos libres: {martes_libres}
""")
        # Se corrobora cuál es el día con más turnos ocupados
        if lunes_ocupados > martes_ocupados:
            print("El día con más turnos ocupados es el Lunes.")
        elif martes_ocupados > lunes_ocupados:
            print("El día con más turnos ocupados es el Martes.")
        else:
            print("Ambos días tienen la misma cantidad de turnos ocupados.")





    # Se genera la salida
    elif opcion_int == 5:
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        break







