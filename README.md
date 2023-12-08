# VioData: Violencia de Género en datos

![](https://github.com/NoeRoson/VioData/blob/main/img/vio.jpeg)

## ¿Qué es VioData? 🟣

<p align="justify">
    Se trata de una plataforma digital para interactuar con todos los datos disponibles sobre la violencia de género en España 📉
    </p>

<p align="justify">
    Debemos abordar esta trágica realidad que afecta a mujeres en todo el mundo y mostrar nuestro compromiso a ser agentes de cambio.
    Este espacio no solo es un depósito de información, sino también una llamada a la acción. El objetivo principal es compartir el conocimiento y herramientas necesarias para que estos datos puedan llegar a cualquier persona interesada en conocer más acerca de esta realidad.
    </p>

    ¿Me acompañas?  👐🏼
</p>

## Pasos seguidos 🐾

En primer lugar, se realiza una **extracción de los datos** que contienen la información necesaria para llevar a cabo las visualizaciones. Estos se obtienen en formato csv del [Portal Estadístico de la Delegación del Gobierno contra la Violencia de Género](https://estadisticasviolenciagenero.igualdad.gob.es/) donde se consigue información acerca de:

- Denuncias interpuestas.
- Órdenes de protección decretadas.
- Víctimas mortales por violencia de género, tanto mujeres como menores.
- Llamadas recibidas por el 016.

También se extraen datos procedentes del [Instituto Nacional de Estadística](https://www.ine.es/) relativos a los tipos de delitos cometidos en el ámbito de la violencia de género, así como el total de población existente por sexo para poder realizar las tasas de población por cada provincia.

Asimismo, se realiza un proceso de web scraping de dos url distintas: 
- Publicación del [BOE](https://www.boe.es/) que recoge información sobre las normativas regionales que han existido a lo largo de los años en las diferentes Comunidades Autónomas en materia de violencia de género.

- Página web del [Ministerio de Trabajo y Economía Social](https://www.mites.gob.es/) que recoge los días festivos en cada provincia.

Todos los datos han sido transformados y cargados en archivos .csv para su posterior análisis, llevándose a cabo una limpieza de datos desde **Python**. Tras la exploración profunda de los mismos, se ha creado una página en **Streamlit** alimentada con distintos **gráficos y filtros**, ideada para que cualquier persona pueda aprendar más sobre este fenómeno.

Las visualizaciones creadas aportan una **visión a nivel global** del fenómeno de la violencia de género en nuestro país de los últimos 20 años y también permite **profundizar** en un estudio más concreto de cada una de las variables descritas anteriormente para cada año, trimestre, mes y provincia.

## Datos destacados ✨




- Cuando comencé esta investigación me llamaba la atención que siempre hubiese más denuncias y llamadas al 016 en el **tercer trimestre**. Es algo que tengo pendiente por descubrir y que continuaré investigando. Sin embargo, una de las posibles explicaciones tiene que ver con que la tasa de denuncias por cada mil mujeres es mayor a la media nacional en las provincias del sur y menor en las del norte. Es posible que siendo el tercer trimestre el más caluroso del año esté influyendo en estos datos.

- Valorando la posibilidad de que se trate de algo estacional, otra posible explicación es que en verano tanto los adultos como los hijos menores tienen vacaciones habitualmente, lo cual puede traducirse en una mayor **fuente de estrés** que desencadene más conflictos. Sin embargo, no podemos comprobar si las denuncias interpuestas durante ese trimestre son por parte de mujeres con hijos menores o no.

- En verano, al asociarse este con más **festividades** podría llevar a pensar que en épocas más festivas aumentan las denuncias o las víctimas. Esto se puede observar para muchas de las ciudades, siendo parecida la línea de tendencia de festivos por trimestre que la de mujeres asesinadas.

- También resulta de interés observar cómo varían las distintas gráficas durante la época del confinamiento y la **pandemia**, comprobándose que baja el número de denuncias pero, en cambio, aumenta el de llamadas al 016. Esto demuestra que, a pesar de estar ambas variables bastante correlacionadas, no todas las llamadas finalizan con una denuncia.

- Otro dato relevante es el hecho de que se producen más **suicidios** por parte del agresor cuando las víctimas mortales también son los hijos menores que, además, suelen ser hijos biólogicos del agresor en la mayoría de los casos.

- Se denota la importancia de revisar por parte de las Comunidades Autónomas las actualizaciones pertinentes en las leyes de esta materia, ya que el rango de leyes en los últimos 20 años han sido de una o dos, demostrándose la **falta de relevancia política** que aún tiene este fenómeno.


## Próximos pasos 🔮

Hacer este proyecto solo me ha dejado con más ganas de descubrir datos relevantes para la lucha contra la violencia de género y de conocer por qué suceden ciertos fenómenos, para seguir investigando y poder encontrar explicaciones lógicas a esta problemática y poder actuar en consecuencia.

Como próximos pasos para seguir alimentando mi proyecto, actualmente se podría continuar por:

- Intentar descubrir el motivo de que el tercer trimestre tenga, desde siempre, mayores datos de denuncias y llamadas al 016. Sería interesante poder comparar los datos de España con los de otros países europeos y con aquellos del otro hemisferio para poder comprobar la estacionalidad de los hechos.

- Construir un mapa de calor de España en el que se pueda estudiar con detenimiento si existe diferencia significativa entre los datos de las ciudades del norte y las ciudades del sur, como a priori indican los datos.


## Recursos utilizados:

- [Instituto Nacional de Estadística](https://www.ine.es/)

- [Portal Estadístico Delegación del Gobierno contra la Violencia de Género](https://estadisticasviolenciagenero.igualdad.gob.es/)
- [Streamlit](https://streamlit.io/)
- [Selenium](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/stable/)