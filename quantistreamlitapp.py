import pandas as pd
import streamlit as st
import plotly.express as px

# Daten einfügen
data = {
    'Kategorie': [
        'Prumer', 'First Call', 'Second Call', 'Zuvor teilgenommen', 'Zuvor nicht teilgenommen',
        'Privat', 'Öffentlich', 'Öffentlich Wissenschaft', 'Öffentlich Bund',
        'Öffentlich Land', 'Öffentlich Region', 'Öffentlich Kommune'
    ],
    'Anzahl der Personen pro Projektpartner (Anzahl)': [2.3902, 2.5769, 2.5238, 2.3429, 3, 2.5833, 2.3103, 2.4615, 3, 1.5, 2.5, 2.4],
    'Anteil der Arbeitszeit dieser Personen am Projekt (%)': [46.439, 54.667, 43.714, 48.242, 45.273, 40.8333, 42.8462, 58.4615, 40, 22.75, 51.6667, 42.3],
    'Anteil an projektadministrativen Aufgaben (%)': [31.1795, 37, 12.188, 31.25, 10.125, 26.9091, 36.2069, 37.3077, 20, 41, 21.25, 10],
    'Einstellung neuer Mitarbeiter (%)': [61.22, 66.67, 54.55, 59.46, 66.67, 53.33, 64.71, 60, 100, 50, 50, 75],
    'Anteil neu eingestellter Mitarbeiter (%)': [55.2308, 52.5, 66.222, 53.5, 59.571, 48.8571, 57.5789, 59.5714, 33, 34, 100, 67.75],
    'Externe Aufgabenvergabe (%)': [40.82, 48.15, 31.82, 37.84, 50, 26.67, 47.06, 26.67, 100, 50, 75, 66.67],
    'Anteil externer Aufgabenvergabe (%)': [31.2778, 21.667, 49, 36.538, 32, 7.6667, 35, 10, 20, 65, 33.33, 37.1429],
    '(Gesamt)Anteil an Aufgaben des Projektpartners im Projekt (%)': [18.0698, 17.818, 13.125, 12.8, 37.273, 16.3846, 18.8, 14.3846, 15, 22, 34.25, 23.6364],
    'Zeitplan eingehalten (%)': [86, 82.14, 90.91, 84.21, 91.67, 86.67, 85.71, 81.25, 100, 100, 100, 83.33],
    'Zeitplan nicht eingehalten (%)': [14, 17.86, 9.09, 15.79, 8.33, 13.33, 14.29, 18.75, 0, 0, 0, 16.67],
    'Herausforderungen vorhanden (%)': [28, 39.29, 13.64, 31.58, 16.67, 13.33, 34.29, 31.25, 100, 33.33, 50, 41.67],
    'Keine Herausforderungen (%)': [72, 60.71, 86.36, 68.42, 83.33, 86.67, 65.71, 68.75, 0, 66.67, 50, 58.33]
}

# In ein DataFrame konvertieren
df = pd.DataFrame(data)

# Streamlit App
st.title("Projektanalyse - Interaktive Darstellung")

# Dropdown für Kategorieauswahl
selected_categories = st.multiselect(
    "Kategorie auswählen:",
    options=['Alle'] + df['Kategorie'].tolist(),
    default=['Alle']
)

# Checkliste für absolute und prozentuale Merkmale
st.sidebar.header("Merkmale auswählen")
selected_absolute_metrics = st.sidebar.multiselect(
    "Absolute Merkmale auswählen:",
    options=['Anzahl der Personen pro Projektpartner (Anzahl)'],
    default=['Anzahl der Personen pro Projektpartner (Anzahl)']
)

selected_percentage_metrics = st.sidebar.multiselect(
    "Prozentuale Merkmale auswählen:",
    options=[
        'Anteil der Arbeitszeit dieser Personen am Projekt (%)',
        'Anteil an projektadministrativen Aufgaben (%)',
        'Einstellung neuer Mitarbeiter (%)',
        'Anteil neu eingestellter Mitarbeiter (%)',
        'Externe Aufgabenvergabe (%)',
        'Anteil externer Aufgabenvergabe (%)',
        '(Gesamt)Anteil an Aufgaben des Projektpartners im Projekt (%)',
        'Zeitplan eingehalten (%)',
        'Zeitplan nicht eingehalten (%)',
        'Herausforderungen vorhanden (%)',
        'Keine Herausforderungen (%)'
    ],
    default=['Anteil der Arbeitszeit dieser Personen am Projekt (%)']
)

# Daten filtern
if 'Alle' in selected_categories:
    filtered_df = df  # Alle Kategorien anzeigen
else:
    filtered_df = df[df['Kategorie'].isin(selected_categories)]

# Absolutwerte-Diagramm
st.subheader("Absolutwerte")
if selected_absolute_metrics:
    fig_absolute = px.bar(
        filtered_df,
        x='Kategorie',
        y=selected_absolute_metrics,
        barmode='group',
        title="Absolute Werte (Anzahl)"
    )
    st.plotly_chart(fig_absolute)

# Prozentwerte-Diagramm
st.subheader("Prozentwerte")
if selected_percentage_metrics:
    fig_percentage = px.bar(
        filtered_df,
        x='Kategorie',
        y=selected_percentage_metrics,
        barmode='group',
        title="Prozentuale Werte"
    )
    st.plotly_chart(fig_percentage)