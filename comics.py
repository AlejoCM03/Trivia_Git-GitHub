from preguntas import *

def mostrar_pregunta(pregunta):
    print("\n" + pregunta["texto"])
    for idx, opcion in enumerate(pregunta["opciones"], start=1):
        print(f"{idx}. {opcion}")

def trivia():
    aciertos = 0
    errores = 0

    for pregunta in preguntas:
        while True:
            mostrar_pregunta(pregunta)
            
            try:
                respuesta = int(input("Elige la opción correcta (1-3): "))
                if respuesta not in range(1, len(pregunta["opciones"]) + 1):
                    print("Entrada no válida. Por favor, elige una opción válida.")
                    continue
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número.")
                continue

            # Verificar si la respuesta es correcta
            if respuesta != pregunta["correcta"]:
                print("Respuesta incorrecta. La respuesta correcta es:", pregunta["opciones"][pregunta["correcta"] - 1])
                errores += 1
            else:
                print("¡Correcto!")
                aciertos += 1
            break
    
    print(f"\n¡Felicidades! Has completado todas las preguntas.")
    print(f"Aciertos totales: {aciertos}")
    print(f"Errores totales: {errores}")

if __name__ == "__main__":
    trivia()
