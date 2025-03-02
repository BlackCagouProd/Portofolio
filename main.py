import streamlit as st
from pages import home, about, skills, projects, contact, verification
import os
# Configuration de la page
st.set_page_config(page_title="Mon Portfolio", layout="wide")

# Importer le CSS
css_file = "utils/style.css"
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Définir les pages
pages = [
    st.Page(home.home_show, title="Home", icon="🏠", default=True),  # Page par défaut
    st.Page(about.about_show, title="About", icon="📘"),
    st.Page(skills.skills_show, title="Skills", icon="💡"),
    st.Page(projects.projects_show, title="Projects", icon="🚀"),
    st.Page(contact.contact_show, title="Contact", icon="📧"),
    st.Page(verification.verification_show, title="Verification", icon="🔒"),
]

# Créer la navigation
pg = st.navigation(pages)

# Exécuter la navigation
pg.run()