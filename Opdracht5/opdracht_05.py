#maak hier een functie voor een top 3 van bijvoorbeeld je favoriete games, eten of iets anders
#elke keer dat je de functie aanroept voeg je een nieuwe game toe als parameter
#weet je niet meer hoe? Check het solution filmpje op: https://www.linkedin.com/learning/programming-foundations-fundamentals-3/solution-favorite-cities

def favoriete_albums(name):
    print("een van mijn favoriete albums is", name)
    if (name == 1):
        print("divide, Ed Sheeran")
    if (name == 2):
        print ("continuum, John Mayer")
    if (name == 3):
        print ("tryhard, The band camino")

favoriete_albums(1)
favoriete_albums(2)
favoriete_albums(3)