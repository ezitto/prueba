import streamlit as st

# Título de la aplicación
st.title("¡Hola, Mundo con Streamlit!")

# Texto
st.write("Esta es una aplicación sencilla de prueba.")

# Entrada de texto
name = st.text_input("¿Cómo te llamas?")

# Botón
if st.button("Saludar"):
    st.write(f"Hola, {name}!")
