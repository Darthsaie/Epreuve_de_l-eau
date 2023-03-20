import sys

# Fonction qui vérifie si un nombre est premier ou non
def est_premier(n):
    # Un nombre premier est un nombre entier naturel qui est divisible uniquement par 1 et par lui-même
    # On peut donc commencer à tester s'il est divisible par 2
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 2:
    # Si le nombre d'arguments est différent de 2, on affiche -1
    print("-1")
else:
    try:
        num = int(sys.argv[1])
        if num < 0:
            # Si le nombre est négatif, on affiche -1
            print("-1")
        else:
            prime = num + 1
            while not est_premier(prime):
                # Tant que le nombre n'est pas premier, on incrémente prime de 1 et on teste à nouveau
                prime += 1
            # Une fois qu'on a trouvé le premier nombre premier supérieur à num, on l'affiche
            print(prime)
    except ValueError:
        # Si l'argument n'est pas un nombre entier, on affiche -1
        print("-1")
