# Lees een lijn in van de console
# Blijf lijnen inlezen tot je een lijn
# ingeeft die je al eens hebt ingegeven.
# Print de dubbel ingegeven lijn uit.

ingegevenLijnen = set()

lijn = input('Geef een lijn in: ')
while lijn not in ingegevenLijnen:
    ingegevenLijnen.add(lijn)
    lijn = input('Geef een lijn in: ')
else:
    print(lijn)



#---------------------

# Geef een getal in op de console
# Lees dat aantal lijnen in
# Print enkel de unieke lijnen in volgorde
# waarin ze zijn ingegeven.
