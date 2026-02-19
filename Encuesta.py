# Encuesta

import streamlit as st

# 1. EL ARCHIVADOR (Nuestra base de datos de preguntas)
# Cada bloque entre { } es una pregunta distinta. Cada pregunta es un diccionario de 3 entradas (texto, opciones, correcta).
# Creamos la lista de preguntas: 
preguntas = [
    {
        "texto": "¿Cuál es el país más grande del mundo por extensión territorial?",
        "opciones": ["Canadá", "Rusia", "USA", "China"],
        "correcta": "Rusia"
    },
    {
        "texto": "¿A qué temperatura (en grados Celsius) hierve el agua a nivel del mar?",
        "opciones": ["110ºC", "100ºC", "90ºC", "80ºC"],
        "correcta": "100ºC"
    },
    {
        "texto": "¿Quién fue el pintor austriaco?",
        "opciones": ["Adolf Hitler", "John F. Kennedy", "Ronald Reagan"],
        "correcta": "Adolf Hitler"
    },
    {
        "texto": "¿Qué nombre tenía el avión que lanzó la primera bomba nuclear?",
        "opciones": ["Enola Gay", "B-2 Spirit", "Boeing 747", "Catar Airways"],
        "correcta": "Enola Gay"
    },
    {
        "texto": "¿Qué libro escribió Hitler mientras estaba en cárcel?",
        "opciones": ["Mi Lucha", "Putos Judíos", "100 días"],
        "correcta": "Mi Lucha"
    },
    {
        "texto": "¿Eeeen qué año se lanzó la Web 1.0?",
        "opciones": ["1983", "1990", "2005"],
        "correcta": "1990"
    },
    
]

# Configuración visual de la página
st.title("🎓 Mi Primer Examen Interactivo")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")

# 2. EL FORMULARIO (Agrupamos todo para que no se recargue la web a cada clic)
# Eso se consigue con el comando with

with st.form("quiz_form"):

    # Aquí guardaremos las respuestas que elija el alumno. Será una lista.
    respuestas_usuario = []
    
    # Recorremos el archivador usando un bucle 'for' para crear las preguntas
    for pregunta in preguntas:
        st.subheader(pregunta["texto"]) # Ponemos el texto de la pregunta

        # Creamos los botones de opción (radio)
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])

        # Guardamos la elección en nuestra lista usando append ()
        respuestas_usuario.append(eleccion)
        st.write("---") # Una línea para separar preguntas

    # Botón obligatorio para cerrar el formulario
    boton_enviar = st.form_submit_button("Entregar Examen")

# 3. LA CORRECCIÓN (Solo ocurre cuando pulsamos el botón)
if boton_enviar:
    aciertos = 0
    # Total es número de preguntas (usa el método len)
    total = len(preguntas)

    # Comparamos las respuestas del usuario con las 'correctas' del archivador
    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos = aciertos + 1

    # Calculamos la nota sobre 10
    nota = (aciertos / total) * 10

    # Mostramos el resultado con colores
    st.divider()
    st.header(f"Resultado final: {nota} / 10")

    if nota >= 5:
        st.success(f"¡Felicidades! Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!
    else:
        st.error(f"Has sacado un {nota}. ¡Toca estudiar un poco más!")
