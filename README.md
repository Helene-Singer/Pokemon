# Projet Pokémon


## Description

Ce projet est un projet d'entrainement à la POO en Python. Il a pour but de créer des combats de Pokémon. J'ai suivi l'énoncé donné lors de la formation Data Engineer chez M2i, mais j'ai pris quelques libertés. Le voici ci-dessous.

## Énoncé
> Vous connaissez certainement tous ces petites bêtes toute mignonnes (ou pas pour certaines). Ces petites créatures sont dressées par des "dresseurs de Pokémon" et sont amenées à combattre entre elles. Et bien, nous allons aussi les faire combattre !
>
> Les Pokémon sont certes de très mignonnes créatures, mais ils sont également un bon exemple pour illustrer l’héritage.
>
> Je vous propose de commencer par créer une classe "Pokemon" qui contient les champs suivants : 
> - un attribut nom qui représente le nom du Pokémon.
> - un attribut hp (pour Health Points) qui représente les points de vie du Pokémon.
> - un attribut qui s’appelle atk qui représente la force de base de l’attaque du Pokémon.
> - un constructeur pour instancier des Pokémon adéquatement.
> - une méthode isDead() qui retourne un boolean pour indiquer si un Pokémon est mort (hp == 0) ou non.
>
> Créez une méthode "attaquer(Pokemon p)" qui permet au Pokémon appelant d’attaquer le Pokémon passé en paramètre. L’attaque déduit atk points de la vie hp du Pokémon attaqué p. Redéfinissez la méthode toString() qui va nous permettre d'afficher les informations du Pokémon.
>
> En plus des Pokémon de type Normal (décrits à travers la classe Pokemon), on recense trois types de Pokémon (en réalité il existe 17 types en tout mais on ne va pas s’amuser à tous les coder) :
> - les Pokémon de type Feu
> - les Pokémon de type Eau
> - les Pokémon de type Plante 
>
> Les Pokémon de type Feu sont super efficaces contre les Pokémon de type Plante et leur infligent deux fois plus de dégâts (2 x atk). Par contre, ils sont très peu efficaces contre les Pokémon de type Eau ou de type Feu et ne leur infligent que la moitié des dégâts (0.5 x atk). Ils infligent des dégâts normaux aux Pokémon de type Normal.
>
> Les Pokémon de type Eau sont super efficaces contre les Pokémon de type Feu et leur infligent deux fois plus de dégâts (2 x atk). Par contre, ils sont très peu efficaces contre les Pokémon de type Eau ou de type Plante et ne leur infligent que la moitié des dégâts (0.5 x atk). Ils infligent des dégâts normaux aux Pokémon de type Normal.
>
> Les Pokémon de type Plante sont super efficaces contre les Pokémon de type Eau et leur infligent deux fois plus de dégâts (2 x atk). Par contre, ils sont très peu efficaces contre les Pokémon de type Plante ou de type Feu et ne leur infligent que la moitié des dégâts (0.5 x atk). Ils infligent des dégâts normaux aux Pokémon de type Normal.
>
> Créez trois classes :
> - PokemonFeu
> - PokemonEau
> - PokemonPlante
> 
> Ces classes héritent de la classe Pokemon et représentent les trois types de Pokémon susmentionnés.
> 
> Ensuite, amusez-vous à faire des combats de Pokémon.