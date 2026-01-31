import streamlit as st
import os
import streamlit.components.v1 as components



# def home_show():
    

#     col1, col2= st.columns(2)
#     with col1:
#         st.title("Ma passion , mon métier ")
#         st.subheader("Ingénierie, Sécurité, Réflexion : Exploration d'un esprit curieux.")
#         # Courts paragraphes de présentation
#         st.write("""
#             Bienvenue ! Je suis un étudiant ingénieur en cybersécurité, passionné par la complexité du monde numérique. 
#             Au-delà des lignes de code et des protocoles de sécurité, je suis fasciné par la philosophie et les mécanismes de l'économie. 
#             Ce portfolio est une fenêtre ouverte sur mes explorations, mes projets et mes réflexions.
#     """)
#         st.write("""
#         Mon objectif ? Obtenir mon diplôme et contribuer à un avenir numérique plus sûr et plus éthique. 
#         Mais aussi, continuer à explorer les liens fascinants entre la technologie, la société et l'esprit humain.
#     """)
#          # Aperçu des centres d'intérêt
#         st.subheader("Mes Passions ")
#         st.write("-  Cybersécurité : Protéger les données et les systèmes.")
#         st.write("-  Développement : Créer des solutions innovantes.")
#         st.write("-  Philosophie : Comprendre le monde et notre place dedans.")
#         st.write("-  Économie : Analyser les forces qui façonnent notre société.")
#     with col2:
#     # Citation inspirante
#         components.iframe("https://tryhackme.com/api/v2/badges/public-profile?userPublicId=3974252", width=400)
#         st.markdown("> \"Je pense, donc je suis vulnérable... mais je me protège !\"  - *Clément WAHAGA,35ans*")

    
def home_show():
    # Hero Section - Titre impactant avec phrase d'accroche
    st.markdown("""
        <h1 style='text-align: center; font-size: 3.5em; margin-bottom: 0.2em;'>
            Ingénierie de la Sécurité Numérique
        </h1>
        <p style='text-align: center; font-size: 1.5em; font-style: italic; color: #1f77b4; margin-top: 0.5em; margin-bottom: 0.3em;'>
            Le sens guide la technique
        </p>
        <p style='text-align: center; font-size: 1.2em; color: #666; margin-top: 0;'>
            Conception, Protection, Gouvernance, Innovation
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Proposition de valeur
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div style='text-align: center; line-height: 1.8;'>
                <p style='font-size: 1.1em;'>
                    Spécialisé en cybersécurité et développement logiciel, je conçois des solutions 
                    techniques robustes qui allient performance, sécurité et conformité réglementaire. 
                    Mon approche combine expertise technique, maîtrise des frameworks de gouvernance 
                    et vision globale des enjeux numériques.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Domaines d'expertise
    st.markdown("<h2 style='text-align: center; margin-bottom: 2em;'>Domaines d'Expertise</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div style='padding: 2em; border-left: 3px solid #1f77b4;'>
                <h3>Cybersécurité</h3>
                <p>Analyse de vulnérabilités, tests d'intrusion, conception d'architectures sécurisées</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='padding: 2em; border-left: 3px solid #1f77b4;'>
                <h3>Développement</h3>
                <p>Conception et développement d'applications web et mobiles performantes et évolutives</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style='padding: 2em; border-left: 3px solid #1f77b4;'>
                <h3>Infrastructure</h3>
                <p>Administration système, gestion de bases de données, architecture réseau</p>
            </div>
        """, unsafe_allow_html=True)
    
    
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Section Gouvernance - SANS BACKGROUND BLANC
    st.markdown("<h2 style='text-align: center; margin-bottom: 1.5em;'>Gouvernance et Conformité</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div style='padding: 2em; border-left: 3px solid #1f77b4; line-height: 1.8;'>
                <p style='text-align: justify;'>
                    La sécurité ne se limite pas à la technique. Elle s'inscrit dans un cadre 
                    réglementaire et normatif rigoureux. Ma maîtrise des méthodologies d'analyse 
                    de risques et des référentiels de gouvernance me permet d'accompagner les 
                    organisations dans leur mise en conformité et la structuration de leur 
                    démarche sécurité.
                </p>
                <ul style='margin-top: 1em; line-height: 2;'>
                    <li>EBIOS Risk Manager - Méthode d'analyse et de gestion des risques</li>
                    <li>MEHARI - Méthode harmonisée d'analyse des risques</li>
                    <li>MAGERIT - Méthodologie d'analyse et de gestion des risques</li>
                    <li>Normes ISO 27001/27005 - Systèmes de management de la sécurité</li>
                    <li>RGPD - Protection des données personnelles</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Approche méthodologique
    st.markdown("<h2 style='text-align: center; margin-bottom: 1.5em;'>Une Approche Globale</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div style='text-align: justify; line-height: 1.8;'>
                <p>
                    Au-delà de la technique, je m'intéresse aux dimensions philosophiques, économiques 
                    et juridiques du numérique. Cette perspective élargie me permet d'aborder les projets 
                    avec une compréhension approfondie des enjeux humains, éthiques, réglementaires et 
                    stratégiques qui sous-tendent les solutions technologiques.
                </p>
                <p>
                    Chaque projet est une opportunité de créer de la valeur en combinant rigueur 
                    méthodologique, conformité réglementaire, innovation technique et vision stratégique.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Call to action subtil
    st.markdown("<hr style='border: 1px solid #333;'>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div style='text-align: center; padding: 1em;'>
                <h4>Compétences</h4>
                <p style='font-size: 0.9em; color: #666;'>Découvrez mon expertise technique et transversale</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='text-align: center; padding: 1em;'>
                <h4>Projets</h4>
                <p style='font-size: 0.9em; color: #666;'>Explorez mes réalisations et cas d'usage</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style='text-align: center; padding: 1em;'>
                <h4>Parcours</h4>
                <p style='font-size: 0.9em; color: #666;'>Consultez mon parcours académique et professionnel</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div style='text-align: center; padding: 1em;'>
                <h4>Contact</h4>
                <p style='font-size: 0.9em; color: #666;'>Échangeons sur vos projets</p>
            </div>
        """, unsafe_allow_html=True)


    

   

    