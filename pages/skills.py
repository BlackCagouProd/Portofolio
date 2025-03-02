import streamlit as st
import plotly.graph_objects as go

def skills_show():
    st.header("Mes Compétences")
    
    # Navigation horizontale
    tab1, tab2, tab3 = st.tabs(["💻 Hard Skills", "🧠 Soft Skills", "🔄 Compétences Transversales"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            # Graphique en étoile
            categories = [
                'Architecture technique', 'Administration système',
                'Développement logiciel', 'Ingénierie des données',
                'Méthodologies', 'Web et Mobile',
                'Cybersécurité', 'Outils et technologies',
                'Réseaux', 'Mathématiques appliquées'
            ]
            values = [4, 4, 5, 4, 4, 5, 3, 4, 3, 3]

            fig = go.Figure(data=go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself'
            ))
            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Détail des compétences")
            hard_skills = [
                "Architecture technique : Conception de réseaux, théorie des graphes",
                "Administration système : Linux, supervision d'infrastructures",
                "Développement logiciel : Python, PHP, Java, HTML/CSS, JavaScript, Flutter",
                "Ingénierie des données : Bases de données relationnelles, SQL, conception et gestion",
                "Méthodologies : UML, spécification et tests, gestion de projet",
                "Web et Mobile : Création de sites web, e-commerce, développement d'applications",
                "Cybersécurité : Diagnostic de sécurité, tests de pénétration",
                "Outils et technologies : Git, GitHub, GitLab, Suite Microsoft Office",
                "Réseaux : Technologies Cisco, Opendaylight",
                "Mathématiques appliquées : Analyse, mathématiques pour le numérique"
            ]
            for skill in hard_skills:
                st.markdown(f"- {skill}")
    
    with tab2:
        col1, col2 = st.columns(2)
        with col2:
            # Graphique en barres horizontales pour les Soft Skills
            soft_skills = [
                "Communication",
                "Créativité", 
                "Résolution de problèmes",
                "Pensée critique",
                "Gestion du stress", 
                "Intelligence émotionnelle"
            ]
            skill_levels = [4, 3, 5, 4, 3, 4]

            fig = go.Figure(go.Bar(
                x=skill_levels,
                y=soft_skills,
                orientation='h',
                marker_color='rgba(50, 171, 96, 0.7)'
            ))
            fig.update_layout(title="Niveau de Soft Skills", xaxis_title="Niveau de compétence", yaxis_title="Compétences", height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col1:
            st.subheader("Détail des Soft Skills")
            for skill, level in zip(soft_skills, skill_levels):
                st.markdown(f"- **{skill}**: Niveau {level}/5")
    
    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            # Graphique radar pour Compétences Transversales
            transversal_skills = [
                "Utilisation des outils numériques",
                "Esprit d'équipe", 
                "Autonomie",
                "Capacité d'adaptation", 
                "Esprit de synthèse",
                "Méthodologie"
            ]
            skill_levels = [4, 4, 5, 4, 3, 4]

            fig = go.Figure(data=go.Scatterpolar(
                r=skill_levels,
                theta=transversal_skills,
                fill='toself'
            ))
            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=False, title="Compétences Transversales")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Détail des Compétences Transversales")
            for skill, level in zip(transversal_skills, skill_levels):
                st.markdown(f"- **{skill}**: Niveau {level}/5")