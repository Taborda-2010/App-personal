import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import networkx as nx



st.title('Analisis de estadisticas de jugadores de FIFA 23')

# Read CSV file
#csv_file = st.file_uploader('Upload a CSV file', type='csv')

df = pd.read_csv('FIFA23_official_data.csv')

# Show table
st.write('Table:')
st.write(df)

# Display Nationality Frequency
st.write('Frequency of Nationalities:')
st.write(df['Nationality'].value_counts())

# Display Nationality vs Overall Rating
st.write('Nationality vs Overall Rating:')
plt.figure(figsize=(10, 5))
df.groupby('Nationality')['Overall'].mean().plot(kind='bar')
plt.xlabel('Nationality')
plt.ylabel('Average Overall Rating')
plt.title('Average Overall Rating by Nationality')
st.pyplot(plt)

# Display Heatmap of Potential vs Overall Rating
#st.write('Heatmap of Potential vs Overall Rating:')
#plt.figure(figsize=(10, 5))
#sns.heatmap(df[['Potential', 'Overall']].corr(), annot=True, cmap='coolwarm')
#st.pyplot(plt)

# Display Player Distribution by Club
st.write('Player Distribution by Club:')
plt.figure(figsize=(10, 5))
df['Club'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Player Distribution by Club')
st.pyplot(plt)

# Display Graph of Connections between Players based on Similarity in Overall Rating
#st.write('Graph of Connections between Players based on Similarity in Overall Rating:')
#G = nx.Graph()
#edges = df[['Name', 'Overall']].values.tolist()
#for edge in edges:
#    if edge[0] != edge[1]:
#        G.add_edge(edge[0], edge[1], weight=abs(edge[2] - edge[3]))

pos = graphviz_layout(G, prog='neato')
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10)
st.pyplot(plt)