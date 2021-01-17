from random import randint
import grille_joueur

class CJouer:
    def __init__(self):
        self.des = []
        self.g = grille_joueur.CGrille()
        self.nbjoueurs = 0
        self.joueuractif = 1
    
    # def demarrage(self):

    def lancerpartie1j(self):
        """Lancement de la partie un joueur"""
        print("Mode 1 joueur.")
        for i in range(12):
            self.des = []
            self.jouer()
        print("Vous avez fait un total de " + str(self.totalpointsj1()) + " points. (" + str(grille_joueur.JoueurUn.grille) + ")")

    # def lancerpartie2j(self): # etc...

    def jouer(self):
        """Premier tour de jeu"""
        destemporaires = []
        for i in range(5):
            de = randint(1, 6)
            destemporaires.append(de)
        print("vos dés : " + str(destemporaires))
        for i in range(5):
            testverif = None
            while testverif != "oui" and testverif != "non":
                testverif = str(input("Voulez vous garder le dé numéro " + str(i+1) + " (valeur = " + str(destemporaires[i]) + ") ? (oui ou non) "))
                if testverif == "oui":
                    self.des.append(destemporaires[i])
                elif testverif == "non":
                    self.des.append(0)
                else:
                    print("Erreur.")
        print("vos dés gardés : " + str(self.des))
        if 0 in self.des:
            self.deuxiemetour()
            if 0 in self.des:
                self.points3emetour()
            else:
                self.des.sort()
                print("voici vos dés finaux : " + str(self.des))
                self.points()
        else:
            self.des.sort()
            print("voici vos dés finaux : " + str(self.des))
            self.points()

    def deuxiemetour(self):
        """Deuxième tour de jeu si besoin"""
        nbdes = 0
        checksum = 0
        for i in self.des:
            if i == 0:
                nbdes += 1
        destemporaires = []
        for i in range(5):
            if self.des[i] == 0:
                de = randint(1, 6)
                destemporaires.append(de)
        print("votre/vos nouveau(x) dé(s) : " + str(destemporaires))
        for i in range(5):
            if self.des[i] == 0:
                checksum += 1
                testverif = None
                while testverif != "oui" and testverif != "non":
                    testverif = str(input("Voulez vous garder le dé numéro " + str(i+1) + " (valeur = " + str(destemporaires[checksum-1]) + ") ? (oui ou non) "))
                    if testverif == "oui":
                        self.des[i] = destemporaires[checksum-1]
        print("vos dés gardés : " + str(self.des))

    def troisiemetour(self):
        """Troisième tour de jeu si besoin"""
        nbdes = 0
        checksum = 0
        for i in self.des:
            if i == 0:
                nbdes += 1
        destemporaires = []
        for i in range(5):
            if self.des[i] == 0:
                de = randint(1, 6)
                destemporaires.append(de)
        print("votre/vos nouveau(x) dé(s) : " + str(destemporaires))
        for i in range(5):
            if self.des[i] == 0:
                checksum += 1
                self.des[i] = destemporaires[checksum-1]

    def combinaisonspossibles(self):
        """
        Combinaisons possibles du joueur actif
        :return: list
        """
        combpossibles = []
        if self.joueuractif == 1:
            if "1" in self.g.dispojoueur1() and 1 in self.des:
                    combpossibles.append("1")
            if "2" in self.g.dispojoueur1() and 2 in self.des:
                    combpossibles.append("2")
            if "3" in self.g.dispojoueur1() and 3 in self.des:
                    combpossibles.append("3")
            if "4" in self.g.dispojoueur1() and 4 in self.des:
                    combpossibles.append("4")
            if "5" in self.g.dispojoueur1() and 5 in self.des:
                    combpossibles.append("5")
            if "6" in self.g.dispojoueur1() and 6 in self.des:
                    combpossibles.append("6")
            if "brelan" in self.g.dispojoueur1():
                if self.des[0] == self.des[1] == self.des[2] or self.des[1] == self.des[2] == self.des[3] or self.des[2] == self.des[3] == self.des[4]:
                    combpossibles.append("brelan")
            if "petite suite" in self.g.dispojoueur1():
                if self.des[0] == 1 and self.des[1] == 2 and self.des[2] == 3 and self.des[3] == 4 and self.des[4] == 5:
                    combpossibles.append("petite suite")
            if "grande suite" in self.g.dispojoueur1():
                if self.des[0] == 2 and self.des[1] == 3 and self.des[2] == 4 and self.des[3] == 5 and self.des[4] == 6:
                    combpossibles.append("grande suite")
            if "full" in self.g.dispojoueur1():
                if self.des[0] == self.des[1] == self.des[2] and self.des[3] == self.des[4]:
                    combpossibles.append("full")
                if self.des[0] == self.des[1] and self.des[2] == self.des[3] == self.des[4]:
                    if "full" not in combpossibles:
                        combpossibles.append("full")
            if "carre" in self.g.dispojoueur1():
                if self.des[0] == self.des[1] == self.des[2] == self.des[3] or self.des[1] == self.des[2] == self.des[3] == self.des[4]:
                    combpossibles.append("carre")
            if "yam" in self.g.dispojoueur1():
                if self.des[0] == self.des[1] == self.des[2] == self.des[3] == self.des[4]:
                    combpossibles.append("yam")
        return combpossibles

    # def combienjoueurs(self):
    #     while 1 > self.nbjoueurs > 4:
    #         self.nbjoueurs = int(input("Combien de joueurs y a-t-il ? "))
    #         if 1 > self.nbjoueurs > 4:
    #             print("Erreur. Maximum 4 joueurs, minimum 1.")

    def points(self):
        apoint = self.ouajouter()
        if self.joueuractif == 1:
            if apoint == "1":
                totalas = 0
                for i in range(5):
                    if self.des[i] == 1:
                        totalas += 1
                grille_joueur.JoueurUn.grille["1"] = totalas
            if apoint == "2":
                totaldeux = 0
                for i in range(5):
                    if self.des[i] == 2:
                        totaldeux += 2
                grille_joueur.JoueurUn.grille["2"] = totaldeux
            if apoint == "3":
                totaltrois = 0
                for i in range(5):
                    if self.des[i] == 3:
                        totaltrois += 3
                grille_joueur.JoueurUn.grille["3"] = totaltrois
            if apoint == "4":
                totalquatre = 0
                for i in range(5):
                    if self.des[i] == 4:
                        totalquatre += 4
                grille_joueur.JoueurUn.grille["4"] = totalquatre
            if apoint == "5":
                totalcinq = 0
                for i in range(5):
                    if self.des[i] == 5:
                        totalcinq += 5
                grille_joueur.JoueurUn.grille["5"] = totalcinq
            if apoint == "6":
                totalsix = 0
                for i in range(5):
                    if self.des[i] == 6:
                        totalsix += 6
                grille_joueur.JoueurUn.grille["6"] = totalsix
            if apoint == "brelan":
                totalbrelan = 0
                for i in range(5):
                    totalbrelan += self.des[i]
                grille_joueur.JoueurUn.grille["brelan"] = totalbrelan
            if apoint == "petite suite":
                grille_joueur.JoueurUn.grille["petite suite"] = 15
            if apoint == "grande suite":
                grille_joueur.JoueurUn.grille["grande suite"] = 20
            if apoint == "full":
                grille_joueur.JoueurUn.grille["full"] = 30
            if apoint == "carre":
                grille_joueur.JoueurUn.grille["carre"] = 40
            if apoint == "yam":
                grille_joueur.JoueurUn.grille["yam"] = 50
            print("la grille du joueur 1 contient : " + str(grille_joueur.JoueurUn.grille))

    def points3emetour(self):
        apoint = self.ouajouter3emetour()
        self.troisiemetour()
        self.des.sort()
        print("voici vos dés finaux : " + str(self.des))
        if self.joueuractif == 1:
            if apoint == "1":
                totalas = 0
                for i in range(5):
                    if self.des[i] == 1:
                        totalas += 1
                print(totalas)
                grille_joueur.JoueurUn.grille["1"] = totalas
            if apoint == "2":
                totaldeux = 0
                for i in range(5):
                    if self.des[i] == 2:
                        totaldeux += 2
                grille_joueur.JoueurUn.grille["2"] = totaldeux
            if apoint == "3":
                totaltrois = 0
                for i in range(5):
                    if self.des[i] == 3:
                        totaltrois += 3
                grille_joueur.JoueurUn.grille["3"] = totaltrois
            if apoint == "4":
                totalquatre = 0
                for i in range(5):
                    if self.des[i] == 4:
                        totalquatre += 4
                grille_joueur.JoueurUn.grille["4"] = totalquatre
            if apoint == "5":
                totalcinq = 0
                for i in range(5):
                    if self.des[i] == 5:
                        totalcinq += 5
                grille_joueur.JoueurUn.grille["5"] = totalcinq
            if apoint == "6":
                totalsix = 0
                for i in range(5):
                    if self.des[i] == 6:
                        totalsix += 6
                grille_joueur.JoueurUn.grille["6"] = totalsix
            if apoint == "brelan":
                if apoint in self.combinaisonspossibles():
                    totalbrelan = 0
                    for i in range(5):
                        totalbrelan += self.des[i]
                    grille_joueur.JoueurUn.grille["brelan"] = totalbrelan
                else:
                    grille_joueur.JoueurUn.grille[apoint] = 0
            if apoint == "petite suite":
                if apoint in self.combinaisonspossibles():
                    grille_joueur.JoueurUn.grille["petite suite"] = 15
                else:
                    grille_joueur.JoueurUn.grille[apoint] = 0
            if apoint == "grande suite":
                if apoint in self.combinaisonspossibles():
                    grille_joueur.JoueurUn.grille["grande suite"] = 20
                else:
                    grille_joueur.JoueurUn.grille[apoint] = 0
            if apoint == "full":
                if apoint in self.combinaisonspossibles():
                    grille_joueur.JoueurUn.grille["full"] = 30
                else:
                    grille_joueur.JoueurUn.grille[apoint] = 0
            if apoint == "carre":
                if apoint in self.combinaisonspossibles():
                    grille_joueur.JoueurUn.grille["carre"] = 40
                else:
                    grille_joueur.JoueurUn.grille[apoint] = 0
            if apoint == "yam":
                if apoint in self.combinaisonspossibles():
                    grille_joueur.JoueurUn.grille["yam"] = 50
                else:
                    grille_joueur.JoueurUn.grille[apoint] = 0
            print("la grille du joueur 1 contient : " + str(grille_joueur.JoueurUn.grille))

    def ouajouter(self):
        quelajout = 0
        if self.combinaisonspossibles() != []:
            print("Les combinaisons possibles sont : " + str(self.combinaisonspossibles()))
            while quelajout not in self.combinaisonspossibles():
                quelajout = str(input("Où voulez-vous ajouter vos points ? "))
                if quelajout not in self.combinaisonspossibles():
                    print("Erreur. Les combinaisons possibles sont : " + str(self.combinaisonspossibles()))
        else:
            if self.joueuractif == 1:
                print("Les combinaisons possibles sont : " + str(self.g.dispojoueur1()))
                while quelajout not in self.g.dispojoueur1():
                    quelajout = str(input("Où voulez-vous ajouter vos points ? "))
                    if quelajout not in self.g.dispojoueur1():
                        print("Erreur. Les combinaisons possibles sont : " + str(self.g.dispojoueur1()))
        return quelajout

    def ouajouter3emetour(self):
        quelajout = 0
        if self.joueuractif == 1:
            print("Les combinaisons possibles sont : " + str(self.g.dispojoueur1()))
            while quelajout not in self.g.dispojoueur1():
                quelajout = str(input("Où voulez-vous ajouter vos points ? "))
                if quelajout not in self.g.dispojoueur1():
                    print("Erreur. Les combinaisons possibles sont : " + str(self.g.dispojoueur1()))
            return quelajout
        # elif self.joueuractif == 2:
        #     print("Les combinaisons possibles sont : " + str(self.g.dispojoueur2()))
        #     while quelajout not in self.g.dispojoueur2():
        #         quelajout = str(input("Où voulez-vous ajouter vos points ? "))
        #         if quelajout not in self.g.dispojoueur2():
        #             print("Erreur. Les combinaisons possibles sont : " + str(self.g.dispojoueur2()))
        #     return quelajout

    def totalpointsj1(self):
        total1j1 = grille_joueur.JoueurUn.grille["1"] + grille_joueur.JoueurUn.grille["2"] + grille_joueur.JoueurUn.grille["3"] + grille_joueur.JoueurUn.grille["4"] + grille_joueur.JoueurUn.grille["5"] + grille_joueur.JoueurUn.grille["6"]
        print("Total 1 = " + str(total1j1) + ".")
        if total1j1 >= 63:
            total1j1 += 35
            print("Il est égal ou dépasse 63 points, il vaut donc maintenant " + str(total1j1) + " points ! (+35)")
        total2j1 = grille_joueur.JoueurUn.grille["brelan"] + grille_joueur.JoueurUn.grille["petite suite"] + grille_joueur.JoueurUn.grille["grande suite"] + grille_joueur.JoueurUn.grille["full"] + grille_joueur.JoueurUn.grille["carre"] + grille_joueur.JoueurUn.grille["yam"]
        print("Total 2 = " + str(total2j1) + ".")
        totalfinalj1 = total1j1 + total2j1
        return totalfinalj1

# test = CJouer()
# test.lancerpartie1j()
