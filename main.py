# Importa librerías necesarios
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Título de la aplicación
st.title('Análisis de estadísticas de jugadores de FIFA 23')

# Carga de datos desde el archivo CSV
df = pd.read_csv('FIFA23_official_data.csv')

# Muestra la tabla
st.write('Jugadores:')
st.write(df)

# Muestra la frecuencia de las nacionalidades
st.write('Frecuencia de Nacionalidades:')
st.write(df['Nationality'].value_counts())

# Muestra la relación entre Nacionalidad y Calificación General
st.write('Nacionalidad vs Calificación General:')
plt.figure(figsize=(10, 5))
df.groupby('Nationality')['Overall'].mean().plot(kind='bar')
plt.xlabel('Nacionalidad')
plt.ylabel('Calificación General Promedio')
plt.title('Calificación General Promedio por Nacionalidad')
st.pyplot(plt)

# Calcula la correlación entre 'Potential' y 'Overall'
correlation_matrix = df[['Potential', 'Overall']].corr()

# Muestra el mapa de calor usando Matplotlib
st.write('Mapa de Calor de Potential vs Calificación General:')
plt.figure(figsize=(10, 5))
heatmap = plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar(heatmap)
plt.xticks(ticks=[0, 1], labels=['Potential', 'Overall'])
plt.yticks(ticks=[0, 1], labels=['Potential', 'Overall'])
for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        plt.text(i, j, f"{correlation_matrix.iloc[i, j]:.2f}", ha='center', va='center', color='black', fontsize=12)
st.pyplot(plt)

# Muestra la distribución de jugadores por club
st.write('Distribución de Jugadores por Club:')
plt.figure(figsize=(10, 5))
df['Club'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribución de Jugadores por Club')
st.pyplot(plt)
