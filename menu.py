import produits
from produits import supprimer_produit

def affichage_menu():
    print("1. Ajouter un produiit.")
    print("2. Supprimer Produit.")

    return input("Choisir une Option : ")

#affichage_menu()

def recherche_nom_id():
    print("1. Rechercher un produit par id_produit.")
    print("2. Rechercher un produit par nom_produit. ")

    return input("Choisir une option : ")

def verifier_stock():
    print("1. verifier stock par idProduit.")
    print("2. Verifier stock par nomProduit. ")

    return input("Choisir une option : ")

def rapport_vente():
    print("1.Gestion de produits et du stock.")
    print("2.Gestiond de ventes et des commandes.")
    print("3.Analyse et rapports.")

    return input("choisir une Option : ")

def rapport_ventes_1():
    print("\n________________Voici l'interface de produits et du Stock____________________")
    print("1.Historique des modifications de stoock.")
    print("2.Recherche par plage de prix.")
    print("3.Alerte de produit en rupture de stock.")
    print("4.Produits les moins vendus.")
    print("5.Gestion des stock multi_enmplacement.")
    print("6.Suivi des avis clients.")
    print("7.Gestion des remises et des promotions.")

    return input("choisir une Option : ")