preguntas = [
    {"texto": "¿De qué planeta proviene Superman?",
     "opciones": ["Jupyter","Mundo de Guerra","Krypton"],
     "correcta": 3
    },
    {"texto": "¿Cuál es la identidad del Hombre araña?",
     "opciones": ["Juan Conor","Peter Parker","Clark Kent"],
     "correcta": 2

    },
    {"texto": "¿Cuál es el fetiche de Homelander?",
     "opciones": ["Leche materna","Tomar jugo de naranja","pies"],
     "correcta": 1
    },

    {"texto": "¿Cuál es el origen del Joker?",
     "opciones": ["Enfermo mental que escapó de un hospital psiquiátrico","Era profesor y luego se volvió loco","No tiene origen"],
     "correcta": 3
    },
    {"texto": "¿Qué tipo de radiación dotó de poderes a los 4 fantásticos?",
     "opciones": ["Radiación Gamma","Rayos X","Rayos cósmicos"],
     "correcta": 3

    },
    {"texto": "¿Cuál es una de las debilidades principales de superman además de la kryptonita?",
     "opciones": ["Alcohol","Magia","Drogas"],
     "correcta": 2
    },
    {"texto": "¿Qué planeta gobierna Darksaid",
     "opciones": ["Krypton","Marte","Apocolips"],
     "correcta": 3
        
    },
    {"texto": "¿De qué metal está hecho las garras de Wolverine?",
     "opciones": ["Adamantium","Vibranium","Uru"],
     "correcta": 1

    },
    {"texto": "¿De qué está hecho el escudo del Capitán América?",
     "opciones": ["Acero","Uru","Vibranium"],
     "correcta": 3

    },
    {"texto": "¿Cuál es la raza extraterrestre que cambia de forma y se infiltró en la Tierra ?",
     "opciones": ["Los shiar","Skrulls","Vultrumita"],
     "correcta": 2
    },
    {"texto": "¿De qué reino proviene Thor?",
     "opciones": ["Asgard","Juntenhein","Midgar"],
     "correcta": 1

    },
    {"texto": "¿Cómo se llama el ser que se alimenta de planetas?",
     "opciones": ["Ego","Galactus","Thanos"],
     "correcta": 2

    }
]

print(len(preguntas))

def mostrar_pregunta(pregunta):
    print("\n" + pregunta["texto"])
    for idx, opcion in enumerate(pregunta["opciones"],start =1):
        print(f"{idx}.{opcion}")


for pregunta in preguntas:
    mostrar_pregunta(pregunta)


"""""
def trivia():
    aciertos = 0
    errores = 0

    for i, pregunta in enumerate(preguntas, start = 1):
        while True:
            mostrar_pregunta(pregunta)
            
            try:
                respuesta = int(input("Elige la opción correcta (1-3): "))
                if respuesta not in range(1,len(preguntas["opciones"])+1):
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

"""""