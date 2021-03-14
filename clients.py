# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:40:51 2021

@author: cmayi
"""
import os,os.path
def erreur():
    print("Erreur dans la saisie")

def form(client,a,b):
    
    client.write(" ")
    client.write("<"+b+">")
    client.write(a)
    client.write("</"+b+">")
    client.write("\n")
def op(client,a) :
    client.write(" ")
    client.write("<"+a+">")
    client.write("\n")
def clo(client,a):
    client.write(" </"+a+">")
    client.write("\n")
def form2(client,valeur,var):
    
    client.write("  ")
    client.write("<"+var+">")
    client.write(valeur)
    client.write("</"+var+">")
    client.write("\n")
def day(mois):
    jour = input("jour : ")
    if(int(mois) in [1,3,5,7,8,10,12]):
        while(int(jour)>31) :
            erreur()
            jour = input("jour : ")
    elif(int(mois) in [4,6,9,11]):
        while(int(jour)>30):
            erreur()
            jour = input("jour : ")
    elif(int(mois) == 2):
        while(int(jour)>29):
            erreur()
            jour = input("jour : ")
    else:
        while(not(jour.isnumeric())) :
          erreur()
          jour = input("jour : ")
    return jour

monthConv ={
    1:"Janvier",
    2:"Février",
    3:"Mars",
    4:"Avril",
    5:"Mai",
    6:"Juin",
    7:"Juillet",
    8:"Août",
    9:"Septembre",
    10:"Octobre",
    11:"Novembre",
    12:"Décembre"
    }
def len_i():
    DIR = 'Clients'
    return len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])


def main():
    i = len_i()  
    rep = "oui"
    while(rep=="oui"):
        save_path = 'Clients'
        file_name = "client"+str(i)+".xml"
        file = os.path.join(save_path,file_name)
        print("Création d'un client.")
        
        nom = input("Veuillez entrer le nom du client : ")
        while(not(nom.isalpha())) :
            erreur()
            nom = input("Veuillez entrer le nom du client : ")
        
        prenom = input("Veuillez entrer le prénom du client : ")
        while(not(prenom.isalpha())) :
            erreur()
            prenom = input("Veuillez entrer le prénom du client : ")
        
        print("Veuillez entrer la date de naissance du client\n")
        mois = input("mois : ")
        while(not(mois.isnumeric()) or int(mois)>12 or int(mois)<1):
            erreur()
            mois = input("mois (en chiffres): ")
        jour = day(mois)
        annee = input("année : ")
        while(not(annee.isnumeric())):
            erreur()
            annee = input("année : ")
        dateNaiss = [jour,monthConv.get(int(mois)),annee]
        
    
        rue = input("Veuillez entrer son adresse : ")
   
    
        ville = input("Veuillez entrer sa ville : ")
        while(not(ville.isalpha())) :
            erreur()
            ville = input("Veuillez entrer la ville du client : ")
    
        CP = input("Veuillez entrer son code postal : ")
        while(not(CP.isnumeric())) :
            erreur()
            CP = input("Veuillez entrer le code postal du client : ")
        adresse = [rue,ville,CP]
        
        catSP = input("Veuillez entrer la catégorie socio-professionnelle du client : ")
        while(not(catSP.isalpha())):
            erreur()
            catSP = input("Veuillez entrer la catégorie socio-professionnelle du client : ")
        
        tel = input("Veuillez renseigner le numéro de téléphone du client : ")
        while(not(tel.isnumeric())):
            erreur()
            tel = input("Veuillez renseigner le numéro de téléphone du client : ")
        
        mail = input("Le client possède t-il une adresse email ? (oui/non) ")
        while((mail!="oui")and(mail!="non")):
            erreur()
            mail = input("Le client possède t-il une adresse email ? (oui/non) ")
        if(mail=="oui"):
            mail = input("Entrez l'adresse mail : ")
        
        carCom = input("Veuillez renseigner la caractéristique commerciale du client (prospect, client, interdit) : ")
        while(carCom not in ["prospect","client","interdit"]):
            erreur()
            carCom = input("Veuillez renseigner la caractéristique commerciale du client (prospect, client, interdit) : ")    
        
        print("Voici le nouveau client")
        print("Nom :",nom ,"Prenom :",prenom ,"Date de Naissance :",dateNaiss)
        print("Catégorie socio-professionnelle : ",catSP , "Adresse : ",adresse ,"Numéro de téléphone :",tel)
        print("Adresse email :",mail ,"Caractéristique commerciale :",carCom)
        client = open(file,"w")
        client.write("<clients>")
        client.write("\n")
        form(client,nom,"nom")
        form(client,prenom,"prenom")
        op(client,"dateNaiss")
        form2(client,jour,"jour")
        form2(client,mois,"mois")
        form2(client,annee,"annee")
        clo(client,"dateNaiss")
        op(client,"adresse")
        form2(client,rue,"rue")
        form2(client,ville,"ville")
        form2(client,CP,"CP")
        clo(client,"adresse")
        form(client,catSP,"catSP")
        form(client,tel,"tel")
        form(client,mail,"mail")
        form(client,carCom,"carCom")
        client.write("</clients>")
        
        client.close()
        rep = input("Voulez-vous entrer un nouveau client ? (oui/non) ")
        while((rep!="oui") and (rep!="non")):
            erreur()
            rep = input("Voulez-vous entrer un nouveau client ? (oui/non)")
        
        
        
    