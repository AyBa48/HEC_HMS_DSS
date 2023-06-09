# -*- coding: cp1252 -*-
#............Programme de cr�ation de fichier de donn�es....... #
#............Par lintermediaire d'une interface graphique.......#
#............Ayouba Hasseye Badou-ayoubah@gmail.com........#
#............LASH-EMI....................#
#.............19 juin 2012...............#

import Tkinter as tk
import os
import sys
import tkFont

class tkinterTuto(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Gestion des donn�es d'entr�e")
        self.master.columnconfigure(0, weight=0)
        self.master.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=0)
        self.rowconfigure(0, weight=0)
        self.grid(sticky="NSEW")
        self.createWidgets()
        
        
        
        
    def createWidgets(self):
#..............creation des objets variables.............#
       self.valeurOneVar = tk.StringVar()
       self.valeurOneVar.set("Ecrivez ici")
       self.valeurtoVar = tk.StringVar()
       self.valeurtoVar.set("Ecrivez ici")
       self.valeurtreVar = tk.StringVar()
       self.valeurtreVar.set("Ecrivez ici")
       self.valeurforVar = tk.StringVar()
       self.valeurforVar.set("Ecrivez ici")
       self.valeurfiveVar = tk.StringVar()
       self.valeurfiveVar.set("Ecrivez ici")
       self.valeursixVar = tk.StringVar()
       self.valeursixVar.set("Ecrivez ici")
       self.valeursevVar = tk.StringVar()
       self.valeursevVar.set("Ecrivez ici")
       self.valeureigVar = tk.StringVar()
       self.valeureigVar.set("Ecrivez ici")
       self.valeurnineVar = tk.StringVar()
       self.valeurnineVar.set("Ecrivez ici")
       self.valeurtenVar = tk.StringVar()
       self.valeurtenVar.set("Ecrivez ici")
       self.valeurelevVar = tk.StringVar()
       self.valeurelevVar.set("Ecrivez ici")
       self.valeurtweVar = tk.StringVar()
       self.valeurtweVar.set("Ecrivez ici")
       self.valeurtherVar = tk.StringVar()
       self.valeurtherVar.set("Ecrivez ici")
#...........creation des widgets...........#
       mainFrame = tk.Frame(self, borderwidth=1, relief="ridge", bg = 'black')
       valeurOneLabel = tk.Label(mainFrame, text="Nom du dossier contenant les donn�es:",  width =38, bg = 'darkgray', fg = 'blue')
       valeurOneEntry = tk.Entry(mainFrame, textvariable=self.valeurOneVar, width = 38)
       valeurtoLabel = tk.Label(mainFrame, text="Nom du dossier de destination des scenarios:", width =38, bg = 'darkgray', fg = 'blue')
       valeurtoEntry = tk.Entry(mainFrame, textvariable=self.valeurtoVar, width = 38)
       valeurtreLabel = tk.Label(mainFrame, text="Nom de la 1ere station:",  bg = 'darkgray', width =38, fg = 'blue')
       valeurtreEntry = tk.Entry(mainFrame, textvariable=self.valeurtreVar, width = 38)
       valeurforLabel = tk.Label(mainFrame, text="Longitude de  la station:",  bg = 'darkgray', width =38, fg = 'blue')
       valeurforEntry = tk.Entry(mainFrame, textvariable=self.valeurforVar, width = 38)
       valeurfiveLabel = tk.Label(mainFrame, text="Latitude de  la station:", bg= 'darkgray',  width =38,fg = 'blue')
       valeurfiveEntry = tk.Entry(mainFrame, textvariable=self.valeurfiveVar, width = 38)
       valeursixLabel = tk.Label(mainFrame, text="Nom de la 2eme station:", bg= 'darkgray', width =38, fg = 'blue')
       valeursixEntry = tk.Entry(mainFrame, textvariable=self.valeursixVar, width = 38)
       valeursevLabel = tk.Label(mainFrame, text="Longitude de  la station:", bg= 'darkgray', width =38, fg = 'blue')
       valeursevEntry = tk.Entry(mainFrame, textvariable=self.valeursevVar, width = 38)
       valeureigLabel = tk.Label(mainFrame, text="Latitude de la station:", bg= 'darkgray', width =38, fg = 'blue')
       valeureigEntry = tk.Entry(mainFrame, textvariable=self.valeureigVar, width = 38)
       valeurnineLabel = tk.Label(mainFrame, text="Entrer l\'ann�e de simulation:", bg= 'darkgray', width =38, fg = 'blue')
       valeurnineEntry = tk.Entry(mainFrame, textvariable=self.valeurnineVar, width = 38)
       valeurtenLabel = tk.Label(mainFrame, text="Entrer le mois de simulation:", bg= 'darkgray', width =38, fg = 'blue')
       valeurtenEntry = tk.Entry(mainFrame, textvariable=self.valeurtenVar, width = 38)
       valeurelevLabel = tk.Label(mainFrame, text="Entrer le nombre de jour � simuler:", bg= 'darkgray', width =38, fg = 'blue')
       valeurelevEntry = tk.Entry(mainFrame, textvariable=self.valeurelevVar, width = 38)
       valeurtweLabel = tk.Label(mainFrame, text="Entrer le pas de temps:", bg= 'darkgray', width =38, fg = 'blue')
       valeurtweEntry = tk.Entry(mainFrame, textvariable=self.valeurtweVar, width = 38)
       valeurtherLabel = tk.Label(mainFrame, text="Entrer la precision souhait�e:", bg= 'darkgray', width =38, fg = 'blue')
       valeurtherEntry = tk.Entry(mainFrame, textvariable=self.valeurtherVar, width = 38)
       button = tk.Button(mainFrame, text="Calculer", command=self.RecupererValeurs, bg ='white')       
       button3= tk.Button(mainFrame, text="Demarrer HEC-DSSvue", command=self.demarrer, bg ='white')
       button2 = tk.Button(mainFrame, text="Quitter", command=self.master.destroy, bg ='white')
