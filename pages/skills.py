import streamlit as st
import plotly.graph_objects as go


def skills_show():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: 0.5em;'>
            Mes Compétences
        </h1>
        <p style='text-align: center; font-size: 1.1em; font-style: italic; color: #1f77b4;'>
            Le sens guide la technique
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigation horizontale
    tab1, tab2, tab3 = st.tabs(["Hard Skills", "Soft Skills", "Compétences Transversales"])
    
    with tab1:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Graphique en étoile
            categories = [
                'Cybersécurité',
                'Développement',
                'Gouvernance',
                'IA & Data',
                'Infrastructure',
                'Réseaux',
                'DevOps',
                'Cloud'
            ]
            values = [5, 5, 4, 4, 4, 3, 4, 3]

            fig = go.Figure(data=go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                line_color='#1f77b4',
                fillcolor='rgba(31, 119, 180, 0.3)'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True, 
                        range=[0, 5],
                        gridcolor='#333'
                    ),
                    bgcolor='rgba(0,0,0,0)'
                ), 
                showlegend=False,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=80, r=80, t=40, b=40)
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("<h3 style='border-left: 3px solid #1f77b4; padding-left: 15px;'>Détail des compétences</h3>", unsafe_allow_html=True)
            
            # 2 colonnes pour le détail
            detail_col1, detail_col2 = st.columns(2)
            
            with detail_col1:
                st.markdown("**Cybersécurité**")
                st.markdown("- Pentest & OWASP Top 10")
                st.markdown("- Audit RGPD, ISO 27001")
                st.markdown("- Cryptographie")
                
                st.markdown("**Développement**")
                st.markdown("- Python, PHP, Java, JS")
                st.markdown("- HTML/CSS, Flutter")
                st.markdown("- WordPress, Shopify, Odoo")
                
                st.markdown("**Gouvernance & Risques**")
                st.markdown("- EBIOS Risk Manager")
                st.markdown("- MEHARI, MAGERIT")
                st.markdown("- ISO 27001/27005, NIS2")
                
                st.markdown("**IA & Data**")
                st.markdown("- OCR (Reconnaissance optique)")
                st.markdown("- Machine Learning")
                st.markdown("- MySQL, SQLite")
            
            with detail_col2:
                st.markdown("**Infrastructure & Cloud**")
                st.markdown("- Linux, Windows")
                st.markdown("- Azure Cloud")
                st.markdown("- Google Cloud")
                
                st.markdown("**DevOps**")
                st.markdown("- Git, GitHub, GitLab")
                st.markdown("- Docker, Kubernetes")
                st.markdown("- Terraform")
                
                st.markdown("**Réseaux**")
                st.markdown("- Cisco, Opendaylight")
                st.markdown("- Architecture réseau")
                st.markdown("- Théorie des graphes")
                
                st.markdown("**Méthodologies**")
                st.markdown("- UML")
                st.markdown("- Spécification & tests")
                st.markdown("- Gestion de projet")
    
    with tab2:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("<h3 style='border-left: 3px solid #1f77b4; padding-left: 15px;'>Détail des Soft Skills</h3>", unsafe_allow_html=True)
            
            soft_skills_detail = [
                ("Communication", 4, "Capacité à expliquer des concepts techniques complexes"),
                ("Résolution de problèmes", 5, "Approche analytique et méthodique"),
                ("Pensée critique", 4, "Analyse approfondie et remise en question"),
                ("Créativité", 3, "Innovation dans les solutions proposées"),
                ("Gestion du stress", 3, "Adaptabilité face aux situations complexes"),
                ("Intelligence émotionnelle", 4, "Compréhension et gestion des relations")
            ]
            
            for skill, level, desc in soft_skills_detail:
                st.markdown(f"""
                    <div style='margin-bottom: 15px;'>
                        <p style='margin: 0; font-weight: bold;'>{skill}</p>
                        <p style='margin: 0; color: #1f77b4; font-size: 0.9em;'>Niveau {level}/5</p>
                        <p style='margin: 0; font-size: 0.85em; color: #aaa;'>{desc}</p>
                    </div>
                """, unsafe_allow_html=True)
        
        with col2:
            # Graphique en barres horizontales pour les Soft Skills
            soft_skills = [
                "Communication",
                "Résolution de problèmes",
                "Pensée critique",
                "Intelligence émotionnelle",
                "Créativité",
                "Gestion du stress"
            ]
            skill_levels = [4, 5, 4, 4, 3, 3]

            fig = go.Figure(go.Bar(
                x=skill_levels,
                y=soft_skills,
                orientation='h',
                marker_color='#1f77b4',
                marker_line_color='#1f77b4',
                marker_line_width=1.5
            ))
            
            fig.update_layout(
                xaxis=dict(
                    range=[0, 5],
                    gridcolor='#333',
                    title=""
                ),
                yaxis=dict(
                    gridcolor='#333',
                    title=""
                ),
                height=400,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=0, r=20, t=20, b=20)
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Graphique radar pour Compétences Transversales
            transversal_skills = [
                "Outils numériques",
                "Esprit d'équipe", 
                "Autonomie",
                "Adaptation", 
                "Synthèse",
                "Méthodologie"
            ]
            skill_levels = [5, 4, 5, 4, 4, 4]

            fig = go.Figure(data=go.Scatterpolar(
                r=skill_levels,
                theta=transversal_skills,
                fill='toself',
                line_color='#1f77b4',
                fillcolor='rgba(31, 119, 180, 0.3)'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True, 
                        range=[0, 5],
                        gridcolor='#333'
                    ),
                    bgcolor='rgba(0,0,0,0)'
                ), 
                showlegend=False,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=80, r=80, t=40, b=40)
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("<h3 style='border-left: 3px solid #1f77b4; padding-left: 15px;'>Détail des Compétences Transversales</h3>", unsafe_allow_html=True)
            
            transversal_detail = [
                ("Utilisation des outils numériques", 5, "Maîtrise avancée des technologies"),
                ("Esprit d'équipe", 4, "Collaboration efficace en projet"),
                ("Autonomie", 5, "Capacité à travailler de manière indépendante"),
                ("Capacité d'adaptation", 4, "Flexibilité face aux changements"),
                ("Esprit de synthèse", 4, "Extraction rapide des informations clés"),
                ("Méthodologie", 4, "Approche structurée et rigoureuse")
            ]
            
            for skill, level, desc in transversal_detail:
                st.markdown(f"""
                    <div style='margin-bottom: 15px;'>
                        <p style='margin: 0; font-weight: bold;'>{skill}</p>
                        <p style='margin: 0; color: #1f77b4; font-size: 0.9em;'>Niveau {level}/5</p>
                        <p style='margin: 0; font-size: 0.85em; color: #aaa;'>{desc}</p>
                    </div>
                """, unsafe_allow_html=True)
