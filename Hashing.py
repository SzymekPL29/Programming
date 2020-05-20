import bcrypt
# import time

wachtwoord = b"HiddenPa$$w0rd!"

hashed = bcrypt.hashpw(wachtwoord, bcrypt.gensalt())

print(hashed)

if bcrypt.checkpw(wachtwoord, hashed):
    print("Password is hetzelfde!")
else:
    print("Password is niet hetzelfde!")

#start = time.time()
#hashed = bcrypt.hashpw(wachtwoord, bcrypt.gensalt(rounds=14)) #default is 12 rounds (hoger is langer)
#einde = time.time()
#x = einde - start

#print(x)