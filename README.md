# Bank Marketing Campaign Analysis

## Présentation du projet

Ce projet a pour objectif d’analyser un jeu de données relatif à une campagne de marketing bancaire afin d’identifier les facteurs qui influencent la souscription à un dépôt à terme.

Le dataset contient des informations démographiques, financières et comportementales sur des clients contactés par télémarketing.

L’étude vise à :
- comprendre la structure des données ;
- réaliser une analyse exploratoire complète ;
- identifier les variables les plus informatives ;
- préparer les données pour une future modélisation prédictive.

## Structure du projet

```text
bank-marketing-project/
├── Data/
│   ├── Raw/
│   │   ├── bank_data.csv
│   │   └── bank_data_copy.csv
│   └── Processed/
│       └── bank_data_cleaned.csv
├── Exports/
├── Images/
├── Notebooks/
│   └── exploration.ipynb
├── Src/
│   ├── __init__.py
│   ├── cleaning.py
│   ├── preprocessing.py
│   └── visualisation.py
├── .gitignore
├── README.md
└── requirements.txt

## Fichiers principaux

Fichiers principaux
Src/cleaning.py
Script de nettoyage des données :

standardisation des noms de colonnes ;
nettoyage des valeurs textuelles ;
conversion des variables binaires ;
remplacement de certaines valeurs par des valeurs manquantes ;
suppression des doublons ;
export du fichier nettoyé.
Src/preprocessing.py
Script de prétraitement :

séparation des variables explicatives et de la cible ;
imputation des valeurs manquantes ;
encodage des variables catégorielles ;
standardisation des variables numériques ;
préparation des données pour la modélisation.
Src/visualisation.py
Script de visualisation :

distributions des variables numériques ;
comparaison des variables avec la cible ;
corrélations ;
sauvegarde automatique des figures.
Notebooks/exploration.ipynb
Notebook d’analyse exploratoire :

aperçu du jeu de données ;
statistiques descriptives ;
analyses visuelles ;
premières interprétations.
Jeu de données
Le jeu de données contient notamment les variables suivantes :

age, job, marital, education, default, balance, housing, loan, contact
day, month, duration, campaign, pdays, previous, poutcome, deposit

La variable cible est deposit, qui indique si le client a souscrit au dépôt à terme (yes) ou non (no).

# Installation
        Créer un environnement virtuel puis installer les dépendances :
pip install -r requirements.txt

# Utilisation
1. Nettoyage des données

python Src/cleaning.py
2. Prétraitement

python Src/preprocessing.py
3. Visualisation

python Src/visualisation.py
4. Exploration
Notebooks/exploration.ipynb

Objectif analytique
L’analyse vise à comprendre les caractéristiques des clients les plus susceptibles de souscrire à un dépôt à terme afin d’aider la banque à mieux cibler ses campagnes marketing.

Auteur
Projet d’analyse de données bancaires.
