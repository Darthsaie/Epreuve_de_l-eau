# Générer toutes les combinaisons possibles de 2 nombres entre 00 et 99
combinaisons = []
for i in range(100):
    for j in range(i + 1, 100):
        combinaisons.append(f"{i:02d} {j:02d}")

# Afficher les combinaisons
print(", ".join(combinaisons))
