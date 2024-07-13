import json
import datetime


def charger_produit():
    try :
        fichier = 'Produits.json'
        with open(fichier, 'r') as file:
            produits = json.load(file)
    except FileNotFoundError :
        produits = []
    return produits

def savegarder_produit(produits):
    fichier = 'Produits.json'
    with open(fichier, 'w') as file:
        json.dump(produits, file, indent=4)

def ajout_produit():
    
    produits = charger_produit()
    while True:
        nomProd = input("Entrez nom de produit : ")
        nomProd = nomProd.upper()
        if nomProd.isalpha():
            break
        else:
            print("Erreur ! le nom doit-etre en lettre ")

    #verification du produit si il existe dans la base de donne 
    for produit in produits :
        if produit['nom'] == nomProd:
            print('nom produit existant !')
            return
    while True: 
        PrixProd = input("Entrez le Prix de Produit : ")
        if PrixProd.isdigit():
            break
        else : 
            print("Erreur ! veuillez taper un entier ")

    while True: 
        QteProd = input("Entrez la quanité de produit : ")
        if QteProd.isnumeric():
            break
        else : 
            print('erreur ! taper un nombre !')
    idProd = len(produits) + 1
    date =datetime.datetime.now().date().isoformat()
    time =datetime.datetime.now().time().strftime('%H:%M:%S')
    
        
    produit = {'idProd': idProd, 'nom':nomProd, 'prix':int(PrixProd), 'quantite':int(QteProd),'date': date, 'heure': time}

    produits.append(produit)
    
    savegarder_produit(produits)
    print("produit ajouter avec succes !")

# histotique de produit 
def historique_produit():
    with open("produits.json", 'r') as fichier :
        produits = json.load(fichier) 
    for produit in produits : 
        print("=================Voici l'historique de chaque produit================================")
        print(f"Id_Prod : {produit['idProd']}, Nom : {produit['nom']},\nprix : {produit['prix']}FC, Quantite : {produit['quantite']},\ndate_de_mise_a_jour: {produit['date']}, heure : {produit['heure']}")
        print("=================================================")


#affichage produit 
def affichage_produit():
    with open("produits.json", 'r') as fichier :
        produits = json.load(fichier)
    for produit in produits : 
        print("=================================================")
        print(f"Id_Prod : {produit['idProd']}, Nom : {produit['nom']},\nprix : {produit['prix']}FC, Quantite : {produit['quantite']}")
        print("=================================================")

def recherche_par_plage_prix():
    produits = charger_produit()
    filtrage = int(input("Entrez le prix à filtrer : "))
    filtra_trouve = False
    for produit in produits:
        if filtrage <= produit['prix'] and filtrage >= produit['prix']:
            print(f"Id_Prod : {produit['idProd']}, Nom : {produit['nom']},\nprix : {produit['prix']}FC, Quantite : {produit['quantite']}")
            filtra_trouve = True
                        
    if not filtra_trouve :
        print("pas de filtrage pour ce prix !")   

#alerte le produit en rupture de stock
def alerte_produit():
    produits = charger_produit()
    alerte_trouve = False
    for produit in produits:
        
        if produit['quantite']==0:
            print(f"{produit['nom']},Code_Prod : {produit['idProd']} \nQuantite {produit['quantite']}, En rupture de stock!!!")
            alerte_trouve = True
    if not alerte_trouve : 
        print("pas d'article en rupture de stock")


#recherche_par_plage_prix()
#ajout_produit()

#recherche produit par nom 
def recherche_produit_nom():
    with open("produits.json", 'r') as fichier :
        produits = json.load(fichier)
    nom_article = input("Entrez le nom du produit à rechercher : ")
    nom_article = nom_article.upper()
    produit_trouve = False
    for produit in produits : 
        if produit['nom'] == nom_article :
            print(f"Voici les informations de produit {nom_article}") 
            print(f"Id_Prod : {produit['idProd']}, Nom : {produit['nom']},\nprix : {produit['prix']}, Quantite : {produit['quantite']}")
            produit_trouve = True
    if not produit_trouve :
        print("Produit inexistant ! ")
#fichier_produit = 'Produits.json'



def recherche_produit_id():
    with open("produits.json", 'r') as fichier :
        produits = json.load(fichier)

    while True : 
        id_produit = input("Entrez id_produit à rechercher : ")
        if id_produit.isdigit(): 
            break
        else : 
            print("erreur l'id doit etre un entier ")
    id_produit = int(id_produit)
    produit_trouve = False
    for produit in produits : 
        if produit['idProd'] == id_produit :
            print(f"Voici les informations de produit {produit['nom']}") 
            print(f"Id_Prod : {produit['idProd']}, Nom : {produit['nom']},\nprix : {produit['prix']}, Quantite : {produit['quantite']}")
            produit_trouve = True
            break
    if not produit_trouve :
        print("id_inexistant ")

def supprimer_produit():
    produits = charger_produit()
    nom = input("Entrez le nom du produit à supprimer : ")
    nom = nom.upper()
    produit_trouve = False
    for produit in produits: 
        if produit['nom'] == nom : 
            produits.remove(produit)
            savegarder_produit(produits)
            print("Produit supprimer avec succes ")
            produit_trouve = True
            break 
    if not produit_trouve :
        print("Produit inexistant  ")




def mise_a_jour_stock():
    with open("produits.json", 'r') as fichier :
        produits = json.load(fichier)

    while True : 
        nom_produit = input("Entrez nom_produit à mettre à jour : ")
        nom_produit= nom_produit.upper()
        if nom_produit.isalpha():  
            break
        else : 
            print("erreur sur le nom doit etre un entier ")
    produit_trouve = False
    for produit in produits : 
        if produit['nom'] == nom_produit :
            while True : 
                quantite = input("saisir la quantite : ")
                if quantite.isnumeric():
                    break
                else: 
                    print("saisir une valeur correcte ! ")
            produits.remove(produit)
            produit['quantite'] +=int(quantite)
            produits.append(produit)
            savegarder_produit(produits)
            print("mise à jour effecuté avec succes")
            produit_trouve = True
            
            break
    if not produit_trouve :
        print("pas d'article pour ce nom_inexistant ")

# verification du stock par idprod
def verification_stock_id():
    with open("produits.json", 'r') as fichier :
        produits = json.load(fichier)
    
    while True : 
        idProd = input("Entrez l'id du produit :")
        
        if idProd.isdigit():
            break
        else: 
            print("erreur id doit_etre un chiffre ! ")
    id_trouve = False
    for produit in produits : 
        if produit['idProd'] == int(idProd) : 
            print(f"Id_Prod : {produit['idProd']}, Nom_Produit : {produit['nom']},\nprixUnit : {produit['prix']}$, Qte_Stock : {produit['quantite']} \n")
            id_trouve = True
            break
    if not id_trouve : 
        print("pas de stock pour cet_Id")


# verification du stock par nomprod
def verification_stock_nomprod():
    with open("produits.json", 'r') as fichier :
        produits = json.load(fichier)
    
    while True : 
        nomprod = input("Entrez nom produit :")
        nomprod = nomprod.upper()
        if nomprod.isalpha():
            break
        else: 
            print("erreur nom produit doit être un entier ! ")
    id_trouve = False
    for produit in produits : 
        if produit['nom'] == nomprod : 
            print(f"Id_Prod : {produit['idProd']}, Nom_Produit : {produit['nom']},\nprixUnit : {produit['prix']}$, Qte_Stock : {produit['quantite']} \n")
            id_trouve = True
            break
    if not id_trouve : 
        print("pas de stock pour pour ce produit")
