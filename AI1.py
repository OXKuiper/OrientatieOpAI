''' Code gebruikt in les AI1

Bij programmeren moet je vaak het probleem eerst opknippen:
Wat moet je functie nu precies doen, en welke stappen moet je zetten om daar te komen?

Soms kan je die stappen al in halve programeeer taal zetten (#"Als het getal negatief is, return het getal als int min 1.")
Dat noemen we 'pseudocode'

Soms is het iets meer trial-and-error: de functie deels schrijven, en goed kijken naar de
output om steeds je functie aan te passen.

Voor de opdrachten van AI les 1 was er nog iets wat je aan het begin moet checken:
Welk greedschap heb je om dit probleem op te lossen?
Naast if-statements, zijn int() en de floor divider (//) handig.

Hoe kan je uitvinden hoe je die kan gebruiken? Of zoeken/vragen, of zelf uitproberen'''

# tip, open een nieuw .py bestand, en probeer het gewoon uit
print(int(-1.5)) # geeft dit -2 of -1? Probeer het uit.

# tip2: maak een loopje om te kijken naar wat int() of //1 bij een range van getallen doet
getallen = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
for i in getallen:
    print(f' int({i:>4}) = {int(i):>3}')

'''Ok, je wil een functie schrijven floor() die getallen naar beneden afrond

Manier 1: Eerst nadenken wat je functie precies moet doen, en dat alvast in stappen 
opschrijven in woorden/comments, en die uitprogrammeren

Manier 2: Gewoon ergens mee starten, en goed naar de output van je functie kijken. 
Bijv begin gewoon met alleen int() om naar beneden af te ronden. Wanneer werkt dat wel/niet?

Vaak gebruik je een mix van manier 1 en 2.

'''

# Hieronder wat oplossingen voor de programming opdrachten.
# Uitwerkingen staan ook steeds op canvas voor de volgende les.
# Je mag van mij de docstrings afkorten! Zelfs leerzaam om ze zelf te schrijven.

# Floor() heeft minstens 2 goede oplossing
def floor(real):
    """Function that rounds a number down, returns an int"""
    x = int(real)
    if real < x:  # voor negatieve niet-hele getallen geldt dit. (-0.5, -1.1, etc. Niet voor -1, 1, 1.5 etc)
        nr_int = x - 1
    return x

def floor(real):
    """Function that rounds a number down, returns an int"""
    return int(real//1)  # Kort/goed, maar deze aanpak werkt niet voor ceil()

def ceil(real):
    """Function that rounds a number up, returns an int"""
    x = int(real)
    if real > x:  # voor positieve niet-hele getallen geldt dit. (0.5, 1.1, etc. Niet voor 1, -1, -1.5 etc)
        x = x - 1
    return x


def is_even(n):
    """Function that returns True if n is even, False if n is uneven"""
    return n % 2 == 0


def is_uneven(n):
    """Function that returns False if n is even, True if n is uneven"""
    return n % 2 != 0

