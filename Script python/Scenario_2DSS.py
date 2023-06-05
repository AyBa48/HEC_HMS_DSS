# name=Scenario_2DSS
# displayinmenu=true
# displaytouser=true
# displayinselector=true
from hec.script import *
from hec.heclib.dss import *
from hec.heclib.util import *
from hec.io import *
import java
import sys
import os
import math
import datetime

# Declartion du vecteur libele des mois
cMois = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print (now.strftime("%y"))
nowDateTime = now.strftime("%d") + cMois[now.month-1] + now.strftime("%y") + now.strftime("  %H:%M:%S")

print("\n\nLe Repertoire courant est :", os.getcwd(), "\n\n")
param = open("C:\Documents and Settings\utile\Bureau\HEC-DSSVue 2.0.1\param", "r")
#param = open("param.txt", "r") # ouvre le fichier param en lecture seulement
pfname = "ascii.PF" # YYYYMMDD.dt chaine de caractere
vData_Dest = "Scenario"  # YYYYMMDD/Station/  chaine de caractere
LonX = "LongitudeX "  # chaine de caractere
LatY = "LatitudeY " # chaine de caractere
vStation = "JEBL_OUNAGHA" 
# Lire la 1ere ligne de param et la transfomée en liste de valeur auquel on affecte les variables lData_Source, vData_Source
lData_Source, vData_Source = param.readline().split()
# Lire la 2eme ligne de param et la transfomée en liste de valeur auquel on affecte les variables Data_Dest, vData_Dest
lData_Dest, vData_Dest = param.readline().split()
# Lire la 3eme ligne de param et la transfomée en liste de valeur auquel on affecte les variables lAn, vAn
lAn, vAn     = param.readline().split()
# Lire la 4eme ligne de param et la transfomée en liste de valeur auquel on affecte les variables lMois, vMois
lMois, vMois = param.readline().split()
# Lire la 5eme ligne de param et la transfomée en liste de valeur auquel on affecte les variables lPas, vPas
lPas, vPas   = param.readline().split()
# Lire la 6eme ligne de param et la transfomée en liste de valeur auquel on affecte les variables lDelta, vDelta
lDelta, vDelta = param.readline().split()
print (lData_Source, vData_Source)
print (lData_Dest, vData_Dest)
print (lAn, vAn)
print (lMois, vMois)
print (lPas, vPas)
print (lDelta, vDelta)
line = param.readline()
pinfname = vData_Source + "/" + pfname + vAn + vMois  #SEBOU-DATA-prevision-12_01_2012+/+ascii.PF+2010+02
vData_Dest += "_" + vAn + "_" + vMois         #Scenario+_+2010+_+02
iStation = 1

if not (os.path.isdir(vData_Source)): #si le dossier SEBOU-DATA-prevision-12_01_2012 n'existe pas sortir du programme 
	exit()

if not (os.path.isdir(vData_Dest)):  #si le dossier Scenario_2010_02 n'existe pas créer le 
	os.mkdir(vData_Dest)

