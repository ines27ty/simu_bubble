import matplotlib.pyplot as plt
import numpy as np
from math import * 

# Cd et Re
# Ouvrir le fichier
with open("0524/Cd_Re.txt", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
Re = []
Cd_num = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()         # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')      # Remplacer les tabulations par des virgules
    values = line.split(',')     # Diviser la ligne en une liste de valeurs

    # Convertir chaque valeur en float et ajouter à la liste correspondante
    Re.append(float(values[0]))
    Cd_num.append(float(values[1]))

Cd_th = [24/Re[i]*(1+0.125*Re[i]**0.72) for i in range(len(Re))]

Cd_num_Re = [Cd_num[i]*Re[i]/24 for i in range(len(Re))]
Cd_th_Re = [Cd_th[i]*Re[i]/24 for i in range(len(Re))]
#Tracer la courbe
plt.figure(0)
plt.loglog(Re, Cd_num_Re, label='Numerique')
plt.loglog(Re, Cd_th_Re, label='Theorique')  
plt.xlabel('Re')
plt.ylabel('Cd*Re/24')
plt.title('')
plt.legend()
plt.grid()


# Pe Sh Re 0.1
# Ouvrir le fichier
with open("0524/Pe_Sh_Re_0_1.txt", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
Pe = []
Sh = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()         # Supprimer les espaces en début et fin de ligne
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    Pe.append(float(values[0]))
    Sh.append(float(values[1]))

Re = 0.1
Sc = [Pe[i]/Re for i in range(len(Pe))]
Sh_th_rm= [2+0.6*Re**0.5*(Sc[i]**(1/3)) for i in range(len(Sc)) ]
Sc_th_c = [1+(1+Pe[i])**(1/3) for i in range(len(Pe))]

#Tracer la courbe
plt.figure(2)
plt.loglog(Pe, Sh, label='Numérique')
plt.loglog(Pe, Sh_th_rm, label='Theorique, Ranz & Marshall')
#plt.loglog(Pe, Sc_th_c, label='Theorique, Clift', linestyle='--')   
plt.xlabel('Pe')
plt.ylabel('Sh')
plt.ylim(0,100)
plt.title('')
plt.legend()
plt.grid()


# Da et Sc
# Ouvrir le fichier
with open("0524/Da_Sc_1.txt", 'r') as fichier:
    # Lire les lignes du fichier
    lines = fichier.readlines()

# Initialiser des listes vides pour stocker les données
Da = []
Sc = []
Ha = []
E_th = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()         # Supprimer les espaces en début et fin de ligne
    values = line.split()     # Diviser la ligne en une liste de valeurs
    
    # Convertir chaque valeur en float et ajouter à la liste correspondante
    Da.append(float(values[0]))
    Sc.append(float(values[1]))
    Ha.append(np.sqrt(Da[-1])/3.7)
    E_th.append(Ha[-1]/np.tanh(Ha[-1]))

print(np.abs(E_th[-1]-Sc[-1])/Sc[-1])
print(Ha[-1])

# Ha théo = sqrt(k'delta^2/D)
#Tracer la courbe
plt.figure(1)
plt.plot(Ha, Sc, label = 'Numérique', color = 'orange')
plt.plot(Ha, E_th, label = 'Prédiction théorique', color = 'blue')
plt.xlabel('Ha')
plt.ylabel('E')
#plt.loglog()
plt.title('')
plt.legend()
plt.grid()




plt.show()

