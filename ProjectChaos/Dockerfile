# Utilisation d'une image Python officielle en tant que base
FROM python:3.9-slim

# Variables d'environnement pour éviter les problèmes avec les interfaces de ligne de commande
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Définition du répertoire de travail dans le conteneur
WORKDIR /code

# Installation des dépendances du projet
COPY requirements.txt /code/
RUN  pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt ---vvv


# Copie du code source dans le conteneur
COPY . /code/
