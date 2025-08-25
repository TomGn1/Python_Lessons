prenom = input("Quel est ton prénom ? ")
nom = input("Quel est ton nom de famille ? ")
age = int(input("Quel âge as-tu ?"))
print(f"Bonjour {prenom} {nom}, tu as {age} ans !")
if age <= 18:
    print(f"Tu as {age} ans, tu est mineur !")
else:
    print(f"Tu as {age} ans, tu est majeur !")
i = 0
while i < 5:
    i += 1
    print("Bonjour !")
i = 0
while i < age:
    i += 1
    print(f"Laisse moi compter ton age : {i} ans !")
