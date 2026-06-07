# BMS — Battery Management System Monitor

Serveur web Flask pour la surveillance en temps réel d'un pack de batteries Li-ion 3S. Les données sont collectées par une carte Arduino via un Raspberry Pi, puis envoyées au serveur et stockées dans une base de données SQLite.

---

## Architecture du système

```
Arduino (capteurs)
      |
      | UART (série 9600 baud)
      v
Raspberry Pi  ──── bmss/ard.py ────► HTTP GET /insertMesures
                                            |
                                     Serveur Flask (main.py)
                                            |
                                      SQLite (measurements.db)
                                            |
                              ┌─────────────┴─────────────┐
                              v                           v
                        Dashboard (/)              Historique (/history)
```

---

## Structure du projet

```
server/
├── main.py              # Point d'entrée Flask — définit les routes
├── database.py          # ORM SQLAlchemy — modèle et accès à la BDD
├── config.py            # Configuration : port, seuils de tension/courant/température
├── dashboard_html.py    # Génération HTML du tableau de bord temps réel
├── history_html.py      # Génération HTML de la page historique
├── htmlParser.py        # Fonctions utilitaires de mise en couleur des valeurs
├── requirements.txt     # Dépendances Python
├── static/
│   ├── style.css        # Feuille de style du tableau de bord
│   └── img/             # Icônes (batterie, ampèremètre, thermomètre, volt)
└── bmss/
    ├── ard.py           # Script Raspberry Pi : lecture Arduino → envoi au serveur
    └── data.py          # (variante du module BDD)
```

---

## Mesures surveillées

| Paramètre | Description | Unité |
|-----------|-------------|-------|
| `voltage1` | Tension cellule 1 | V |
| `voltage2` | Tension cellule 2 | V |
| `voltage3` | Tension cellule 3 | V |
| `current` | Courant de charge/décharge | mA |
| `temperature` | Température du pack | °C |
| `soc` | State of Charge (niveau de charge) | % |
| `soh` | State of Health (état de santé) | % |

Seuils configurés dans `config.py` :
- Tension cellule : 2.7 V – 4.2 V
- Tension totale : 8.1 V – 12.6 V
- Courant : 10 mA – 110 mA
- Température : -20 °C – 62 °C

---

## Installation

### Prérequis
- Python 3.8+
- pip

### Étapes

```bash
# Cloner le dépôt
git clone https://github.com/jaw266/BMS.git
cd BMS

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur
python main.py
```

Le serveur démarre sur **http://0.0.0.0:3000** (accessible depuis tout le réseau local).

---

## Routes de l'API

### `GET /`
Tableau de bord principal — affiche la dernière mesure enregistrée. La page se rafraîchit automatiquement toutes les 10 secondes.

### `GET /history`
Historique de toutes les mesures. Filtrage par plage de dates possible via les paramètres :
- `DateDebut` — date de début (format `YYYY-MM-DDTHH:MM`)
- `DateFin` — date de fin (format `YYYY-MM-DDTHH:MM`)

Exemple :
```
/history?DateDebut=2024-01-01T00:00&DateFin=2024-01-31T23:59
```

### `GET /insertMesures`
Endpoint d'insertion des données (appelé par le Raspberry Pi).

Paramètres obligatoires :
```
/insertMesures?voltage1=3.9&voltage2=3.8&voltage3=4.0&current=25&temperature=30&soc=85&soh=95
```

Retourne `OK` si l'insertion réussit.

---

## Script Raspberry Pi (`bmss/ard.py`)

Le script tourne en continu sur le Raspberry Pi. Il lit les données envoyées par l'Arduino via le port série (UART), calcule le SOC, puis envoie les mesures au serveur Flask toutes les 60 secondes.

Format de trame Arduino attendu (séparateur `/`) :
```
voltage1/voltage2/voltage3/temperature/current/soh
```

Configuration à adapter dans `bmss/ard.py` :
- `url` : adresse IP du serveur Flask
- `device` : port série de l'Arduino (`/dev/ttyACM0` par défaut)

---

## Configuration (`config.py`)

```python
PORT = 3000       # Port du serveur
HOST = '0.0.0.0'  # Écoute sur toutes les interfaces réseau
DEBUG = True      # Mode debug Flask (désactiver en production)

DATABASE_URL = 'sqlite:///measurements.db'
```

---

## Technologies utilisées

- **Flask** — serveur web Python
- **SQLAlchemy** — ORM pour la base de données SQLite
- **PySerial** — communication série avec l'Arduino (côté Raspberry Pi)
- **RPi.GPIO** — lecture GPIO Raspberry Pi
