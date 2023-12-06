# ---IMPORTAMOS LIBRERIAS NECESARIAS---

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, '..', 'src'))
sys.path.append(src_dir)
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
    page_title =' VioData',
    page_icon = '🟣',
    layout = 'wide',
    initial_sidebar_state = 'expanded',)


# ---CUERPO DE LA PAGINA---

st.header('VioData: Violencia de género en datos', divider='rainbow')

def home():

    col1, col2 = st.columns(2)

    # ---COLUMNA 1---

    with col1:
        st.markdown('<span style="color:#9777e8; font-size: 18px; font-weight: bold; ">#niunamás</span>', unsafe_allow_html=True)
        st.markdown('<span style="font-size: 24px;font-weight: bold; ">¡Bienvenidas a VioData!</span>', unsafe_allow_html=True)
        st.markdown(
    f"""
    <div style='text-align: justify;'>
        <h6 style='font-size: 18px; color: #4757BB;'> Tu nueva plataforma para interactuar con todos los datos disponibles 
        sobre la violencia de género en España 📊
        </h6>
        <h6 style='font-size: 16px;font-weight: normal; color: #4D458E;'> En este espacio, nos embarcamos en un viaje de conciencia 
        y acción contra la violencia de género, desde una perspectiva feminista. Reconocemos la urgencia de abordar esta trágica realidad 
        que afecta a mujeres en todo el mundo y estamos comprometidas a ser agentes de cambio.
        </h6>
        <h6 style='font-size: 16px;font-weight: normal; color: #4D458E;'> Este espacio no solo es un depósito de información, sino también una llamada a la acción. 
        Creemos en la importancia de la concienciación como primer paso hacia un cambio real. Queremos empoderarte con el conocimiento necesario 
        para desafiar y transformar las normas sociales que perpetúan la violencia de género.
        </h6>
        <h6 style='font-size: 16px;font-weight: normal; color: #4D458E;'> A través del análisis analítico y la difusión de recursos de prevención, aspiramos a crear 
        una comunidad comprometida con la erradicación de la violencia de género. Cada estadística contribuye a 
        nuestro objetivo colectivo de construir un mundo donde todas las personas, independientemente de su género, vivan libres de miedo y violencia.
        </h6>
        <h6 style='font-size: 16px;font-weight: normal; color: #4D458E;'> Únete a nosotras en este viaje. Juntas, estamos tejiendo una red de apoyo, solidaridad y resistencia 
        que desafiará y cambiará el status quo. La violencia de género no tiene cabida en nuestro futuro, y trabajaremos incansablemente hasta que sea una realidad para todas y todos.
        </h6>
        <h6 style='font-size: 20px; color: #4757BB;'>¿Nos acompañas?♀︎
        </h6>
    </div>
    """, 
    unsafe_allow_html=True)
   


    # ---COLUMNA 2---

    with col2:

        st.markdown(
    """
        <div style='background-color: #E9B1EC; padding: 10px; border-radius: 5px;text-align: center;'>
        <p style='color: #4D458E; font-weight: bold;'>ULTIMA ACTUALIZACIÓN:</p>
        <p style='color: #4757BB; font-weight: bold;font-size: 20px'>¿Sabías que van 1237 asesinatos de mujeres desde 2003 y 50 de menores desde 2013?</p>
        </div>
        """,
        unsafe_allow_html=True)
        st.text('   ')
        st.image(espalda, width = 500)
        
        st.text('   ')
       
        st.markdown(
        """
        <div style='background-color: #E9B1EC; padding: 5px; border-radius: 3px;text-align: center;'>
        <p style='color: #4757BB; font-weight: bold;'>SÚSCRIBETE AQUÍ PARA MÁS RECIBIR MÁS INFORMACIÓN SOBRE VIOLENCIA DE GÉNERO</p>
        <button style='background-color: #9777e8; color: #E9D6F3; border: 2px solid #340252; padding: 5px; border-radius: 3px; font-weight: bold; '>¡Pulsa!</button>
        </div>
        """,
        unsafe_allow_html=True)

    
# --- ESTRUCTURA INTERNA DEL CONTENIDO DEL MENU LATERAL---

# --- PAGINA 1. DENUNCIAS DE VIOLENCIA DE GENERO---


