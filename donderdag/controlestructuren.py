# if

# tekst = 'toon iets'
# tekst = 'abc'
# tekst = 'een andere lange tekst'
# tekst = 'Hoofdletter'
tekst = 'Zoveel tekst met hoofdletter'

#
uitkomst = 'Tekst begint niet met "toon"'
if tekst.startswith('toon '):
    uitkomst = tekst
elif 'A' <= tekst <= 'Z':
    uitkomst = 'Begint met hoofdletter'
elif len(tekst) < 5:
    uitkomst = 'Dat is wel een heel korte tekst'

print(uitkomst)

del uitkomst

print(uitkomst)

if 1< 2:
    pass
