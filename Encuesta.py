import sys
print("******************Bienvenido al sistema de trivia de Git 1****************** ")
print("En esta trivia veremos que tanto conoces acerca de videojuegos")
i=1
print("-------------------------------------------------------------------------------")
print("Primera pregunta:")
print("¿Quién es el personaje principal de Halo?\n 1.-Marcus Fénix\n 2.-Solid Snake\n 3.- Mater Chief \n 4.- The Doomslayer \n 5.- Siguiente pregunta \n 6.- Salir. \n")
while(1):
    opcion=0 
    print("\t\tIntento número",i)
    opcion= int(input("Seleccione la opción:"))
    i+=1
    if opcion==1 or opcion==2 or opcion==4:
        print("Error, intenta de nuevo.")
    elif opcion==3:
        print("¡Correcto!")
        break
    elif opcion==5:
        break
    elif opcion==6:
        exit()
    else:
        print("Introduce una opción de las que se muestran en pantalla.")
print("-------------------------------------------------------------------------------")
print("Segunda pregunta:")
print("¿Cuál es el nombre del protagonista principal de la serie de videojuegos The Legend of Zelda?")
print(" 1.- Zelda\n 2.-Link\n 3.- Ganondorf\n 4.-Epona\n 5.- Siguiente pregunta \n 6.- Salir. \n")
while(1):
    opcion=0 
    print("\t\tIntento número",i)
    opcion= int(input("Seleccione la opción:"))
    i+=1
    if opcion==1 or opcion==3 or opcion==4:
        print("Error, intenta de nuevo")
    elif opcion==2:
        print("¡Correcto!")
        break
    elif opcion==5:
        break
    elif opcion==6:
        exit()
    else:
        print("Introduce una opción de las que se muestran en pantalla.")
