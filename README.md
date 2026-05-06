# ⚛️ Simulateur de Pile ou Face Quantique

Application web qui simule un **lancer de pièce quantique** grâce à la superposition quantique (porte Hadamard).

---

## Ce que fait l'application

1. Une pièce animée tourne pendant 2 secondes le temps de la simulation
2. La pièce s'arrête et affiche **PILE** ou **FACE** selon le résultat majoritaire
3. Affiche le nombre de `0` (Pile) et de `1` (Face) obtenus
4. Affiche un graphique en barres avec la distribution des résultats
5. Vous pouvez choisir librement le nombre d'essais (entre 1 et 1 000)

---

## Lancer l'application

### Étape 1 — Installer Python

1. Téléchargez Python sur **https://www.python.org/downloads/windows/**
2. Lancez l'installateur
3. **Important** : cochez la case **"Add python.exe to PATH"** avant d'installer
4. Répondez **Y** à toutes les questions posées pendant l'installation

### Étape 2 — Installer les dépendances

Ouvrez un terminal PowerShell dans le dossier du projet et exécutez :

```
pip install -r requirements.txt
```

> L'installation prend 2 à 5 minutes.

### Étape 3 — Configurer Streamlit (une seule fois)

Créez le fichier `C:\Users\<votre-nom>\.streamlit\credentials.toml` avec ce contenu :

```toml
[general]
email = ""
```

Cela évite la question d'email au démarrage.

### Étape 4 — Démarrer l'application

```
python -m streamlit run app.py
```

L'application s'ouvre automatiquement dans votre navigateur à l'adresse :
**http://localhost:6000**

---

## Structure du projet

```
Pileface/
├── app.py            # Application principale Streamlit
├── requirements.txt  # Dépendances Python
└── README.md         # Ce fichier
```

---

## Technologies utilisées

### Python
Langage de programmation principal du projet. Simple, lisible, et très utilisé en science et en informatique quantique.

### Streamlit
Framework Python qui permet de créer des applications web interactives sans écrire de HTML ou de JavaScript. Idéal pour des projets de data science et de visualisation.

### Qiskit
Bibliothèque open source développée par IBM pour programmer des ordinateurs quantiques. Elle permet de construire des circuits quantiques, d'appliquer des portes logiques quantiques et de les exécuter sur un simulateur ou un vrai ordinateur quantique.

### Qiskit Aer
Simulateur quantique local fourni avec Qiskit. Il reproduit le comportement d'un ordinateur quantique sur votre propre machine, sans avoir besoin de connexion internet ni d'accès à un vrai quantum computer.

### Matplotlib
Bibliothèque Python de visualisation de données. Utilisée ici pour générer le graphique en barres qui affiche la distribution des résultats Pile / Face.

---

## Concepts quantiques abordés

- **Qubit** : unité d'information quantique pouvant être 0, 1 ou les deux simultanément
- **Superposition** : état où le qubit n'est ni 0 ni 1 avant la mesure
- **Porte Hadamard (H)** : crée une superposition parfaite 50/50
- **Mesure** : effondrement de la superposition vers 0 ou 1 de façon aléatoire

---
