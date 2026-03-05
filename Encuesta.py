# Encuesta

import streamlit as st

# 1. EL ARCHIVADOR
preguntas = [
    {"texto": "¿Cuál es el país más grande del mundo?", "opciones": ["Canadá", "Rusia", "USA", "China"], "correcta": "Rusia"},
    {"texto": "¿A qué temperatura hierve el agua a nivel del mar?", "opciones": ["110ºC", "100ºC", "90ºC", "80ºC"], "correcta": "100ºC"},
    {"texto": "¿Quién fue el pintor austriaco?", "opciones": ["Adolf Hitler", "John F. Kennedy", "Ronald Reagan"], "correcta": "Adolf Hitler"},
    {"texto": "¿Qué nombre tenía el avión que lanzó la primera bomba nuclear?", "opciones": ["Enola Gay", "B-2 Spirit", "Boeing 747", "Catar Airways"], "correcta": "Enola Gay"},
    {"texto": "¿Qué libro escribió Hitler mientras estaba en cárcel?", "opciones": ["Mi Lucha", "Putos Judíos", "100 días"], "correcta": "Mi Lucha"},
    {"texto": "¿Qué inventó Alan Turing?", "opciones": ["La Bombe", "Apple", "Tesla", "General Motors"], "correcta": "La Bombe"},
    {"texto": "¿Qué piloto de la F1 se quedó a 3 puntos de ganar el mundial?", "opciones": ["Max Verstappen", "Fernando Alonso", "Lewis Hamilton"], "correcta": "Max Verstappen"},
    {"texto": "¿Quién es el actual entrenador del Benfica?", "opciones": ["Pep Guardiola", "Carlo Ancelotti", "José Mourinho"], "correcta": "José Mourinho"},
    {"texto": "¿Qué es Qwerty?", "opciones": ["Un teclado único", "Un tipo de mecanografía", "Un diseño de teclado"], "correcta": "Un diseño de teclado"}
]

st.title("🎓 Mi Primer Examen Interactivo")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")

# 2. EL FORMULARIO
with st.form("quiz_form"):
    respuestas_usuario = []
    
    for i, pregunta in enumerate(preguntas):
        st.subheader(f"{i+1}. {pregunta['texto']}")
        # Usamos el índice 'i' en la key para evitar errores de claves duplicadas
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=f"p_{i}")
        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar Examen")

# 3. LA CORRECCIÓN
if boton_enviar:
    aciertos = 0
    total = len(preguntas)

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1

    nota = (aciertos / total) * 10
    nota_redondeada = round(nota, 2)
    
    st.divider()
    st.header(f"Resultado final: {nota_redondeada} / 10")
    st.metric(label="Nota Final", value=nota_redondeada)

    # Lógica de mensajes corregida
    if nota >= 8:
        st.success(f"¡Excelente! Has sacado un {nota_redondeada}. ¡Ole Guacamole!")
        st.balloons()
    elif nota >= 5:
        st.success(f"¡Felicidades! Has aprobado con {aciertos} aciertos.")
        st.balloons()
    else:
        st.error(f"Has sacado un {nota_redondeada}. ¡Estudia chaval! Toca esforzarse más.")
