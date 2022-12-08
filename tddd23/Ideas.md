# Ideér
## 1.
Isometric perspective pusselspel som man använder sig av skuggor man skapar själv för att lösa pussel i ett område. T.ex hoppa på en knapp så skapar man en skugga som forstätter göra det för att hålla uppe en dörr

## 2. 
Stealth RPG där man inte ska bli upptäckt av fiender, man ska kunna lvl:a upp olika delar av sin gubbe (stealth, attack osv) för att lättare kunna ta sig igenom banorna. Fiender har olika attributer för att undvika eller döda.

## 3. 
Battle pvp 1v1 samla grejer a lá hunger games, när tiden är slut så måste man hinna tillbaka till spawn för att möta motståndaren med vad den har hittat. Bäst vinner. 2D.
## 4. 
Katt och råtta, en personer letar efter den andra och om man hinner ifatt så förlorar den andra. Massa powerups och skit som gör att det blir svårare att fånga eller lättare att hitta

# Utvecklingsmiljö
Godot

# Vald idé
## Pusselspel med skuggor
Man styr en gubbe genom olika banor

### Vad kan gubben göra?
1. Röra sig båda upp, ner, höger, vänster
2. Hoppa
3. Interagera med knappar
4. Göra något med musen? (Meny)
5. Hålla/placera i objekt

### Vad ska klonerna göra?
1. När man håller in en knapp på datorn (typ E) så ska man record:a vad för interaktioner man gör (t.ex går till ett ställe, hoppar). När man klickar av så startar en klon från startplatsen och gör exakt samma interaktioner gubben har gjort under recording fasen
2. Skugga följer bara efter, kan ej interagera med object
3. Loopas om och om igen tills man bekräftar att den inte ska loopa mer
4. Man kan ha 3 kloner aktiva samtidigt
5. En loop kan bara vara fullständig om den inte kolliderar med något
6. Loopen kan bara vara arbiträrt sekunder lång
7. 
8. Använda state machine för att lösa detta??

### Banor
1. 7-8 banor progresserande svårare
2. (Kanske) progression i spelet (typ dubbelhopp osv.)
3. Tutorial är 3 banor lång (3 kloner i slutet, kanske lite introduktion till fysik i 2:a banan?)