# Tant que il y des lignes dans le fichier param faire
while line:
	vStation, vLX, vLY = line.split()
	print ("Station ", iStation, vStation, vLX, vLY)
	jour = 1
	oufname = vData_Dest + "/" + vStation
	print ("	Fichier de sortie Station :", oufname, "\n")
	# Ouverture du fichier de sortie de la station en ecriture, et ecriture de la première line de l'Entete
	ouf = open(oufname, "w")
	ouf.write ("//" + vStation + "/PRECIP-INC/" + str(jour).zfill(2) + cMois[int(vMois)-1] + str(vAn).zfill(4) + "/3hours/GAGE/\n")
	nbLine = 0
	cStartDate = "START"
	cEndDate = "END"
	outLine = []
	while jour <=8:
		pas = int(vPas)
		PF = 0 # initialiser PF à 0
		lavgPF = 0 # Contient la dernière valeur calculée de avgPF
		while pas <= 24: # MAX 24 heures
			cLPF = 0
			infname = pinfname + str(jour).zfill(2) + "." + str(pas).zfill(2)
			if os.path.exists(infname):
				infile = open(infname, "r")
				for line in infile.readlines():
					data = line.split()
					if ((math.fabs(float(data[0]) - float(vLX)) <= float(vDelta)) and (math.fabs(float(data[1]) - float(vLY)) <= float(vDelta))):
						PF = PF + float(data[2]) + float(data[3]) + float(data[4]) + float(data[5])
						cLPF += 1
				infile.close()
			if cLPF > 0:
				avgPF = PF / cLPF # moyenne (par fichier) inc dans précédent avec - valeur precedente (ajouter l'heure dans la sortie)
				avgPF = avgPF - lavgPF
				lavgPF = avgPF
				# Construire une ligne de sortie (cLine)
				cDate = str(jour).zfill(2) + cMois[int(vMois)-1] + str(vAn).zfill(4)
				cLine= (str("%.1f" % avgPF) + "\n")
				# Ajouter la ligne de sortie à un vecteur de sortie (outLine)
				outLine.append(cLine)
				if cStartDate == "START":
					cStartDate = cDate
				else:
					cEndDate = cDate
				nbLine +=1
			pas += int(vPas)
		jour += 1
	# Ecriture des autres ligne de l'entete
	#ouf.write ("RTD  Ver:  1   Prog:DssVue  LW:" + nowDateTime + "   Tag:Tag        Prec:2\n")
	ouf.write ( cStartDate +'  '+ vPas+"00" +"\n") #;   End: " + cEndDate + " at 2400 hours;  Number: " + str(nbLine) + "\n")
	ouf.write (" MM    PER-INC\n" ) 
                    # ouf.write ("Type  PER-INC\n")
	jour = 0
	while jour < nbLine:
		ouf.write(outLine[jour])
		jour +=1
	ouf.close()
	iStation += 1
	line = param.readline()
param.close()

station1file=open("C:/Documents and Settings/utile\Bureau/HEC-DSSVue 2.0.1/Scenario_2010_02/Bab_Ouender", "r")
station2file=open("C:/Documents and Settings/utile\Bureau/HEC-DSSVue 2.0.1/Scenario_2010_02/Jbel_Outka", "r")
pthname1=station1file.readline()
pthname2=station2file.readline()
dte1, hre1=station1file.readline().split()
dte2, hre2=station2file.readline().split()
unit1,typ1=station1file.readline().split()
unit2,typ2=station2file.readline().split()
prec=[]
prec2=[]
vPas = int(vPas)
for line in station1file:
       prec.append(float(line))
for lines in station2file:
       prec2.append(float(lines))
try : 
  try :
    myDss = HecDss.open("C:/Documents and Settings/utile/Bureau/HEC-DSSVue 2.0.1/wmsexport.dss")
    tsc1 = TimeSeriesContainer()
    tsc2 = TimeSeriesContainer()
    tsc1.fullName = pthname1
    tsc2.fullName = pthname2
    start = HecTime(dte1, hre1)
    start = HecTime(dte2, hre2)
    tsc1.interval = vPas
    tsc2.interval = vPas
    preci = prec 
    preci2 = prec2 
    times = []
    times2=[] 
    for value in preci :
      times.append(start.value())
      start.add(tsc1.interval)
    tsc1.times = times
    tsc1.values = preci
    tsc1.numberValues = len(preci)
    tsc1.units = unit1
    tsc1.type = typ1
    myDss.put(tsc1)
    for value in preci2 :
      times2.append(start.value())
      start.add(tsc2.interval)
    tsc2.times = times2
    tsc2.values = preci2
    tsc2.numberValues = len(preci2)
    tsc2.units = unit2
    tsc2.type = typ2
    myDss.put(tsc2)
    
  except Exception, e :
    MessageBox.showError(' '.join(e.args), "Python Error")
  except java.lang.Exception, e :
    MessageBox.showError(e.getMessage(), "Error")
finally :
  myDss.close()


