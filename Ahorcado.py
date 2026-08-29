print("AHORCADO DE NUMEROS \n Juego de 2 jugadores")

palabra = input("Escribe el numero a adivinar: ")
Ganar = False
intentos = 5
print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTienes {intentos} intentos")
adivinada = []

def preguntar_seguir_jugando():
    while True:
        seguir_jugando = input("¿Volver a jugar? Escribe Si/No: ")
            
        if seguir_jugando == "No":
            print("Gracias por jugar")
            
            break
        elif seguir_jugando == "Si":
            
            return True
                
        else:
                print("Para la otra, escribe la palabra bien")
    
while Ganar == False:
    numero = (input("Adivina el numero: ")) #IA

    if numero in adivinada: #IA
        print(f"Cuidado, ya habías puesto el número {numero}") #IA
        continue
    else: #IA
        adivinada.append(numero) #IA
   
    if palabra in adivinada:
        
        print("GANASTEE!!!!")
        if preguntar_seguir_jugando():
            intentos = 5
            palabra = input("Escribe el numero a adivinar: ")
            adivinada = []
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        else:
            Ganar = True
        

    else:
        intentos -= 1
        print(f"ERROR te quedan {intentos} intentos")
        if intentos == 0:
            print("Te has quedado sin intentos")
            print(f"El numero era {palabra}")
            if preguntar_seguir_jugando():
                intentos = 5
                palabra = input("Escribe el numero a adivinar: ")
                adivinada = []
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            else:
                Ganar = True