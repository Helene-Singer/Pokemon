import random
from Capacite import Capacite

class Pokemon:

    """_summary_: Classe mère dont le type est 0 ("Normal")
    """

    # constructeur
    def __init__(self, nom : str, pv : int, atk : int, defense : int, vitesse : int, poketype : int = 0) -> None:
        self.set_nom(nom)
        self.set_pv(pv)
        self.set_atk(atk)
        self.set_defense(defense)
        self.set_vitesse(vitesse)
        self.set_poketype(poketype)
        self.__capacite = []
    # setter
    def set_nom(self, valeur : str) -> None:
        if type(valeur) == str:
            self.__nom = valeur
        else:
            raise TypeError("Veuillez renseignez une chaine de caractères.")

    # setter
    def set_pv(self, valeur : int) -> None:
        if type(valeur) == int:
            self.__pv = valeur
        else:
            raise TypeError("Veuillez renseignez un entier.")

    # setter
    def set_atk(self, valeur : int) -> None:
        if type(valeur)== int:
            self.__atk = valeur
        else:
            raise TypeError("Veuillez renseignez un entier.")
    
    # setter
    def set_defense(self, valeur : int) -> None:
        if type(valeur)== int:
            self.__defense = valeur
        else:
            raise TypeError("Veuillez renseignez un entier.")
    
    # setter
    def set_vitesse(self, valeur : int) -> None:
        if type(valeur)== int:
            self.__vitesse = valeur
        else:
            raise TypeError("Veuillez renseignez un entier.")
        
    # setter
    def set_poketype(self, valeur : int) -> None:
        if type(valeur) == int:
            self.__poketype = valeur
        else:
            raise TypeError("Veuillez renseignez un entier.")
    
    # setter
    def set_capacite(self, liste : list) -> None:
        self.__capacite = liste

    # getter
    def get_nom(self) -> str:
        return self.__nom
    
    # getter
    def get_pv(self) -> int:
        return self.__pv
    
    # getter
    def get_atk(self) -> int:
        return self.__atk
    
    # getter
    def get_defense(self) -> int:
        return self.__defense
    
    # getter
    def get_vitesse(self) -> int:
        return self.__vitesse
    
    # getter
    def get_poketype(self)  -> int:
        return self.__poketype
    
    # getter
    def get_capacite(self) -> list:
        return self.__capacite
    
        
    def ajouter_capacite(self, capacite : Capacite) -> None:
        """_summary_: Ajoute une capacité au Pokémon et puisque la liste est privée propre à la classe, on passe par une liste temporaire car le self.set_capacite(self.get_capacite().append(capacite)) retournera "None"

        Args:
            capacite (Capacite): capacité que l'on souhaite ajouter à la liste des capacités du Pokémon
        """
        liste_temporaire = self.get_capacite()
        liste_temporaire.append(capacite)
        self.set_capacite(liste_temporaire)

    def isDead(self) -> bool:
        """_summary_: Retourne un booléen pour indiquer si un Pokémon est K.O. ou non

        Returns:
            _type_: booléen : Si un Pokémon est K.O., retourne vrai, sinon retourne faux
        """
        if self.get_pv() > 0:
            return False
        else:
            return True
        
    def attaquer(self, pokemon2) -> None:
        """_summary_: Permet au Pokémon appelant d'attaquer le Pokémon passé en paramètre. L'attaque déduit l'attaque du Pokémon appelant de la vie du Pokémon pokemon2 attaqué

        Args:
            pokemon2 (Pokemon): Pokémon qui se fait attaquer et qui va perdre de la vie
        """

        # On se rappelle que le type normal = 0, type Eau = 1, type Feu = 2, type Plante = 3

        # affiche l'attaque que le Pokémon utilise
        nom_attaque = ""
        if self.__poketype == 0:
            nom_attaque = "Charge"
        elif self.__poketype == 1:
            nom_attaque = "Pistolet à O"
        elif self.__poketype == 2:
            nom_attaque = "Flammèche"
        else:
            nom_attaque = "Feuillage"
        print(f"{self.__nom} utilise {nom_attaque} !")
        
        # stocke les dégâts qui seront infligés selon les types et les faiblesses
        degats = self.__atk // pokemon2.get_defense()

        # modification des dégâts en fonction des types et des faiblesses
        if(self.__poketype == 2 and pokemon2.get_poketype() == 3) or (self.__poketype == 3 and pokemon2.get_poketype() == 1) or (self.__poketype == 1 and pokemon2.get_poketype() == 2):
            degats *= 2
            print("C'est super efficace !")
        elif not(self.__poketype == 0 or pokemon2.get_poketype() == 0):
            degats = int(degats*0.5)
            print("Ce n'est pas très efficace...")

        # coup critique
        if random.randint(0,23) == 0:
            degats = int(degats * 1.5)
            print("Coup critique !")
        
        # mise à jour des pv du Pokémon et affichage des PV perdus
        pokemon2.set_pv(int(pokemon2.get_pv() - degats))
        if pokemon2.get_pv() > 0:
            print(f"{pokemon2.get_nom()} perd {degats} PV. Il lui en reste {pokemon2.get_pv()}.\n")
        else:
            print(f"{pokemon2.get_nom()} perd {degats} PV.\n")


    def toString(self) -> None:
        """ _summary_: Affiche les informations du Pokémon choisi
        """

        print(f"Nom : {self.get_nom()}\nPV : {self.get_pv()}\nAttaque : {self.get_atk()}\nDéfense : {self.get_defense()}\nVitesse : {self.get_vitesse()}\nType : normal")