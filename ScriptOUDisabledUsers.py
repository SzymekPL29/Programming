#Benodigde Libraries
from pyad import *
from pyad.adgroup import ADGroup
from pyad.adcontainer import ADContainer

#Gegevens die wij gebruiken
server=("dc01.challenge.local")
username=("administrator")
password=("Passw0rd!")

#Connectie maken met de server
pyad.set_defaults(ldap_server=server,username=username,password=password)

#De groep waar alle users in staan:
group = pyad.from_cn("WerkGroep")

for each in group.get_members(recursive=False): #Wij gebruiken geen functie die zichzelf oproept.

# print(each.Displayname,each.UserAccountControl) #Kan gebruikt worden om te controlleren.

    if each.UserAccountControl == 514:
        print(each.name)
        print('User is Disabled...')
        print('moving User to proper Organisation Unit...')
        each.move(ADContainer.from_dn("ou=DisabledGebruikers,ou=Challenge,dc=challenge,dc=local"))
        print('User has been moved succesfully! No further action required...\n')

    elif each.UserAccountControl == 546:
        print(each.name)
        print('User is Disabled...')
        print('moving User to proper Organisation Unit...')
        each.move(ADContainer.from_dn("ou=DisabledGebruikers,ou=Challenge,dc=challenge,dc=local"))
        print('User has been moved succesfully! No further action Required...\n')

    elif each.UserAccountControl == 66050:
        print(each.name)
        print('User is Disabled...')
        print('moving User to proper Organisation Unit...')
        each.move(ADContainer.from_dn("ou=DisabledGebruikers,ou=Challenge,dc=challenge,dc=local"))
        print('User has been moved succesfully! No further action Required...\n')

    elif each.UserAccountControl == 66082:
        print(each.name)
        print('User is Disabled...')
        print('moving User to proper Organisation Unit...')
        each.move(ADContainer.from_dn("ou=DisabledGebruikers,ou=Challenge,dc=challenge,dc=local"))
        print('User has been moved succesfully! No further action Required...\n')

    elif each.UserAccountControl == 262658:
        print(each.name)
        print('User is Disabled...')
        print('moving User to proper Organisation Unit...')
        each.move(ADContainer.from_dn("ou=DisabledGebruikers,ou=Challenge,dc=challenge,dc=local"))
        print('User has been moved succesfully! No further action Required...\n')

    elif each.UserAccountControl == 262690:
        print(each.name)
        print('User is Disabled...')
        print('moving User to proper Organisation Unit...')
        each.move(ADContainer.from_dn("ou=DisabledGebruikers,ou=Challenge,dc=challenge,dc=local"))
        print('User has been moved succesfully! No further action Required...\n')

    elif each.UserAccountControl == 262690:
        print(each.name)
        print('User is Disabled...')
        print('moving User to proper Organisation Unit...')
        each.move(ADContainer.from_dn("ou=DisabledGebruikers,ou=Challenge,dc=challenge,dc=local"))
        print('User has been moved succesfully! No further action Required...\n')

    elif each.UserAccountControl == 328194:
        print(each.name)
        print('User is Disabled...')
        print('moving User to proper Organisation Unit...')
        each.move(ADContainer.from_dn("ou=DisabledGebruikers,ou=Challenge,dc=challenge,dc=local"))
        print('User has been moved succesfully! No further action Required...\n')

    elif each.UserAccountControl == 328226:
        print(each.name)
        print('User is Disabled...')
        print('moving User to proper Organisation Unit...')
        each.move(ADContainer.from_dn("ou=DisabledGebruikers,ou=Challenge,dc=challenge,dc=local"))
        print('User has been moved succesfully! No further action Required...\n')

    else:
        print(each.name)
        print('User is Enabled!')
        print('No further action required...\n')









