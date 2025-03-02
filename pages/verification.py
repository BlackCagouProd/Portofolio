import streamlit as st
from utils.Cr import dechiffrement_rsa, verifier_signature
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def verification_show():
    st.header("Vérification du message")
    
    message_chiffre_b64 = st.text_area("Message chiffré (Base64)")
    signature_b64 = st.text_area("Signature (Base64)")
    public_key_pem = st.text_area("Clé publique (PEM)", value=st.session_state.get('public_key_pem', ''))

    if st.button("Vérifier le message"):
        try:
            # 1. Décoder depuis Base64
            message_chiffre = base64.b64decode(message_chiffre_b64)
            signature = base64.b64decode(signature_b64)

            # 2. Charger la clé publique
            loaded_public_key = serialization.load_pem_public_key(
                public_key_pem.encode('utf-8'),
                backend=default_backend()
            )

            # 3. Déchiffrer le message
            private_key = st.session_state['private_key']
            message_dechiffre = dechiffrement_rsa(message_chiffre, private_key)
            message_dechiffre_str = message_dechiffre.decode('utf-8')

            # 4. Vérifier la signature
            signature_valide = verifier_signature(message_dechiffre, signature, loaded_public_key)

            st.subheader("Message déchiffré :")
            st.write(message_dechiffre_str)

            if signature_valide:
                st.success("La signature est VALIDE. Le message est authentique et n'a pas été modifié.")
            else:
                st.error("La signature est INVALIDE. Le message a peut-être été falsifié !")

        except Exception as e:
            st.error(f"Erreur lors du traitement du message : {e}")