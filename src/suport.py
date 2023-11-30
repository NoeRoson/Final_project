import pandas as pd
import numpy as np
from unidecode import unidecode
import warnings
warnings.filterwarnings('ignore')
import re



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