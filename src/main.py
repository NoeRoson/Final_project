import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import numpy as np
import altair as alt



st.title('VIODATA: Violencia de género en datos')
# aqui poner una foto

# aqui poner un subtitulo

# aqui poner una introducción



def home():
    st.title('#niunamás')
    st.write('¡Bienvenido a la página de inicio!')

def denuncias():
    st.title('Denuncias por violencia de género')
    st.write('Esta es la página de información sobre denuncias.')

def llamadas():
    st.title('Llamadas recibidas por el 016')
    st.write('Esta es la página de información sobre llamadas al 016.')

def victimas():
    st.title('Información sobre víctimas por violencia de género')
    st.write('Aquí te mostramos datos sobre víctimas mujeres y menores.')

def proteccion():
    st.title('Protección a las Víctimas')
    st.write('Información sobre órdenes de protección y dispositivos de seguimiento.')

def delitos():
    st.title('Tipología de delitos en materia de violencia de género')
    st.write('Datos sobre los distintos tipos de delitos')

def recursos():
    st.title('Recursos en tu ciudad')
    st.write('Aquí puedes encontrar información sobre recursos de prevención de la violencia de género')

def denun():
    st.title('¿Qué puedo hacer yo?')
    st.write('Aquí puedes encontrar información sobre qué hacer si conoces un caso de violencia de género')

def normas():
    st.title('¿Qué normativas rigen en mi Comunidad Autónoma')
    st.write('Aquí puedes encontrar información sobre las distintas normativas regionales en materia de violencia de género')

def info():
    st.title('Más información sobre la violencia de género')
    st.write('Aquí puedes encontrar información adicional sobre violencia de género')

# Crear un diccionario que asocie nombres de página con funciones de página
pages = {
    'Bienvenid@': home,
    'Denuncias por violencia de género': denuncias,
    'Llamadas al 016': llamadas,
    'Víctimas de violencia de género': victimas,
    'Protección a víctimas': proteccion,
    'Tipología de delitos': delitos}

rec = {
    'Recursos en tu ciudad': recursos,
    '¿Qué hacer ante la violencia de género?': denun,
    'Normativas en materia de violencia de género': normas,
    'Más información': info}

# Título en el menú lateral
st.sidebar.title('VIODATA')

# Selección de la página principal
selected_page_main = st.sidebar.selectbox('Despliega para saber más', list(pages.keys()))

# Selección de la página de recursos
selected_page_rec = st.sidebar.selectbox('¿Qué puedes hacer frente a la Violencia de Género?', list(rec.keys()))

# Obtener la función de la página seleccionada y ejecutarla
if selected_page_main in pages:
    pages[selected_page_main]()
elif selected_page_rec in rec:
    rec[selected_page_rec]()



