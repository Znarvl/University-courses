***Totalt 10 av 11 poäng*** - Godkända

Riktigt fin och "pythonic" kod igenom hela projektet. Snyggt jobbat!

Nedan följer kommentarer på varje feature.

### A* search for shortest path (2 av 2 points) 
Exemplarisk a-star, snyggt.

### Grid search for closest node (1 av 2 points)
Om jag tolkat `get_closest_node_id_grid_search` rätt så verkar det som att ni bara expanderar sökningen via hörnet uppe till höger och nere till vänster. Alltså får vi bara två nya tiles för varje expansion, istället för `8n` kandidater, där `n` är vilken iteration vi är på. Så om den första tilen inte innehåller några noder så kommer sökningen bli väldigt skev. Detta kan testas på Linköpings golfbana, där det finns få noder. Noden som hittas är alltid uppe till höger eller nere till vänster, och är inte den närmaste noden. 

I övrigt var det väldigt clean python-kod, med snygg användning av `map` och `operator`.

### Allowing users to login and register ('securely') (2 av 2 points)
Ser väldigt bra ut, en straight forward approach. Snygg användning av `with open` för att automatiskt stänga filen. 

Dock kan jag ifrågasätta användandet av `del logged_in_user` som ett sätt att logga ut personen. Detta tar bort variabeln `logged_in_user`, vilket skulle kunna krasha programmet om man försöker kalla på den efter det. Visserligen kollar ni först om `logged_in` innan ni försöker komma åt den variabeln, men blir lite otydligt när en global variabel ibland bara försvinner. Ett annat sätt hade varit att sätta `logged_in_user = None` vid utloggning. Sen istället för `if logged_in:` hade ni då kunnat ha `if logged_in_user != None:` eller bara `if logged_in_user:`.

### Provide a browser icon for your web page (1 av 1 point)
Finns inte så mycket att säga här, bra jobbat.

### Choose mode of transportation (3 av 3 points)
Största utmaningen för den här uppgiften var att hitta alla giltiga bil/cykel-vägar, och det har ni lyckats bra med. Också väldigt clean lösning med att ha olika grids och nodes-listor för de olika transportmetoderna.

### Get last saved path (1 av 1 point)
Cool feature, och bra genomfört!