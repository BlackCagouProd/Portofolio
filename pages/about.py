import streamlit as st

def about_show():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: 0.5em;'>
            À Propos
        </h1>
        <p style='text-align: center; font-size: 1.3em; font-style: italic; color: #1f77b4;'>
            Le sens guide la technique
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Présentation courte
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div style='text-align: center; padding: 1.5em; border-left: 3px solid #1f77b4; border-right: 3px solid #1f77b4;'>
                <h2 style='margin: 0;'>Clément Wahaga</h2>
                <p style='margin: 0.5em 0; font-size: 1.1em; color: #aaa;'>
                    35 ans | Originaire de Nouvelle-Calédonie
                </p>
                <p style='margin: 0.5em 0; color: #1f77b4;'>
                    Étudiant Ingénieur en Cybersécurité
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Introduction
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div style='text-align: center; line-height: 1.8;'>
                <p style='font-size: 1.1em;'>
                    Étudiant-ingénieur en 5ème année de Cybersécurité à l'ESAIP, je mène un parcours 
                    atypique : BTP → Développement Web → Cybersécurité & Gouvernance. Cette trajectoire 
                    m'a forgé une vision globale alliant rigueur technique, adaptabilité et compréhension 
                    des enjeux métiers.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Bouton de téléchargement du CV
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        with open("./assets/pdf/CV_2026.pdf", "rb") as file:
            st.download_button(
                label="Télécharger mon CV",
                data=file,
                file_name="CV_Clement_Wahaga_2026.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Parcours
    st.markdown("<h2 style='text-align: center; margin-bottom: 2em;'>Parcours</h2>", unsafe_allow_html=True)
    
    # Timeline épurée
    timeline_data = [
        ("2026", "Diplôme d'Ingénieur Cybersécurité", "ESAIP, Angers", 
         "Spécialisation AppSec & Gouvernance des Risques", "left"),
        ("2025-2026", "Erasmus", "Universidad de Almería, Espagne", 
         "Semestre d'échange international", "right"),
        ("2025", "Développeur Web", "LegalSphère", 
         "WordPress, Shopify, Odoo", "left"),
        ("2025", "Consultant Informatique", "Comat Group", 
         "OCR, MVP application mobile", "right"),
        ("2024", "Erasmus", "Gebze Technical University, Turquie", 
         "Semestre d'échange international", "left"),
        ("2024", "Développeur Logiciel", "Korriganed", 
         "Mise en place SIEM Wazuh", "right"),
        ("2021", "Titre Professionnel", "CFA de la CCI de Nouvelle-Calédonie", 
         "Développeur Web et Web Mobile", "left"),
        ("2021", "Développeur Web", "IODNC", 
         "Générateur de PDF", "right"),
        ("2021", "Développeur Web", "DFPC", 
         "Formulaires Webform Drupal", "left"),
        ("2014-2019", "Animateur Multimédia", "Mairie de Dumbéa", 
         "Ateliers bureautique et multimédia", "right"),
        ("2014", "Titre Professionnel", "AFBTP Nouvelle-Calédonie", 
         "Constructeur Professionnel Voirie et Réseaux", "left"),
    ]
    
    for year, title, company, desc, align in timeline_data:
        if align == "left":
            col1, col2, col3 = st.columns([0.45, 0.1, 0.45])
            
            with col1:
                st.markdown(f"""
                    <div style='text-align: right; padding-right: 20px; margin-bottom: 40px;'>
                        <p style='margin: 0; font-size: 0.9em; color: #888;'>{year}</p>
                        <h4 style='margin: 5px 0;'>{title}</h4>
                        <p style='margin: 0; color: #aaa; font-size: 0.95em;'>{company}</p>
                        <p style='margin: 5px 0 0 0; font-size: 0.9em;'>{desc}</p>
                    </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                    <div style='width: 2px; background: linear-gradient(180deg, #1f77b4 0%, #1f77b4 100%); 
                         height: 120px; margin: 0 auto; position: relative;'>
                        <div style='width: 10px; height: 10px; background-color: #1f77b4; 
                             border-radius: 50%; position: absolute; left: -4px; top: 10px;'></div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("<div style='height: 120px;'></div>", unsafe_allow_html=True)
                
        else:
            col1, col2, col3 = st.columns([0.45, 0.1, 0.45])
            
            with col1:
                st.markdown("<div style='height: 120px;'></div>", unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                    <div style='width: 2px; background: linear-gradient(180deg, #1f77b4 0%, #1f77b4 100%); 
                         height: 120px; margin: 0 auto; position: relative;'>
                        <div style='width: 10px; height: 10px; background-color: #1f77b4; 
                             border-radius: 50%; position: absolute; left: -4px; top: 10px;'></div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                    <div style='text-align: left; padding-left: 20px; margin-bottom: 40px;'>
                        <p style='margin: 0; font-size: 0.9em; color: #888;'>{year}</p>
                        <h4 style='margin: 5px 0;'>{title}</h4>
                        <p style='margin: 0; color: #aaa; font-size: 0.95em;'>{company}</p>
                        <p style='margin: 5px 0 0 0; font-size: 0.9em;'>{desc}</p>
                    </div>
                """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Section Engagement
    st.markdown("<h2 style='text-align: center; margin-bottom: 1.5em;'>Engagement Associatif</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div style='padding: 1.5em; border-left: 2px solid #1f77b4;'>
                <h4>Lutte contre l'illectronisme</h4>
                <p style='color: #aaa;'>Maison de quartier des 3 Mâts (2023-2025)</p>
                <p style='font-size: 0.95em;'>Accompagnement des publics en difficulté avec les outils numériques</p>
                <br>
                <h4>Animation périscolaire</h4>
                <p style='color: #aaa;'>Maison de quartier de Val-Suzon (2014-2018)</p>
                <p style='font-size: 0.95em;'>Encadrement d'activités éducatives pour les jeunes</p>
            </div>
        """, unsafe_allow_html=True)
