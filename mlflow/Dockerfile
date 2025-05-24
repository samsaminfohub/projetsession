FROM python:3.9-slim

# Définir le répertoire de travail à /app dans le conteneur
WORKDIR /app

# Installer les dépendances nécessaires : MLflow et une version spécifique de scikit-learn
RUN pip install mlflow scikit-learn==1.2.0

# Copier tous les fichiers du répertoire local (.) vers le répertoire de travail dans le conteneur (/app)
COPY . .

# Configurer MLflow comme serveur en définissant la commande à exécuter lors du démarrage du conteneur
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000", "--backend-store-uri", "sqlite:///mlflow.db", "--default-artifact-root", "/mlflow"]
