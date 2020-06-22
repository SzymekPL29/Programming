#Benodigde Libraries
from pyad import *
from pyad.adgroup import ADGroup
from pyad.adcontainer import ADContainer

#Gegevens die wij gebruiken
server=("dc01.challenge.local")
username=("administrator")
password=("Passw0rd!")
controllist = [514, 546, 66050, 66082, 262658, 262690, 328194, 328226]

#Connectie maken met de server
pyad.set_defaults(ldap_server=server, username=username, password=password)

#De groep waar alle users in staan:
group = pyad.from_cn("WerkGroep")

for user in group.get_members(recursive=False): #Wij gebruiken geen functie die zichzelf oproept.

#print(user.Displayname,user.UserAccountControl) #Kan gebruikt worden om te controlleren.

    if user.UserAccountControl in controllist:
        print("User "+user.name+" is disabled...")
        print("moving user "+user.name+" to proper Organisation Unit...")
        user.move(ADContainer.from_dn("ou=DisabledGebruikers,ou=Challenge,dc=challenge,dc=local"))
        print("User "+user.name+" has been moved succesfully! No further action required...\n")
    else:
        print("User "+user.name+" is enabled!")
        print("No further action required...\n")

input("Press any key to close...")

