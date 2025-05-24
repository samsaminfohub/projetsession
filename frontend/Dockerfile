# Utiliser l'image Python 3.9 slim comme image de base
FROM python:3.9-slim
# Définir le répertoire de travail à /app dans le conteneur
WORKDIR /app
# Installer les dépendances nécessaires pour l'application Streamlit
RUN pip install --no-cache-dir streamlit requests
# Copier tous les fichiers du répertoire local (.) vers le répertoire de travail dans le conteneur (/app)
COPY . ./
# Exposer le port 8502 utilisé par Streamlit pour être accessible depuis l'extérieur du conteneur
EXPOSE 8502
# Définir l'entrée principale pour lancer l'application Streamlit dans le conteneur
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8502", "--server.address=0.0.0.0"]
