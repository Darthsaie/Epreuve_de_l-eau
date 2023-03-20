import sys

# Vérifier si au moins un argumlents est passé
if len(sys.argv) != 2:
    print("Erreur : Veuillez entrer un seul argument représentant l'index de l'élément de la suite de Fibonacci à afficher.")
    sys.exit(1)

# Récupérer l'argument et le convertir en entier
try:
    n = int(sys.argv[1])
except ValueError:
    print("Erreur : L'argument doit être un entier.")
    sys.exit(1)

# Vérrifier si l'index est positif
if n < 0:
    print("-1")
    sys.exit(1)

# Calculer le n-ème de la suite de Fibonacci
a, b = 0, 1
for i in range(n):
    a, b = b, a+b

# Afficher le résultat
print(a)

