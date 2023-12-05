import pandas as pd
import numpy as np
from unidecode import unidecode
import warnings
warnings.filterwarnings('ignore')
import re
from fuzzywuzzy import fuzz
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import altair as alt


def unif_col(columns):
    '''Entran todas las columnas de un df:
    Se convierte a minúsculas y se eliminan tildes
    '''
    return map(lambda x: unidecode(x.lower()), columns)


def lower_tildes(column):
    '''Entra una columna:
    Se convierte a minúsculas y se eliminan tildes
    '''
    return column.apply(lambda x: unidecode(str(x).lower()))


def clean_year(columna):
    '''
    Entra una columna:
    Elimina caracteres no numéricos y convierte a tipo de dato de año
    '''
    columna = columna.astype(str) #  Nos aseguramos de que la columna sea de tipo cadena
    columna = columna.str.replace(r'\D', '', regex=True)  # Elimina caracteres no numéricos
    columna = pd.to_datetime(columna, format='%Y', errors='coerce')  # Convierte a tipo de dato de año
    return columna.dt.year  # Extrae el año de la fecha resultante


def trimestre(mes):
    '''
    Entra un mes y sale el número del trimestre
    '''
    if mes in ['enero', 'febrero', 'marzo']:
        return 'primero'
    elif mes in ['abril', 'mayo', 'junio']:
        return 'segundo'
    elif mes in ['julio', 'agosto', 'septiembre']:
        return 'tercero'
    else:
        return 'cuarto'
    

def eliminar_alfa(columna):
    '''
    Entra una columna de un DataFrame.
    Elimina los caracteres alfabéticos de cada elemento de la columna y los espacios.
    '''
    return columna.apply(lambda x: ''.join(c if not c.isalpha() and not c.isspace() else '' for c in str(x)))


def ccaa(texto):
    '''
    Entra una columna de un DataFrame.
    Divide la cadena en caso de encontrar un paréntesis.
    Se queda con la primera parte (antes del '(').
    '''
    nombres = texto.split('(')
    comunidad = nombres[0].strip()
    
    return comunidad




def comunidades(dataframes, column_name='comunidad'):
    '''
    Entra una lista de DataFrames (dataframes) y un nombre de columna por defecto ('comunidad')
    '''

    nombres = ['andalucia', 'aragon', 'asturias', 'baleares', 'canarias',
                             'cantabria', 'castilla y leon', 'castilla la mancha', 'cataluña',
                             'valencia', 'extremadura', 'galicia', 'madrid',
                             'region de murcia', 'navarra', 'pais vasco', 'la rioja',
                             'ceuta', 'melilla']

    def normalizar_comunidad(nombre_comunidad):
        '''
        Toma un nombre de comunidad y devuelve la mejor coincidencia de la lista de nombres dados 
        utilizando la función fuzz.ratio para calcular la similitud.
        '''
        mejor_coincidencia = max(nombres, key=lambda x: fuzz.ratio(x, nombre_comunidad.lower()))
        return mejor_coincidencia
       
    for df in dataframes:
        '''
        Se itera sobre cada df de la lista de dataframes. Si la columna especificada (column_name) 
        está presente, se aplica la normalización
        '''
        if column_name in df.columns:
            df[column_name] = df[column_name].apply(normalizar_comunidad)

    return dataframes



def eliminar_num(texto):
    return ''.join(caracter for caracter in texto if not caracter.isdigit())



def provincias(dataframes, provincia_column='provincia'):
    '''
    Normaliza los nombres de provincias en una lista de DataFrames.
    '''

    def normalizar_provincia(nombre_provincia):
        '''
        Toma un nombre de provincia y devuelve la mejor coincidencia de la lista de nombres dados 
        utilizando la función fuzz.ratio para calcular la similitud.
        '''
        nombres_provincias = ['alava', 'albacete', 'alicante', 'almeria', 'asturias', 'avila', 'badajoz',
                              'barcelona', 'burgos', 'caceres', 'cadiz', 'cantabria', 'castellon', 'ciudad real',
                              'cordoba', 'cuenca', 'gerona', 'granada', 'guadalajara', 'guipuzcoa', 'huelva',
                              'huesca', 'islas baleares', 'jaen', 'coruña', 'rioja', 'las palmas', 'leon',
                              'lerida', 'lugo', 'madrid', 'malaga', 'melilla', 'murcia', 'navarra', 'orense',
                              'palencia', 'pontevedra', 'salamanca', 'santa cruz de tenerife', 'segovia', 'sevilla',
                              'soria', 'tarragona', 'teruel', 'toledo', 'valencia', 'valladolid', 'vizcaya',
                              'zamora', 'zaragoza']

        mejor_coincidencia = max(nombres_provincias, key=lambda x: fuzz.ratio(x, nombre_provincia.lower()))
        return mejor_coincidencia

    for df in dataframes:
        '''
        Normalizar provincias si la columna especificada (provincia_column) está presente
        '''
        if provincia_column in df.columns:
            df[provincia_column] = df[provincia_column].apply(normalizar_provincia)

    return dataframes



