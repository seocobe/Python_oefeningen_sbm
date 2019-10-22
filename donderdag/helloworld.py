'''
uitleg over de module helloworld


>>> helloworld.__doc__
'uitleg over de module helloworld'

'''

# bestand = open('voorbeeld.txt', 'r+')
# print(bestand.readline())
# bestand.close()

with open('voorbeeld.txt') as bestand:
    print(bestand.readline())
    print('bestand is nu open')
    print(bestand.closed)
    print(type(bestand))

print('bestand is nu gesloten')

print(bestand.closed)

# dit is commentaar
