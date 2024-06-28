# Dockerfile

# Utiliser une image officielle de Python comme base
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /code

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copier le reste de l'application
COPY . /code/

# Exposer le port sur lequel l'application Django sera accessible
EXPOSE 8000

# Commande par défaut pour exécuter l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