def crear_ccaa(dataframes, provincia_column='provincia'):
    '''
    Toma un nombre de provincia y crea en una nueva columna llamada comunidad la comunidad autónoma a la que pertenece
    '''

    prov_ccaa = {'alava': 'pais vasco',
    'albacete': 'castilla la mancha',
    'alicante': 'comunidad valenciana',
    'almeria': 'andalucia',
    'asturias': 'asturias',
    'avila': 'castilla y leon',
    'badajoz': 'extremadura',
    'barcelona': 'cataluña',
    'burgos': 'castilla y leon',
    'caceres': 'extremadura',
    'cadiz': 'andalucia',
    'cantabria': 'cantabria',
    'castellon': 'comunidad valenciana',
    'ciudad real': 'castilla la mancha',
    'cordoba': 'andalucia',
    'cuenca': 'castilla la mancha',
    'gerona': 'cataluña',
    'granada': 'andalucia',
    'guadalajara': 'castilla la mancha',
    'guipuzcoa': 'pais vasco',
    'huelva': 'andalucia',
    'huesca': 'aragon',
    'islas baleares': 'islas baleares',
    'jaen': 'andalucia',
    'coruña': 'galicia',
    'rioja': 'la rioja',
    'las palmas': 'canarias',
    'leon': 'castilla y leon',
    'lerida': 'cataluña',
    'lugo': 'galicia',
    'madrid': 'madrid',
    'malaga': 'andalucia',
    'melilla': 'melilla',
    'murcia': 'murcia',
    'navarra': 'navarra',
    'orense': 'galicia',
    'palencia': 'castilla y leon',
    'pontevedra': 'galicia',
    'salamanca': 'castilla y leon',
    'santa cruz de tenerife': 'canarias',
    'segovia': 'castilla y leon',
    'sevilla': 'andalucia',
    'soria': 'castilla y leon',
    'tarragona': 'cataluña',
    'teruel': 'aragon',
    'toledo': 'castilla la mancha',
    'valencia': 'comunidad valenciana',
    'valladolid': 'castilla y leon',
    'vizcaya': 'pais vasco',
    'zamora': 'castilla y leon',
    'zaragoza': 'aragon'}

    for df in dataframes:
        '''
        Normaliza provincias si la columna especificada (provincia_column) está presente
        Mapea las provincias y crea una nueva columna 'comunidad' al lado de 'provincia'
        '''
        df.insert(df.columns.get_loc(provincia_column) + 1, 'comunidad', df[provincia_column].map(prov_ccaa))


    return dataframes



def plot_denuncias(df, provincia):
    # Filtramos el DataFrame para la provincia específica
    pro = df[df['provincia'] == provincia]

    # Calculamos la media total del DataFrame
    media_total = df.groupby('año')['tasa_por_1000'].mean().reset_index()

    # Crear el gráfico de barras para la provincia
    plt.figure(figsize=(10, 6))
    plt.bar(pro['año'], pro['tasa_por_1000'], color='pink', label=provincia.capitalize())

    # Línea para la media total del DataFrame
    plt.plot(media_total['año'], media_total['tasa_por_1000'], linestyle='--', color='purple', label='Media España')

    plt.xlabel('Año')
    plt.ylabel('Tasa por 1000 mujeres')
    plt.title(f'Evolución de la tasa de denuncias por VG en {provincia.capitalize()} y media de España')
    plt.legend()
    plt.show()



