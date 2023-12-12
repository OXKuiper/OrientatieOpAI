########### Faculteit recursief #########
# Factulteit: bijv 5! = 5*4*3*2*1... En dus is 5!=5*4!

# NIET-recursieve manier
factuleit = 5
totaal = 1
for x in range(factuleit,0,-1):
    print(x)
    totaal = totaal * x
print(totaal)

def fac_recursief(getal):
    print(f'Getal is nu...{getal}')
    if getal == 1:
        print('Base case!')
        return 1
    print(f"Uitkomst van deze aanroep van de functie is {getal} * factulteit{getal}-1")
    return getal * fac_recursief(getal-1)  # n * f(n-1)

print(fac_recursief(5))



##### Palindroom recursief #################
# Bijv odido, lepel, radar.
# De buitenste letters zijn hetzelfde, en de 1-na-buitenste, etc.
# Oftewel, het woord is omkeerbaar. (Extra: Dat kan ook makkelijker. w == w[::-1], maar hee)
#

def palindroom(wrd):
    print('Functie aanroep met',wrd)
    if len(wrd) <= 1:
        print('Nog 0 of 1 letter over')
        return True
    # bepaal of meest linker en meest rechter letter zelfde zijn.
    # ...en kijk of wat over is ook nog een palindroom is. Bijv 'lepel' --> 'epe'
    return wrd[0] == wrd[-1] and palindroom(wrd[1:-1])

woord = 'radar'
print(palindroom(woord))
