print("AHORCADO DE NUMEROS \n Juego de 2 jugadores")

palabra = input("Escribe el numero a adivinar: ")

Ganar = False
intentos = 5

while Ganar == False:
    print(f"Te quedan {intentos} intentos")
    adivinada = input("Adivina el numero: ")
    if adivinada != palabra:
        print(f"ERROR te quedan {intentos} intentos")
        intentos -= 1
        if intentos == 0:
            print("Te haz quedado sin intentos")
            print(f"El numero era {palabra}")
            s_j_respuesta = False
            
            while s_j_respuesta == False:
                seguir_jugando = input("¿Volver a jugar? Escribe Si/No: ")
                if seguir_jugando == "No":
                    print("Gracias por jugar")
                    Ganar = True
                    s_j_respuesta = True
                elif seguir_jugando == "Si":
                    intentos = 5 
                    palabra = input("Escribe el numero a adivinar: ")
                    s_j_respuesta = True
                else:
                    print("Para la otra escribe la palabra bien")
            
        
    elif adivinada == palabra:
        s_j_respuesta = False
        print("GANASTEE!!!!")
        while s_j_respuesta == False:
            seguir_jugando = input("¿Volver a jugar? Escribe Si/No: ")
            
            if seguir_jugando == "No":
                print("Gracias por jugar")
                Ganar=True
                s_j_respuesta = True
            elif seguir_jugando == "Si":
                intentos = 5
                palabra = input("Escribe el numero a adivinar: ")
                s_j_respuesta = True
            else:
                print("Para la otra, escribe la palabra bien")

        
    
