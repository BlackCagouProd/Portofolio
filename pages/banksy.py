import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from config import COLORS

def banksy_show():
    """Affiche la page Banksy avec carte interactive"""
    
    st.markdown(f"""
        <h1 style='text-align: center; margin-bottom: 0.5em;'>
            Banksy Investigation Hub
        </h1>
        <p style='text-align: center; font-size: 1.1em; font-style: italic; color: {COLORS["primary"]};'>
            Le sens guide la technique
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charger les données
    df_oeuvres = load_data()
    
    # Sidebar - Filtres
    st.sidebar.markdown(f"<h2 style='border-left: 3px solid {COLORS['primary']}; padding-left: 15px;'>Filtres</h2>", unsafe_allow_html=True)
    
    # Filtre par année
    annee_min, annee_max = st.sidebar.slider(
        "Période d'analyse",
        min_value=int(df_oeuvres['annee'].min()),
        max_value=int(df_oeuvres['annee'].max()),
        value=(int(df_oeuvres['annee'].min()), int(df_oeuvres['annee'].max()))
    )
    
    # Filtre par type
    types_selectionnes = st.sidebar.multiselect(
        "Type d'œuvres",
        options=df_oeuvres['type'].unique(),
        default=df_oeuvres['type'].unique()
    )
    
    # Filtrage
    df_filtre = df_oeuvres[
        (df_oeuvres['annee'] >= annee_min) &
        (df_oeuvres['annee'] <= annee_max) &
        (df_oeuvres['type'].isin(types_selectionnes))
    ]
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total œuvres", len(df_filtre))
    with col2:
        st.metric("Pays couverts", len(df_filtre['lieu'].str.split(', ').str[-1].unique()))
    with col3:
        st.metric("Collaborations", len(df_filtre[df_filtre['artistes_lies'] != '']))
    with col4:
        st.metric("Période active", f"{df_filtre['annee'].max() - df_filtre['annee'].min()} ans")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tabs principales
    tab1, tab2, tab3 = st.tabs(["Carte Interactive", "Timeline", "Statistiques"])
    
    with tab1:
        render_folium_map(df_filtre)
    
    with tab2:
        render_timeline(df_filtre)
    
    with tab3:
        render_analytics(df_filtre)

@st.cache_data
def load_data():
    """Charge les données des œuvres"""
    df = pd.read_csv("assets/data/banksy_oeuvres.csv")
    df['date'] = pd.to_datetime(df['date'])
    df['annee'] = df['date'].dt.year
    # Gérer les valeurs manquantes
    df['artistes_lies'] = df['artistes_lies'].fillna('')
    df['description'] = df['description'].fillna('Description non disponible')
    return df

def get_marker_color(type_oeuvre):
    """Retourne une couleur pour chaque type d'œuvre"""
    colors_map = {
        'Street Art': 'blue',
        'Mural': 'green',
        'Exposition': 'red',
        'Installation': 'orange',
        'Intervention': 'purple',
        'Série': 'cadetblue'
    }
    return colors_map.get(type_oeuvre, 'blue')

def render_folium_map(df):
    """Carte interactive Folium avec survol des œuvres"""
    st.markdown(f"<h2 style='border-left: 3px solid {COLORS['primary']}; padding-left: 15px;'>Carte Mondiale Interactive</h2>", unsafe_allow_html=True)
    
    if df.empty:
        st.warning("Aucune donnée à afficher avec les filtres actuels.")
        return
    
    # Créer la carte centrée sur la moyenne des coordonnées
    m = folium.Map(
        location=[df['latitude'].mean(), df['longitude'].mean()],
        zoom_start=2,
        tiles='CartoDB dark_matter'  # Thème sombre
    )
    
    # Ajouter les marqueurs pour chaque œuvre
    for idx, row in df.iterrows():
        # HTML du popup personnalisé
        popup_html = f"""
        <div style="
            font-family: Arial, sans-serif;
            width: 280px;
            background-color: #1a1a1a;
            border-left: 4px solid {COLORS['primary']};
            padding: 15px;
            border-radius: 6px;
        ">
            <h3 style="
                margin: 0 0 10px 0;
                color: {COLORS['primary']};
                font-size: 16px;
                font-weight: bold;
            ">{row['oeuvre']}</h3>
            
            <p style="
                margin: 5px 0;
                color: #aaa;
                font-size: 13px;
            ">
                <strong>Lieu:</strong> {row['lieu']}
            </p>
            
            <p style="
                margin: 5px 0;
                color: #aaa;
                font-size: 13px;
            ">
                <strong>Type:</strong> {row['type']}
            </p>
            
            <p style="
                margin: 5px 0;
                color: #aaa;
                font-size: 13px;
            ">
                <strong>Année:</strong> {row['annee']}
            </p>
            
            <p style="
                margin: 10px 0 0 0;
                color: #ccc;
                font-size: 12px;
                line-height: 1.5;
            ">{row['description']}</p>
            
            {f'<p style="margin: 10px 0 0 0; color: #888; font-size: 11px; font-style: italic;">Collaborateurs: {row["artistes_lies"]}</p>' if row['artistes_lies'] else ''}
        </div>
        """
        
        # Créer le marqueur
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=8,
            popup=folium.Popup(popup_html, max_width=300),
            color=get_marker_color(row['type']),
            fill=True,
            fillColor=get_marker_color(row['type']),
            fillOpacity=0.7,
            weight=2,
            tooltip=f"{row['oeuvre']} - {row['lieu']}"
        ).add_to(m)
    
    # Ajouter une légende
    legend_html = f"""
    <div style="
        position: fixed;
        bottom: 50px;
        right: 50px;
        background-color: rgba(26, 26, 26, 0.9);
        border-left: 3px solid {COLORS['primary']};
        padding: 15px;
        border-radius: 6px;
        z-index: 1000;
        font-family: Arial, sans-serif;
    ">
        <h4 style="margin: 0 0 10px 0; color: {COLORS['primary']};">Légende</h4>
        <p style="margin: 5px 0; color: #ccc; font-size: 12px;">
            <span style="color: blue;">●</span> Street Art
        </p>
        <p style="margin: 5px 0; color: #ccc; font-size: 12px;">
            <span style="color: green;">●</span> Mural
        </p>
        <p style="margin: 5px 0; color: #ccc; font-size: 12px;">
            <span style="color: red;">●</span> Exposition
        </p>
        <p style="margin: 5px 0; color: #ccc; font-size: 12px;">
            <span style="color: orange;">●</span> Installation
        </p>
        <p style="margin: 5px 0; color: #ccc; font-size: 12px;">
            <span style="color: purple;">●</span> Intervention
        </p>
        <p style="margin: 5px 0; color: #ccc; font-size: 12px;">
            <span style="color: cadetblue;">●</span> Série
        </p>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    
    # Afficher la carte
    st_folium(m, width=1400, height=600)
    
    st.markdown(f"""
        <p style='text-align: center; color: {COLORS["text_secondary"]}; font-size: 0.9em; margin-top: 1em;'>
            Cliquez sur les points pour voir les détails des œuvres
        </p>
    """, unsafe_allow_html=True)

def render_timeline(df):
    """Timeline des œuvres"""
    st.markdown(f"<h2 style='border-left: 3px solid {COLORS['primary']}; padding-left: 15px;'>Chronologie des Œuvres</h2>", unsafe_allow_html=True)
    
    if df.empty:
        st.warning("Aucune donnée à afficher.")
        return
    
    fig = px.scatter(
        df,
        x='date',
        y='oeuvre',
        color='type',
        hover_data=['lieu', 'description'],
        color_discrete_sequence=[COLORS['primary'], '#2ECC71', '#FF6B6B', '#FFA500', '#9B59B6', '#52A8D9']
    )
    
    fig.update_layout(
        height=600,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['text_primary']),
        xaxis=dict(gridcolor=COLORS['border'], title='Date'),
        yaxis=dict(gridcolor=COLORS['border'], title='Œuvre')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tableau détaillé
    st.markdown(f"<h3 style='margin-top: 2em;'>Détails des Œuvres</h3>", unsafe_allow_html=True)
    st.dataframe(
        df[['date', 'oeuvre', 'lieu', 'type', 'description']],
        use_container_width=True,
        hide_index=True
    )

def render_analytics(df):
    """Statistiques et analyses"""
    st.markdown(f"<h2 style='border-left: 3px solid {COLORS['primary']}; padding-left: 15px;'>Analyses & Statistiques</h2>", unsafe_allow_html=True)
    
    if df.empty:
        st.warning("Aucune donnée à afficher.")
        return
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribution par type
        type_counts = df['type'].value_counts()
        fig_pie = px.pie(
            values=type_counts.values,
            names=type_counts.index,
            title="Répartition par Type d'Œuvre",
            color_discrete_sequence=[COLORS['primary'], '#2ECC71', '#FF6B6B', '#FFA500', '#9B59B6']
        )
        fig_pie.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color=COLORS['text_primary'])
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Distribution géographique
        lieu_counts = df['lieu'].value_counts().head(10)
        fig_bar = px.bar(
            x=lieu_counts.values,
            y=lieu_counts.index,
            orientation='h',
            title="Top 10 Lieux",
            color_discrete_sequence=[COLORS['primary']]
        )
        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color=COLORS['text_primary']),
            xaxis=dict(gridcolor=COLORS['border'], title='Nombre d\'œuvres'),
            yaxis=dict(gridcolor=COLORS['border'], title='Lieu')
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Activité par année
    st.markdown("<br>", unsafe_allow_html=True)
    activite = df.groupby('annee').size()
    fig_line = px.line(
        x=activite.index,
        y=activite.values,
        title="Activité par Année",
        markers=True
    )
    fig_line.update_traces(line_color=COLORS['primary'], marker_color=COLORS['primary'])
    fig_line.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['text_primary']),
        xaxis=dict(gridcolor=COLORS['border'], title='Année'),
        yaxis=dict(gridcolor=COLORS['border'], title='Nombre d\'œuvres')
    )
    st.plotly_chart(fig_line, use_container_width=True)
