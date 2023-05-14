import streamlit as st
import matplotlib.pyplot as plt
import pydeck as pdk
import pandas as pd

@st.cache_data
def show_kpi_1():
    st.title("KPI 1")
    
    # Crear un DataFrame de ejemplo
    data = pd.read_csv('chile.csv')
    df = pd.DataFrame(data)

    # Ejemplo de Markdown básico
    st.markdown("# Título 1")
    st.markdown("Este es un texto en **negrita** y *cursiva*.")


    import geopandas as gpd
    from shapely.geometry import Point

    # Obtener los datos de latitud, longitud y magnitud del DataFrame
    data = df[['latitud', 'longitud', 'magnitud']].values.tolist()

    # Crear el mapa de calor con Pydeck
    layer = pdk.Layer(
        "HeatmapLayer",
        data=data,
        get_position="[1, 0]",
        get_weight="2",
        opacity=0.8,
        intensity=1,
        radius_pixels=30
    )
    view_state = pdk.ViewState(latitude=-33.4489, longitude=-70.6693, zoom=10)  # Ubicación de Chile
    deck = pdk.Deck(layers=[layer], initial_view_state=view_state)

    # Cargar el mapa mundial de Geopandas
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Crear el GeoDataFrame con los datos de latitud, longitud y magnitud
    crs = 'EPSG:4326'
    geometry = [Point(xy) for xy in zip(df['longitud'], df['latitud'])]
    geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(12, 10))

    # Graficar el mapa mundial en los ejes
    world.to_crs(epsg=4326).plot(ax=ax, color='lightgrey')

    # Graficar el GeoDataFrame en los ejes con colores por magnitud
    geo_df.plot(column='magnitud', ax=ax, cmap='rainbow', legend=True, legend_kwds={'shrink': 0.3}, markersize=5, alpha=0.5)

    # Establecer el título del gráfico
    ax.set_title('Sismos por magnitud Chile')



    # Crear dos columnas con proporciones 60% y 40%
    col1, col2 = st.columns([0.6, 0.4])

    # Mostrar el gráfico 3D en la columna izquierda
    with col1:
        # Mostrar el gráfico 3D en la columna izquierda
        # Mostrar el mapa mundial y el gráfico de GeoDataFrame en Streamlit
        st.pyplot(fig)
        #st.pydeck_chart(deck)


    # Definir los valores de ejemplo para el gráfico circular
    umbral = 7.0
    num_sismos_intensos = 10
    num_sismos_total = 100
    kpi = num_sismos_intensos / num_sismos_total
    porcentaje = kpi * 100
    etiquetas = ['Sismos con Intensidad > 7.0', 'Otros Sismos']
    valores = [porcentaje, 100 - porcentaje]
    colores = ['lightblue', 'lightgray']

    # Crear el gráfico circular en la columna derecha
    with col2:
        fig, ax = plt.subplots()
        ax.pie(valores, labels=etiquetas, colors=colores, autopct='%1.1f%%')
        ax.set_title('Identificación de Epicentros de Sismos más Intensos')
        st.pyplot(fig)


    # Crear un bloque vacío
    empty_block = st.empty()
    # Utilizar el bloque vacío para generar un espacio en blanco
    empty_block.text("")


    # Mostrar la tabla en Streamlit
    st.dataframe(df)



    # Estilo CSS para el footer
    footer_style = """
        text-align: center;
        background-color: #f5f5f5;
        margin:30px;
        padding: 50px;
        color: #777777;
    """

    # Contenido del footer
    footer_text = "Quake Alert ONG Prevención eventos sísmicos"

    # Agregar el footer a tu aplicación
    st.markdown(f'<p style="{footer_style}">{footer_text}</p>', unsafe_allow_html=True)