def denuncias():

    # ---INTRODUCCION---

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
    

    # ---GRÁFICO 1.A. TASA DE DENUNCIAS POR CADA MIL MUJERES POR PROVINCIA---

    denu_combi = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/portal_estadistico_vio_gen/denu_combi.csv')
    provincias = denu_combi['provincia'].unique()
    provincia_seleccionada = st.selectbox('Selecciona una provincia:', provincias)
    pro = denu_combi[denu_combi['provincia'] == provincia_seleccionada]
    media_total = denu_combi.groupby('año')['tasa_por_1000'].mean().reset_index()

    st.text('   ')

    # Filtramos ya que no hay datos posteriores para el total de la población
    pro = pro[pro['año'] <= 2021]
    media_total = media_total[media_total['año'] <= 2021]

    # Creamos el gráfico de barras para la provincia
    bars = alt.Chart(pro).mark_bar(color='lightsteelblue').encode(
        x='año:O',
        y='tasa_por_1000:Q',
        tooltip=['tasa_por_1000:Q']).properties(width=1000, height=600)

    # Línea para la media total de España
    line = alt.Chart(media_total).mark_line(color='purple', strokeDash=[5, 5]).encode(
        x='año:O',
        y='tasa_por_1000:Q')

    # Configuración del diseño del gráfico
    chart = (bars + line).properties(
        title=f'Evolución de la tasa de denuncias por violencia de género en {provincia_seleccionada.capitalize()} y media de España:')

    st.altair_chart(chart)

    st.text('   ')

    st.divider()


    # ---GRAFICO 1.B. DENUNCIAS POR TRIMESTRE---

    st.write('''
             En el siguiente gráfico se visualizan las variaciones por trimestre que se dan en 
             las denuncias por violencia de género entre 2009 y 2022. Como podemos observar, estas han 
             seguido una tendencia similar a lo largo de los años, si bien en el tercer trimestre
             se aprecia siempre una mayor cantidad de denuncias.
             ''')


    denu = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/portal_estadistico_vio_gen/denuncias.csv')
    denu = denu[(denu['año'] >= 2008) & (denu['año'] <= 2022)]
    df_grouped = denu.groupby(['año', 'trimestre']).agg({'total_denuncias': 'mean'}).reset_index()
    orden = ['primero', 'segundo', 'tercero', 'cuarto']
    # Creamos gráfico interactivo con Plotly Express
    fig = px.line(df_grouped, x='año', y='total_denuncias', color='trimestre',
                labels={'total_denuncias': 'Media de Denuncias', 'trimestre': 'Trimestre'},
                title='Evolución de las denuncias por violencia de género según trimestre a lo largo de los años',
                color_discrete_sequence=['#AED6F1', '#F5B7B1', '#A9DFBF', '#BB8FCE'],
                category_orders={'trimestre': orden},
                width=1000, height=600)

    # Diseño del gráfico
    fig.update_layout(xaxis_title='Año', yaxis_title='Media de Denuncias', legend_title='Trimestre',
                    legend=dict(orientation='h', y=-0.15)) # Ajustar la posición de la leyenda
                    
    st.plotly_chart(fig)




# --- PAGINA 2. LLAMADAS RECIBIDAS POR EL 016 ---

def llamadas():
    st.title('Llamadas recibidas por el 016')
    st.write('''
            El Ministerio de Igualdad, a través de la [Delegación del Gobierno contra la Violencia de Género](https://violenciagenero.igualdad.gob.es/home.htm), 
            ofrece un servicio integral para brindar [información](https://violenciagenero.igualdad.gob.es/informacionUtil/recursos/telefono016/home.htm), 
            asesoramiento jurídico, y atención psicosocial inmediata por personal especializado a todas las formas de violencia contra las mujeres,
            a través del número telefónico de marcación abreviada [016](https://violenciagenero.igualdad.gob.es/informacionUtil/recursos/telefono016/home.htm); 
            por WhatsApp en el número [600 000 016](https://wa.me/600000016); a través de un chat online en la página web de la Delegación del Gobierno contra 
            la Violencia de Género y por correo electrónico al servicio 016 online: [016-online@igualdad.gob.es](mailto:016-online@igualdad.gob.es).
            En el siguiente gráfico puedes seleccionar la provincia sobre la que deseas ver la tasa de llamadas recibidas por el 016
            por cada mil mujeres que residen en dicha provincia y podrás compararla con la media nacional.
            ''')


