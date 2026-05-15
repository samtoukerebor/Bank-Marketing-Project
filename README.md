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

- `Src/cleaning.py` : nettoyage des données.
- `Src/preprocessing.py` : préparation des données pour l’analyse ou la modélisation.
- `Src/visualisation.py` : génération des graphiques et analyses visuelles.
- `Notebooks/exploration.ipynb` : exploration des données et interprétations.
