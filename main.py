import streamlit as st
import streamlit.components.v1 as components
from pages import home, about, skills, projects,banksy, contact, verification
import os
# Configuration de la page
st.set_page_config(page_title="Mon Portfolio", layout="wide")

# Importer le CSS
css_file = "utils/style.css"
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Définir les pages
pages = [
    st.Page(home.home_show, title="Accueil",  default=True),  # Page par défaut
    st.Page(about.about_show, title="A propos de moi", ),
    st.Page(skills.skills_show, title="Mes competences", ),
    st.Page(projects.projects_show, title="Mes projects", ),
    st.Page(banksy.banksy_show,title="Banksy",),
    # st.Page(contact.contact_show, title="Me contacter", ),
    # st.Page(verification.verification_show, title="Verification", ),
]

# Créer la navigation
pg = st.navigation(pages)

# Exécuter la navigation
pg.run()