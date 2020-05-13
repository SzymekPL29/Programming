#Database Login


status = ""

def BeginScherm():
    status = input("Bent u een geregistreerde gebruiker? Ja/Nee?\n")

    if status == "Ja":
        KnownUser()
    elif status == "Nee":
        NewUser()

def NewUser():
    CreateUser = input("Vul hier uw gebruikersnaam in: ")

    for line in open("Users.txt", "r").readlines():
        login_info = line.split()  # Spatie in het txt bestand zorgt voor 2 losse strings.
        if CreateUser == login_info[0]:
            print("\nLogin naam bestaat al!\n")
            return False
    else:
        CreatePassword = input("Vul hier uw nieuw wachtwoord in: ")
        print("\nGebruiker aangemaakt!\n")
        file = open("Users.txt", "a")
        file.write(CreateUser)
        file.write(" ")
        file.write(CreatePassword)
        file.write("\n")
        file.close()
        return True

def KnownUser():
    login = input("Gebruikersnaam: ")
    Password = input("Wachtwoord: ")
    for line in open("Users.txt", "r").readlines():
        login_info = line.split()  # Spatie in het txt bestand zorgt voor 2 losse strings.
        if login == login_info[0] and Password == login_info[1]:
            print("\nU bent ingelogd!")
            input("\nDruk op een willekeurige toets om verder te gaan...")
            exit()
        print("\nGebruiker bestaat niet of verkeerde wachtwoord!\n")
        return False

while status != "x":
    BeginScherm()

#Versie 1 zonder Txt Bestand checker
#  if login in User and User[login] == Password:
#        print("\nU bent ingelogd!")
#        input("\nDruk op een willekeurige toets om verder te gaan...")
#        exit()
#    else:
#        print("\nGebruiker bestaat niet of verkeerde wachtwoord!\n")



