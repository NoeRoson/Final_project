# VioData: Violencia de Género en datos

![](https://github.com/NoeRoson/VioData/blob/main/img/vio.jpeg)

## ¿Qué es VioData?

<p align="justify">
    Se trata de una plataforma digital para interactuar con todos los datos disponibles sobre la violencia de género en España 📉
    </p>

<p align="justify">
    Debemos abordar esta trágica realidad que afecta a mujeres en todo el mundo y mostrar nuestro compromiso a ser agentes de cambio.
    Este espacio no solo es un depósito de información, sino también una llamada a la acción. El objetivo principal es compartir el conocimiento y herramientas necesarias para que estos datos puedan llegar a cualquier persona interesada en conocer más acerca de esta realidad.
    </p>

    ¿Me acompañas?  ♀ 
</p>

## Pasos seguidos

En primer lugar, se realiza una extracción de los datos que contienen la información necesaria para llevar a cabo las visualizaciones. Estos se obtienen en formato csv del [Portal Estadístico de la Delegación del Gobierno contra la Violencia de Género](https://estadisticasviolenciagenero.igualdad.gob.es/) donde se consigue información acerca de:

- Denuncias interpuestas.
- Órdenes de protección decretadas.
- Víctimas mortales por violencia de género, tanto mujeres como menores.
- Llamadas recibidas por el 016.

También se extraen datos procedentes del [Instituto Nacional de Estadística](https://www.ine.es/) relativos a los tipos de delitos cometidos en el ámbito de la violencia de género, así como el total de población existente por sexo para poder realizar las tasas de población por cada provincia.

Asimismo, se llevo a cabo web scraping de dos url distintas: 
- Publicación del [BOE](https://www.boe.es/) que recoge información sobre los festivos por provincias en España.

- Página web del [Ministerio de Trabajo y Economía Social](https://www.mites.gob.es/ que recoge )

Todos los datos obtenidos se relacionan a través del trimestre, mes y año, así como de la provincia en que sucede cada fenómeno. También se registran datos acerca de las edades de las víctimas y los agresores para conocer la correlación existente entre las mismas. 

Las visualizaciones creadas aportan una **visión a nivel global** del fenómeno de la violencia de género en nuestro país entre los años 2009 y 2023, aunque también permite **profundizar** en un estudio más concreto de cada una de las variables descritas anteriormente para cada año, trimestre, mes y provincia.

Para llevarlas a cabo, se ha utilizado la herramienta Tableau Desktop, con la que se pueden elaborar visualizaciones interactivas que permiten comprender el dato y aportar valor al análisis.

</p>

### [Dashboard mapas:](https://public.tableau.com/app/profile/noelia.roson/viz/Impacto_violencia_mapas/Mapas?publish=yes)
![](https://github.com/NoeRoson/Project_Visualization/blob/main/img/Dashboard1_maps.png)

Con esta visualización podemos observar para cada provincia, el total de órdenes de protección decretadas, llamadas al 016, víctimas mortales y denuncias interpuestas por violencia de género, filtrando en la ciudad, al igual que en los gráficos siguientes. 

### [Dashboard gráficos](https://public.tableau.com/app/profile/noelia.roson/viz/Impacto_violencia_genero/Grficos?publish=yes)
![](https://github.com/NoeRoson/Project_Visualization/blob/main/img/Dashboard2_graphics.png)

Estos gráficos nos aportan información sobre las campañas llevadas a cabo para la prevención de la violencia de género y las denuncias registradas por trimestre, donde se puede observar que el tercer trimestre siempre es el que mayores datos registra.

Por otro lado, tenemos una comparativa de las denuncias, llamadas al 016, órdenes de protección y víctimas mortales, según el año, siendo destacados los datos máximos y mínimos para cada una de ellas. 

Finalmente, podemos observar la correlación existente entre las edades víctima-agresor, viendo cómo aumentan los datos y la coincidencia en las edades centrales, especialmente entre los 30 y los 50.


## Recursos utilizados:

- [Tableau Desktop](https://www.tableau.com/es-es)
- [Pandas](https://pandas.pydata.org/)
- [Portal Estadístico Delegación del Gobierno contra la Violencia de Género](https://estadisticasviolenciagenero.igualdad.gob.es/)