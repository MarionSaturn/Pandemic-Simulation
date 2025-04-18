# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random

N = 100
ALPHA = 1/2
BETA = 0.5     #Infektionsrate
GAMMA = 0.2     #Genesungsrate
MORTALITY = 0.0000315
MORTALITY_V = 0.12 #D
BIRTH = 0.0000252

#Suceptible, Exposed, Infected, Recovered
days = 0
steps = 50
#First day:
S = 99.0
E = 0.0       #Inkubationszeit
I = 1.0
R = 0.0
D = 0.0


sim = {
       "S":[],
       "E":[],
       "I":[],
       "R":[],
       "D":[]
       }

for days in range(365):
    exposed = (BETA * S * I)/N
    infectious = ALPHA * E
    recoveries = GAMMA * I
    deaths = (MORTALITY * N)+(MORTALITY_V * I)
    births = BIRTH * N
    
    #if deaths > N*0.1:
        #deaths = N*0.1
        
    if N <= 0:
        quit()
             
        
    newS = S-exposed+births
    newE = E+exposed-infectious
    newI = I+infectious-recoveries-deaths
    newR = R+recoveries
    newD = D+deaths
    
    #Neue Leute im Dorf
    if random.random() < 0.1:
        newI += 1
    
    if days >= 50:
        vacc_today = min(5, S)
        newS -= vacc_today
        newR += vacc_today
    
    
    sim["S"].append(newS)
    sim["E"].append(newE)
    sim["I"].append(newI)
    sim["R"].append(newR)
    sim["D"].append(newD)
    
    S = newS
    E = newE
    I = newI
    R = newR
    D = newD
    
    S = max(0, S)
    E = max(0, E)
    I = max(0, I)
    R = max(0, R)
    D = max(0, D)
    N = max(1, N)
    
sim["I"][0] = 1.0

x = list(range(0, days, steps)) #amount of days

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(x, sim["S"][::steps], label="Suceptible (S)", color="blue")
ax2.plot(x, sim["E"][::steps], label="Exposed (E)", color="orange")
ax2.plot(x, sim["I"][::steps], label="Infected (I)", color="red")
ax1.plot(x, sim["R"][::steps], label="Recovered (R)", color="green")
ax2.plot(x, sim["D"][::steps], label="Dead (D)", color="purple")

plt.axvline(x=50, color="gray", linestyle='--', linewidth=1)
plt.text(52, N*0.7, 'Vaccination', rotation=90, color="gray")
plt.figtext(1, 0.7, 'Simulation of Black Death \nwith \nbeta = 0.5\ny = 0.2 \nvaccination starting \non day 50',fontsize=9, bbox=dict(facecolor='white', edgecolor='gray'))

plt.xticks(x)
plt.yticks(list(range(0, int(N)+1, int(N/steps))), color="white")
plt.title("SEIR-Model in a 100 person village - The Black Death")
plt.xlabel("days")
plt.ylabel("Number of people")
plt.legend(loc='center right', bbox_to_anchor=(1,0.5))
ax1.legend(loc='center right', bbox_to_anchor=(1,0.7))
#plt.tight_layout()
ax1.grid(True)
plt.show()