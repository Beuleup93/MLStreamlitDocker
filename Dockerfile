FROM python:3.11.4

# repertoire de travail
WORKDIR /app

# copie du contenu du dossier courant vers /app/
ADD . /app/

# Mise à jour des packages
RUN apt-get update && apt-get install -y libgomp1

# installation des packages obligatoires
RUN pip install -r requirements.txt

# Port exposé
EXPOSE 1664

# Commande à executer au demarrage du container
CMD streamlit run --server.port 1664 streamlitApp.py
