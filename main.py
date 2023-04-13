from Dresseur import Dresseur
from Capacite import Capacite
from Pokemon import Pokemon
from PokemonEau import PokemonEau
from PokemonFeu import PokemonFeu
from PokemonPlante import PokemonPlante
import random

def prioSelonVitesse(dresseur1 : Dresseur, dresseur2 : Dresseur, k = int, i = int) -> tuple:
    # si le premier Pokémon du deuxième dresseur est plus rapide, il attaquera en premier
    if dresseur2.pokemon[i].get_vitesse() > dresseur1.pokemon[k].get_vitesse():
        return dresseur2, dresseur1, k, i

def combat(dresseur1 : Dresseur, dresseur2 : Dresseur) -> None:
    """_summary_: Permet à deux dresseurs de se battre en appelant des Pokémon au combat

    Args:
        dresseur1 (Dresseur): premier dresseur du combat
        dresseur2 (Dresseur): deuxième dresseur du combat
    """

    # deux dresseurs se battent et envoient leur Pokémon sur le terrain
    print(f"{dresseur1.get_nom()} et {dresseur2.get_nom()} veulent se battre !\n")
    print(f"{dresseur1.get_nom()} envoie un {dresseur1.pokemon[0].get_nom()} !")
    print(f"{dresseur2.get_nom()} envoie un {dresseur2.pokemon[0].get_nom()} !\n")

    # compteurs pour savoir à quel Pokémon on est
    k = i = 0

    dresseur1, dresseur2, i, k = prioSelonVitesse(dresseur1, dresseur2, k, i)

    # tant qu'on n'est pas au dernier Pokémon de l'un des dresseurs
    while k != len(dresseur1.pokemon) and i != len(dresseur2.pokemon):
    #while 10 > 11:
        # dresseur1.pokemon[k].toString()
        # print("")
        # dresseur2.pokemon[i].toString()
        # print("")

        while (not dresseur1.pokemon[k].isDead() or not dresseur2.pokemon[i].isDead()):

            dresseur1.pokemon[k].attaquer(dresseur2.pokemon[i])
            if dresseur2.pokemon[i].isDead():
                print(f"{dresseur2.pokemon[i].get_nom()} est K.O.")
                print(f"{dresseur1.pokemon[k].get_nom()} a gagné {random.randint(12,100)} points d'expérience.\n")
                i += 1
                if i == len(dresseur2.pokemon):
                    print(f"{dresseur1.get_nom()} a remporté le combat !")
                else:
                    print(f"{dresseur2.get_nom()} envoie un {dresseur2.pokemon[i].get_nom()} !\n")
                    #dresseur1, dresseur2, i, k = prioSelonVitesse(dresseur1, dresseur2, k, i)
                break
            
            dresseur2.pokemon[i].attaquer(dresseur1.pokemon[k])
            if dresseur1.pokemon[k].isDead():
                print(f"{dresseur1.pokemon[k].get_nom()} est K.O.")
                print(f"{dresseur2.pokemon[i].get_nom()} a gagné {random.randint(12,100)} points d'expérience.\n")
                k += 1
                if k ==  len(dresseur1.pokemon):
                    print(f"{dresseur2.get_nom()} a remporté le combat !")
                else:
                    print(f"{dresseur1.get_nom()} envoie un {dresseur1.pokemon[k].get_nom()} !\n")
                    #dresseur1, dresseur2, i, k = prioSelonVitesse(dresseur1, dresseur2, k, i)
                break


evoli = Pokemon("Évoli", 300, random.randint(49,61), random.randint(10, 20), 0)
evoli.ajouter_capacite(capacite=Capacite("Charge",10,10,10,0))
print(evoli.get_capacite()[0].get_nom())
carapuce = PokemonEau("Carapuce", 300, random.randint(49,61), random.randint(10, 20), random.randint(45,65))
salameche = PokemonFeu("Salamèche", 300, random.randint(49,61), random.randint(10, 20),10)
salameche.ajouter_capacite(capacite=Capacite("Flamèche",20,10,20,0))
bulbizarre = PokemonPlante("Bulbizarre", 300, random.randint(49,61), random.randint(10, 20), random.randint(45,65))
mysterbe = PokemonPlante("Mysterbe", 300, random.randint(49,61), random.randint(10, 20), random.randint(45,65))


# liste_poke1 = [evoli, carapuce]
# liste_poke2 = [salameche, mysterbe]
liste_poke1 = [evoli]
liste_poke2 = [salameche]
# création des dresseurs
liste_dresseur = ["Lorgane la Jeune Sportive", "Kendall le Gamin", "Lumi la Petite", "Guylain le Dresseur en Herbe", "Samia la Prof", "Tili le Dresseur", "Adelaïde la Fillette", "Sbire de la Team Rocket", "Althéo le Capitaine", "Kala le Canon", "Ikue l'Éleveuse", "Léonard le Gentleman", "Yoshio l'Employé", "James de la team Rocket", "Jeff le Petit", "Ayumi la Randonneuse", "Vijay l'Éleveur", "Fedra la Petite", "Chaz le Topdresseur", "Pectorius le Doyen", "Henri le Groom", "Alexis le Vacancier", "Gibus le Cuisinier", "Jessie de la Team Rocket"]
dresseur1 = Dresseur(liste_dresseur[random.randint(0,len(liste_dresseur)-1)], liste_poke1)
dresseur2 = Dresseur(liste_dresseur[random.randint(0,len(liste_dresseur)-1)], liste_poke2)


#capacité : 20 à 100

# 0 = physique, 1 = spécial
feuillage = Capacite("Feuillage", 40, 100, 40, 0)
feuille_magik = Capacite("Feuille Magik", 60, 100, 20, 1)
vive_attaque = Capacite("Vive-Attaque", 40, 100, 30, 0)
canon_graine = Capacite("Canon Graine", 80, 100, 15, 0)
eco_sphere = Capacite("Éco-Sphère", 90, 100, 10, 1)
tempete_verte = Capacite("Tempête Verte", 130, 90,  0, 0)
liste_capacite = []


# création des Pokémon
# evoli = Pokemon("Évoli", random.randint(45,55), random.randint(49,61), random.randint(10, 20), random.randint(45,65))
# carapuce = PokemonEau("Carapuce", random.randint(45,55), random.randint(49,61), random.randint(10, 20), random.randint(45,65))
# salameche = PokemonFeu("Salamèche", random.randint(45,55), random.randint(49,61), random.randint(10, 20), random.randint(45,65))
# bulbizarre = PokemonPlante("Bulbizarre", random.randint(45,55), random.randint(49,61), random.randint(10, 20), random.randint(45,65))

evoli = Pokemon("Évoli", 300, random.randint(49,61), random.randint(10, 20), 0)
carapuce = PokemonEau("Carapuce", 300, random.randint(49,61), random.randint(10, 20), random.randint(45,65))
salameche = PokemonFeu("Salamèche", 300, random.randint(49,61), random.randint(10, 20), random.randint(45,65))
bulbizarre = PokemonPlante("Bulbizarre", 300, random.randint(49,61), random.randint(10, 20), random.randint(45,65))
liste_pokemon = [evoli, carapuce, salameche, bulbizarre]

combat(dresseur1, dresseur2)
#combat(dresseur1, dresseur2, liste_pokemon[random.randint(0,len(liste_pokemon)-1)], liste_pokemon[random.randint(0,len(liste_pokemon)-1)])