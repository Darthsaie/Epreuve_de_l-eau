# Générer toutes les combinaisons possibles de 3 chiffres différents
combinaisons = []
for i in range(10):
    for j in range(i + 1, 10):
        for k in range(j + 1, 10):
            combinaisons.append(f"{i}{j}{k}")

# Afficher les combinaisons
print(", ".join(combinaisons))