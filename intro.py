import streamlit as st #traer objeto de libreria "st"
from PIL import Image

st.title("Mi primeera APP!")

st.header("En este espacio comienzo a desarrollar ...")
st.write("Faclmente puedo realizar backend y frontend.")
image=Image.open('BTM.jpg')

st.image(image, caption='Interfaces multimodales')
