import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import plotly.express as px
import calendar
from datetime import datetime

st.set_page_config(page_title="Financial Analysis", layout="wide")

# -------------------- Funciones auxiliares --------------------
@st.cache_data
def load_data(file) -> pd.DataFrame:
    df = pd.read_excel(file, sheet_name="Sheet1")
    # Convertir 'Date' a datetime si no lo está
    if not pd.api.types.is_datetime64_any_dtype(df["Date"]):
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    # Extraer año y mes
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()
    return df

def plot_monthly_trend(df: pd.DataFrame, title="Monthly Total Amount", color_by=""):
    # Agrupar por mes
    monthly_data = df.groupby("Month")["Amount"].sum().reset_index().sort_values("Month")
    if color_by == "Year":
        # Agrupar por Año y Mes
        monthly_data_year = df.groupby([df["Date"].dt.year.rename("Year"), "Month"])["Amount"].sum().reset_index()
        fig = px.line(
            monthly_data_year,
            x="Month",
            y="Amount",
            color="Year",
            markers=True,
            title="Monthly Total Amount by Year"
        )
        fig.update_layout(
            yaxis_title="Amount",
            hovermode="x unified",
            legend_title_text="Year"
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
            xaxis_title="Month",
            yaxis_title="Amount",
            hovermode="x unified",
            showlegend=False
        )
    # Agregar una línea horizontal en y=0 para facilitar la interpretación.
    fig.add_hline(y=0, line_dash="dash", line_color="gray")
    return fig

def plot_histogram(df: pd.DataFrame, title: str):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["Amount"], kde=True, ax=ax)
    ax.set_title(title)
    ax.axvline(df["Amount"].mean(), color="r", linestyle="--", label="Mean")
    ax.legend(ncol=1, bbox_to_anchor=(1.02,1.02,0.25,0.25), loc='center', fontsize='x-small')
    st.pyplot(fig)

# -------------------- Sidebar Navigation --------------------
menu = st.sidebar.radio("🌍 Navigation", ["Home", "Descriptive Analysis", "Exploratory Analysis"])

# -------------------- HOME --------------------
if menu == "Home":
    st.title("📊 Financial Analysis 📊")
    archivo = st.file_uploader("📁 Upload your Excel file (.xlsx)", type=["xlsx"])
    
    if archivo is not None:
        myDf = load_data(archivo)

        # Guardar el DataFrame en session_state
        st.session_state["df"] = myDf

        msj = st.empty()
        msj.success("✅ File uploaded successfully! 🎉")
        time.sleep(2)
        msj.empty()

        st.subheader("📄 Data Overview")
        st.write("Here is a preview of your data:")
        st.dataframe(myDf.head(10))
    else:
        st.warning("Please upload a file to continue.")

# -------------------- DESCRIPTIVE ANALYSIS --------------------
elif menu == "Descriptive Analysis":
    st.title("📈 Descriptive Analysis")
    
    st.markdown("""
    ### 🧠 What is Descriptive Analysis?

    Descriptive analysis summarizes and organizes data in a meaningful way, allowing us to understand its key characteristics. 
    It includes measures such as **mean**, **median**, **standard deviation**, and **data distribution** to give insights into past behavior or performance.
    """)

    if "df" in st.session_state:
        df = st.session_state["df"]

        st.subheader("📊 Statistical Summary")
        st.write("This table shows a statistical summary of the numerical columns in your dataset:")
        st.dataframe(df.describe())
        
        st.subheader("📌 Additional Insights")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Mean (Amount)", round(df["Amount"].mean(), 2), border=True)
        with col2:
            st.metric("Median (Amount)", round(df["Amount"].median(), 2), border=True)
        with col3:
            st.metric("Standard Deviation (Amount)", round(df["Amount"].std(), 2), border=True)
        
        st.markdown("### Visual Exploration of Amounts")
        
        df_Incomes = df[df["Amount"] > 0].copy()
        df_Expenses = df[df["Amount"] < 0].copy()
        
        col4, col5 = st.columns(2)
        
        with col4:
            
            st.subheader("📈 Income Distribution")
            # Visualización adicional: Histograma
            plot_histogram(df=df_Incomes, title="Distribution of Amounts - Incomes")
            
        with col5:
            
            st.subheader("📉 Expense Distribution")
            # Visualización adicional: Histograma
            plot_histogram(df=df_Expenses, title="Distribution of Amounts - Expenses")
    
    else:
        st.warning("⚠️ Please upload a file first in the 'Home' section.")