# ---GRÁFICO 2.A. TASA DE LLAMADAS AL 016 POR CADA MIL MUJERES POR PROVINCIA---
    
    llam_combi = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/portal_estadistico_vio_gen/llam_combi.csv')
    provincias = llam_combi['provincia'].unique()
    provincia_seleccionada = st.selectbox('Selecciona una provincia:', provincias)
    pro = llam_combi[llam_combi['provincia'] == provincia_seleccionada]
    media_total = llam_combi.groupby('año')['tasa_por_1000'].mean().reset_index()

    st.text('   ')

    # Filtramos ya que no hay datos posteriores para el total de la población
    pro = pro[pro['año'] <= 2021]
    media_total = media_total[media_total['año'] <= 2021]

    # Creamos el gráfico de barras para la provincia
    bars = alt.Chart(pro).mark_bar(color='#EDBB99').encode(
        x='año:O',
        y='tasa_por_1000:Q',
        tooltip=['tasa_por_1000:Q']).properties(width=1000, height=600)

    # Línea para la media total de España
    line = alt.Chart(media_total).mark_line(color='#16A085', strokeDash=[5, 5]).encode(
        x='año:O',
        y='tasa_por_1000:Q')

    # Configuración del diseño del gráfico
    chart = (bars + line).properties(
        title=f'Evolución de la tasa de llamadas al 016 en {provincia_seleccionada.capitalize()} y media de España:')

    st.altair_chart(chart)

    st.text('   ')

    st.divider()

    # ---GRAFICO 2.B. LLAMADAS AL 016 Y DENUNCIAS POR AÑO ---


    st.write('''
             En el siguiente gráfico se visualiza la evolución tanto de las llamadas como de
             las denuncias por violencia de género entre 2009 y 2022. Como podemos observar, podría existir cierta
             correlación entre ambas variables, lo cual cobra sentido si pensamos que muchas de esas llamadas es posible que 
             hayan terminado en una denuncia real. Ambas variables se han ido incrementando con el paso del tiempo, lo que
             puede traducirse en una mayor concienciación sobre la violencia de género y el aumento de la
             voluntad de las mujeres en solicitar apoyo ante tal situación.
             ''')
    llam_denu = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/portal_estadistico_vio_gen/llam_denu.csv')
    df_selected = llam_denu[['año', 'total_llamadas', 'total_denuncias']]
    df_selected = df_selected[df_selected['año'] <= 2022]

    # Agrupar por año y calcular la suma de llamadas y denuncias
    df_grouped = df_selected.groupby('año').mean().reset_index()

    # Crear gráfico interactivo con Plotly Express
    fig = px.line(df_grouped, x='año', y=['total_llamadas', 'total_denuncias'],
                labels={'value': 'Media', 'variable': 'Tipo'},
                title='Evolución de las denuncias por violencia de género y llamadas al 016 por año',
                markers={'total_llamadas': 'circle', 'total_denuncias': 'x'},
                color_discrete_sequence=['#EDBB99', 'cornflowerblue'])

    # Diseño del gráfico
    fig.update_layout(xaxis_title='Año', yaxis_title='Media', legend=dict(orientation='h'),
                      width=1000, height=600)

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig)


    st.text('   ')

    st.divider()

    # ---GRAFICO 2.C. LLAMADAS AL 016 SEGÚN PERSONA LLAMANTE ---

    llam = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/portal_estadistico_vio_gen/llamadas016.csv')
    df_filtered = llam[llam['año'] <= 2022]

    # Creamos el gráfico interactivo con Plotly Express
    fig = px.bar(df_filtered, x='año', y='total_llamadas', color='llamante',
                labels={'total_llamadas': 'Total de Llamadas', 'año': 'Año'},
                title='Llamadas al 016 según la persona llamante',
                category_orders={'llamante': sorted(df_filtered['llamante'].unique())},  # Orden personalizado para la leyenda
                width=1000, height=600,
                color_discrete_sequence=['lightsteelblue', 'cadetblue', '#C884D1'])

    # Diseño del gráfico
    fig.update_layout(xaxis_title='Año', yaxis_title='Total de Llamadas', legend_title='Llamante',
                    legend=dict(orientation='h', y=-0.15))  # Ajustar la posición de la leyenda

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig)



