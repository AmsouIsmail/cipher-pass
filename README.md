# 🔐 Cipher PWD - Chiffrement et Déchiffrement de Fichiers

## 📌 Description
**Cipher PWD** est un script Python permettant de **chiffrer et déchiffrer** le contenu d'un fichier texte en utilisant **AES (Advanced Encryption Standard) en mode CBC**.  
Le chiffrement protège le fichier en remplaçant son contenu par une version sécurisée, accessible uniquement avec le bon mot de passe.

## 🚀 Fonctionnalités
- 🔑 **Chiffrement sécurisé** avec AES-128 CBC.
- 🔓 **Déchiffrement** du fichier avec la même clé.
- ⚠️ **Vérification du mot de passe** (détecte les erreurs de déchiffrement).
- ⏳ **Auto-chiffrement après 30 secondes** pour protéger les données.

## 🛠️ Installation
1. Installer les dépendances nécessaires :  
   ```bash
   pip install pycryptodome
   python -m pip install pycryptodome

## Télécharger ou cloner ce dépôt :
git clone https://github.com/AmsouIsmail/cipher-pwd.git
cd cipher-pwd

📜 Utilisation
Exécuter le script :
    python cipher_passe_word.py
    
## Suivre les instructions :
.Choisir 1 pour chiffrer un fichier.
.Choisir 2 pour déchiffrer un fichier.
.Entrer le chemin du fichier à protéger.
.Saisir un mot de passe.

⚠️ Remarque
Si le mot de passe est incorrect lors du déchiffrement, un message d'erreur s'affiche et le programme s'arrête.
Après déchiffrement, le fichier est automatiquement rechiffré après 30 secondes pour éviter tout risque d'accès non autorisé.
