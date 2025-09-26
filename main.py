#### Fonction secondaire


def ispalindrome(p):

    # Transformer tous les lettres en minuscule
    p = p.lower()

    # Supprimer les caractères spéciaux
    # isalmum vérifice is c est alphanumeric
    p = ''.join(c for c in p if c.isalnum())

    # Supprimer les accents
    # c
    p = p.replace('ç','c')

    # o
    p = p.replace('ô','o')

    # a
    p = p.replace('à','a')
    p = p.replace('â','a')

    # i
    p = p.replace('î','i')
    p = p.replace('ï','i')

    # u
    p = p.replace('ù','u')
    p = p.replace('û','u')
    p = p.replace('ü','u')

    # e
    p = p.replace('é','e')
    p = p.replace('è', 'e')
    p = p.replace('ê', 'e')
    p = p.replace('ë', 'e')


    # Vérfication de palindrome
    temp = p[::-1]
    # print(p)
    # print(temp)
    if p == temp:
        return True

    return False

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
