import json
import produits
import ventes

from produits import *
from ventes import *


def rapport_ventes():
    with open("ventes.json", 'r') as fichier :
            ventes = json.load(fichier)
    if not ventes: 
        print("rapport enregistre")
    for vente in ventes : 
        #print(f"client:{vente['client']}, produit : {vente['produit']}, quantite : {vente['quantite']} date {vente['date']},")

        print("============ Voici les rapports de ventes ==============")
        print(f"Client: {vente['client']}, nom_produit : {vente['produit']}, \nQuantite : {vente['quantite']}, facturation: {vente['facturation']}$. \nDate :{vente['date']} ")
        print("========================================================")
