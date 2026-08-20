#Definimos las variables iniciales
vida_gladiador = 100
vida_enemigo = 100
pocion = 3
ataque_pesado = 15
daño_enemigo = 12
turno_gladiador = True
golpe_critico = 1.5

#Solicitamos nombre del jugador, se valida que se ingresen letras en un bucle
nombre = input("Ingrese el nombre del Gladiador: ")

while not nombre.isalpha():
    nombre = input("Error: Solo se permiten letras. Intente nuevamente: ")

nombre = nombre.title()

#Se inicializa el juego, condicionado por la vida de los combatientes
while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"""
Gladiador {nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo})

Pociones: {pocion}
""")
    if turno_gladiador:
        #Se muestra el menú 
        print("""---Turno Gladiador---
    Acciones:
    1. Ataque pesado
    2. Ráfaga veloz
    3. Curar
    """)
        #Se solicita seleccionar una opción, validando que se ingresen los números correspondientes
        opcion = input("Seleccione una acción: ")

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            opcion = input("Error. Debe ingresar un número entre 1 y 3: ")

        opcion_int = int(opcion)

        #Se define la opción 1 
        if opcion_int == 1:
            print("\n Iniciaste: ¡Ataque pesado!")
            #Se condiciona cuándo se debe aplicar el golpe crítico
            if vida_enemigo < 20:
                daño = ataque_pesado * golpe_critico
                print("\nGolpe Crítico")
            else:
                daño = ataque_pesado

            #Se redefine la vida del enemigo 
            vida_enemigo -= daño

            print(f"\n¡Atacaste al enemigo por {daño} puntos de daño!")    

        #Se definen las acciones de la opción 2 
        elif opcion_int == 2:
            print("\nIniciaste: ¡Ráfaga de golpes!")
            for golpe in range(3):
                vida_enemigo -= 5
                print(">Golpe conectado por 5 de daño")

        #Se define la opción 3 y el uso de pociones
        elif opcion_int == 3:
            if pocion > 0:
                vida_gladiador += 30
                pocion -= 1

            else: 
                print ("\n¡No quedan pociones!")
        #Se finaliza el turno del jugador
        turno_gladiador =False

    #Se genera el turno del enemigo y en base al daño se actualiza la vida del jugador
    if vida_enemigo > 0 and not turno_gladiador:

        vida_gladiador -= daño_enemigo
        print(f"\n¡El enemigo te atacó por {daño_enemigo} puntos de daño!")

        #Se cambia la variable para volver al turno del jugador
        turno_gladiador = True

#Se define las condiciones de victoria y derrota
if vida_gladiador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla")

else:
    print(f"\nDERROTA. Has caido en combate")
    