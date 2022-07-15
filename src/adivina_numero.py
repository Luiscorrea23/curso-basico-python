# Un programa que pide adivinar al usuario un numero entre el 1 y 100 

import random 

#Una funcion que compare numero de usuario con numero de computadora

# def life_game(vidas): 
#     vidas -= 1
#     if vidas <= 0:
#         print("Te quedaste sin vidas")

# def game_choice(vidas):
#     if vidas > 0:
#         numero = int(input("Introduce un numero: "))
#     else:
#         print("te quedaste sin vidas")
#         break
def check_answer(vidas, puntaje):
    numero = int(input("Introduce un numero: "))
    machine_number = random.randint(1,100)
    print(machine_number)
    while numero != machine_number:
        vidas -= 1
        if numero > machine_number:
            print("El numero a adivinar es mas pequeño")
            if vidas > 0:
                numero = int(input("Introduce un numero: "))
            else:
                print("te quedaste sin vidas")
                break
                
        else:
            print("El numero a adivinar es mas grande")
            if vidas > 0:
                numero = int(input("Introduce un numero: "))
            else:
                print("te quedaste sin vidas")
                break
    else:
        puntaje += 1
        print("Ganaste, tu puntaje es: " + str(puntaje))

def run(): 
    puntaje = 0
    check_answer(3, puntaje)
    


if __name__ == "__main__":
    run()