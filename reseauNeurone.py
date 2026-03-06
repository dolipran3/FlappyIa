import numpy as np

class ReseauNeurone:
    def __init__(self, nbEntrees = 2, nbCouches = 1, nbNeuronesParCouche = 4, nbSorties = 1):
        self.nbEntrees = nbEntrees
        self.nbCouches = nbCouches
        self.nbNeuronesParCouche = nbNeuronesParCouche
        self.nbSorties = nbSorties
        self.poids = []
        self.fitness = 0

        for i in range(nbCouches):
            if i == 0:
                self.poids.append(np.random.uniform(-1, 1, (nbEntrees, nbNeuronesParCouche)))
            else:
                self.poids.append(np.random.uniform(-1, 1, (nbNeuronesParCouche, nbNeuronesParCouche)))
        self.poids.append(np.random.uniform(-1, 1, (nbNeuronesParCouche, nbSorties)))

    def activation(self, x):
        return 1 / (1 + np.exp(-x))
    
    def threshold(self, x):
        return 1 if x > 0 else 0
    
    def copy(self):
        copie = ReseauNeurone(self.nbEntrees, self.nbCouches, self.nbNeuronesParCouche, self.nbSorties)
        copie.poids = [np.copy(p) for p in self.poids]
        return copie
    
    def mutation(self, tauxMutation=0.1):
        for i in range(len(self.poids)):
            masque = np.random.random(self.poids[i].shape) < tauxMutation
            self.poids[i] += masque * np.random.uniform(-0.5, 0.5, self.poids[i].shape)

    def feedforward(self, entree):
        sortie = entree
        for i in range(self.nbCouches):
            sortie = self.activation(np.dot(sortie, self.poids[i]))
        sortie = self.threshold(np.dot(sortie, self.poids[-1]))
        return sortie

if __name__ == "__main__":
    nbEntrees = 2
    nbCouches = 1
    nbNeuronesParCouche = 4
    nbSorties = 1

    reseau = ReseauNeurone(nbEntrees, nbCouches, nbNeuronesParCouche, nbSorties)

    print("couches d'entrée :")
    print(reseau.poids[0])

    print("couche cachée :")
    for i in range(1, nbCouches):
        print(reseau.poids[i])

    print("couche de sortie :")
    print(reseau.poids[-1])

    entree = np.array([0.5, 0.2])
    sortie = reseau.feedforward(entree)
    print("Sortie du réseau de neurones :", sortie)