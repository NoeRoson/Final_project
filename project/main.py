# ---IMPORTAMOS LIBRERIAS NECESARIAS---

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, '..', 'src'))
sys.path.append(src_dir)
from suport import plot_denuncias
import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import numpy as np
import altair as alt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# ---IMAGENES---

espalda = Image.open('/Users/noeliarosonmartin/Ironhack/final_project_viodata/img/vio.jpeg')


# ---CONFIGURACION DE LA PAGINA---

st.set_page_config(
    page_title="VioData",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---CUERPO DE LA PAGINA---

st.header('VioData: Violencia de género en datos', divider='rainbow')

def home():

    col1, col2 = st.columns(2)

    # ---COLUMNA 1---

    with col1:
        st.markdown('<span style="color:#9777e8; font-size: 18px; font-weight: bold; ">#niunamás</span>', unsafe_allow_html=True)
        st.markdown('<span style="font-size: 24px;font-weight: bold; ">¡Bienvenidxs a VioData!</span>', unsafe_allow_html=True)
        st.markdown(
    f"""
    <div style='text-align: justify;'>
        <h6 style='font-size: 18px; color: #4D458E;'> Tu nueva plataforma para interactuar con todos los datos disponibles 
        sobre la violencia de género en España 📊
        </h6>
        <h6 style='font-size: 16px; color: #4D458E;'> En este espacio, nos embarcamos en un viaje de conciencia 
        y acción contra la violencia de género, desde una perspectiva feminista. Reconocemos la urgencia de abordar esta trágica realidad 
        que afecta a mujeres en todo el mundo y estamos comprometidas a ser agentes de cambio.
        </h6>
        <h6 style='font-size: 16px; color: #4D458E;'> Este espacio no solo es un depósito de información, sino también una llamada a la acción. 
        Creemos en la importancia de la concienciación como primer paso hacia un cambio real. Queremos empoderarte con el conocimiento necesario 
        para desafiar y transformar las normas sociales que perpetúan la violencia de género.
        </h6>
        <h6 style='font-size: 16px; color: #4D458E;'> A través del análisis analítico y la difusión de recursos de prevención, aspiramos a crear 
        una comunidad comprometida con la erradicación de la violencia de género. Cada estadística contribuye a 
        nuestro objetivo colectivo de construir un mundo donde todas las personas, independientemente de su género, vivan libres de miedo y violencia.
        </h6>
        <h6 style='font-size: 16px; color: #4D458E;'> Únete a nosotras en este viaje. Juntas, estamos tejiendo una red de apoyo, solidaridad y resistencia 
        que desafiará y cambiará el status quo. La violencia de género no tiene cabida en nuestro futuro, y trabajaremos incansablemente hasta que sea una realidad para todas y todos.
        </h6>
        <h6 style='font-size: 20px; color: #4D458E;'>¿Nos acompañas?♀︎
        </h6>
    </div>
    """, 
    unsafe_allow_html=True)
   


    # ---COLUMNA 2---

    with col2:

        st.markdown(
    """
        <div style='background-color: #B177BB; padding: 10px; border-radius: 5px;text-align: center;'>
        <p style='color: #E2BBFA; font-weight: bold;'>ULTIMA ACTUALIZACIÓN:</p>
        <p style='color: #E2BBFA; font-weight: bold;font-size: 20px'>¿Sabías que desde 2003 son 1237 las mujeres asesinadas por violencia machista?</p>
        </div>
        """,
        unsafe_allow_html=True
        )
        st.text("  ")
        st.image(espalda, width = 500)
        
        st.text("  ")
       
        st.markdown(
        """
        <div style='background-color: #B177BB; padding: 5px; border-radius: 3px;text-align: center;'>
        <p style='color: #E2BBFA; font-weight: bold;'>SÚSCRIBETE AQUÍ PARA MÁS RECIBIR MÁS INFORMACIÓN SOBRE VIOLENCIA DE GÉNERO</p>
        <button style='background-color: #80048C; color: #9777e8; border: 2px solid #340252; padding: 5px; border-radius: 3px; font-weight: bold; '>¡Pulsa!</button>
        </div>
        """,
        unsafe_allow_html=True
        )

    
# --- ESTRUCTURA INTERNA DEL CONTENIDO DEL MENU LATERAL---

# ---PAGINA SOBRE DENUNCIAS DE VIOLENCIA DE GENERO---
def denuncias():

    #INTRODUCCION

    st.title('Denuncias por violencia de género')
    st.write('''
             En el siguiente gráfico podemos observar la evolución de la tasa por mil mujeres
             desde el año 2009 hasta el 2021, último año de actualización de la población total
             de mujeres por provincia. Destaca el caso de Cuenca que, junto a las provincias de 
             Alicante, Almería, Granada, Huelva o Melilla, entre otras, superan la tasa media de España.
             ''')

    provincias = ['alava', 'albacete', 'alicante', 'almeria', 'asturias', 'avila', 'badajoz',
                              'barcelona', 'burgos', 'caceres', 'cadiz', 'cantabria', 'castellon', 'ciudad real',
                              'cordoba', 'cuenca', 'gerona', 'granada', 'guadalajara', 'guipuzcoa', 'huelva',
                              'huesca', 'islas baleares', 'jaen', 'coruña', 'rioja', 'las palmas', 'leon',
                              'lerida', 'lugo', 'madrid', 'malaga', 'melilla', 'murcia', 'navarra', 'orense',
                              'palencia', 'pontevedra', 'salamanca', 'santa cruz de tenerife', 'segovia', 'sevilla',
                              'soria', 'tarragona', 'teruel', 'toledo', 'valencia', 'valladolid', 'vizcaya',
                              'zamora', 'zaragoza']    
    
    # GRÁFICO 1. TASA DE DENUNCIAS POR CADA MIL MUJERES POR PROVINCIA
    denu_combi = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/portal_estadistico_vio_gen/denu_combi.csv')
    provincias = denu_combi['provincia'].unique()
    provincia_seleccionada = st.selectbox('Selecciona una provincia:', provincias)
    pro = denu_combi[denu_combi['provincia'] == provincia_seleccionada]
    media_total = denu_combi.groupby('año')['tasa_por_1000'].mean().reset_index()

    # Filtramos ya que no hay datos posteriores para el total de la población
    pro = pro[pro['año'] <= 2021]
    media_total = media_total[media_total['año'] <= 2021]

    # Creamos el gráfico de barras para la provincia
    bars = alt.Chart(pro).mark_bar(color='pink').encode(
        x='año:O',
        y='tasa_por_1000:Q',
        tooltip=['tasa_por_1000:Q']
    ).properties(width=800, height=500)

    # Línea para la media total de España
    line = alt.Chart(media_total).mark_line(color='purple', strokeDash=[5, 5]).encode(
        x='año:O',
        y='tasa_por_1000:Q'
    )

    # Configuración del diseño del gráfico
    chart = (bars + line).properties(
        title=f'Evolución de la tasa de denuncias por violencia de género en {provincia_seleccionada.capitalize()} y media de España'
    )

    st.altair_chart(chart)

    st.text('   ')

    # GRAFICO 2. DENUNCIAS POR TRIMESTRE
    denu = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/portal_estadistico_vio_gen/denuncias.csv')
    df_filtered = denu[(denu['año'] >= 2008) & (denu['año'] <= 2022)]
    
    # Crear el gráfico de líneas
    plt.figure(figsize=(6, 3))
    sns.lineplot(x='año', y='total_denuncias', hue='trimestre', palette=['#C378FA', '#F9B0E4', '#FDC148', '#87CEFA'],
                data=df_filtered, marker='o', markersize=3, err_style=None)

    # Configuración adicional
    plt.xlabel('Año', color='gray', fontsize=8)
    plt.ylabel('Total de Denuncias por VG', color='gray', fontsize=8)

    # Ajustar tamaño de leyenda
    plt.legend(fontsize=6)

    # Ajustar tamaño de etiquetas en los ejes
    plt.tick_params(axis='both', which='both', labelsize=6, color='gray')

    plt.title('')  # Eliminar el título

    # Eliminar bordes
    sns.despine()

    # Guardar el gráfico con fondo transparente
    st.pyplot(plt, transparent=True)
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
st.sidebar.markdown('<span style="color: #511973; font-size: 24px; font-weight: bold;">VIODATA 🟣</span>', unsafe_allow_html=True)

# Selección de la página principal con estilo personalizado
st.sidebar.markdown('<span style="color: #511973; font-size: 18px; font-weight: bold;">¿Qué quieres saber hoy?</span>', unsafe_allow_html=True)
selected_page_main = st.sidebar.selectbox('Elige una opción:', list(pages.keys()))

# Línea divisoria con estilo personalizado
st.sidebar.markdown('<hr style="border-color: #511973;">', unsafe_allow_html=True)

# Selección de la página de recursos con estilo personalizado
selected_page_rec = st.sidebar.selectbox('¿QUÉ PUEDES HACER CONTRA LA VIOLENCIA DE GÉNERO?', list(rec.keys()))

# Línea divisoria con estilo personalizado
st.sidebar.markdown('<hr style="border-color: #511973;">', unsafe_allow_html=True)

# Obtener la función de la página seleccionada y ejecutarla
if selected_page_main in pages:
    pages[selected_page_main]()
elif selected_page_rec in rec:
    rec[selected_page_rec]()



