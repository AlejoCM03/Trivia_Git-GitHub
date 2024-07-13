import random
import questions

trivia_github = questions.trivia_github
# Función para hacer una pregunta y comprobar la respuesta
def hacer_pregunta(pregunta):
    print(pregunta["pregunta"])
    for idx, opcion in enumerate(pregunta["opciones"], 1):
        print(f"{idx}. {opcion}")
    respuesta_usuario = input("Tu respuesta (1-4): ")
    if pregunta["opciones"][int(respuesta_usuario) - 1].strip().lower() == pregunta["respuesta"].lower():
        print("¡Correcto!")
        return True
    else:
        print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}")
        return False

# Función principal para la trivia
def trivia_game():
    print("¡Bienvenido a la trivia sobre GitHub!")
    random.shuffle(trivia_github)
    puntaje = 0
    for pregunta in trivia_github:
        if hacer_pregunta(pregunta):
            puntaje += 1
    print(f"Tu puntaje final es: {puntaje} de {len(trivia_github)}")

# Iniciar el juego de trivia
if __name__ == "__main__":
    trivia_game()