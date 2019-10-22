# tuples

tup = 1,2,3
type(tup)
print(repr(tup))
dir(tup)
len(tup) # aantal elementen

a,b,c = tup

tup[-1]
tup[-2]

tup.count(22)

tup[2] = 'dsdf'

tup4567 = 4,5.1,'zes',7
tup4567

addedTup = tup + tup4567
addedTup

tup4567
tup

tup * 10

tup < tup4567


langTuple = 1,2,3,4,5,6
a,*b,c,d = langTuple


leegTuple = (   )
leegTuple
leegTuple[0] # IndexError


singleton = 'een enkel element'
singleton = ('een enkel element')
singleton = ('een enkel element',)
singleton
type(singleton)
type(singleton[0]) #

str(tup)


# lists

legeLijst = []
len(legeLijst)
type(legeLijst)
dir(list)

'waarde' in legeLijst

legeLijst

nietLegeLijst = ['alpha', 1, 1.234]
'alpha' in nietLegeLijst

legeLijst == nietLegeLijst # False

legeLijst >= nietLegeLijst

legeLijst != nietLegeLijst
legeLijst == nietLegeLijst


[] < [-10,0]
['a'] < ['Tekst', -10,0]

'Grote letter' < 'geen grote letter'

legeLijst.append(1)
legeLijst
len(legeLijst)

a=10
b=20


a += b
a = a + b

nietLegeLijst
list(reversed(nietLegeLijst))

nietLegeLijst.reverse()
nietLegeLijst

# sets

# dicts

d = { 'sleutel': 'waarde', 4:'pop', 'lijst':[1,2,3]}
dir(d)

'spam' in d
'waarde' in d
'sleutel' in d
'sleutel' in d.keys()

type(d.keys())
set(d.keys())

d['sleutel']

list(d.items())


d['nieuwe waarde'] = 'nieuw'
d
d['nieuwe waarde'] = 'nog nieuwer'
d
d.setdefault('nieuwe waarde', 'aller allernieuwste')
d
d.setdefault('bestond nog niet', 5)
d

del d['bestond nog niet']
d