def victimas():
    st.title('Mujeres asesinadas por violencia de género')
    st.write('''
    Aquí te mostramos datos relacionados con múltiples variables que ofrecen diferente
    información sobre las mujeres que han sido asesinadas por sus agresores durante
    estos años.
    ''')

    # GRAFICO 3.A. VICTIMAS COMBINADO:
    
    # Cargar datos
    vic = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/portal_estadistico_vio_gen/victimas_mortales.csv')

    # Crear una lista con las columnas que puedes usar como filtros
    filtros_disponibles = ['pareja', 'convivencia', 'suicidio', 'denuncia', 'edad_agresor',
                            'edad_victima', 'nacimiento_agresor', 'nacimiento_victima']

    # Diccionario de nombres de columnas personalizados
    filtros = {
        'pareja': '¿Eran pareja?',
        'convivencia': '¿Había convivencia?',
        'suicidio': '¿Hubo suicidio por parte del agresor?',
        'denuncia': '¿Existía denuncia previa?',
        'edad_agresor': 'Rango de edad Agresor',
        'edad_victima': 'Rango de edad Víctima',
        'nacimiento_agresor': 'Procedencia Agresor',
        'nacimiento_victima': 'Procedencia Víctima'}
    
    # Crear una lista con las columnas que puedes usar como filtros
    filtros_disponibles = list(filtros.values())

    # Agregar un widget de selección para que el usuario elija el filtro
    filtros_nuevos = st.selectbox('Selecciona un filtro:', filtros_disponibles)

    # Encontrar la clave correspondiente al valor seleccionado
    filtro_seleccionado = next(key for key, value in filtros.items() if value == filtros_nuevos)

    # Ordenar las edades de manera lógica
    orden_edades = ['<16', '16-17', '18-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-84', '81-90', '>=85', 'desconocido']

    # Elegimos los colores:
    colores = ['#FEB4D2', '#F8A1C4', '#F580AB', '#F15C93', '#EB3A7B', '#E81863', '#DC0052', '#C50042', '#AC0032', '#920021', '#631333']
    fig = px.bar(vic, x='año', y='total_victimas_mortales', color=filtro_seleccionado,
                labels={'total_victimas_mortales': 'Total de mujeres asesinadas'},
                title=f'Evolución anual de mujeres asesinadas según filtro seleccionado',
                width=1000, height=600, 
                category_orders={'edad_agresor': orden_edades, 'edad_victima': orden_edades},
                color_discrete_sequence=colores)

    # Diseño del gráfico
    fig.update_layout(xaxis_title='Año', yaxis_title='Total de mujeres asesinadas')

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig)

    st.text('   ')

    st.divider()

    #--GRAFICO 3.B. DISTRIBUCIÓN VÍCTIMAS MORTALES POR TRIMESTRE Y PROVINCIA

    # Filtrar por provincia
    provincia_seleccionada = st.selectbox('Selecciona una provincia:', vic['provincia'].unique())
    df_provincia = vic[vic['provincia'] == provincia_seleccionada]

    # Crear gráfico interactivo con Plotly Express
    fig = px.bar(df_provincia, x='año', y='total_victimas_mortales', color='trimestre',
                labels={'total_victimas_mortales': 'Víctimas Mortales', 'año': 'Año'},
                title=f'Distribución de Víctimas Mortales por Trimestre y Año en {provincia_seleccionada.capitalize()}',
                barmode='stack',
                width=1000, height=600,
                color_discrete_sequence=['#AED6F1', '#F5B7B1', '#A9DFBF', '#BB8FCE'])

    # Diseño del gráfico
    fig.update_layout(xaxis_title='Año', yaxis_title='Víctimas Mortales')

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig)

    st.text('   ')

    st.divider()


#------------------------------------------
    # --GRAFICO DE PRUEBA PARA NORMATIVAS--
    norm = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/scrapeo/norm.csv')
    norm['normativas_presentes'] = norm['total_normativas'].apply(lambda x: 'Sí' if x > 0 else 'No')


    # Creamos el gráfico interactivo con Plotly Express
    fig = px.histogram(norm, x='año', color='normativas_presentes',
                    labels={'año': 'Año', 'normativas_presentes': '¿Hubo normativa?'},
                    title='Presencia de Normativas por Año y Comunidad Autónoma',
                    category_orders={'normativas_presentes': ['Sí', 'No']},
                    width=1000, height=600,
                    color_discrete_sequence=['#AED6F1', '#F5B7B1'])

    # Diseño del gráfico
    fig.update_layout(xaxis_title='Año', yaxis_title='Número de Comunidades Autónomas',
                    legend_title='¿Hubo normativa ese año?',
                    legend=dict(orientation='h', y=-0.15, x=0.5),  # Ajustamos la posición de la leyenda
                    barmode='group')  # Mostrar barras agrupadas


    st.plotly_chart(fig)
   


def menores():
    st.title('Menores asesinados por violencia de género')
    st.write('Información sobre muertes de menores víctimas de violencia machista.')

