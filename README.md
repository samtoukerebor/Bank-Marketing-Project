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

## Installation
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
