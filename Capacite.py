class Capacite:
    """_summary_: Classe permettant de créer une capacité
    """

    # constructeur
    def __init__(self, nom : str, puissance : int, precision : int, points_pouvoirs : int, type : int) -> None:
        self.set_nom(nom)
        self.set_puissance(puissance)
        self.set_precision(precision)
        self.set_points_pouvoirs(points_pouvoirs)
        self.set_type(type)

    # setter
    def set_nom(self, valeur) -> None:
        if type(valeur) == str:
            self.__nom = valeur
        else:
            raise TypeError("Veuillez renseignez une chaine de caractères.")
        
    # setter
    def set_puissance(self, valeur) -> None:
        if type(valeur) == int:
            self.__puissance = valeur
        else:
            raise TypeError("Veuillez renseignez un entier.")
        
    # setter
    def set_precision(self, valeur) -> None:
        if type(valeur) == int:
            self.__precision = valeur
        else:
            raise TypeError("Veuillez renseignez un entier.")
        
    # setter
    def set_points_pouvoirs(self, valeur) -> None:
        if type(valeur) == int:
            self.__points_pouvoirs = valeur
        else:
            raise TypeError("Veuillez renseignez un entier.")
        
    # setter
    def set_type(self, valeur) -> None:
        if type(valeur) == int:
            self.__type = valeur
        else:
            raise TypeError("Veuillez renseignez un entier.")
        
    # getter
    def get_nom(self) -> str:
        return self.__nom
    
    # getter
    def get_puissance(self) -> int:
        return self.__puissance
        
    # getter
    def get_precision(self) -> int:
        return self.__precision
        
    # getter
    def get_points_pouvoirs(self) -> int:
        return self.__points_pouvoirs
    
    # getter
    def get_type(self) -> int:
        return self.__type