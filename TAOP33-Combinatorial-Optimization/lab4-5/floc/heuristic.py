#TAOP33
#Simon Jakobsson (simja649) Gustav Hanstorp (gusha433)

import numpy as np
import time
import sys
import copy

e=100

prob=" ".join(sys.argv[1:]).split('.')[0]
fil=prob+'.npz'

npzfile = np.load(fil)
npzfile.files
m=npzfile['m']
n=npzfile['n']
s=npzfile['s']
d=npzfile['d']
f=npzfile['f']
c=npzfile['c']
#print 'm:',m,' n:',n
#print 's:',s
#print 'd:',d
#print 'f:',f
#print 'c:',c
'''
m = möjliga platser
n = antalet kunder
d = efterfrågan från kund
s = kapaciten på plats i
f = fasta kostanden på öppna anläggning
c = transportkost per kund
'''


t1=time.time()
x=np.zeros((m,n),dtype=np.int)
y=np.zeros((m),dtype=np.int)

ss=copy.deepcopy(s)
dd=copy.deepcopy(d)
ff=copy.deepcopy(f)
fff=copy.deepcopy(f)
ff.sort() #soerterar fabrikerna efter kostnad så vi hittar den billigaste

#Första forloopen går igenom alla fabriker från den billigaste till den dyraste.
#Där kollar vi sedan vilket nummer (i) som är den billigaste fabriken och kollar vilka kunder som har den i loop 2.
for i in range(m):
    curr_fab = ff[i] #Hur mycket kostar den billigaste fabriken
    curr_fab_in_array = np.where(fff == curr_fab)[0][0] #kollar i originalarryen vilken placering den billigaste fabriken har
    cheapest_customers = c[curr_fab_in_array] #tar ut arrayen med transportkostnader för den billigaste fabriken
    cheapest_customers.sort() #sorterar så vi hittar den billigaste kunden för den billigaste fabriken
    for j in range(n):
        current_cust = cheapest_customers[j] #Vad kostar den billigaste kunden
        curr_cust_in_array = np.where(cheapest_customers == current_cust)[0][0] #hittar vilket nummer den billigaste kunden har
        if (ss[curr_fab_in_array] > 0 and dd[curr_cust_in_array] > 0):
            amount_of_packages = np.minimum(ss[curr_fab_in_array], dd[curr_cust_in_array]) #hitta maximalbeloppet som kan skickas från fabrik till kund
            ss[curr_fab_in_array] = ss[curr_fab_in_array] - amount_of_packages #Ta bort antalet skickade packet från kapaciteten
            dd[curr_cust_in_array] = dd[curr_cust_in_array] - amount_of_packages #Ta bort antalet mottagna paket från efterfrågan
            x[curr_fab_in_array, curr_cust_in_array] = amount_of_packages #Uppdatera x så det blir korrekt
            is_placed = True
        else:
             fff[curr_fab_in_array] = 0 #Ändrar kostnaden att bygga en fabrik till 0 efter att den byggts så att det går att ha fabriker med samma kostnad

    if is_placed:
        y[i] = 1 #Placerar en fabrik och uppdaterar Y
        is_placed = False #kontroll så vi inte placerar för många fabriker

elapsed = time.time() - t1
print('Tid: ' + str(elapsed))

cost=sum(sum(np.multiply(c,x))) + e*np.dot(f,y)
print('Problem: '+ str(prob) + ' Totalkostnad: ' + str(cost))
print('Antal byggda fabriker: ' + str(sum(y)) + ' av ' + str(m))