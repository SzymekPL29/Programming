import random

characters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#$%^&*"

number = input("\nHoeveel wachtwoorden wil jij maken?")
number = int(number)

length = input("Hoe lang moet het wachtwoord zijn?")
length = int(length)

list =[]

for n in range(number):
    wachtwoord = ""
    for l in range(length):
        wachtwoord += random.choice(characters)
        if len(wachtwoord) == length:
            print("\n"+ wachtwoord)
            list.append(wachtwoord)

print("\nDit is jouw nieuw wachtwoord of nieuwe wachtwoorden")
print(list)

print("\nJe wachtwoord/wachtwoorden zijn geexporteerd naar het volgende bestand 'wachtwoord.txt'")

with open('wachtwoord.txt', 'w') as f:
    for item in list:
        f.write("%s\n" % item)









