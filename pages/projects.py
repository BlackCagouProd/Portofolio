import streamlit as st
import os
import fitz  # PyMuPDF
from PIL import Image

def projects_show():
    st.header(" Mes Projets")

    # Tabs pour catégoriser les projets
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        " Cybersécurité", " Développement", " Académiques", " Open Source", "Bénevolat"
    ])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(" Analyseur d'URL")
            st.write("""
            - **Objectif :** Identifier les url malvaillante (phishing) 
            - **Outils utilisés :** streamlit,API_virustotal , API_ipqualityscore.
            - **Résultat :** Détection de plusieurs cas utilisation, localisation d' IP
            """)
            st.link_button(" Voir sur GitHub", "https://github.com/ClemEsaipProject/phishingdataviz")

        with col2:
            st.subheader(" Keylogger Furtif - Étude de Malware")
            st.write("""
            - **Objectif :** Analyser le comportement d'un malware de type keylogger et développer des méthodes de détection.
            - **Outils :** Python • PyInstaller • Cryptography • Wireshark • Snowflake (pour l'analyse des logs)
            - **Résultats :**
                - Développement d'un keylogger furtif avec chiffrement AES-256 et exfiltration DNS
                - Reverse engineering de 15+ techniques d'obfuscation
                - Détection réussie dans 92% des cas via des règles YARA personnalisées
            """)
            st.link_button(" Voir le Code Source", "https://github.com/monprojet")

    with tab2:
        col1, col2,col3 = st.columns(3)
        with col1:
            st.subheader(" CryptoBC - Projet Blockchain")
            st.write("""
            - **Technologies :** Python, Solidity, Web3.js, React, Ganache.
            - **Description :** Une plateforme blockchain complète avec smart contracts, wallet crypto et système de transactions sécurisées.
            - **Fonctionnalités :** Minage de blocs, transactions P2P, interface dashboard analytique.
            """)
            st.link_button(" Voir sur GitHub", "https://github.com/ClemEsaipProject/CryptoBC")

        with col2:
            st.subheader(" EVOD - Calculateur d'empreinte carbone")
            st.write("""
            - **Technologies :** PHP, wordpress.
            - **Description :** creation d'unn plugin calcualteur d'empreinte carbone et du template .
            """)
            st.link_button(" Voir sur GitHub", "https://github.com/BlackCagouProd/EVOD")

        with col3:
            st.subheader(" createur de dataset et apprentissage du LMM pour OCR")
            st.write("""
            - **Technologies :** python, streamlit,tensorflow
            - **Description :** creation de dataset en .h5, entrainement et test un LLM et analyse et prediction .
            """)
            st.link_button(" Voir sur GitHub", "https://github.com/ClemEsaipProject/OCRDIGIT")
    with tab3:
        PDF_FOLDER = "./assets/pdf/"

        st.title("📂 Aperçu des Rapports PDF")

        # Vérifier si le dossier existe
        # Vérifier si le dossier existe
        if not os.path.exists(PDF_FOLDER):
            st.error(f"Le dossier '{PDF_FOLDER}' n'existe pas. Vérifiez le chemin.")
        else:
            pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]

            if not pdf_files:
                st.warning("Aucun fichier PDF trouvé dans le dossier.")
            else:
                # Diviser les fichiers en groupes de 2
                for i in range(0, len(pdf_files), 2):
                    cols = st.columns(2)  # Créer 2 colonnes

                    for j in range(2):  # Remplir les colonnes
                        if i + j < len(pdf_files):  # Vérifier qu'on ne dépasse pas la liste
                            pdf = pdf_files[i + j]
                            pdf_path = os.path.join(PDF_FOLDER, pdf)

                            with cols[j]:  # Affichage dans la colonne correspondante
                                st.subheader(f" {pdf}")

                                # Charger la première page du PDF en image
                                doc = fitz.open(pdf_path)
                                page = doc[0]  # Première page
                                pix = page.get_pixmap()
                                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                                # Afficher l'aperçu
                                st.image(img, caption=f"Aperçu de {pdf}")

                                # Ajouter un bouton de téléchargement
                                with open(pdf_path, "rb") as file:
                                    st.download_button(
                                        label=" Télécharger",
                                        data=file,
                                        file_name=pdf,
                                        mime="application/pdf"
                                    )

                    st.markdown("---")  # Ligne de séparation entre les PDF

    with tab5 :
         col1, col2 = st.columns(2)
         with col1:
            st.subheader(" Maison de quartier des 3 Mâts (2023 - 2024)")
            st.markdown("""
            - **Lutte contre l’illectronisme** : Accompagnement des personnes en difficulté avec le numérique.
            - Organisation d’ateliers d’initiation à l’informatique et à l’usage d’Internet.
            """)
         with col2:
            st.subheader(" Maison de quartier de Val-Suzon (2015 - 2019)")
            st.markdown("""
            - **Animateur multimédia** : Formation des habitants aux outils numériques.
            - Sensibilisation à la cybersécurité et à la protection des données.
            - Accompagnement des seniors et des jeunes à la découverte du digital.
            """)

                
            
