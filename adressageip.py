adr_ip = input("Entrez une adresse IP : ").split('.')
masque = input(
    "Entrez un masque de sous-réseau : ").split('.')

adr_ip = [int(octet) for octet in adr_ip]
masque = [int(octet) for octet in masque]

liste_octets = [0, 128, 192, 224, 240, 248, 252, 254, 255]
liste_cidr = [0, 8, 16, 24, 32]

# ip_int = (adr_ip[0]<<(24)) + (adr_ip[1]<<(16)) + (adr_ip[2]<<(8)) + adr_ip[3]
# masque_int = (masque[0]<<(24)) + (masque[1]<<(16)) + (masque[2]<<(8)) + masque[3]


def masque_valide(octs):
    if len(octs) != 4 or any(o not in range(256) for o in octs):
        return False
    seen_drop = False
    for o in octs:
        if o not in liste_octets:
            return False
        if seen_drop and o != 0:
            return False
        if o != 255:
            seen_drop = True
    return True


def int_to_ip(addr_int):
    return ".".join(str((addr_int >> (8*i)) & 0xFF) for i in [3, 2, 1, 0])


for nombre in adr_ip:
    if 0 <= int(nombre) <= 255:
        print("... OK")
    else:
        print("Entrez un nombre entre 0 et 255")

while True:
    if masque_valide(masque):
        adressage = "o"
        if adressage.lower() == "o":
            # code pour calculer l'adresse réseau
            ip_int = (adr_ip[0] << (24)) + (adr_ip[1] <<
                                            (16)) + (adr_ip[2] << (8)) + adr_ip[3]
            masque_int = (masque[0] << (24)) + (masque[1]
                                                << (16)) + (masque[2] << (8)) + masque[3]
            reseau_int = ip_int & masque_int
            reseau = [
                (reseau_int >> 24) & 255,
                (reseau_int >> 16) & 255,
                (reseau_int >> 8) & 255,
                reseau_int & 255
            ]
            print("Adresse réseau :", ".".join(map(str, reseau)))
            # code pour calculer l'adresse de broadcast
            ip_int = (adr_ip[0] << (24)) + (adr_ip[1] <<
                                            (16)) + (adr_ip[2] << (8)) + adr_ip[3]
            masque_int = (masque[0] << (24)) + (masque[1]
                                                << (16)) + (masque[2] << (8)) + masque[3]
            broadcast_int = ip_int | (~masque_int & 0xFFFFFFFF)
            broadcast = [
                (broadcast_int >> 24) & 255,
                (broadcast_int >> 16) & 255,
                (broadcast_int >> 8) & 255,
                broadcast_int & 255
            ]
            print("Adresse de broadcast :", ".".join(map(str, broadcast)))
            prem_adresse = reseau_int + 1
            print("Première adresse sur le réseau :", int_to_ip(prem_adresse))
            dern_adresse = broadcast_int - 1
            print("Dernière adresse sur le réseau :", int_to_ip(dern_adresse))
            nb_adresses = (broadcast_int - reseau_int) + 1
            nb_appareils = nb_adresses - 2 if nb_adresses > 2 else 0
            print(
                f"Nombre d'appareils disponibles sur le réseau : {nb_appareils}")
        break
    else:
        print("ERREUR ! Masque de sous réseau invalide !")
        masque = [int(octet)
                  for octet in input("Entrez un masque valide : ").split('.')]
