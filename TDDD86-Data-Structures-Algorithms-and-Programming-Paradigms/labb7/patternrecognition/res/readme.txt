/**********************************************************************
 *  M�nsterigenk�nning readme.txt
 **********************************************************************/

/**********************************************************************
 *  Empirisk    Fyll i tabellen nedan med riktiga k�rtider i sekunder
 *  analys      n�r det k�nns vettigt att v�nta p� hela ber�kningen.
 *              Ge uppskattningar av k�rtiden i �vriga fall.
 *
 **********************************************************************/

      N       brute       sortering
 ----------------------------------
 150       0.066		0.030
 200       0.112 		0.071
 300       0.325 		0.157
 400	      0,694		0.247
 800       4.724		0.812
1600	      36,796		2.395
3200	      287,963		7.626
6400       3000		31.858
12800       24000		137.037

/**********************************************************************
 *  Teoretisk   Ge ordo-uttryck f�r v�rstafallstiden f�r programmen som
 *  analys      en funktion av N. Ge en kort motivering.
 *
 **********************************************************************/

Brute: O(n^4)
Funktionens average case är O(n^3) är då vi ser att de första 3 noderna inte är är linjärtberoende, då den använder 3 for-loopar för att uppnå detta (n^3). Då den hittar 3 som är linjärtberoende så ser vi att vi använder oss av 4 for-loopar för att leta om resterande noderna är linjärtberoende. Då får vi worst case O(n^4), men uppnås sällan.

Sortering: O(n^2 log n)
Den nya algoritmen går igenom nästan varje punkt i listan två gånger (n^2) och att hämta data från map tar (log n) tid.
