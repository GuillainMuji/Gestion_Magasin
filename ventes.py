import json
import produits 
from produits import *
import datetime

def charger_vente():
    try :
        fichier = 'ventes.json'
        with open(fichier, 'r') as file:
            ventes = json.load(file)
    except FileNotFoundError :
        ventes = []
    return ventes

def savegarder_ventes(ventes):
    fichier = 'ventes.json'
    with open(fichier, 'w') as file:
        json.dump(ventes, file, indent=4)

def enregistrement_vente():
    produits = charger_produit()
    ventes = charger_vente()
    client = input("Entrez le nom du client : ")
    client= client.upper()
    nom_produit = input("Entrez le nom de produit :")
    nom_produit = nom_produit.upper()
    quantite = int(input("Entrez la quantite :"))
    date =datetime.datetime.now().date().isoformat()
    produit_trouve = False
    for produit in produits: 
        if produit['nom'] == nom_produit:
            if produit['quantite'] >= quantite :
                produit['quantite'] -=quantite
                facture = produit['prix'] * quantite
                vente = {'client': client, 'quantite' : quantite, 'produit':nom_produit, 'facturation': facture, 'date':date }
                ventes.append(vente)
                savegarder_produit(produits)
                savegarder_ventes(ventes)
                print("vente effectue avec succes")
                produit_trouve = True  
                break
    if not produit_trouve : 
        print("Pas de correspondance d'articles")
#enregistrement_vente()

def affichager_vente():
    with open("ventes.json", 'r') as fichier :
        ventes = json.load(fichier)
    if not ventes: 
        print("aucune vente n'a été enregistée")
    for vente in ventes : 
        #print(f"client:{vente['client']}, produit : {vente['produit']}, quantite : {vente['quantite']} date {vente['date']},")

        print("============ voici les informations sur la ventes ==============")
        print(f"client {vente['client']}, nom_produit : {vente['produit']}, Quantite : {vente['quantite']} \nDate {vente['date']}, facturation: {vente['facturation']} $ ")
        print("=================================================")
#enregistrement_vente()


#vente par client 
def vente_par_client():
    with open("ventes.json", 'r') as fichier :
        ventes = json.load(fichier)
    client = input("Entrez le nom client : ")
    client = client.upper()
    vente_trouve = False 
    for vente in ventes : 
        if vente['client'] == client : 
            print(f"Releves de facture : {vente['client']}. \nQuantite : {vente['quantite']}. \nNom_produit : {vente['produit']}\nDate : {vente['date']}, \nFacture:{vente['facturation']} $")
            vente_trouve = True 
            break
    if not vente_trouve : 
        print(f"{client} n'a pas effectuer la vente chez MyGool")




