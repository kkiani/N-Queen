from random import randint
from listOperator import *
import copy
from chromosome import *
import Test
import view


initPopulationSize = 30
breakPoint = 4
mutationRatio = 0.25
generation = 100
selectionRatioOnGeneration = 0.15
Gens_Length = 8

population = Population() #Test.makePopulation()
gens = Chromosome()


def init():
	global initPopulationSize
	global population
	global Gens_Length
	global gens

	for i in range(0, Gens_Length):
		gens.append(i)

	for i in range(0, initPopulationSize):
		new_chromosome = generate_random_chromosome()
		population.append(new_chromosome)


def prob(chromosome=Chromosome()):
	return chromosome.fitness()/population.Efitness()

def mutation_pool():
	pool = []
	for item in population:
		CHNumber = int(prob(item) * 100)
		for i in range(0, CHNumber):
			pool.append(copy.deepcopy(item))

	return pool

def selection(pool=[]):
	parent1_I = randint(0, pool.__len__() - 1)
	parent2_I = randint(0, pool.__len__() - 1)

	return pool[parent1_I], pool[parent2_I]

def crossover(chromosome1=Chromosome(), chromosome2=Chromosome()):
	global gens

	gens_copy = copy.deepcopy(gens)
	child = Chromosome(copy.deepcopy(gens))
	for i in range(0 , breakPoint):
		child[i] = chromosome1[i]

	j = breakPoint
	for i in range(breakPoint, gens_copy.__len__()):
		if chromosome2[i] not in child[:breakPoint]:
			child[j] = chromosome2[i]
			j = j + 1

	gencopy = copy.deepcopy(gens)
	availabeGens = subList(gencopy, child[:j])
	for i in range(j, child.__len__()):
		child[i] = availabeGens[i-j]

	return child


def generate_random_chromosome():
	global gens

	chromosome = Chromosome(copy.deepcopy(gens))
	gens_copy = copy.deepcopy(gens)
	for i in range(0,gens_copy.__len__()):
		randGenIndex = randint(0,gens_copy.__len__() - 1)
		randGen = gens_copy[randGenIndex]
		gens_copy.remove(randGen)
		chromosome[i] = randGen

	return chromosome


def main():
	global population
	global mutationRatio
	global generation
	global gens

	bests = Population()
	bests.append(population.bestChromosome())

	fitAnswer = 0
	generation_counter = 0
	while fitAnswer != gens.fullScore() and generation_counter < generation:
		population_childs = Population()
		for j in range(0, initPopulationSize):
			parent1, parent2 = selection(mutation_pool())
			child = crossover(parent1, parent2)
			population_childs.append(child)

		population.mutating(mutationRatio)

		population = population.NextGeneration(selectionRatioOnGeneration, population_childs)
		
		nextGenerationBestAnswer = population.bestChromosome()
		bests.append(nextGenerationBestAnswer)

		fitAnswer = nextGenerationBestAnswer.fitness()
		print("Generation " + str(generation_counter) + ": " + str(nextGenerationBestAnswer) + " fitness: " + str(
			nextGenerationBestAnswer.fitness()))

		generation_counter = generation_counter + 1

	# for i in range(0, generation):	#generations


	# for item in bests:
	# 	print(str(item) + " : " + str(item.fitness()))
	answer = bests.bestChromosome()
	print("-----------------------------------------------------")
	print("|  Best answer: " + str(answer) + " fitness:" + str(answer.fitness()) + "  |")
	print("-----------------------------------------------------")
	view.showChromosome(answer, Gens_Length)
	print(answer)

init()
main()
# print(population.bestChromosome())
# print(mutation_pool())
# print(fitness([0, 1, 2, 3, 4, 5, 6, 7]))
# print(population[0].fitness())
# print(population[4])
# print(crossover(population[0], population[4]))


