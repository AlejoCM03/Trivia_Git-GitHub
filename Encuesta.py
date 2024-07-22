import sys
def encuesta():
    i=1
    PreguntasCorrectas=0
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
            PreguntasCorrectas+=1
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
            PreguntasCorrectas+=1
            break
        elif opcion==5:
            break
        elif opcion==6:
            exit()
        else:
            print("Introduce una opción de las que se muestran en pantalla.")
    print("-------------------------------------------------------------------------------")
    print("Tercer pregunta:")
    print("¿En qué año se lanzó el primer videojuego de Super Mario Bros.?")
    print(" 1.-1983\n 2.-1985 \n 3.-1987 \n 4.-1989 \n 5.- Siguiente pregunta \n 6.- Salir. \n")
    while(1):
        opcion=0 
        print("\t\tIntento número",i)
        opcion= int(input("Seleccione la opción:"))
        i+=1
        if opcion==1 or opcion==3 or opcion==4:
            print("Error, intenta de nuevo")
        elif opcion==2:
            print("¡Correcto!")
            PreguntasCorrectas+=1
            break
        elif opcion==5:
            break
        elif opcion==6:
            exit()
        else:
            print("Introduce una opción de las que se muestran en pantalla.")
    print("-------------------------------------------------------------------------------")
    print("Cuarta pregunta:")
    print("¿Cuál de estos videojuegos fue desarrollado por la empresa Blizzard Entertainment?")
    print(" 1.-The Elder Scrolls V: Skyrim \n 2.- Grand Theft Auto V \n 3.- World of Warcraft\n 3.- The Witcher 3: Wild Hunt\n 5.- Siguiente pregunta \n 6.- Salir. \n")
    while(1):
        opcion=0 
        print("\t\tIntento número",i)
        opcion= int(input("Seleccione la opción:"))
        i+=1
        if opcion==1 or opcion==2 or opcion==4:
            print("Error, intenta de nuevo")
        elif opcion==3:
            print("¡Correcto!")
            PreguntasCorrectas+=1
            break
        elif opcion==5:
            break
        elif opcion==6:
            exit()
        else:
            print("Introduce una opción de las que se muestran en pantalla.")
    print("-------------------------------------------------------------------------------")
    print("Quinta pregunta:")
    print("¿Qué consola de videojuegos lanzó Sony en 1994?")
    print("1.- Sega Saturn \n 2.- PlayStation \n 3.- Nintendo 64 \n 4.- Xbox \n 5.- Siguiente pregunta \n 6.- Salir. \n")
    while(1):
        opcion=0 
        print("\t\tIntento número",i)
        opcion= int(input("Seleccione la opción:"))
        i+=1
        if opcion==1 or opcion==3 or opcion==4:
            print("Error, intenta de nuevo")
        elif opcion==2:
            print("¡Correcto!")
            PreguntasCorrectas+=1
            break
        elif opcion==5:
            break
        elif opcion==6:
            exit()
        else:
            print("Introduce una opción de las que se muestran en pantalla.")
    print("-------------------------------------------------------------------------------")
    print("Sexta pregunta:")
    print("¿Quién es el desarrollador principal de la serie de videojuegos Dark Souls?")
    print("1.- Capcom \n 2.- Bethesda Game Studios \n 3.- FromSoftware \n 4.- CD Projekt Red \n 5.- Siguiente pregunta \n 6.- Salir. \n")
    while(1):
        opcion=0 
        print("\t\tIntento número",i)
        opcion= int(input("Seleccione la opción:"))
        i+=1
        if opcion==1 or opcion==2 or opcion==4:
            print("Error, intenta de nuevo")
        elif opcion==3:
            print("¡Correcto!")
            PreguntasCorrectas+=1
            break
        elif opcion==5:
            break
        elif opcion==6:
            exit()
        else:
            print("Introduce una opción de las que se muestran en pantalla.")
    print("-------------------------------------------------------------------------------")
    print("Septima pregunta:")
    print("¿Cuál de estos juegos es un juego de construcción y supervivencia que permite a los jugadores crear y destruir bloques en un mundo tridimensional?")
    print("1.- Terraria \n 2.- Rust \n 3.- Ark: Survival Evolved \n 4.- Minecraft \n 5.- Siguiente pregunta \n 6.- Salir. \n")
    while(1):
        opcion=0 
        print("\t\tIntento número",i)
        opcion= int(input("Seleccione la opción:"))
        i+=1
        if opcion==1 or opcion==2 or opcion==3:
            print("Error, intenta de nuevo")
        elif opcion==4:
            print("¡Correcto!")
            PreguntasCorrectas+=1
            break
        elif opcion==5:
            break
        elif opcion==6:
            exit()
        else:
            print("Introduce una opción de las que se muestran en pantalla.")
    print("-------------------------------------------------------------------------------")
    print("Octava pregunta:")
    print("¿En qué videojuego aparece el personaje Pikachu?")
    print("1.- Pokémon \n 2.- Digimon \n 3.- Animal Crossing\n 4.- Yo-Kai Watch \n 5.- Siguiente pregunta \n 6.- Salir. \n")
    while(1):
        opcion=0 
        print("\t\tIntento número",i)
        opcion= int(input("Seleccione la opción:"))
        i+=1
        if opcion==4 or opcion==2 or opcion==3:
            print("Error, intenta de nuevo")
        elif opcion==1:
            print("¡Correcto!")
            PreguntasCorrectas+=1
            break
        elif opcion==5:
            break
        elif opcion==6:
            exit()
        else:
            print("Introduce una opción de las que se muestran en pantalla.")
    print("-------------------------------------------------------------------------------")
    print("Novena pregunta:")
    print("¿Qué compañía desarrolló el videojuego The Last of Us?")
    print("1.- Bungie \n 2.- Bethesda \n 3.- Insomniac Games\n 4.- Naughty dog \n 5.- Siguiente pregunta \n 6.- Salir. \n")
    while(1):
        opcion=0 
        print("\t\tIntento número",i)
        opcion= int(input("Seleccione la opción:"))
        i+=1
        if opcion==4 or opcion==2 or opcion==3:
            print("Error, intenta de nuevo")
        elif opcion==1:
            print("¡Correcto!")
            PreguntasCorrectas+=1
            break
        elif opcion==5:
            break
        elif opcion==6:
            exit()
        else:
            print("Introduce una opción de las que se muestran en pantalla.")

print("******************Bienvenido al sistema de trivia de Git 1****************** ")
print("En esta trivia veremos que tanto conoces acerca de videojuegos")
try:
    encuesta()
except(ValueError): 
    print("Selecciona un dato válido")
    encuesta()
