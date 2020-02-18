#Wachtwoord sterkte

Lengte = 8
Hoofdletters = 1
Cijfer = 1
SpecialeTeken = 1

txt = "Het wachtwoord moet minimaal bestaan uit {} characters, {} hoofdletter,\n {} cijfer en {} speciale teken."
print(txt.format(Lengte, Hoofdletters, Cijfer, SpecialeTeken))

import re

x = True
while x:
    Wachtwoord = input("\nNieuw Wachtwoord: ")
    if (len(Wachtwoord) < 8):
        print("Het opgegeven wachtwoord voldoet niet aan de minimale lengte\nProbeer het opnieuw...")
        x = True
    elif re.search('[0-9]', Wachtwoord) is None:
        print("Het opgegeven wachtwoord bevat geen cijfer\nProbeer het opnieuw...")
        x = True
    elif re.search('[A-Z]', Wachtwoord) is None:
        print("Het opgegeven wachtwoord heeft geen hoofdletter\nProbeer het opnieuw...")
        x = True
    elif re.search('[!@#$%^&*(){}_]', Wachtwoord) is None:
        print("Het opgegeven wachtwoord bevat geen speciale teken\nProbeer het opnieuw...")
        x = True
    else:
        print("Het wachtwoord is gewijzigd!")
        x = False

input()