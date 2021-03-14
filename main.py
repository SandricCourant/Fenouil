# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:51:16 2021

@author: cmayi
"""
import clients,articles

def erreur():
    print("Erreur dans la saisie")

print("Bienvenue dans le système de saisie FENOUIL.")
rep=str(None)
while(rep!="q"):
    print("Que voulez-vous faire ?")
    rep = input("Entrer un client (c)|Entrer un article (a)|Statistiques (h)|Quitter (q) :")
    while((rep!="c")and(rep!="a")and(rep!="q")and(rep!="h")):
            erreur()
            rep = input("Entrer un client (c)|Entrer un article (a)|Statistiques (h)|Quitter (q) :")
    if(rep=="c") :
        clients.main()
    elif(rep=="a"):
        articles.main()
    elif(rep=="q"):
        print("A bientôt !")
    elif(rep=="h"):
        print("Il y a actuellement",clients.len_i(),"clients et",articles.len_i(),"articles enregistrés dans la base de données.")