# -------------------- EXPLORATORY ANALYSIS --------------------
elif menu == "Exploratory Analysis":
    st.title("🔍 Exploratory Analysis")
    
    st.markdown("""
    ### 🔬 What is Exploratory Analysis?

    Exploratory analysis is a process of analyzing data sets to summarize their main characteristics, often with visual methods. 
    It helps to discover patterns, spot anomalies, test hypotheses, and check assumptions with the help of summary statistics and graphical representations.
    """)

    if "df" in st.session_state:
        df = st.session_state["df"]
        
        # Filtros interactivos adicionales
        st.sidebar.markdown("## Filter Data")
        
        # Filtro por año (si hay datos)
        years = sorted(df["Year"].dropna().unique())
        selected_year = st.sidebar.selectbox("Select Year", options=["All"] + years, index=0)
        
        # Filtro por rango de fechas
        min_date = df["Date"].min()
        max_date = df["Date"].max()
        date_range = st.sidebar.date_input("Select Date Range", value=[min_date, max_date], min_value=min_date, max_value=max_date)
        
        # Aplicamos filtros
        filtered_df = df.copy()
        if selected_year != "All":
            filtered_df = filtered_df[filtered_df["Year"] == selected_year]
        if len(date_range) == 2:
            start_date, end_date = date_range
            filtered_df = filtered_df[(filtered_df["Date"] >= pd.to_datetime(start_date)) & (filtered_df["Date"] <= pd.to_datetime(end_date))]
        
        st.subheader("Filtered Data Overview")
        st.write(f"Displaying filtered data (Total rows: {filtered_df.shape[0]}):")
        st.dataframe(filtered_df.head(10))
        
        # KPIs financieros generales
        st.markdown("### 💰 Financial KPIs")
        col1, col2, col3 = st.columns(3)
        total_balance = filtered_df["Amount"].sum()
        total_income = filtered_df[filtered_df["Amount"] > 0]["Amount"].sum()
        total_expenses = filtered_df[filtered_df["Amount"] < 0]["Amount"].sum()

        with col1:
            st.metric("Total Balance", f"{round(total_balance, 2)} $", border=True)
        with col2:
            st.metric("Total Income", f"{round(total_income, 2)} $", border=True)
        with col3:
            st.metric("Total Expenses", f"{round(total_expenses, 2)} $", border=True)
        
        # Evolución del saldo acumulado
        st.subheader("📈 Cumulative Balance Over Time")
        cum_data = filtered_df.sort_values("Date").copy()
        cum_data["Cumulative Balance"] = cum_data["Amount"].cumsum()
        fig_cum = px.line(
            cum_data,
            x="Date",
            y="Cumulative Balance",
            title="Evolution of the Cumulative Balance",
            markers=True
        )
        fig_cum.update_layout(
            xaxis_title="Date",
            yaxis_title="Cumulative Balance",
            hovermode="x unified"
        )
        st.plotly_chart(fig_cum, use_container_width=True)
        
        # Gráfico interactivo de tendencia mensual
        st.subheader("📈 Monthly Trend")
        fig_monthly = plot_monthly_trend(filtered_df, title="Monthly Total Amount")
        st.plotly_chart(fig_monthly, use_container_width=True)
        
        # Gráfico de tendencias desglosadas por año (si hay más de un año)
        if len(filtered_df["Year"].unique()) > 1:
            st.subheader("📈 Monthly Trend by Year")
            fig_monthly_year = plot_monthly_trend(filtered_df, title="Monthly Total Amount by Year", color_by="Year")
            st.plotly_chart(fig_monthly_year, use_container_width=True)
        
        # Análisis: Mes con mayor monto por año
        st.subheader("🏆 Month with Highest Sales per Year")
        monthly_sum = df.groupby([df["Date"].dt.year.rename("Year"), df["Date"].dt.month.rename("Month")])["Amount"].sum().reset_index()
        idx_max_month = monthly_sum.groupby("Year")["Amount"].idxmax()
        max_month_per_year = monthly_sum.loc[idx_max_month]
        max_month_per_year["Month Name"] = max_month_per_year["Month"].apply(lambda x: calendar.month_name[x])
        
        fig_bar = px.bar(
            max_month_per_year,
            x="Year",
            y="Amount",
            color="Month Name",
            text="Month Name",
            title="Month with Highest Sales per Year",
            labels={"Amount": "Total Sales Amount", "Year": "Year"}
        )
        fig_bar.update_traces(textposition="outside")
        fig_bar.update_layout(yaxis=dict(title="Amount"), xaxis=dict(title="Year"), uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Extras: Comparación de dos periodos (si los datos lo permiten)
        st.subheader("📊 Period Comparison")
        period1 = st.sidebar.date_input("Select Period 1", value=[min_date, min_date + pd.DateOffset(months=3)], key="p1")
        period2 = st.sidebar.date_input("Select Period 2", value=[min_date + pd.DateOffset(months=3), min_date + pd.DateOffset(months=6)], key="p2")
        
        if len(period1) == 2 and len(period2) == 2:
            period1_data = filtered_df[(filtered_df["Date"] >= pd.to_datetime(period1[0])) & (filtered_df["Date"] <= pd.to_datetime(period1[1]))]
            period2_data = filtered_df[(filtered_df["Date"] >= pd.to_datetime(period2[0])) & (filtered_df["Date"] <= pd.to_datetime(period2[1]))]
            
            comp_df = pd.DataFrame({
                "Period": ["Period 1", "Period 2"],
                "Total Amount": [period1_data["Amount"].sum(), period2_data["Amount"].sum()],
                "Transactions": [period1_data.shape[0], period2_data.shape[0]]
            })
            st.dataframe(comp_df)
            fig_comp = px.bar(comp_df, x="Period", y="Total Amount", color="Period", text="Total Amount", title="Total Amount Comparison Between Periods")
            st.plotly_chart(fig_comp, use_container_width=True)
        
    else:
        st.warning("⚠️ Please upload a file first in the 'Home' section.")
