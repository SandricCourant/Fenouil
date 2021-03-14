# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:18:58 2021

@author: cmayi
"""
import os,os.path
def erreur():
    print("Erreur dans la saisie")

def form(article,a,b):
    
    article.write(" ")
    article.write("<"+b+">")
    article.write(a)
    article.write("</"+b+">")
    article.write("\n")
def len_i():
    DIR = 'Articles'
    return len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

def main():
    i = len_i()
    rep ="oui"
    while(rep=="oui"):
        save_path = 'Articles'
        file_name = "article"+str(i)+".xml"
        file = os.path.join(save_path,file_name)
        print("Création d'un article.")
    
        
        numero = input("Entrez le numéro unique de l'article : ")
        while(not(numero.isnumeric())):
            erreur()
            numero = input("Entrez le numéro unique de l'article : ")
        
        designation = input("Entrez la désignation de l'article : ")
        
        prix = input("Entrez le prix de l'article (en euros) : ")
        while(not(prix.isnumeric())):
            erreur()
            prix = input("Entrez le prix de l'article (en euros) : ")
        
        print("Voici le nouvel article")
        print("Article numéro",numero , "Désignation :",designation ,"Prix :",prix)
        article = open(file,"w")
        article.write("<article>\n")
        form(article,numero,"numero")
        form(article,designation,"designation")
        form(article,prix,"prix")
        article.write("</article>\n")
        article.close()
        rep = input("Voulez-vous entrer un nouvel article ? (oui/non) ")
        while((rep!="oui")and(rep!="non")):
            erreur()
            rep = input("Voulez-vous entrer un nouvel article ? (oui/non) ")
        
       
        
    