# ---GRAFICO 4.A. MENORES:

    # Cargar datos
    men = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/portal_estadistico_vio_gen/menores.csv')

    # Crear una lista con las columnas que puedes usar como filtros
    filtros_disponibles = ['padre_biologico', 'suicidio', 'edad']

    # Diccionario de nombres de columnas personalizados
    filtros = {
        'edad': 'Edad del menor',
        'suicidio': '¿Hubo suicidio por parte del agresor?',
        'provincia': 'Provincia'}
    
    # Crear una lista con las columnas que puedes usar como filtros
    filtros_disponibles = list(filtros.values())

    # Agregar un widget de selección para que el usuario elija el filtro
    filtros_nuevos = st.selectbox('Selecciona un filtro:', filtros_disponibles)

    # Encontrar la clave correspondiente al valor seleccionado
    filtro_seleccionado = next(key for key, value in filtros.items() if value == filtros_nuevos)
    
    # Ordenar las edades de manera lógica
    orden_edades = ['<1', '1-2', '3-4', '5-6', '7-8', '9-10', '11-12', '13-14', '15-17']

    # Elegimos los colores:
    color = ['#FFD1DC', '#FFC3D3', '#FFB5CA', '#FFA7C1', '#FF99B8', '#FF8BAF', '#FF7DA6', '#FF6F9D', '#FF6194',
             '#FF538B', '#FF4582', '#FF3779', '#FF296F', '#FF1B66', '#FF0D5D', '#F90053', '#EC0049', '#DF003F', '#D20035']


    fig = px.bar(men, x='año', y='total_menores_vict_mortales', color=filtro_seleccionado,
                labels={'total_menores_vict_mortales': 'Total de menores asesinados'},
                title=f'Evolución anual de menores asesinados según filtro seleccionado',
                width=1000, height=600, 
                category_orders={'edad': orden_edades},
                color_discrete_sequence=color)

    # Diseño del gráfico
    fig.update_layout(xaxis_title='Año', yaxis_title='Total de menores asesinados')

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig)




def proteccion():
    st.title('Protección a las Víctimas')
    st.write('Información sobre órdenes de protección y dispositivos de seguimiento.')

    ord = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/portal_estadistico_vio_gen/ordenes_prot.csv')
    provincias = ord['provincia'].unique()
    provincia_seleccionada = st.selectbox('Selecciona una provincia:', provincias)
    pro = ord[ord['provincia'] == provincia_seleccionada]
    media_total = pro['numero_ordenes_proteccion'].mean()

    # Creamos el gráfico de barras para la provincia
    bars = alt.Chart(pro).mark_bar(color='#A2D9CE').encode(
    x='año:O',
    y='mean(numero_ordenes_proteccion):Q',
    tooltip=['año:N', alt.Tooltip('mean(numero_ordenes_proteccion):Q', title='Número de Órdenes de Protección')]
    ).properties(
        width=1000,
        height=600,
        title='Evolución anual del número de órdenes de Protección por Provincia'
    )

    # Línea para la media total de España
    line = alt.Chart(pro).mark_line(color='#D35400', strokeDash=[5, 5]).encode(
        x='año:O',
        y='mean(numero_ordenes_proteccion):Q'
    )

    # Configuración del diseño del gráfico
    chart = (bars + line).properties(
        title=f'Evolución de las órdenes de protección interpuestas en {provincia_seleccionada.capitalize()} y media de España:'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_title(
        fontSize=16
    ).configure_legend(
        title=None
    )

    st.altair_chart(chart, use_container_width=True)


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
    st.title('¿Qué normativas rigen en mi Comunidad Autónoma?')
    st.write('Aquí puedes encontrar información sobre las distintas normativas regionales en materia de violencia de género')
    norm = pd.read_csv('/Users/noeliarosonmartin/Ironhack/final_project_viodata/data_clean/scrapeo/norm.csv')
    norm['normativas_presentes'] = norm['total_normativas'].apply(lambda x: 'Sí' if x > 0 else 'No')

    # Creamos el gráfico interactivo con Plotly Express
    fig = px.histogram(norm, x='año', color='normativas_presentes',
                    labels={'año': 'Año', 'normativas_presentes': 'Normativas Presentes'},
                    title='Presencia de Normativas por Año y Comunidad Autónoma',
                    category_orders={'normativas_presentes': ['No', 'Sí']},
                    width=800, height=500)

    # Diseño del gráfico
    fig.update_layout(xaxis_title='Año', yaxis_title='Número de Comunidades Autónomas',
                    legend_title='Normativas Presentes',
                    legend=dict(orientation='h', y=-0.15, x=0.5),  # Ajustar la posición de la leyenda
                    barmode='group')  # Mostrar barras agrupadas

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig)



def info():
    st.title('Más información sobre la violencia de género')
    st.write('Aquí puedes encontrar información adicional sobre violencia de género')


pages = {
    'Página principal': home,
    'Denuncias por violencia de género': denuncias,
    'Llamadas al 016': llamadas,
    'Mujeres víctimas': victimas,
    'Menores víctimas': menores,
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



