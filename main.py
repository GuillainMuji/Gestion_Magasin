import produits
from produits import *
import menu
from menu import *
import ventes
from ventes import * 
import rapport 
from rapport import *

def menu_principal():
    print("1. Ajouter produit/supprimer")
    print("2. Afficher produits")
    print("3. Rechercher produit")
    print("4. Enregistrer vente")
    print("5. Afficher les ventes")
    print("6. afficher les Ventes par client")
    print("7. Mettre à jour le stock")
    print("8. verifier le stock")
    print("9. Gererer un rapport de ventes")
    print("0. Quitter")
    return input("Choisissez une option: ")

def main():
    #charger_donnees()
    while True:
        choix = menu_principal()
        if choix == '0':
            print("----------------Merci d'avoir utiliser notre service ---------------------")
            break
        elif choix == '1':
            #affichage_menu()
            sous_choix = affichage_menu()
            if sous_choix == '1':
                print("interface_ajout_produit")
                ajout_produit()
            elif sous_choix == '2':
                #print("suppression d'un produit ")
                while True : 
                    suppression = input("Voullez-vous supprimer un produit ?  oui ou non ! ")
                    suppression = suppression.upper()
                    if suppression != 'OUI' and suppression != 'NON': 
                        print("la reponse doit etre oui ou non ! ")
                    elif suppression == "OUI": 
                        supprimer_produit()
                        break
                        #print("Voullez-vous continuer ! oui /non ")
                    else: 
                        affichage_menu()
        elif choix == '2': 
            print("\nVoici nos differents produits ")
            affichage_produit()
        elif choix == '3' : 
            sous_choix1 = recherche_nom_id()
            if sous_choix1 =='1': 
                recherche_produit_id()
            elif sous_choix1 == '2':
                recherche_produit_nom()
            else : 
                print("erreur touche non valide ! ")
                continue
        elif choix == '4':
            print("Interface des ventes ")
            enregistrement_vente()
        elif choix == '5': 
            affichager_vente()
        elif choix == '6':
            vente_par_client()
        elif choix == '7':
            mise_a_jour_stock()
        elif choix == '8':
            sous_choix2 = verifier_stock()
            if sous_choix2 == '1':
                verification_stock_id()
            elif sous_choix2 == '2':
                print("_________Voici-les informations relatives au stock du produit:_________________")
                verification_stock_nomprod()
        elif choix == '9':
            sous_choix3 = rapport_ventes_1()
            if sous_choix3 =='1':
                    historique_produit()
            elif sous_choix3 =='2':
                recherche_par_plage_prix()
            elif sous_choix3 == '3':
                rapport_ventes
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
