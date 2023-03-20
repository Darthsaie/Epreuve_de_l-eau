import sys

if len(sys.argv) != 3:
    # Si le nombre d'arguments est différents de 3, on affiche "error et on quitte le programme"
    sys.exit()

# On récupère les deux arguments passés en ligne de commande
mot = sys.argv[1]
sous_mot = sys.argv[2]

if mot.find(sous_mot) != -1:
    # Si le mot se trouve dans le mot, on affiche "true"
    print("true")
else:
    # Sinon, on affiche "false"
    print("false")

    