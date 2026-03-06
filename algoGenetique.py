from reseauNeurone import ReseauNeurone
import numpy as np

class AlgoGenetique:
    def __init__(self, populationSize=100, mutationRate=0.01, eliteRate=0.1):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.eliteRate = eliteRate
        self.meilleurScore = 0
        self.generations = 0
        self.historiqueScores = []
        self.population = []

    def initialiserPopulation(self, nbEntrees=2, nbCouches=1, nbNeuronesParCouche=4):
        self.population = [
            ReseauNeurone(nbEntrees, nbCouches, nbNeuronesParCouche, 1) 
            for _ in range(self.populationSize)
        ]

    def selection(self):
        """Sélectionne les meilleurs individus"""
        self.population.sort(key=lambda x: x.fitness, reverse=True)

        # Sauvegarde le meilleur score
        if self.population[0].fitness > self.meilleurScore:
            self.meilleurScore = self.population[0].fitness

        self.historiqueScores.append(self.meilleurScore)

        nb_elites = int(self.populationSize * self.eliteRate)
        elites = self.population[:nb_elites]

        return elites
    
    def crossover(self, parent1, parent2):
        """Crée un enfant à partir de deux parents"""
        enfant = parent1.copy()
        
        for i in range(len(enfant.poids)):
            masque = np.random.random(enfant.poids[i].shape) > 0.5
            enfant.poids[i] = np.where(masque, parent1.poids[i], parent2.poids[i])
            
        return enfant
    
    def newGeneration(self):
        """Crée une nouvelle génération"""
        elites = self.selection()
        nouvelle_pop = elites.copy()
        
        # Compléter avec des enfants
        while len(nouvelle_pop) < self.populationSize:
            # Sélection par tournoi
            parent1 = elites[np.random.randint(0, len(elites))]
            parent2 = elites[np.random.randint(0, len(elites))]
            
            enfant = self.crossover(parent1, parent2)
            enfant.mutation(self.mutationRate)
            nouvelle_pop.append(enfant)
        
        self.population = nouvelle_pop
        self.generations += 1
        
        print(f"Génération {self.generations} - Meilleur score: {self.meilleurScore}")
