import pandas as pd
import numpy as np
from unidecode import unidecode
import warnings
warnings.filterwarnings('ignore')
import re


def lower_tildes(columna):
    '''Entra una columna:
    Se convierte a minúsculas y se eliminan tildes
    '''
    return columna.apply(lambda x: unidecode(str(x).lower()))

def format_col(columns):
    '''Entra un df.columns:
    Se convierte a minúsculas y se eliminan tildes
    '''
    return columns.map(lambda x: unidecode(x.lower()))


def clean_year(columna):
    '''
    Entra una columna:
    Elimina caracteres no numéricos y convierte a tipo de dato de año
    '''
    columna = columna.astype(str)  # Asegúrate de que la columna sea de tipo cadena
    columna = columna.str.replace(r'\D', '', regex=True)  # Elimina caracteres no numéricos
    columna = pd.to_datetime(columna, format='%Y', errors='coerce')  # Convierte a tipo de dato de año
    return columna.dt.year  # Extrae el año de la fecha resultante

