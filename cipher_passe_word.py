#cipher passe word
#pour proteger votre pwd.txt par un seul mot de pass

#pip install pycryptodome
#or
#python -m pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64
from time import sleep
from sys import exit

#pour verifier le choix d'utilisateur
def choix() :
    userchoix = int(input("1.chiffrement \t 2.dechiffrement : "))
    if userchoix!=1 and userchoix!=2 :
        print("\n❌ choix incorrect!!!\n")
        return choix()
    else :
        return userchoix


#pour avoir le chemain de fichier et de verifier ce chemain avec svg le contenu de fichier
def filecheck() :
    while True :
        try:
            chemain = input("\nchemain du fichier : ")
            with open(chemain , "r") as file:
                message = list(file.read())
            return message,chemain
        except FileNotFoundError :
            print("\n❌ Chemin incorrect. Veuillez réessayer.")


#avoir chaque line de fichier dans un liste
def listemessage(message):
    x = ''
    messageliste = []
    for i in message:
        if i != "\n":  # Si le caractère n'est pas un saut de ligne, on l'ajoute à 'x'
            x += str(i)
        else:  # Lorsque c'est un saut de ligne, on ajoute la chaîne formée à la liste
            messageliste.append(x)
            x = ''  # Réinitialiser 'x' pour commencer une nouvelle ligne

    # Ajouter le dernier élément s'il n'a pas été ajouté (dans le cas où il n'y a pas de saut de ligne à la fin)
    
    if x: # x n'est pas vide
        messageliste.append(x)

    return messageliste



def chiffrement(messageliste,key) :
    chif_aes = AES.new(key,AES.MODE_CBC) # Créer un objet AES avec la clé et le mode cbc
    liste_chiffrement = []
    for i in messageliste :
            message_pad = pad(i.encode(),AES.block_size)    # Ajouter du padding au message
            chif = chif_aes.encrypt(message_pad)    # Chiffrement du message
            message_chif_base64 = base64.b64encode(chif_aes.iv + chif).decode() #le message chiffré avec le vecteur initiale pour pouvoir déchiffrer plus tard
            liste_chiffrement.append(message_chif_base64)
    return liste_chiffrement


def dechiffrement(messageliste, key):
    liste_dechiffrement = []

    message_chif_byte = base64.b64decode(messageliste[0])  # Décoder le message chiffré
    iv = message_chif_byte[:AES.block_size]  # Extraire le vecteur d'initialisation (IV)
    dechif_aes = AES.new(key, AES.MODE_CBC, iv)  # Créer un objet AES pour le déchiffrement avec l'IV
    for i in messageliste:
        try:
            message_chif_byte = base64.b64decode(i)  # Décoder le message chiffré
            message_chif = message_chif_byte[AES.block_size:]  # Extraire le message chiffré
            dechif = unpad(dechif_aes.decrypt(message_chif), AES.block_size).decode()  # Retirer le padding
            liste_dechiffrement.append(dechif)
        except (ValueError,KeyError) :  # Capture l'erreur de padding ou autre erreur liée au chiffrement
            print("\n❌ Mot de passe incorrect. Veuillez réessayer.")
            return None

    return liste_dechiffrement




userchoix = choix() 
message,chemain =  filecheck()
messageliste = listemessage(message)
userkey = input("\nsaisir votre mot de passe : ")
key = hashlib.sha256(userkey.encode()).digest()[:16] # eviter le problem de taille de cle je le hash et sous forme d'octets (avec digest option de hashlib) et prendre 16 1er

if userchoix == 1 :
    message_chiffrer = []
    message_chiffrer = chiffrement(messageliste,key)
    with open(chemain,"w", encoding="utf-8") as fichier : # Ouvrir le fichier en mode écriture ("w" supprime le contenu existant)
        for msg in message_chiffrer :
            fichier.write(msg + "\n")
    print("\n✔️ le fichier a ete chiffrer en succes !!!")
else :
    message_dechiffrer = []
    message_dechiffrer = dechiffrement(messageliste,key)

    # if il y a un erreur soit mot de passe incorrect soit simple erreur de dechiffrement il return les ancien ligne de fichier
    if message_dechiffrer == None :
        with open(chemain,"w", encoding="utf-8") as fichier : # Ouvrir le fichier en mode écriture ("w" supprime le contenu existant)
            for msg in messageliste :
                fichier.write(msg + "\n")
            exit()

    with open(chemain,"w", encoding="utf-8") as fichier : # Ouvrir le fichier en mode écriture ("w" supprime le contenu existant)
        for msg in message_dechiffrer :
            fichier.write(msg + "\n")
    print("\n✔️ le fichier a ete dechiffrer en succes !!!")

    for i in range(30, -1,-1):
        print(f"\r⏳ Il va être chiffré pendant {i} secondes ", end="")
        sleep(1) 

    message_chiffrer = []
    message_chiffrer = chiffrement(message_dechiffrer,key)
    with open(chemain,"w", encoding="utf-8") as fichier : # Ouvrir le fichier en mode écriture ("w" supprime le contenu existant)
        for msg in message_chiffrer :
            fichier.write(msg + "\n")
    print("\n✔️ le fichier a ete chiffrer en succes !!!")
