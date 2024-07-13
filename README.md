# Trivia_Git-GitHub ❓🏆

## Instrucciones



## Ramas asignadas por temas

- Bryan ➡️ **deportes**.
- Alan  ➡️ **videojuegos**
- Victor ➡️ **comics**
- Mariana ➡️ *pendiente*
- Iram ➡️ *pendiente*


## Archivos de Python

Archivo de preguntas (**questions.py**)

```python
# Preguntas y respuestas
trivia_github = [
    {
        "pregunta": "¿Qué es GitHub?",
        "opciones": ["Una plataforma para el control de versiones y colaboración de código", 
                     "Un lenguaje de programación", 
                     "Una red social", 
                     "Un sistema operativo"],
        "respuesta": "Una plataforma para el control de versiones y colaboración de código"
    },
    {
        "pregunta": "¿En qué año se lanzó GitHub?",
        "opciones": ["2005", "2008", "2010", "2012"],
        "respuesta": "2008"
    },
    {
        "pregunta": "¿Quién es el creador de Git?",
        "opciones": ["Linus Torvalds", "Bill Gates", "Mark Zuckerberg", "Elon Musk"],
        "respuesta": "Linus Torvalds"
    },
    {
        "pregunta": "¿Qué comando de Git se usa para clonar un repositorio?",
        "opciones": ["git clone", "git commit", "git push", "git merge"],
        "respuesta": "git clone"
    },
    {
        "pregunta": "¿Qué es un pull request en GitHub?",
        "opciones": ["Una solicitud para fusionar cambios en un repositorio", 
                     "Una solicitud para clonar un repositorio", 
                     "Una solicitud para eliminar un repositorio", 
                     "Una solicitud para renombrar un repositorio"],
        "respuesta": "Una solicitud para fusionar cambios en un repositorio"
    }
]
```

Archivo de principal (**main.py**)
```python
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
```