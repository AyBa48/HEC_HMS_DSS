# name=test
# displayinmenu=true
# displaytouser=true
# displayinselector=true
# -*- coding: cp1252 -*-
import os

direct= os.getcwd()
Annee = raw_input ('veuiller entrer l\'ann�e :' )
x=int(Annee)
Mois = raw_input ('Veuiller entrer le mois:' )
y=int(Mois)
Pas= raw_input('Veuiller entrer le pas: ')
z=int(Pas)
a= raw_input('Veuiller entrer la precision: ')
q=float(a)
print y, z, q
obfichier= open ('param','w')
obfichier.write('Ann�e'+' '+str(x).zfill(4)+'\n')
obfichier.write('Mois'+' '+str(y).zfill(2)+'\n')
obfichier.write('Pas'+' '+str(z).zfill(2)+'\n')
obfichier.write('Pr�cision'+' '+str(q).zfill(2))
obfichier.close()