#...............Position des widgets...................#
       mainFrame.grid(column=0, row=0, sticky="NSEW")
       valeurOneEntry.grid(column=1, row=0, sticky="E", )
       valeurOneLabel.grid(column =0, row =0, sticky = "S", pady =3)
       valeurtoEntry.grid(column=1, row=1, sticky="E")
       valeurtoLabel.grid(column =0, row =1, sticky = "SW", pady =3)
       valeurtreEntry.grid(column=1, row=2, sticky="SW")
       valeurtreLabel.grid(column =0, row =2, sticky = "W", pady =3)
       valeurforEntry.grid(column=1, row=3, sticky="W")
       valeurforLabel.grid(column =0, row =3, sticky = "W", pady =3)
       valeurfiveEntry.grid(column=1, row=4, sticky="W")
       valeurfiveLabel.grid(column =0, row =4, sticky = "W", pady =3)
       valeursixLabel.grid(column =0, row =5, sticky = "W", pady =3)
       valeursixEntry.grid(column=1, row=5, sticky="W")
       valeursevLabel.grid(column =0, row =6,  sticky = "W", pady =3)
       valeursevEntry.grid(column=1, row=6, sticky="W")
       valeureigLabel.grid(column =0, row =7, sticky = "W", pady =3)
       valeureigEntry.grid(column=1, row=7, sticky="W")
       valeurnineLabel.grid(column =0, row =8, sticky = "W", pady =3)
       valeurnineEntry.grid(column=1, row=8, sticky="W")
       valeurtenLabel.grid(column =0, row =9, sticky = "W", pady =3)
       valeurtenEntry.grid(column=1, row=9, sticky="W")
       valeurelevLabel.grid(column =0, row =10, sticky = "W", pady =3)
       valeurelevEntry.grid(column=1, row=10, sticky="W")
       valeurtweLabel.grid(column =0, row =11, sticky = "W", pady =3)
       valeurtweEntry.grid(column=1, row=11, sticky="W")
       valeurtherLabel.grid(column =0, row =12, sticky = "W", pady =3)
       valeurtherEntry.grid(column=1, row=12, sticky="W")
       button.grid(column=0, columnspan=2, row=13, sticky="NSEW", pady =2)
       button2.grid(column=0, columnspan=2, row= 15, sticky="NSEW", pady =2)
       button3.grid(column=0, columnspan=2, row = 14, sticky = "NSEW", pady =2)
    def RecupererValeurs(self):
        nom_dos =self.valeurOneVar.get()
        nom_destina =self.valeurtoVar.get()
        nstat=self.valeurtreVar.get()
        longit=self.valeurforVar.get()
        lat=self.valeurfiveVar.get()
        mstat=self.valeursixVar.get()
        longitud=self.valeursevVar.get()
        latitud=self.valeureigVar.get()
        Annee=self.valeurnineVar.get()
        Mois=self.valeurtenVar.get()
        nj=self.valeurelevVar.get()
        Pas=self.valeurtweVar.get()
        a=self.valeurtherVar.get()
        os.chdir("C:/Documents and Settings/utile/Bureau/HEC-DSSVue 2.0.1")
        obfichier= open ('param','w')
        obfichier.write('data_source'+' '+ nom_dos+'\n')
        obfichier.write('data_dest'+' '+ nom_destina+'\n')
        obfichier.write('Ann�e' + ' ' + str(Annee).zfill(4)+'\n')
        obfichier.write('Mois' + ' ' + str(Mois).zfill(2)+'\n')
        obfichier.write('nj'+ ' ' + str(nj).zfill(1)+ '\n')
        obfichier.write('Pas' + ' '+ str(Pas).zfill(2)+'\n')
        obfichier.write('Pr�cision' + ' ' + str(a).zfill(2)+'\n')
        obfichier.write(nstat + ' '+  str(longit) + ' ' +str(lat)+'\n')
        obfichier.write(mstat + ' ' + str(longitud) + ' ' +str(latitud))
        obfichier.close()
    def demarrer(self):
        os.system('"HEC-DSSVue.exe"')	
tkinterTuto().mainloop()

            

