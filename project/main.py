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
import json




# ---CONFIGURACION DE LA PAGINA---

st.set_page_config(
    page_title =' VioData',
    page_icon = '🟣',
    layout = 'wide',
    initial_sidebar_state = 'expanded',)


# ---CUERPO DE LA PÁGINA PRINCIPAL---

st.header('VioData: Violencia de género en datos', divider='rainbow')

def home():

    col1, col2 = st.columns(2)

    # ---COLUMNA 1---

    with col1:
        st.markdown('<span style="color:#9381ffff; font-size: 18px; font-weight: bold; ">#niunamás</span>', unsafe_allow_html=True)
        st.markdown('<span style="font-size: 24px;font-weight: bold; ">¡Bienvenidas a VioData!</span>', unsafe_allow_html=True)
        st.markdown(
    f"""
    <div style='text-align: justify;'>
        <h6 style='font-size: 18px; color: #4757BB;'> Tu nueva plataforma para interactuar con todos los datos disponibles 
        sobre la violencia de género en España 📉
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
        st.text('   ')
        st.text('   ')
        st.text('   ')
        st.markdown(
    """
        <div style='background-color: #B8B8FF; padding: 10px; border-radius: 5px;text-align: center;'>
        <p style='color: #4D458E; font-weight: bold;'>ULTIMA ACTUALIZACIÓN:</p>
        <p style='color: #4757BB; font-weight: bold;font-size: 20px'>¿Sabías que van 1237 asesinatos de mujeres desde 2003 y 50 de menores desde 2013?</p>
        </div>
        """,
        unsafe_allow_html=True)

        
        st.text('   ')
        st.text('   ')
        
        ima = Image.open('img/vio.jpeg')
        st.image(ima, width = 500)
        

    st.text('   ')
       
       

    

# --- ESTRUCTURA INTERNA DEL CONTENIDO DEL MENU LATERAL---


# ---------MENÚ LATERAL----------

# --- PAGINA 1. DENUNCIAS DE VIOLENCIA DE GENERO---
provin = ['alava', 'albacete', 'alicante', 'almeria', 'asturias', 'avila', 'badajoz',
                              'barcelona', 'burgos', 'caceres', 'cadiz', 'cantabria', 'castellon', 'ciudad real',
                              'cordoba', 'cuenca', 'gerona', 'granada', 'guadalajara', 'guipuzcoa', 'huelva',
                              'huesca', 'islas baleares', 'jaen', 'coruña', 'rioja', 'las palmas', 'leon',
                              'lerida', 'lugo', 'madrid', 'malaga', 'melilla', 'murcia', 'navarra', 'orense',
                              'palencia', 'pontevedra', 'salamanca', 'santa cruz de tenerife', 'segovia', 'sevilla',
                              'soria', 'tarragona', 'teruel', 'toledo', 'valencia', 'valladolid', 'vizcaya',
                              'zamora', 'zaragoza'] 

def denuncias():

    # ---INTRODUCCION---

    st.title('Denuncias por violencia de género')
    texto = ('''
             En el siguiente gráfico podemos observar la evolución de la tasa por mil mujeres
             desde el año 2009 hasta el 2021, último año de actualización de la población total
             de mujeres por provincia. Destaca el caso de Cuenca que, junto a las provincias de 
             Alicante, Almería, Granada, Huelva o Melilla, entre otras, superan la tasa media de España.
             ''')
    st.write(f"<div style='text-align: justify;'>{texto}</div>", unsafe_allow_html=True)
    st.text('   ')



    # ---GRÁFICO 1.A. TASA DE DENUNCIAS POR CADA MIL MUJERES POR PROVINCIA---

    denu_combi = pd.read_csv('data_clean/portal_estadistico_vio_gen/denu_combi.csv')
    provincias = denu_combi['provincia'].unique()
    provincia_seleccionada = st.selectbox('Selecciona una provincia:', provincias)
    pro = denu_combi[denu_combi['provincia'] == provincia_seleccionada]
    media_total = denu_combi.groupby('año')['tasa_por_1000'].mean().reset_index()

    # Filtramos ya que no hay datos posteriores para el total de la población
    pro = pro[pro['año'] <= 2021]
    media_total = media_total[media_total['año'] <= 2021]

    # Creamos el gráfico de barras para la provincia
    bars = alt.Chart(pro).mark_bar(color='#A7CAB1').encode(
        x='año:O',
        y='tasa_por_1000:Q',
        tooltip=['tasa_por_1000:Q']).properties(width=1000, height=600)

    # Línea para la media total de España
    line = alt.Chart(media_total).mark_line(color='#4747FF', strokeDash=[5, 5]).encode(
        x='año:O',
        y='tasa_por_1000:Q')
    
    chart = (bars + line).properties(
        title=f'Evolución de la tasa de denuncias por violencia de género en {provincia_seleccionada} y media de España:')

    st.altair_chart(chart)

    st.text('   ')

    st.divider()



    # ---GRAFICO 1.B. DENUNCIAS POR TRIMESTRE---

    texto = ('''
             En el siguiente gráfico se visualizan las variaciones por trimestre que se dan en 
             las denuncias por violencia de género entre 2009 y 2022. Como podemos observar, estas han 
             seguido una tendencia similar a lo largo de los años, si bien en el tercer trimestre
             se aprecia siempre una mayor cantidad de denuncias.
             ''')
    st.write(f"<div style='text-align: justify;'>{texto}</div>", unsafe_allow_html=True)

    st.text('   ')

    denu = pd.read_csv('data_clean/portal_estadistico_vio_gen/denuncias.csv')
    denu = denu[(denu['año'] >= 2008) & (denu['año'] <= 2022)]
    df_grouped = denu.groupby(['año', 'trimestre']).agg({'total_denuncias': 'mean'}).reset_index()
    orden = ['primero', 'segundo', 'tercero', 'cuarto']
    
    fig = px.line(df_grouped, x='año', y='total_denuncias', color='trimestre',
                labels={'total_denuncias': 'Media de Denuncias', 'trimestre': 'Trimestre'},
                title='Evolución de las denuncias por violencia de género según trimestre a lo largo de los años',
                color_discrete_sequence=['#9381FF', '#A7CAB1', '#B8B8FF', '#FF934F'],
                category_orders={'trimestre': orden},
                width=1000, height=600)

    
    fig.update_layout(xaxis_title='Año', yaxis_title='Media de Denuncias', legend_title='Trimestre',
                    legend=dict(orientation='h', y=-0.15)) # Esto sirve para ajustar la posición de la leyenda
                    
    st.plotly_chart(fig)




# --- PAGINA 2. LLAMADAS RECIBIDAS POR EL 016 ---

def llamadas():
    st.title('Llamadas recibidas por el 016')
    texto = '''
        El Ministerio de Igualdad, a través de la [Delegación del Gobierno contra la Violencia de Género](https://violenciagenero.igualdad.gob.es/home.htm), 
        ofrece un servicio integral para brindar [información](https://violenciagenero.igualdad.gob.es/informacionUtil/recursos/telefono016/home.htm), 
        asesoramiento jurídico, y atención psicosocial inmediata por personal especializado a todas las formas de violencia contra las mujeres,
        a través del número telefónico de marcación abreviada [016](https://violenciagenero.igualdad.gob.es/informacionUtil/recursos/telefono016/home.htm); 
        por WhatsApp en el número [600 000 016](https://wa.me/600000016); a través de un chat online en la página web de la Delegación del Gobierno contra 
        la Violencia de Género y por correo electrónico al servicio 016 online: [016-online@igualdad.gob.es](mailto:016-online@igualdad.gob.es).
        En el siguiente gráfico puedes seleccionar la provincia sobre la que deseas ver la tasa de llamadas recibidas por el 016
        por cada mil mujeres que residen en dicha provincia y podrás compararla con la media nacional.
        '''
    st.markdown(texto)



# ---GRÁFICO 2.A. TASA DE LLAMADAS AL 016 POR CADA MIL MUJERES POR PROVINCIA---
    
    llam_combi = pd.read_csv('data_clean/portal_estadistico_vio_gen/llam_combi.csv')
    provincias = llam_combi['provincia'].unique()
    provincia_seleccionada = st.selectbox('Selecciona una provincia:', provincias)
    pro = llam_combi[llam_combi['provincia'] == provincia_seleccionada]
    media_total = llam_combi.groupby('año')['tasa_por_1000'].mean().reset_index()

    st.text('   ')

    # Filtramos ya que no hay datos posteriores para el total de la población
    pro = pro[pro['año'] <= 2021]
    media_total = media_total[media_total['año'] <= 2021]

    # Creamos el gráfico de barras para la provincia
    bars = alt.Chart(pro).mark_bar(color='#A7CAB1').encode(
        x='año:O',
        y='tasa_por_1000:Q',
        tooltip=['tasa_por_1000:Q']).properties(width=1000, height=600)

    # Línea para la media total de España
    line = alt.Chart(media_total).mark_line(color='#4747FF', strokeDash=[5, 5]).encode(
        x='año:O',
        y='tasa_por_1000:Q')

    chart = (bars + line).properties(
        title=f'Evolución de la tasa de llamadas al 016 en {provincia_seleccionada.capitalize()} y media de España:')

    st.altair_chart(chart)

    st.text('   ')

    st.divider()


    # ---GRAFICO 2.B. LLAMADAS AL 016 Y DENUNCIAS POR AÑO ---
        
    texto = '''
    En el siguiente gráfico se visualiza la evolución tanto de las llamadas como de
    las denuncias por violencia de género entre 2009 y 2022. Como podemos observar, podría existir cierta
    correlación entre ambas variables, lo cual cobra sentido si pensamos que muchas de esas llamadas es posible que 
    hayan terminado en una denuncia real. Ambas variables se han ido incrementando con el paso del tiempo, lo que
    puede traducirse en una mayor concienciación sobre la violencia de género y el aumento de la
    voluntad de las mujeres en solicitar apoyo ante tal situación.
    '''
    st.write(f"<div style='text-align: justify;'>{texto}</div>", unsafe_allow_html=True)


    llam_denu = pd.read_csv('data_clean/portal_estadistico_vio_gen/llam_denu.csv')
    df_selected = llam_denu[['año', 'total_llamadas', 'total_denuncias']]
    df_selected = df_selected[df_selected['año'] <= 2022]

    # Agrupamos por año y calculamos la suma de llamadas y denuncias
    df_grouped = df_selected.groupby('año').mean().reset_index()

    # Crear gráfico interactivo con Plotly Express
    fig = px.line(df_grouped, x='año', y=['total_llamadas', 'total_denuncias'],
                labels={'value': 'Media', 'variable': 'Tipo'},
                title='Evolución de las denuncias por violencia de género y llamadas al 016 por año',
                markers={'total_llamadas': 'circle', 'total_denuncias': 'x'},
                color_discrete_sequence=['#A7CAB1', '#9381FF'])

    fig.update_layout(xaxis_title='Año', yaxis_title='Media', legend=dict(orientation='h'),
                      width=1000, height=600)

    st.plotly_chart(fig)


    st.text('   ')

    st.divider()


    # ---GRAFICO 2.C. LLAMADAS AL 016 SEGÚN PERSONA LLAMANTE ---

    texto = ('''
             El siguiente gráfico permite conocer el origen de las llamadas recibidas por el 016, a saber: la propia usuaria, 
             un familiar u origen desconocido. Como se puede apreciar, la mayoría de las llamadas son realizadas por la propia
             usuaria, lo cual indica que la difusión de la existencia de este servicio llega a esas víctimas que pueden requerirlo
             y dan el paso de pedir ayuda.
             ''')
    st.write(f"<div style='text-align: justify;'>{texto}</div>", unsafe_allow_html=True)

    llam = pd.read_csv('data_clean/portal_estadistico_vio_gen/llamadas016.csv')
    df_filtered = llam[llam['año'] <= 2022]

   
    fig = px.bar(df_filtered, x='año', y='total_llamadas', color='llamante',
                labels={'total_llamadas': 'Total de Llamadas', 'año': 'Año'},
                title='Llamadas al 016 según la persona llamante',
                category_orders={'llamante': sorted(df_filtered['llamante'].unique())},  # Orden personalizado para la leyenda
                width=1000, height=600,
                color_discrete_sequence=['#A7CAB1', '#FF934F', '#B8B8FF'])

    
    fig.update_layout(xaxis_title='Año', yaxis_title='Total de Llamadas', legend_title='Llamante',
                    legend=dict(orientation='h', y=-0.15))  # Ajustar la posición de la leyenda

    
    st.plotly_chart(fig)


# --- PAGINA 3. VICTIMAS DE VIOLENCIA DE GENERO---

def victimas():
    st.title('Mujeres asesinadas por violencia de género')
    st.write('''
    Aquí te mostramos datos relacionados con múltiples variables que ofrecen diferente
    información sobre las mujeres que han sido asesinadas por sus agresores durante
    estos años. Podrás visualizar datos relativos a si agresor y víctima eran pareja o 
    había convivencia, si el agresor se suicidó, si había denuncia previa así como otros
    datos relativos a las edades u origen de ambos.
    ''')

    # ---GRAFICO 3.A. VICTIMAS COMBINADO---
    
    vic = pd.read_csv('data_clean/portal_estadistico_vio_gen/victimas_mortales.csv')

    filtros_disponibles = ['pareja', 'convivencia', 'suicidio', 'denuncia', 'edad_agresor',
                            'edad_victima', 'nacimiento_agresor', 'nacimiento_victima']
    # Personalizamos:
    filtros = {
        'pareja': '¿Eran pareja?',
        'convivencia': '¿Había convivencia?',
        'suicidio': '¿Hubo suicidio por parte del agresor?',
        'denuncia': '¿Existía denuncia previa?',
        'edad_agresor': 'Rango de edad Agresor',
        'edad_victima': 'Rango de edad Víctima',
        'nacimiento_agresor': 'Procedencia Agresor',
        'nacimiento_victima': 'Procedencia Víctima'}
    
    filtros_disponibles = list(filtros.values())

    # Agregamos el boton de filtro:
    filtros_nuevos = st.selectbox('Selecciona un filtro:', filtros_disponibles)

    # Buscamos la key:
    filtro_seleccionado = next(key for key, value in filtros.items() if value == filtros_nuevos)

    # Orden de edades:
    orden_edades = ['<16', '16-17', '18-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-84', '81-90', '>=85', 'desconocido']

    colores = ['#9381FF', '#A7CAB1', '#B8B8FF', '#FFD8BE', '#6F9B88', '#B8B8FF', '#FF934F', '#E8998D', '#365939', '#4747FF', '#F3C98B']
    fig = px.bar(vic, x='año', y='total_victimas_mortales', color=filtro_seleccionado,
                labels={'total_victimas_mortales': 'Total de mujeres asesinadas'},
                title=f'Evolución anual de mujeres asesinadas según filtro seleccionado',
                width=1000, height=600, 
                category_orders={'edad_agresor': orden_edades, 'edad_victima': orden_edades},
                color_discrete_sequence=colores)

    fig.update_layout(xaxis_title='Año', yaxis_title='Total de mujeres asesinadas')

    st.plotly_chart(fig)

    st.text('   ')

    st.divider()


    #--GRAFICO 3.B. DISTRIBUCIÓN VÍCTIMAS MORTALES POR TRIMESTRE Y PROVINCIA---
    st.write('''
    En el siguiente gráfico, puedes elegir una provincia para ver la distribución de víctimas mortales
    por trimestre a lo largo de los años en esa provincia.
    ''')
    # Filtramos por provincia
    provincia_seleccionada = st.selectbox('Selecciona una provincia:', vic['provincia'].unique())
    df_provincia = vic[vic['provincia'] == provincia_seleccionada]

    fig = px.bar(df_provincia, x='año', y='total_victimas_mortales', color='trimestre',
                labels={'total_victimas_mortales': 'Víctimas Mortales', 'año': 'Año'},
                title=f'Distribución de Víctimas Mortales por Trimestre y Año en {provincia_seleccionada.capitalize()}',
                barmode='stack',
                width=1000, height=600,
                color_discrete_sequence=['#9381FF', '#A7CAB1', '#B8B8FF', '#FF934F'])

    fig.update_layout(xaxis_title='Año', yaxis_title='Víctimas Mortales')

    st.plotly_chart(fig)

    st.text('   ')

    st.divider()

   

# ---PAGINA 4. MENORES---

def menores():
    st.title('Menores asesinados por violencia de género')
    st.write('''El siguiente gráfico muestra datos relacionados con las muertes de menores a causa de la violencia de género.
             Gracias al mismo, podrás conocer la distribución por edad del menor, si el agresor era su padre biológico o si 
             se produjo suicidio tras los hechos.
             ''')
    
    st.text('   ')

# ---GRAFICO 4.A. MENORES:

    men = pd.read_csv('data_clean/portal_estadistico_vio_gen/menores.csv')

    # Personalizamos filtros
    filtros_disponibles = ['edad', 'suicidio', 'provincia', 'padre_biologico']

    filtros = {
        'edad': 'Edad del menor',
        'suicidio': '¿Hubo suicidio por parte del agresor?',
        'provincia': 'Provincia',
        'padre_biologico': '¿Era el agresor su padre biológico?'}
    
    filtros_disponibles = list(filtros.values())

    # Agregamos boton de filtro: 
    filtros_nuevos = st.selectbox('Selecciona un filtro:', filtros_disponibles)

    # Buscamos la key:
    filtro_seleccionado = next(key for key, value in filtros.items() if value == filtros_nuevos)
    
    # Orden de edades:
    orden_edades = ['<1', '1-2', '3-4', '5-6', '7-8', '9-10', '11-12', '13-14', '15-17']

    color = ['#9381FF', '#A7CAB1', '#B8B8FF', '#FFD8BE', '#6F9B88', '#B8B8FF', '#FF934F', '#E8998D', '#365939', '#4747FF', '#F3C98B']

    fig = px.bar(men, x='año', y='total_menores_vict_mortales', color=filtro_seleccionado,
                labels={'total_menores_vict_mortales': 'Total de menores asesinados'},
                title=f'Evolución anual de menores asesinados según filtro seleccionado',
                width=1000, height=600, 
                category_orders={'edad': orden_edades},
                color_discrete_sequence=color)

    fig.update_layout(xaxis_title='Año', yaxis_title='Total de menores asesinados')

    st.plotly_chart(fig)


# ---PAGINA 5. PROTECCION Y TIPOS DE DELITOS---

def prote_tipos():
    st.title('Protección a las víctimas y tipología de delitos')
    texto = ('''
             La orden de protección es una herramienta legal diseñada para salvaguardar a las víctimas de la violencia 
             de género ante diversas formas de agresión. En una resolución judicial inmediata, conocida como auto, se aplican 
             medidas de protección y seguridad de índole penal y civil. Simultáneamente, esta orden activa los mecanismos de asistencia 
             y protección social ofrecidos por el Estado, las Comunidades Autónomas y las Corporaciones Locales en beneficio de la víctima. 
             En resumen, la orden de protección integra los diferentes recursos legales destinados a proteger a la víctima, otorgándole un 
             estatus completo de resguardo.
             ''')
    
    st.write(f"<div style='text-align: justify;'>{texto}</div>", unsafe_allow_html=True)
    st.text('   ')


    # ---GRAFICO 5.A. ORDENES DE PROTECCION---

    ord = pd.read_csv('data_clean/portal_estadistico_vio_gen/ordenes_prot.csv')

    # Boton de filtro:
    provincias = ord['provincia'].unique()
    provincia_seleccionada = st.selectbox('Selecciona una provincia:', provincias)

    pro_ord = ord[ord['provincia'] == provincia_seleccionada]

    bars = alt.Chart(pro_ord).mark_bar(color='#A7CAB1').encode(
    x='año:O',
    y='numero_ordenes_proteccion:Q',
    tooltip=['año:N', alt.Tooltip('numero_ordenes_proteccion:Q', title='Número de Órdenes de Protección')]
    ).properties(
        width=1000,
        height=600,
        title=f'Evolución anual del número de órdenes de protección en {provincia_seleccionada.capitalize()}')
    
    st.altair_chart(bars, use_container_width=True)

    st.text('   ')
    st.divider()



    # ---GRAFICO 5.B.TIPOLOGIAS DELITOS---

    texto = ('''
             En el siguiente gráfico, exploraremos la evolución de diversos tipos de delitos relacionados con la violencia de 
             género a lo largo de los años. Los delitos considerados incluyen amenazas, delitos, coacciones, daños, faltas, 
             homicidio, lesiones, quebrantamiento de condena y tortura a la integridad moral. Este análisis permite una visión 
             detallada de cómo la incidencia de estos delitos ha variado con el tiempo, brindando la capacidad de realizar 
             filtrados específicos por comunidades para examinar patrones regionales. La información proporcionada busca 
             arrojar luz sobre la dinámica de la violencia de género en distintas localidades y aportar a la comprensión 
             de los desafíos y progresos en la lucha contra esta problemática a lo largo del tiempo.
             ''')
    
    st.write(f"<div style='text-align: justify;'>{texto}</div>", unsafe_allow_html=True)
    st.text('   ')

    tipos = pd.read_csv('data_clean/ine/tipos_violencias.csv')
    tiposs = ['amenazas', 'delito', 'coacciones', 'daños', 'faltas', 'homicidio', 'lesiones', 'quebrantamiento_condena', 'tortura_integridad_moral']
    tipos = tipos[tipos['tipo'].isin(tiposs)]

    # Boton para filtro:
    comunidades = tipos['comunidad'].unique()
    comunidad_seleccionada = st.selectbox('Selecciona una comunidad:', comunidades)

    com = tipos[tipos['comunidad'] == comunidad_seleccionada]

    # Hacemos una pivot table:
    com_pivot = com.pivot_table(index=['año'], columns=['tipo'], values='total', fill_value=0).reset_index()

    # Convertimos el DataFrame a formato largo para el gráfico
    com_pivot_long = com_pivot.melt(id_vars='año', var_name='tipo', value_name='total')

    colores = ['#9381FF', '#FFD8BE', '#B8B8FF', '#A7CAB1', '#6F9B88', '#B8B8FF', '#FF934F', '#E8998D', '#365939']
    
    bars = alt.Chart(com_pivot_long).mark_bar().encode(
        x='año:O',
        y='total:Q',
        color=alt.Color('tipo:N', scale=alt.Scale(range=colores)),
        tooltip=['año:N', 'tipo:N', 'total:Q']
    ).properties(width=1000, height=600)

    st.altair_chart(bars)
        


# ---PAGINA 6. COMBINACIONES CON FESTIVOS---

def datos_combinados():
    st.title('Denuncias, llamadas 016, víctimas y festivos provinciales')
    texto = ('''
             El objetivo del siguiente gráfico es mostrar en un simple vistazo la tendencia trimestral de las denuncias,
             las llamadas al 016, las víctimas asesinadas para tratar de encontrar correlaciones o tendencias. 
             ''')
    st.write(f"<div style='text-align: justify;'>{texto}</div>", unsafe_allow_html=True)
    st.text('   ')
    

# --GRAFICOS COMBINADOS LLAMADAS, DENUNCIAS, VICTIMAS Y FESTIVOS--

    datos = pd.read_csv('data_clean/portal_estadistico_vio_gen/llam_denu_fest_vic.csv')

    # Boton para el filtro
    provincias = datos['provincia'].unique()
    provincia_seleccionada = st.selectbox('Selecciona una provincia:', provincias)
    datos_provincia = datos[datos['provincia'] == provincia_seleccionada]

    orden = ['primero', 'segundo', 'tercero', 'cuarto']
    

    col1, col2 = st.columns(2)

    # ---COLUMNA 1---

    with col1:

        # Agrupamos los datos por trimestre
        datos_agrupados = datos_provincia.groupby('trimestre').agg({
            'total_denuncias': 'mean',
            'total_llamadas': 'mean',
            'total_victimas_mortales': 'mean',
            'total_festivos': 'mean'
        }).reindex(orden).reset_index()

        # --GRAFICO 6.A. DENUNCIAS--

        fig_denuncias = px.line(datos_agrupados, x='trimestre', y='total_denuncias', labels={'total_denuncias': 'Total de Denuncias'},
                                title=f'Denuncias en {provincia_seleccionada.capitalize()} por trimestre',
                                category_orders={'trimestre': orden},
                                color_discrete_sequence=['#9381FF'])

        st.plotly_chart(fig_denuncias, use_container_width=True)

        # --GRAFICO 6.B. LLAMADAS 016--

        fig_llamadas = px.line(datos_agrupados, x='trimestre', y='total_llamadas', labels={'total_llamadas': 'Total de Llamadas'},
                            title=f'Llamadas al 016 en {provincia_seleccionada.capitalize()} por trimestre',
                            category_orders={'trimestre': orden},
                            color_discrete_sequence=['#FF934F'])

        st.plotly_chart(fig_llamadas, use_container_width=True)



    with col2:

        # --GRAFICO 6.C. LLAMADAS 016--

        fig_victimas = px.line(datos_agrupados, x='trimestre', y='total_victimas_mortales', labels={'total_victimas_mortales': 'Total de Víctimas Mortales'},
                            title=f'Víctimas Mortales en {provincia_seleccionada.capitalize()} por trimestre',
                            category_orders={'trimestre': orden},
                            color_discrete_sequence=['#E8998D'])
        
        st.plotly_chart(fig_victimas, use_container_width=True)

        
        # --GRAFICO 6.D. FESTIVOS--


        fig_festivos = px.line(datos_agrupados, x='trimestre', y='total_festivos', labels={'total_festivos': 'Total de Festivos'},
                            title=f'Festivos en {provincia_seleccionada.capitalize()} por trimestre',
                            category_orders={'trimestre': orden},
                            color_discrete_sequence=['#A7CAB1'])
        
        fig_festivos.update_traces(line=dict(dash='solid'))
        st.plotly_chart(fig_festivos, use_container_width=True)


        


# ---PAGINA 9. NORMATIVAS---



def normas():
    st.title('¿Qué normativas rigen en mi Comunidad Autónoma?')
    st.write('''Aquí puedes encontrar información sobre las distintas normativas regionales en materia de violencia de género. En el gráfico
             puedes observar el nº de Comunidades Autónomas que realizaron cada año modificaciones o actualizaciones en esta materia.
             Más abajo, podrás conocer dichas normativas según la Comunidad seleccionada.
             ''')
    
    norm = pd.read_csv('data_clean/scrapeo/norm.csv')
    norm['normativas_presentes'] = norm['total_normativas'].apply(lambda x: 'Sí' if x > 0 else 'No')

   
    fig = px.histogram(norm, x='año', color='normativas_presentes',
                    labels={'año': 'Año', 'normativas_presentes': '¿Hubo normativa?'},
                    title='Presencia de Normativas por Año y Comunidad Autónoma',
                    category_orders={'normativas_presentes': ['Sí', 'No']},
                    width=1000, height=600,
                    color_discrete_sequence=['#9381FF', '#A7CAB1'])


    fig.update_layout(xaxis_title='Año', yaxis_title='Número de Comunidades Autónomas',
                    legend_title='¿Hubo normativa ese año?',
                    legend=dict(orientation='h', y=-0.15, x=0.5),  
                    barmode='group')  # Barras agrupadas

    st.plotly_chart(fig)

    st.text('   ')
    st.divider()


    # Cargamos los datos sobre leyes:

    with open('data_clean/scrapeo/leyes.json', 'r') as archivo_json:
        datos_leyes = json.load(archivo_json)

    # Filtro comunidad:
    comunidad = list(datos_leyes.keys())
    comunidad_selecc = st.selectbox('Selecciona una Comunidad Autónoma para conocer su normativa en materia de Violencia de Género:', comunidad)

    # Mostramos las normas de cada comunidad seleccionada:
    st.write(f"Normativa Regional en {comunidad_selecc}:")
    leyes_regionales = datos_leyes[comunidad_selecc]
    for ley in leyes_regionales:
        st.write(f"- {ley}")



    
# ---PAGINA 10. ---

def info():
    st.title('¿Quieres saber más?')
    
    st.write('''
            - Si estás interesada en obtener más información en esta materia, te invito a que visites la web de [FEMINICIDIO.NET](https://feminicidio.net/)
            donde podrás encontrar más informes y cifras, formación y otros recursos sobre violencia de género.''')

    st.write('''
            - Por aquí te dejo una serie de [testimonios de mujeres supervivientes](https://violenciagenero.igualdad.gob.es/informacionUtil/testimonios/supervivientes/home.htm) para que puedas acercarte más a esta realidad.
            ''')
    
    st.write('- Aquí puedes ver la última campaña del Ministerio de Igualdad contra la Violencia de Género ⬇️')
    

    video = 'https://www.youtube.com/watch?v=bE3r26x-VJM&t=4s'

    st.video(video)
    


# ----ESTRUCTURA DEL MENÚ LATERAL----

options = {
    'Conoce este espacio': home,
    'Denuncias por violencia de género': denuncias,
    'Llamadas al 016': llamadas,
    'Mujeres víctimas': victimas,
    'Menores víctimas': menores,
    'Protección y tipología de delitos': prote_tipos,
    '¿Qué ocurre cuando hay festivos?': datos_combinados,
    'Normativas en materia de violencia de género': normas,
    'Más información': info
}

# Título en el menú lateral
st.sidebar.markdown('<span style="color: #4757BB; font-size: 24px; font-weight: bold;">VIODATA 🟣</span>', unsafe_allow_html=True)


# Selección del menú principal
st.sidebar.markdown('<span style="color: #4757BB; font-size: 18px; font-weight: bold;">¿Qué quieres saber hoy?</span>', unsafe_allow_html=True)
selected_option = st.sidebar.radio('',list(options.keys()))

# Línea divisoria
st.sidebar.markdown('<hr style="border-color: #511973;">', unsafe_allow_html=True)


# Obtener la función de la opción seleccionada y ejecutarla
if selected_option in options:
    options[selected_option]()


