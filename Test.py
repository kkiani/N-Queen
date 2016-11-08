from chromosome import *

populationTest = [[1, 3, 0, 6, 4, 2, 7, 5], [0, 5, 7, 6, 1, 3, 2, 4], [3, 6, 7, 1, 2, 4, 0, 5], [4, 2, 1, 5, 0, 6, 7, 3], [4, 0, 3, 6, 7, 5, 2, 1], [4, 0, 7, 6, 1, 2, 3, 5], [7, 0, 4, 1, 6, 2, 3, 5], [4, 2, 5, 6, 7, 0, 1, 3], [3, 6, 4, 5, 0, 2, 7, 1], [0, 2, 5, 6, 4, 7, 3, 1]]

def makePopulation():
	population = Population()
	for item in populationTest:
		converted_chromosome = Chromosome(item)
		population.append(converted_chromosome)

	return population


def readableCHromosome(chromosome= Chromosome()):
	for i in range(0, chromosome.__len__()):
		chromosome[i] = chromosome[i] + 1
