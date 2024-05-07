import numpy as np
import matplotlib.pyplot as plt
import math

#code by patrick henaff, modifié


#toM = 0.35
#toS = 3.5
#Af = 1
#sigmaS = 2
#"sigmaF = 1.5"
#w_inj = 0.5 #poids synaptique I_inj
V0 = 0
q0 = 0
dt = 0.01

class NeuroneRS : pass  #car pas vraie prog obj



########################################################
###         construction neurone instant t           ###
########################################################  


def create_NRS(nom='RS1', I_inj = 0.0,w_inj=0.5, V=0.0, sigmaS=2.0 ,sigmaF=1.5,Af = 1,q=0.0):
    neurone = NeuroneRS()
    neurone.nom =  nom 
    neurone.I_inj = I_inj  # courant d'entrée:  peut etre une somme de courants
    neurone.w_inj =  w_inj  # poids synaptique courant d'entrée 
    neurone.V=  V    # output neurone- on rappelle V = Vs et la dérivée peut se noter y au lieu de Vs point-
    neurone.sigmaS =  sigmaS 
    neurone.sigmaF =  sigmaF 
    neurone.Af =Af
    neurone.q = q  #signal slow current
    neurone.toM = 0.35
    neurone.toS = 3.5    
    return neurone



########################################################
###          fonctions basiques nécessaire           ###
########################################################  



# -----------------------------------------------------------------------------avoir une section fonction et une section constructrice de listes pour le tracé- on travaille techniquement en temps réel
def F(n):
    return n.V-n.Af*np.tanh((n.sigmaF/n.Af)*n.V)

def Input(t) :
    list_I_inj = []
    if t >=0 and t<=1:
        I = 1
    #list_I_inj.append(I)    
    return I
    
def f_V(n, t):
    '''
    #impuslion dirac pour faire démarrer le système  ancienne version - mtn def autre part
    list_I_inj = []
    if t >=0 and t<=1:
        n.I_inj = 1
    list_I_inj.append(n.I_inj)
    #print(list_I_inj)
    '''
    return -((F(n)+n.q-n.w_inj*n.I_inj))*(1/n.toM)

def f_Q(n):
    return (-n.q + n.sigmaS*n.V)/n.toS




########################################################
###                   intégration                    ###
########################################################  


#faut il mettre à jour le sigmaS avant ou après calcul de Vs? 
#comparer les 2, un des cas peut diverger, 
#sigmaS calculé en fct de l'état courant donc à calculer d'abord car sigmaS de sortie est en t+1

#Methode d'euler pour résoudre les équations différentielles
#intégration / main / boucle de résolution - trouver nom
def Neurone_RS(n):
    t = 0
    T = 20# définition du temps de simulation
    list_V = []
    list_T = []
    
    while t < T:
        n.V = n.V + f_V(n,t)*dt
        n.q = n.q + f_Q(n)*dt
        t += dt
        #print("Temps: ", t, V, I_inj)
        list_V.append(n.V)
        list_T.append(t)    
    return list_V, list_T


neur1 = create_NRS(nom='RS1', I_inj = 0.0,w_inj=0.5, V=0.0, sigmaS=2.0 ,sigmaF=1.5)
neur2 = create_NRS(nom='RS2', I_inj = 0.0,w_inj=0.5, V=0.0, sigmaS=2.0 ,sigmaF=1.5)

Vs1,Ts1 = Neurone_RS(neur1)
plt.plot(Ts1, Vs1)
#Vs2,Ts2 = Neurone_RS(neur2)
#plt.plot(Ts2, Vs2)
plt.show()