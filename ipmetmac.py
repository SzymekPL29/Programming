import subprocess

ip_address = ""
mac_address = ""

# draait alleen maar als de huidige script niet is ge-importeerd, maar uitgevoerd
if __name__ == '__main__':
    process = subprocess.run(['ipconfig', '/all'], capture_output=True)

    # splijt de tekst
    for full_line in process.stdout.splitlines():
        if b"IPv4 Address" in full_line:  # checks of er de bytes text "IPv4 Address" in deze lijn bestaat.
            # neem het 2de deel van de gesplitste lijn
            # "IPv4 Address. . . . . . . . . . . : 192.168.56.1(Preferred)" ->
            # ["IPv4 Address. . . . . . . . . . . ", " 192.168.56.1(Preferred)"]
            # (het is "dirty" omdat er nog steeds spaties en "(Preferred)" erin zit)
            bytes_line_dirty = full_line.split(b":")[1]

            # maak een normale string van de bytes.
            line_dirty = bytes_line_dirty.decode()

            # Haal "whitespace" weg van bijde kanten van de string.
            line = line_dirty.strip()

            # Pak het eerste deel van ["192.168.56.1", "Preferred"]
            ip_address = line.split("(")[0]

        elif b"Physical Address" in full_line:
            # neem het 2de deel van de gesplitste lijn
            # "Physical Address. . . . . . . . . : 0A-00-27-00-00-0E" ->
            # ["Physical Address. . . . . . . . . ", " 0A-00-27-00-00-0E"]
            # (het is "dirty" omdat er nog steeds spaties en "(Preferred)" erin zit)
            bytes_line_dirty = full_line.split(b":")[1]

            # maak een normale string van de bytes.
            line_dirty = bytes_line_dirty.decode()

            # Haal "whitespace" weg van bijde kanten van de string, het mac-address blijft over.
            mac_address = line_dirty.strip()

    print("Je IP-adres is: " + ip_address)
    print("Je MAC-adres is: " + mac_address)
    
    input()
