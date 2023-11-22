''' Code gebruikt in les AI1

Bij programmeren moet je vaak het probleem eerst opknippen:
Wat moet je functie nu precies doen, en welke stappen moet je zetten om daar te komen?

Soms kan je die stappen al in halve programeertaal zetten
Bijv #Als het getal negatief is, return int() van het getal
Dat noemen we 'pseudocode'

Soms is het iets meer trial-and-error (uitproberen):
Gewoon beginnen met een van de stappen,
en goed kijken naar de output om steeds je functie aan te passen.

Voor de opdrachten van AI les 1 was er nog iets wat je aan het begin moet checken:
Welk greedschap heb je om dit probleem op te lossen?
Naast if-statements, zijn int() en de floor divider (//) handig.
Hoe kan je uitvinden hoe je die kan gebruiken? Of zoeken/vragen, of zelf uitproberen!
'''

# tip, open een nieuw .py bestand, bijv test.py, en probeer vanalles gewoon uit
print(int(-1.5)) # geeft dit -2 of -1? Probeer het uit.

# tip2: maak een loopje om te kijken naar wat int() of //1 bij een range van getallen doet
getallen = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
for i in getallen:
    print(f' int({i:>4}) = {int(i):>3}')


# Hieronder wat oplossingen voor de AI1 programmeer-opdrachten.
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

# Round() heeft ook meerdere goede oplossing
def round(real):
    """Function that rounds to the nearest whole number, returns an int"""
    if real >= 0:
        return int(real + 0.5)
    else:
        return int(real - 0.5)


# Andere manier voor round(), credits to Jonah.
def round(real):
    """Function that rounds to the nearest whole number, returns an int"""
    # Dit rond alle negatieve getallen omhoog af, alle positieve getallen omlaag.
    # Soms klopt dat (bijv 1.4 --> 1, -2.2 --> 2) maar soms ook niet. Daarom hieronder if-elif voor die gevallen.
    i = int(real)

    # het decimale deel, bijv dec is 0.1 als je 1.1 of 2.1 als real hebt, -0.9 bij -1.9 of -0.9
    dec = real - i

    # als de dec boven de 0.4999 is (bijv 0.5, 0.6 etc) moet er naar boven afgerond worden
    if dec >= 0.5:
        i = i + 1
    # als de dec onder de -0.4999 is (bijv -0.5, -0.6 etc) moet er naar onder afgerond worden
    elif dec <= -0.5:
        i = i - 1
    return i


def is_even(n):
    """Function that returns True if n is even, False if n is uneven"""
    return n % 2 == 0

def is_uneven(n):
    """Function that returns False if n is even, True if n is uneven"""
    return n % 2 == 1

