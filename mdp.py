mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."



if len(mdp) in range(1,8) :
    print(mdp_trop_court.capitalize())
elif len(mdp) == 0 : 
    print(mdp_trop_court.upper())
elif mdp.isdigit() is True :
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Inscription terminée.")