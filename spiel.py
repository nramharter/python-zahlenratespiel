import random
geheimzahl = random.randint(1, 10)
versuche = 3
while versuche > 0:
    eingabe = int(input("Rate eine Zahl zwischen 1 und 10: "))

    if eingabe == geheimzahl:
        print ("Richtig geraten!")
        break
    elif eingabe < geheimzahl:
        print ("Zu niedrig!")
    else:
        print ("Zu hoch!")

    versuche -= 1
    print ("Verbleibende Versuche:", versuche)

if versuche == 0:
    print ("Game over! Die Zahl war:", geheimzahl)