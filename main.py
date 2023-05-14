import streamlit as st
import KPI_1
import KPI_2
import KPI_3
import KPI_4
import KPI_5

# Configurar la página
st.set_page_config(
    page_title="Alerta sísmica Chile",
    page_icon="🌎",
    layout="wide"    
)

# Mostrar la imagen en el encabezado
st.markdown(
    """
    <div>
        <img src="https://github.com/Mezgo/Quake-Alert/blob/Dibujos/imagenes/logo_slogan.PNG" style="width: 200px; margin-bottom: 20px;">
    </div>
    """,
    unsafe_allow_html=True
)


# Opciones del menú de navegación
menu = ["Inicio", "KPI 1", "KPI 2", "KPI 3", "KPI 4", "KPI 5"]
choice = st.sidebar.selectbox("Menú de navegación", menu)

# Mostrar contenido según la opción seleccionada
if choice == "Inicio":
    st.title("PROYECTO ANALISIS SISMOS")
    # Mostrar contenido de la página de inicio
    import matplotlib.pyplot as plt

    # Crear dos columnas con proporciones 60% y 40%
    col1, col2 = st.columns([0.5, 0.5])

    # Texto en la columna izquierda
    with col1:        
        st.write("Quienes somos:")
        st.write("Somos parte del equipo de Prevención de eventos sísmicos de la ONG 'Quake Alert' de Chile e integramos el departamento de ciencia de datos y machine learning de la misma.")
        st.write("Somos un grupo de profesionales altamente capacitados, utilizamos herramientas tecnológicas para poder brindar soluciones innovadoras en la prevención de desastres de eventos sísmicos. Los datos aportan mucha información, es por eso que nos esforzamos por interpretar qué es lo que la ONG realmente necesita y proporcionar soluciones innovadoras y personalizadas.")

    # Gráfico en la columna derecha
    with col2:
        # Aquí va el código para generar el gráfico de Matplotlib
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
        st.pyplot(fig)
        
elif choice == "KPI 1":
    KPI_1.show_kpi_1()

elif choice == "KPI 2":
    KPI_2.show_kpi_2()

elif choice == "KPI 3":
    KPI_3.show_kpi_3()

elif choice == "KPI 4":
    KPI_4.show_kpi_4()
    
elif choice == "KPI 5":
    KPI_5.show_kpi_5()