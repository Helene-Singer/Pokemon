from Pokemon import Pokemon

class PokemonPlante(Pokemon):

    """_summary_: Classe fille de la classe Pokemon dont le type est 3 ("Plante")
    """

    # constructeur
    def __init__(self, nom : str, pv : int, atk : int, defense : int, vitesse : int) -> None:
        super().__init__(nom, pv , atk, defense, vitesse, 3)

    # redéfinition
    def toString(self) -> None:
        """_summary_: Affiche les informations du Pokémon choisi
        """
        print(f"Nom : {super().get_nom()}\nPV : {super().get_pv()}\nATK : {super().get_atk()}\nDéfense : {self.get_defense()}\nVitesse : {super().get_vitesse()}\nType : plante")