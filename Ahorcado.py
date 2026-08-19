print("AHORCADO DE NUMEROS \n Juego de 2 jugadores")

palabra = input("Escribe el numero a adivinar: ")
Ganar = False
intentos = 5
print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTienes {intentos} intentos")
adivinada = []
while Ganar == False:
    numero = (input("Adivina el numero: "))

    if numero in adivinada:
        print(f"Cuidado, ya habías puesto el número {numero}")
        continue
    else:
        adivinada.append(numero)
   
    if palabra in adivinada:
        
        print("GANASTEE!!!!")
        while True:
            seguir_jugando = input("¿Volver a jugar? Escribe Si/No: ")
            
            if seguir_jugando == "No":
                print("Gracias por jugar")
                Ganar = True
                break
            elif seguir_jugando == "Si":
                intentos = 5
                palabra = input("Escribe el numero a adivinar: ")
                adivinada = []
                break
                
            else:
                print("Para la otra, escribe la palabra bien")

    else:
        intentos -= 1
        print(f"ERROR te quedan {intentos} intentos")
        if intentos == 0:
            print("Te haz quedado sin intentos")
            print(f"El numero era {palabra}")
                
                
            while True:
                seguir_jugando = input("¿Volver a jugar? Escribe Si/No: ")
                if seguir_jugando == "No":
                    print("Gracias por jugar")
                    Ganar = True
                    break
                elif seguir_jugando == "Si":
                    intentos = 5 
                    palabra = input("Escribe el numero a adivinar: ")
                    adivinada = []
                    break
                else:
                    print("Para la otra escribe la palabra bien")
                
    
