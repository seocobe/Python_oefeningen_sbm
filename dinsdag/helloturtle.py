'''
Enkele voorbeelden met Turtle.
'''

import turtle

def maakTurtleMetKleur(kleur):
    '''
    Maak een turtle met een bepaalde kleur
    '''
    t = turtle.Turtle()
    t.color(kleur)
    return t

def maakTurtleSter(*args):
    '''

    '''
    turtles = map(maakTurtleMetKleur, args)
    verschil_hoek = 360/len(args)
    hoek = 0
    for t in turtles:
        t.left(hoek)
        hoek += verschil_hoek
        t.forward(100)
        del t

def maakTurtleSterUitBestand(bestandsnaam):
    '''
    Open een bestand met 1 kleur per lijn
    Lees
    '''
    with open(bestandsnaam) as kleurenBestand:
        kleuren = [k.strip() for k in kleurenBestand.readlines()]
    maakTurtleSter(*kleuren)


if __name__ == '__main__':
    win = turtle.Screen()

    # maakTurtleSter('red','green','blue')

    # from os import path
    # scriptDirectory = path.dirname(__file__)
    # kleurenTxt = path.join(scriptDirectory, 'kleuren.txt')
    # maakTurtleSterUitBestand(kleurenTxt)

    win.exitonclick()