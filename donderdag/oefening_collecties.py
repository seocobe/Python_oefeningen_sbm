

# lees 3 waarden in van stdin
# maak er een tuple van
# maak ook de tuple in omgekeerde volgorde
# toon beide tuples
# geef weer of de omgekeerde tuple groter is dan de oorspronkelijke

a = input('geef eerste element in: ')
b = input('geef tweede element in: ')
c = input('geef derde element in: ')

tup = a,b,c
print(tup)

omgekeerd = tuple(reversed(tup))
print(tup)

print(f"omgekeerd > tup ? {omgekeerd > tup}")






a = input('geef eerste element in: ')
b = input('geef tweede element in: ')
c = input('geef derde element in: ')

if a.startswith('toon ') or b.startswith("toon ")\
    or c.startswith('toon'):


    tp = (a,b,c)

    print(tp)

    print(dir(tp))












# lees 3 waarden in van stdin
# maak er een lijst van
# maak ook de lijst in omgekeerde volgorde
# toon beide lijsten
# geef weer of de omgekeerde lijst groter is dan de oorspronkelijke




#

# set = {1,2,3}

# lijstVanKarakters = list('dit is een lijst van karakters')
# str(lijstVanKarakters)
# ''.join(lijstVanKarakters)



# Lees 2 strings in van de console
# Geef weer welke karakters
# - in beide strings voorkomen
# - enkel in de eerste voorkomen
# - enkel in de tweede voorkomen
# - in minstens 1 van de 2 strings voorkomen
