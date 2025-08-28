import streamlit as st #traer objeto de libreria "st"(objeto que usamos para todo)  'st' herramienta que nos permite para alterar los campos 
from PIL import Image  # libreria para manipulación de img

st.title("Mi primeera APP!")  # titulo 

st.header("En este espacio comienzo a desarrollar ...")
st.write("Faclmente puedo realizar backend y frontend.")
image=Image.open('BTM.jpg')

st.image(image, caption='Interfaces multimodales')


texto = st.text_input('Escribie algo', 'Este es mi texto')  # un campo de texto a mi interfaz 'variable, asignada para manipularla -> almcenar texto...'
st.write('EL texto escrito es', texto) 
