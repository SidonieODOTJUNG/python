import random

nb_mystere = random.randint(0, 10)


essai = 0


while essai < 5 :
    essai += 1
    nb = input("Choisi un nombre entre 0 et 10 : ")
    
    if nb.isdigit() :
        nb = int(nb)
    
        if nb > nb_mystere:
            print(f"Le nombre mystère est plus petit que {nb}")
        elif nb < nb_mystere:
            print(f"Le nombre mystère est plus grand que {nb}")
        elif nb == nb_mystere:
            print("Bravo, vous avez trouvé le nombre mystère ! \nVous avez gagné!")
            break
    elif essai == 5:
        print (f"Vous avez perdu! \nLe nombre mystère était : {nb_mystere}.")
    else:
        print("SVP, entrez un nombre valide.")  