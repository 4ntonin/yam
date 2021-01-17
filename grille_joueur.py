class CGrille:
    def __init__(self):
        self.grille = {"1": -1, "2": -1, "3": -1, "4": -1, "5": -1, "6": -1, "brelan": -1, "petite suite": -1, "grande suite": -1, "full": -1, "carre": -1, "yam": -1}
        self.grillejoueur = []

    def dispojoueur1(self):
        """Cases disponibles du joueur un"""
        JoueurUn.grillejoueur = []
        for i in JoueurUn.grille:
            if JoueurUn.grille[i] == -1:
                JoueurUn.grillejoueur.append(i)
        return JoueurUn.grillejoueur

    def dispojoueur2(self):
        JoueurDeux.grillejoueur = []
        for i in JoueurDeux.grille:
            if JoueurDeux.grille[i] == -1:
                JoueurDeux.grillejoueur.append(i)
        return JoueurDeux.grillejoueur

    def dispojoueur3(self):
        JoueurTrois.grillejoueur = []
        for i in JoueurTrois.grille:
            if JoueurTrois.grille[i] == -1:
                JoueurTrois.grillejoueur.append(i)
        return JoueurTrois.grillejoueur

    def dispojoueur4(self):
        JoueurQuatre.grillejoueur = []
        for i in JoueurQuatre.grille:
            if JoueurQuatre.grille[i] == -1:
                JoueurQuatre.grillejoueur.append(i)
        return JoueurQuatre.grillejoueur


JoueurUn = CGrille()
JoueurDeux = CGrille()
JoueurTrois = CGrille()
JoueurQuatre = CGrille()

# test = CGrille()
# print(test.dispojoueur1())
