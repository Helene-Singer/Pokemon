from Pokemon import Pokemon

class Dresseur:
    """_summary_: Classe permettant de créer un dresseur
    """

    # constructeur
    def __init__(self, nom : str, liste_pokemon : list) -> None:
        self.set_nom(nom)
        self.pokemon = liste_pokemon
    
    # setter
    def set_nom(self, valeur) -> None:
        if type(valeur) == str:
            self.__nom = valeur
        else:
            raise TypeError("Veuillez renseignez une chaine de caractères.")
        
    # getter
    def get_nom(self) -> str:
        return self.__nom
    