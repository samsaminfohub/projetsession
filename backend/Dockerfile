FROM python:3.9-slim
# Définir le répertoire de travail à /app
WORKDIR /app
# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt ./
# Installer les dépendances Python spécifiées dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Installer FastAPI et Uvicorn, même s'ils ne sont pas dans requirements.txt
RUN pip install fastapi uvicorn
# Copier tous les fichiers du répertoire actuel vers le répertoire de travail dans le conteneur
COPY . .
# Copier le modèle ML dans le répertoire de travail du conteneur
COPY app/model.pkl /app/model.pkl
# Définir la commande à exécuter lorsque le conteneur démarre
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

