## Laborationsuppgifter

### 1
a) Notera målfunktionsvärde, primal optimallösning och dual optimallösning.
Vilka variabler är basvariabler i optimallösningen?:
```
Målfunktion: 50
Primal optimallösning: x1,x2,x3 = 10,0,10
Dual optimallösning: x4,x5,x6 = 1,0,1/3
Vilka variabler är basvariabler i optimallösningen?: 3,5,1
```

b) Räkna för hand ut den reducerade kostnaden för en ny variabel med målfunktionskoefficient 2 och bivillkorskoefficienterna (0 2 3). (Använd duallösningen.) Vilken slutsats kan dras av tecknet på den reducerade kostnaden?:
```
Reducerad kostnad: 
2- 1*0 + 2*0 + 3*1/3 = 1
Vi får ny optimallösning
```
c) Bestäm den nya optimallösningen genom att införa kolumnen i tablån. Börja
med tidigare optimalbas. Ange optimallösningen samt ändring i målfunktionsvärde:
```
z = 54
x = (2,0,14,4,0,0,0)
```

### 2
a) Starta i punkten där bivillkor 1 och 2 är aktiva. Vilka variabler ingår i basen
i denna punkt?
```
x1,x2,x5,x6,x7
```
b) Gör en pivotering med en inkommande variabel med fel tecken på den reducerade kostnaden. Markera den erhållna punkten i figuren i resultatbladet. Vad
händer med målfunktionsvärdet? Varför? (Pivotera sedan tillbaka till första
baslösningen.)
```

```
c) Gör en pivotering med rätt inkommande variabel, men med fel utgående
variabel. Använd ett positivt pivotelement. Markera den erhållna punkten i
figuren. Vilken typ av lösning fås? Varför? (Pivotera sedan tillbaka till första
baslösningen.)
```

```
d) Gör en pivotering med rätt inkommande variabel, men med fel utgående
variabel. Använd ett negativt pivotelement. Markera den erhållna punkten i
figuren. Vilken typ av lösning fås? Varför? (Pivotera sedan tillbaka till första
baslösningen.)
```

```
e) Lös problemet korrekt. Rita in varje iterationspunkt i figuren, och notera
målfunktionsvärdena. Ange optimallösningen.
```
skuggpris: 4,667    
z = 59.333 x=(5.667, 1.333)
```
f) Ange skuggpriset för villkor (4). Ändra högerledet i villkor (4) från 7 till 8 (den streckade linjen i figuren). Hur mycket ändras målfunktionsvärdet?
(Jämför med skuggpriset.)
```

z = 64
```



### 3
a) Starta i origo och lös problemet att maximera z med simplexmetoden.
Starta i origo och lös problemet att minimera z med simplexmetoden. (Ändra
inte problemdata.) Ange lösningarna samt vilka bivillkor som är aktiva i de erhållna punkterna.
```
max: x = (2,0,0) z = 8
Bivillkor aktivt: 1 ty 2*2 = 4

min: x = (0,2,0) z = -2
Bivillkor aktivt: 1

```

b) Hur förändras det optimala målfunktionsvärdet i maximeringsproblemet respektive minimeringsproblemet om högerledet till det första bivillkoret ökas
med en enhet? (Ledning: Optimalbaserna ändras ej. Frågan kan besvaras
utan att ändra i problemet.)
```
max: x=(5/2 eller 2,0,0) z = 10 FEL
min  x =(0,2.5 eller 2, 0) z = -2,5 FEL
```

### 4
 Firman Playwood (se avsnitt 7.7 i boken) producerar tre olika sorters enkla träleksaker (anka, hund och katt), och målar dem med fyra färger (rött, blått, grönt
och gult). Nedanstående tabell anger hur mycket färg som går åt för att måla en
leksak, i cl.

Varje dag har man tillgång till 1000 cl röd färg, 1000 cl blå färg, 2000 cl grön färg
och 2000 cl gul färg. En anka ger vinsten 2 kr, en hund 1 kr och en katt 2 kr.
(Antag att man har obegränsat med träråvaror utan kostnad för produktionen.)


a) Formulera Playwoods problem att maximera vinsten för en dag som en LPmodell. Använd variablerna xj = antal producerade enheter av sort j, där
j=1 betyder anka, j=2 betyder hund och j=3 betyder katt.
Skriv in problemet och lös det. Ange optimallösningen i klartext. Blir det
färg över?
```
Optimallösning z = 1250, x = (250, 0, 375, 375, 0,0, 625)
375cl röd x4, 625cl gul x7
```
b) Playwoods marknadsavdelning diskuterar en prisjustering på hunden. För
vilka värden på vinsten för hunden fås fler hundar i optimallösningen? (Använd information från optimaltablån. Lös ej om.)
```
1,75kr
```
c) Playwood får erbjudandet att öka tillgången av en av färgerna med 100 cl
per dag. Vilken färg ska man välja? (Använd information från optimaltablån.
Lös ej om.)
```
x2 blå
```
d) Playwoods utvecklingsavdelning kommer på att man kan göra en gris och
måla den med 4 cl röd, 1 cl blå, 1 cl grön och 1 cl gul färg. Vore det optimalt
att producera grisar, om vinsten per gris är 2 kr? (Utgå från lösningen i
uppgift a och beräkna reducerad kostnad. Inför sedan den nya variabeln
endast om den verkar lönsam.)
```
2-4*0-0,750*1-0,250*1-0=1 ja
z = 1357,143, x = (250,0, 321.429, 107.143)
```
