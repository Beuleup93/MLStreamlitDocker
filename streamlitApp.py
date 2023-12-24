import streamlit as st
from pycaret.classification import load_model, predict_model
import pandas as pd

# insérer un titre
st.title("Déploiement + Docker + Streamlit")

# mise en cache du chargement du modele
# @st.cache_resource
@st.cache_data
def chargement_modele():
    return load_model("modele_saliou")

# chargement effectif
modele = chargement_modele()

# organisation en deux colonnes (1/4, 3/4)
col1, col2 = st.columns([1, 3])

# text_input alignés sur la première colonne
diastolic = col1.text_input("Diastolic : ", "72", max_chars=3)
bodymass = col1.text_input("Bodymass : ", "33", max_chars=3)
age = col1.text_input("Age : ", "50", max_chars=3)
plasma = col1.text_input("Plasma : ", "148", max_chars=3)

# fonction pour transtypage avec contrôle
# valeur pas valide = NaN pour valeur manquante parce que pycaret gère ainsi
def try_parse(str_value):
    try:
        value = float(str_value)
    except Exception:
        value = float('NaN')
    # renvoyer le resultat
    return value

# conversion en dictionnaire des données saisies par l'utilisateur
la_data = {
    'diastolic': try_parse(diastolic),
    'bodymass': try_parse(bodymass),
    'Age': try_parse(age),
    'plasma': try_parse(plasma)
}

# fonction pour effectuer le calcul
def calculer():
    # calcul de la classe d'appartenance
    # appel de la fonction de prédiction basée sur le modele chargé
    try:
        la_prediction = predict_model(modele, data=pd.DataFrame([la_data]))
        # affichage de la classe et du score d'appartenance
        st.write("Classe d'appartenance =", la_prediction[['prediction_label', 'prediction_score']])
    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")

# bouton pour faire calculer
if st.button("Calculer"):
    calculer()
