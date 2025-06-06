# Aplicación de Análisis Financiero con Streamlit

Una aplicación de Streamlit para realizar análisis descriptivo y exploratorio de datos financieros. Los usuarios pueden subir un archivo Excel que contenga transacciones financieras para visualizar y obtener información sobre ingresos, gastos y tendencias de saldo a lo largo del tiempo.

---

## Tabla de Contenidos

* [Características](#características)
* [Demostración](#demostración)
* [Instalación](#instalación)
* [Uso](#uso)
* [Estructura de Archivos](#estructura-de-archivos)
* [Configuración](#configuración)
* [Dependencias](#dependencias)
* [Estructura de la Aplicación](#estructura-de-la-aplicación)

  * [Home](#home)
  * [Análisis Descriptivo](#análisis-descriptivo)
  * [Análisis Exploratorio](#análisis-exploratorio)
* [Funciones y Componentes](#funciones-y-componentes)
* [Cómo Contribuir](#cómo-contribuir)
* [Licencia](#licencia)

---

## Características

* **Carga de Archivos**
  Permite subir un archivo `.xlsx` con una hoja llamada `Sheet1` que contenga al menos las columnas `Date` (fecha) y `Amount` (monto).

* **Carga de Datos con Caché**
  La función `load_data` utiliza el sistema de caché de Streamlit para acelerar cargas posteriores del mismo archivo.

* **Análisis Descriptivo**

  * Resumen estadístico (conteo, media, desviación estándar, mínimo, percentiles 25%, 50%, 75%, y máximo) de todas las columnas numéricas.
  * Métricas destacadas: media, mediana y desviación estándar de la columna `Amount`.
  * Histogramas (con estimación de densidad de núcleo) para las distribuciones de ingresos y gastos; con una línea que indica el valor medio.

* **Análisis Exploratorio**

  * Filtros interactivos por año y rango de fechas.
  * Indicadores clave (KPIs) financieros:

    * Saldo Total
    * Ingresos Totales
    * Gastos Totales
  * Gráfica de saldo acumulado en el tiempo.
  * Tendencia mensual (monto total por mes) y opción para colorear por año.
  * Gráfica de barras que muestra el mes con mayores ventas (monto) por año.
  * Comparación entre dos periodos personalizados (monto total y número de transacciones).

* **Diseño Responsivo**
  Utiliza las columnas de Streamlit y Plotly para gráficos interactivos y adaptables.

---

## Demostración

1. Ejecuta la aplicación localmente.
2. Sube un archivo financiero en formato Excel (.xlsx).
   El archivo debe tener al menos la siguiente estructura mínima:

   ```text
   ┌────────────┬────────┐
   │    Date    │ Amount │
   ├────────────┼────────┤
   │ 2024-01-15 │  500.0 │
   │ 2024-01-20 │ -200.0 │
   │ 2024-02-03 │  750.0 │
   │    …       │   …    │
   └────────────┴────────┘
   ```
3. Explora las secciones **Análisis Descriptivo** y **Análisis Exploratorio** desde la barra lateral.

Capturas de pantalla sugeridas (opcional):

* **Home** (subida y vista previa de datos)
* **Análisis Descriptivo** (resumen estadístico e histogramas)
* **Análisis Exploratorio** (KPIs y gráficos interactivos)

---

## Instalación

1. **Clonar el repositorio** (o copiar el código de la aplicación en una carpeta local, por ejemplo, `app_analisis_financiero/`).

   ```bash
   git clone https://github.com/tuusuario/analisis-financiero-streamlit.git
   cd analisis-financiero-streamlit
   ```

2. **Crear un entorno virtual** (recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate       # Linux / macOS
   venv\Scripts\activate.bat      # Windows
   ```

3. **Instalar dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

   Si no tienes un archivo `requirements.txt`, instala manualmente:

   ```bash
   pip install streamlit pandas matplotlib seaborn plotly openpyxl
   ```

4. **Ejecutar la aplicación de Streamlit**:

   ```bash
   streamlit run app.py
   ```

   *(Reemplaza `app.py` por el nombre del archivo que contiene el código de la aplicación.)*

---

## Uso

1. **Página de Inicio (Home)**

   * Haz clic en “Upload your Excel file (.xlsx)” y selecciona tu archivo de datos financieros.
   * Una vez cargado correctamente, verás una vista previa de las primeras 10 filas.

2. **Análisis Descriptivo**

   * Accede desde la barra lateral (“Descriptive Analysis”).
   * Observa el resumen estadístico de las columnas numéricas.
   * Visualiza las métricas (media, mediana, desviación estándar) para la columna `Amount`.
   * Inspecciona las distribuciones de ingresos y gastos mediante histogramas anotados con la línea de la media.

3. **Análisis Exploratorio**

   * Accede desde la barra lateral (“Exploratory Analysis”).
   * Usa los controles del panel lateral **Filter Data** para:

     * Seleccionar un año específico (por defecto “All”).
     * Seleccionar un rango de fechas (por defecto abarca desde la fecha mínima hasta la máxima del conjunto de datos).
   * Observa la vista previa de los datos filtrados (primeras 10 filas).
   * Revisa los KPIs financieros:

     * Saldo Total
     * Ingresos Totales (suma de montos positivos)
     * Gastos Totales (suma de montos negativos)
   * Grafica:

     * Saldo acumulado en el tiempo (gráfica de líneas).
     * Tendencia mensual de montos (gráfica de líneas, con opción de colorear por año).
     * Mes con mayores ventas por año (gráfica de barras).
     * Comparación entre dos periodos definidos por el usuario (gráfica de barras mostrando monto total; una tabla con totales y conteo de transacciones).

---

## Estructura de Archivos

```text
analisis-financiero-streamlit/
├── app.py
├── requirements.txt
├── README.md
└── ejemplos/
    └── sample_data.xlsx
```

* **app.py**
  Contiene el código completo de la aplicación Streamlit (el fragmento proporcionado).
* **requirements.txt**
  Bloquea las versiones de las dependencias. Ejemplo:

  ```
  streamlit>=1.25.0
  pandas>=1.5.0
  matplotlib>=3.7.0
  seaborn>=0.12.0
  plotly>=5.14.0
  openpyxl>=3.1.0
  ```
* **ejemplos/sample\_data.xlsx**
  *(Opcional)* Un archivo Excel de ejemplo con columnas `Date` y `Amount` para pruebas.

---

## Configuración

* **Page Config**

  ```python
  st.set_page_config(page_title="Financial Analysis", layout="wide")
  ```

  Configura el título de la pestaña del navegador y utiliza un diseño ancho para mejor visualización.

* **Caché**
  La función auxiliar `load_data` está decorada con `@st.cache_data` para acelerar la recarga de datos cuando se sube el mismo archivo.

---

## Dependencias

* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Plotly Express](https://plotly.com/python/plotly-express/)
* [OpenPyXL](https://openpyxl.readthedocs.io/) (para leer archivos Excel)

Ejemplo de comando `pip install`:

```bash
pip install streamlit pandas matplotlib seaborn plotly openpyxl
```

---

## Estructura de la Aplicación

A continuación se describe cada sección principal de la aplicación de Streamlit y su funcionalidad.

### Home

* **Título y Selector de Archivo**

  ```python
  st.title("📊 Financial Analysis 📊")
  archivo = st.file_uploader("📁 Upload your Excel file (.xlsx)", type=["xlsx"])
  ```
* **Carga de Datos y Caché**

  ```python
  @st.cache_data
  def load_data(file) -> pd.DataFrame:
      df = pd.read_excel(file, sheet_name="Sheet1")
      # Convertir 'Date' a tipo datetime si no lo está
      if not pd.api.types.is_datetime64_any_dtype(df["Date"]):
          df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
      # Extraer año y mes
      df["Year"] = df["Date"].dt.year
      df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()
      return df
  ```
* **Vista previa y Almacenamiento en sesión**

  * El DataFrame cargado se almacena en `st.session_state["df"]` para usarlo en las demás páginas.
  * Se muestra una vista previa de las primeras 10 filas con `st.dataframe(myDf.head(10))`.

---

### Análisis Descriptivo

1. **Título y Descripción**

   ```python
   st.title("📈 Descriptive Analysis")
   st.markdown("""
   ### 🧠 ¿Qué es el Análisis Descriptivo?

   El análisis descriptivo resume y organiza los datos de manera significativa, permitiendo entender sus características clave. 
   Incluye métricas como **media**, **mediana**, **desviación estándar** y **distribución de datos** para ofrecer información sobre el comportamiento o rendimiento pasado.
   """)
   ```
2. **Verificar si hay datos cargados**

   ```python
   if "df" in st.session_state:
       df = st.session_state["df"]
       ...
   else:
       st.warning("⚠️ Por favor, sube un archivo primero en la sección 'Home'.")
   ```
3. **Resumen Estadístico**

   ```python
   st.subheader("📊 Resumen Estadístico")
   st.write("Esta tabla muestra un resumen estadístico de las columnas numéricas de tu conjunto de datos:")
   st.dataframe(df.describe())
   ```
4. **Métricas Clave**

   ```python
   col1, col2, col3 = st.columns(3)
   with col1:
       st.metric("Media (Amount)", round(df["Amount"].mean(), 2), border=True)
   with col2:
       st.metric("Mediana (Amount)", round(df["Amount"].median(), 2), border=True)
   with col3:
       st.metric("Desviación Estándar (Amount)", round(df["Amount"].std(), 2), border=True)
   ```
5. **Histogramas**

   * **Función Auxiliar**

     ```python
     def plot_histogram(df: pd.DataFrame, title: str):
         fig, ax = plt.subplots(figsize=(8, 5))
         sns.histplot(df["Amount"], kde=True, ax=ax)
         ax.set_title(title)
         ax.axvline(df["Amount"].mean(), color="r", linestyle="--", label="Mean")
         ax.legend(ncol=1, bbox_to_anchor=(1.02,1.02), loc='center', fontsize='x-small')
         st.pyplot(fig)
     ```
   * **Distribución de Ingresos y Gastos**

     ```python
     df_Incomes = df[df["Amount"] > 0].copy()
     df_Expenses = df[df["Amount"] < 0].copy()

     col4, col5 = st.columns(2)
     with col4:
         st.subheader("📈 Distribución de Ingresos")
         plot_histogram(df=df_Incomes, title="Distribución de Montos - Ingresos")
     with col5:
         st.subheader("📉 Distribución de Gastos")
         plot_histogram(df=df_Expenses, title="Distribución de Montos - Gastos")
     ```

---

### Análisis Exploratorio

1. **Título y Descripción**

   ```python
   st.title("🔍 Exploratory Analysis")
   st.markdown("""
   ### 🔬 ¿Qué es el Análisis Exploratorio?

   El análisis exploratorio es un proceso de examinar conjuntos de datos para resumir sus características principales, frecuentemente mediante métodos visuales. 
   Ayuda a descubrir patrones, detectar anomalías, probar hipótesis y validar supuestos con estadísticas sumarias y representaciones gráficas.
   """)
   ```
2. **Verificar si hay datos cargados** (mismo patrón que en Análisis Descriptivo)
3. **Filtros en la Barra Lateral**

   ```python
   st.sidebar.markdown("## Filtrar Datos")
   years = sorted(df["Year"].dropna().unique())
   selected_year = st.sidebar.selectbox("Seleccionar Año", options=["All"] + years, index=0)
   min_date = df["Date"].min()
   max_date = df["Date"].max()
   date_range = st.sidebar.date_input(
       "Seleccionar Rango de Fechas",
       value=[min_date, max_date],
       min_value=min_date,
       max_value=max_date
   )
   ```

   * Filtrar por año y por un rango de fechas definido.
4. **Vista Preliminar de Datos Filtrados**

   ```python
   filtered_df = df.copy()
   if selected_year != "All":
       filtered_df = filtered_df[filtered_df["Year"] == selected_year]
   if len(date_range) == 2:
       start_date, end_date = date_range
       filtered_df = filtered_df[
           (filtered_df["Date"] >= pd.to_datetime(start_date)) &
           (filtered_df["Date"] <= pd.to_datetime(end_date))
       ]
   st.subheader("Vista Previa de Datos Filtrados")
   st.write(f"Mostrando datos filtrados (Total filas: {filtered_df.shape[0]}):")
   st.dataframe(filtered_df.head(10))
   ```
5. **KPIs Financieros**

   ```python
   total_balance = filtered_df["Amount"].sum()
   total_income = filtered_df[filtered_df["Amount"] > 0]["Amount"].sum()
   total_expenses = filtered_df[filtered_df["Amount"] < 0]["Amount"].sum()

   col1, col2, col3 = st.columns(3)
   with col1:
       st.metric("Saldo Total", f"{round(total_balance, 2)} $", border=True)
   with col2:
       st.metric("Ingresos Totales", f"{round(total_income, 2)} $", border=True)
   with col3:
       st.metric("Gastos Totales", f"{round(total_expenses, 2)} $", border=True)
   ```
6. **Saldo Acumulado a lo Largo del Tiempo**

   ```python
   cum_data = filtered_df.sort_values("Date").copy()
   cum_data["Cumulative Balance"] = cum_data["Amount"].cumsum()
   fig_cum = px.line(
       cum_data,
       x="Date",
       y="Cumulative Balance",
       title="Evolución del Saldo Acumulado",
       markers=True
   )
   fig_cum.update_layout(
       xaxis_title="Fecha",
       yaxis_title="Saldo Acumulado",
       hovermode="x unified"
   )
   st.plotly_chart(fig_cum, use_container_width=True)
   ```
7. **Tendencia Mensual**

   * **Función Auxiliar**

     ```python
     def plot_monthly_trend(df: pd.DataFrame, title="Monthly Total Amount", color_by=""):
         # Agrupar por mes
         monthly_data = df.groupby("Month")["Amount"].sum().reset_index().sort_values("Month")
         if color_by == "Year":
             # Agrupar por Año y Mes
             monthly_data_year = (
                 df.groupby([df["Date"].dt.year.rename("Year"), "Month"])["Amount"]
                 .sum()
                 .reset_index()
             )
             fig = px.line(
                 monthly_data_year,
                 x="Month",
                 y="Amount",
                 color="Year",
                 markers=True,
                 title="Monto Total Mensual por Año"
             )
             fig.update_layout(
                 yaxis_title="Monto",
                 hovermode="x unified",
                 legend_title_text="Año"
             )
         else:
             fig = px.line(
                 monthly_data,
                 x="Month",
                 y="Amount",
                 markers=True,
                 title=title
             )
             fig.update_layout(
                 xaxis_title="Mes",
                 yaxis_title="Monto",
                 hovermode="x unified",
                 showlegend=False
             )
         # Agregar línea horizontal en y=0
         fig.add_hline(y=0, line_dash="dash", line_color="gray")
         return fig
     ```
   * **Visualización sin y con desglose por año**

     ```python
     st.subheader("📈 Tendencia Mensual")
     fig_monthly = plot_monthly_trend(filtered_df, title="Monto Total Mensual")
     st.plotly_chart(fig_monthly, use_container_width=True)

     if len(filtered_df["Year"].unique()) > 1:
         st.subheader("📈 Tendencia Mensual por Año")
         fig_monthly_year = plot_monthly_trend(
             filtered_df,
             title="Monto Total Mensual por Año",
             color_by="Year"
         )
         st.plotly_chart(fig_monthly_year, use_container_width=True)
     ```
8. **Mes con Mayor Ventas por Año**

   ```python
   import calendar
   monthly_sum = (
       df.groupby([
           df["Date"].dt.year.rename("Year"),
           df["Date"].dt.month.rename("Month")
       ])["Amount"]
       .sum()
       .reset_index()
   )
   idx_max_month = monthly_sum.groupby("Year")["Amount"].idxmax()
   max_month_per_year = monthly_sum.loc[idx_max_month]
   max_month_per_year["Month Name"] = max_month_per_year["Month"].apply(
       lambda x: calendar.month_name[x]
   )

   fig_bar = px.bar(
       max_month_per_year,
       x="Year",
       y="Amount",
       color="Month Name",
       text="Month Name",
       title="Mes con Mayor Ventas por Año",
       labels={"Amount": "Monto Total de Ventas", "Year": "Año"}
   )
   fig_bar.update_traces(textposition="outside")
   fig_bar.update_layout(
       yaxis=dict(title="Monto"),
       xaxis=dict(title="Año"),
       uniformtext_minsize=8,
       uniformtext_mode='hide'
   )
   st.plotly_chart(fig_bar, use_container_width=True)
   ```
9. **Comparación de Periodos (Extras)**

   ```python
   st.subheader("📊 Comparación de Periodos")
   period1 = st.sidebar.date_input(
       "Seleccionar Periodo 1",
       value=[min_date, min_date + pd.DateOffset(months=3)],
       key="p1"
   )
   period2 = st.sidebar.date_input(
       "Seleccionar Periodo 2",
       value=[min_date + pd.DateOffset(months=3), min_date + pd.DateOffset(months=6)],
       key="p2"
   )

   if len(period1) == 2 and len(period2) == 2:
       period1_data = filtered_df[
           (filtered_df["Date"] >= pd.to_datetime(period1[0])) &
           (filtered_df["Date"] <= pd.to_datetime(period1[1]))
       ]
       period2_data = filtered_df[
           (filtered_df["Date"] >= pd.to_datetime(period2[0])) &
           (filtered_df["Date"] <= pd.to_datetime(period2[1]))
       ]
       comp_df = pd.DataFrame({
           "Periodo": ["Periodo 1", "Periodo 2"],
           "Monto Total": [period1_data["Amount"].sum(), period2_data["Amount"].sum()],
           "Transacciones": [period1_data.shape[0], period2_data.shape[0]]
       })
       st.dataframe(comp_df)
       fig_comp = px.bar(
           comp_df,
           x="Periodo",
           y="Monto Total",
           color="Periodo",
           text="Monto Total",
           title="Comparación de Monto Total Entre Periodos"
       )
       st.plotly_chart(fig_comp, use_container_width=True)
   ```

---

## Funciones y Componentes

1. **`load_data(file) -> pd.DataFrame`**

   * Lee la hoja “Sheet1” del archivo Excel subido.
   * Convierte la columna `Date` a tipo `datetime` si no lo estaba.
   * Agrega columnas `Year` y `Month`.
   * Está decorada con `@st.cache_data` para cachear resultados y no leer repetidamente el mismo archivo.

2. **`plot_monthly_trend(df, title, color_by)`**

   * Dibuja una gráfica de línea del monto total mensual.
   * Si `color_by="Year"`, agrupa los datos por año y mes y colorea por año.

3. **`plot_histogram(df, title)`**

   * Genera un histograma (con Seaborn) de la columna `Amount`.
   * Superpone una línea vertical en el valor medio de `Amount`.

---

## Cómo Contribuir

¡Las contribuciones, reportes de errores y solicitudes de nuevas funcionalidades son bienvenidos!

<a href="https://www.linkedin.com/in/andres-felipe-lemus-v-7943882a9/" target="_blank" rel="noopener noreferrer">
  <img src="https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/linkedin.svg" alt="LinkedIn Logo" width="30" style="vertical-align:middle;" />
  <span style="font-size: 1.2em; margin-left: 8px;">Andrés Felipe Lemus Victoria</span>
</a>