def plot_llamadas(df, provincia):
    # Filtramos el DataFrame para la provincia específica
    pro = df[df['provincia'] == provincia]

    # Calculamos la media total del DataFrame
    media_total = df.groupby('año')['tasa_por_1000'].mean().reset_index()

    # Crear el gráfico de barras para la provincia
    plt.figure(figsize=(10, 6))
    plt.bar(pro['año'], pro['tasa_por_1000'], color='pink', label=provincia.capitalize())

    # Línea para la media total del DataFrame
    plt.plot(media_total['año'], media_total['tasa_por_1000'], linestyle='--', color='purple', label='Media España')

    plt.xlabel('Año')
    plt.ylabel('Tasa por 1000 mujeres')
    plt.title(f'Evolución de la tasa de llamadas al 016 en {provincia.capitalize()} y media de España')
    plt.legend()
    plt.show()



def norm_data(df, columns_to_normalize):
    """
    Normaliza las columnas especificadas de un DataFrame utilizando la normalización estándar (z-score).

    Parameters:
    - df (pd.DataFrame): El DataFrame que contiene los datos.
    - columns_to_normalize (list): Lista de nombres de columnas que se deben normalizar.

    Returns:
    - pd.DataFrame: Un nuevo DataFrame con las columnas normalizadas.
    """
    scaler = StandardScaler()
    df_normalized = df.copy()
    df_normalized[columns_to_normalize] = scaler.fit_transform(df_normalized[columns_to_normalize].values)
    return df_normalized





def plot_four_lines(df, provincia, año):
    # Filtrar el DataFrame para la provincia y año específicos
    df_provincia_año = df[(df['provincia'] == provincia) & (df['año'] == año)]

    # Crear un gráfico de líneas para cada variable
    fig, axes = plt.subplots(nrows=4, figsize=(10, 12))

    # Iterar sobre las variables y crear gráficos individuales
    for i, variable in enumerate(['total_denuncias', 'total_llamadas', 'total_victimas_mortales', 'total_festivos']):
        sns.lineplot(
            x='trimestre',
            y=variable,
            color=['#FFB6C1', '#FFD700', '#87CEFA', '#98FB98'][i],  # Color diferente para cada variable
            label=variable.capitalize(),
            marker='o',
            ci=None,
            ax=axes[i],
            data=df_provincia_año
        )

        # Etiquetas y título para cada subgráfico
        axes[i].set_xlabel('Trimestre')
        axes[i].set_ylabel(variable.capitalize())
        axes[i].set_title(f'{variable.capitalize()} en {provincia.capitalize()} en {año}')
        axes[i].set_xticks(ticks=[0, 1, 2, 3])
        axes[i].set_xticklabels(['primero', 'segundo', 'tercero', 'cuarto'])

        # Mostrar la leyenda en el último subgráfico
        if i == 3:
            axes[i].legend()

    # Ajustar el espaciado entre subgráficos
    plt.tight_layout()

    # Mostrar los gráficos
    plt.show()



def plot_delitos(df, comunidad):
    # Filtrar el DataFrame para la comunidad específica
    df_comunidad = df[df['comunidad'] == comunidad]

    # Crear el gráfico de barras
    plt.figure(figsize=(12, 8))
    sns.set(style="dark")
    sns.lineplot(x='año', y='total', hue='tipo', palette = ("tab10"), marker='o', data=df_comunidad)

    # Etiquetas y título
    plt.xlabel('Año')
    plt.ylabel('Total de Delitos')
    plt.title(f'Evolución del Total de Delitos por Tipo en {comunidad.capitalize()}')

    # Mostrar el gráfico
    plt.legend(title='Tipo de Delito', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()


def plot_interactivo_denuncias(df, provincia):
    # Filtramos el DataFrame para la provincia específica
    pro = df[df['provincia'] == provincia]

    # Calculamos la media total del DataFrame
    media_total = df.groupby('año')['tasa_por_1000'].mean().reset_index()

    # Crear el gráfico de barras para la provincia con Altair
    bars = alt.Chart(pro).mark_bar(color='pink').encode(
        x='año:O',
        y='tasa_por_1000:Q',
        tooltip=['tasa_por_1000:Q']
    ).properties(width=800, height=500)

    # Línea para la media total del DataFrame
    line = alt.Chart(media_total).mark_line(color='purple', strokeDash=[5, 5]).encode(
        x='año:O',
        y='tasa_por_1000:Q'
    )

    # Configuración del diseño del gráfico
    chart = (bars + line).properties(
        title=f'Evolución de la tasa de denuncias por VG en {provincia.capitalize()} y media de España'
    )

    # Mostrar el gráfico
    chart.show()