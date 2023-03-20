import sys
# Vérifier si au moins un argument est passé
if len (sys.argv) <2:
    print("Erreur : Veuillez entrer au moins un argument.")
    sys.exit(1)

# Récupérer les arguments passés en ligne de commande
args = sys.argv[1:]

# Inverser l'ordre des arguments
for i in range(len(args) // 2):
    args[i], args[-i-1] = args[-i-1], args [i]

# Afficher les arguments à l'envers
for arg in args:
    print(arg)