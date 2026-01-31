import streamlit as st
import os
import fitz  # PyMuPDF
from PIL import Image

def projects_show():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: 0.5em;'>
            Mes Projets
        </h1>
        <p style='text-align: center; font-size: 1.1em; font-style: italic; color: #1f77b4;'>
            Le sens guide la technique
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Tabs pour catégoriser les projets
    tab1, tab2, tab3, tab4 = st.tabs([
        "Cybersécurité", "Développement", "Académiques", "Bénévolat"
    ])

    with tab1:
        st.markdown("<h2 style='border-left: 3px solid #1f77b4; padding-left: 15px; margin-bottom: 2em;'>Projets Cybersécurité</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                <div style='padding: 1.5em; margin-bottom: 2em;'>
                    <h3>Analyseur d'URL - Détection de Phishing</h3>
                    <p style='color: #aaa; margin: 0.5em 0;'><strong>Objectif :</strong> Identifier les URLs malveillantes (phishing)</p>
                    <p style='color: #aaa; margin: 0.5em 0;'><strong>Technologies :</strong> Streamlit, API VirusTotal, API IPQualityScore</p>
                    <p style='color: #aaa; margin: 0.5em 0;'><strong>Résultat :</strong> Détection de plusieurs cas d'usage, localisation d'IP suspectes</p>
                </div>
            """, unsafe_allow_html=True)
            
            col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
            with col_btn2:
                st.link_button("Voir sur GitHub", "https://github.com/ClemEsaipProject/phishingdataviz")

        with col2:
            st.markdown("""
                <div style='padding: 1.5em; margin-bottom: 2em;'>
                    <h3>Metric - Analyse de Flux Vidéo</h3>
                    <p style='color: #aaa; margin: 0.5em 0;'><strong>Objectif :</strong> Protocole expérimental d'analyse de flux vidéo</p>
                    <p style='color: #aaa; margin: 0.5em 0;'><strong>Technologies :</strong> Python, Computer Vision, Analyse de flux</p>
                    <p style='color: #aaa; margin: 0.5em 0;'><strong>Application :</strong> Détection et analyse en temps réel des flux vidéo</p>
                </div>
            """, unsafe_allow_html=True)
            
            col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
            with col_btn2:
                st.link_button("Voir sur GitHub", "https://github.com/ClemEsaipProject/metric")

    with tab2:
        st.markdown("<h2 style='border-left: 3px solid #1f77b4; padding-left: 15px; margin-bottom: 2em;'>Projets Développement</h2>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
                <div style='padding: 1.5em; margin-bottom: 2em;'>
                    <h3>CryptoBC</h3>
                    <p style='color: #aaa; font-size: 0.95em;'><strong>Blockchain</strong></p>
                    <p style='margin: 0.5em 0;'>Plateforme blockchain complète avec smart contracts et wallet crypto</p>
                    <p style='color: #888; font-size: 0.9em;'>Python • Solidity • Web3.js • React • Ganache</p>
                </div>
            """, unsafe_allow_html=True)
            
            col_btn1, col_btn2, col_btn3 = st.columns([0.5, 2, 0.5])
            with col_btn2:
                st.link_button("Voir sur GitHub", "https://github.com/ClemEsaipProject/CryptoBC")

        with col2:
            st.markdown("""
                <div style='padding: 1.5em; margin-bottom: 2em;'>
                    <h3>EVOD</h3>
                    <p style='color: #aaa; font-size: 0.95em;'><strong>Empreinte Carbone</strong></p>
                    <p style='margin: 0.5em 0;'>Plugin WordPress calculateur d'empreinte carbone</p>
                    <p style='color: #888; font-size: 0.9em;'>PHP • WordPress</p>
                </div>
            """, unsafe_allow_html=True)
            
            col_btn1, col_btn2, col_btn3 = st.columns([0.5, 2, 0.5])
            with col_btn2:
                st.link_button("Voir sur GitHub", "https://github.com/BlackCagouProd/EVOD")

        with col3:
            st.markdown("""
                <div style='padding: 1.5em; margin-bottom: 2em;'>
                    <h3>OCR Digit</h3>
                    <p style='color: #aaa; font-size: 0.95em;'><strong>Machine Learning</strong></p>
                    <p style='margin: 0.5em 0;'>Création de dataset et apprentissage LLM pour OCR</p>
                    <p style='color: #888; font-size: 0.9em;'>Python • Streamlit • TensorFlow</p>
                </div>
            """, unsafe_allow_html=True)
            
            col_btn1, col_btn2, col_btn3 = st.columns([0.5, 2, 0.5])
            with col_btn2:
                st.link_button("Voir sur GitHub", "https://github.com/ClemEsaipProject/OCRDIGIT")

    with tab3:
        st.markdown("<h2 style='border-left: 3px solid #1f77b4; padding-left: 15px; margin-bottom: 2em;'>Travaux Académiques</h2>", unsafe_allow_html=True)
        
        PDF_FOLDER = "./assets/pdf/"

        if not os.path.exists(PDF_FOLDER):
            st.error(f"Le dossier '{PDF_FOLDER}' n'existe pas. Vérifiez le chemin.")
        else:
            pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]

            if not pdf_files:
                st.warning("Aucun fichier PDF trouvé dans le dossier.")
            else:
                for i in range(0, len(pdf_files), 2):
                    cols = st.columns(2)

                    for j in range(2):
                        if i + j < len(pdf_files):
                            pdf = pdf_files[i + j]
                            pdf_path = os.path.join(PDF_FOLDER, pdf)

                            with cols[j]:
                                st.markdown(f"<h3>{pdf}</h3>", unsafe_allow_html=True)

                                doc = fitz.open(pdf_path)
                                page = doc[0]
                                pix = page.get_pixmap()
                                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                                st.image(img, caption=f"Aperçu de {pdf}")

                                col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
                                with col_btn2:
                                    with open(pdf_path, "rb") as file:
                                        st.download_button(
                                            label="Télécharger",
                                            data=file,
                                            file_name=pdf,
                                            mime="application/pdf"
                                        )

                    st.markdown("<br>", unsafe_allow_html=True)

    with tab4:
        st.markdown("<h2 style='border-left: 3px solid #1f77b4; padding-left: 15px; margin-bottom: 2em;'>Engagement Bénévole</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                <div style='padding: 1.5em;'>
                    <h3>Maison de quartier des 3 Mâts</h3>
                    <p style='color: #aaa;'>2023 - 2025</p>
                    <p style='margin: 0.8em 0;'><strong>Lutte contre l'illectronisme</strong></p>
                    <ul style='color: #ccc; line-height: 1.8;'>
                        <li>Accompagnement des personnes en difficulté avec le numérique</li>
                        <li>Organisation d'ateliers d'initiation à l'informatique</li>
                        <li>Formation à l'usage sécurisé d'Internet</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div style='padding: 1.5em;'>
                    <h3>Maison de quartier de Val-Suzon</h3>
                    <p style='color: #aaa;'>2014 - 2018</p>
                    <p style='margin: 0.8em 0;'><strong>Animateur multimédia</strong></p>
                    <ul style='color: #ccc; line-height: 1.8;'>
                        <li>Formation des habitants aux outils numériques</li>
                        <li>Sensibilisation à la cybersécurité</li>
                        <li>Accompagnement seniors et jeunes au digital</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
