import numpy as np
import matplotlib.pyplot as plt
import math


#toM = 0.35
#toS = 3.5
#Af = 1
#sigmaS = 2
#"sigmaF = 1.5"
#w_inj = 0.5 #poids synaptique I_inj
V0 = 0
q0 = 0
dt = 0.01

class NeuroneRS : pass

#constructeur NeuroneRS

def create_NRS(nom='RS1', I_inj = 0.0,w_inj=0.5, V=0.0, sigmaS=2.0 ,sigmaF=1.5,Af = 1,q=0.0):
    neurone = NeuroneRS()
    neurone.nom =  nom 
    neurone.I_inj = I_inj  # courant d'entrÃ©e:  peut etre une somme de courants
    neurone.w_inj =  w_inj  # poids synaptique courant d'entrÃ©e 
    neurone.V=  V    # output neurone
    neurone.sigmaS =  sigmaS 
    neurone.sigmaF =  sigmaF 
    neurone.Af =Af
    neurone.q = q
    neurone.toM = 0.35
    neurone.toS = 3.5    
    return neurone

def F(n):
    return n.V-n.Af*np.tanh((n.sigmaF/n.Af)*n.V)



def Input_Dirac(t) :
    list_I_inj = []
    if t >=0 and t<=1:
        I = 1
    list_I_inj.append(I)    
    return list_I_inj  



    
def f_V(n, t):
    #impuslion dirac pour faire dÃ©marrer le systÃ¨me
    list_I_inj = []
    if t >=0 and t<=1:
        n.I_inj = 1
    list_I_inj.append(n.I_inj)
    #print(list_I_inj)
    return -((F(n)+n.q-n.w_inj*n.I_inj))*(1/n.toM)

#Ã  modifier pour passer dans la boucle
#def f_V(n, t, Input):
    ##impuslion dirac pour faire dÃ©marrer le systÃ¨me
    #list_I_inj = []
    #if t >=0 and t<=1:
        #n.I_inj = 1
    #list_I_inj.append(n.I_inj)
    ##print(list_I_inj)
    #n.I_inj = Input
    #return -((F(n)+n.q-n.w_inj*n.I_inj))*(1/n.toM)

def f_Q(n):
    return (-n.q + n.sigmaS*n.V)/n.toS

def simulate(n,T):
    t = 0
    
    list_V = []
    list_T = []
    
    while t < T:
        n.V = n.V + f_V(n,t)*dt #Methode d'euler pour rÃ©soudre les Ã©quations diffÃ©rentielles
        n.q = n.q + f_Q(n)*dt
        
        t += dt
        #print("Temps: ", t, V, I_inj)
        list_V.append(n.V)
        list_T.append(t)    
    return list_V, list_T



#######simulation ############"

neur1 = create_NRS(nom='RS1', I_inj = 0.0,w_inj=0.5, V=0.0, sigmaS=2.0 ,sigmaF=1.5)
neur2 = create_NRS(nom='RS2', I_inj = 0.0,w_inj=0.5, V=0.0, sigmaS=10.0 ,sigmaF=1.5)

T = 20# dÃ©finition du temps de simulation

Vs1,Ts1 = simulate(neur1,T)
plt.plot(Ts1, Vs1)
#Vs2,Ts2 = simulate(neur2,T)
#plt.plot(Ts2, Vs2)
plt.show()