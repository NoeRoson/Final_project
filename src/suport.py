import pandas as pd
import numpy as np
from unidecode import unidecode
import warnings
warnings.filterwarnings('ignore')
import re
from fuzzywuzzy import fuzz


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












