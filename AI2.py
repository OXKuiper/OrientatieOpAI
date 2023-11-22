'''
Wat extra uitleg over de 2e functie, meetkundige_rij():

Start is het startgetal
Factor is de factor, dus met hoe veel je iedere stap vermenigvuldigd.
Exponent is hoe vaak je vermenigvuldigd... dus gelijk aan de LENGTE van de rij!

Voorbeeld uitvoer van meetkundige_rij(5,2,5) is [5, 10, 20, 40, 80]
Want: Startgetal is 5, de vermenigvuldiging is steeds keer-2 (dus 5, 10, 20, etc), en de lengte vd lijst moet 5 zijn (ofwel 'de exponent')

Hieronder nog meer voorbeeld-uitvoer van beide functies:

## rekenkundige_rij() (Dit is de 1e functie!) ##
Voorbeeld invoer-uitvoer van wat de functie rekenkundige_rij() moet doen:
rekenkundige_rij(1, 2, 3) geeft [1, 3, 5]
rekenkundige_rij(3, 4, 5) geeft [3, 7, 11, 15, 19]
rekenkundige_rij(3, 5, 7) geeft [3, 8, 13, 18, 23, 28, 33]
rekenkundige_rij(5, 2, 5) geeft [5, 7, 9, 11, 13]
rekenkundige_rij(5, 3, 5) geeft [5, 8, 11, 14, 17]
rekenkundige_rij(10, 10, 10) geeft [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


## meetkundige_rij() (Dit is de 2e functie!) ##
Voorbeeld invoer-uitvoer van wat de functie meetkundige_rij() moet doen:
meetkundige_rij(1, 2, 3) geeft [1, 2, 4]
meetkundige_rij(3, 4, 5) geeft [3, 12, 48, 192, 768]
meetkundige_rij(3, 5, 7) geeft [3, 15, 75, 375, 1875, 9375, 46875]
meetkundige_rij(5, 2, 5) geeft [5, 10, 20, 40, 80]
meetkundige_rij(5, 3, 5) geeft [5, 15, 45, 135, 405]
meetkundige_rij(10, 10, 10) geeft [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]
'''