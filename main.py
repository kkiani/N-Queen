from random import randint
from listOperator import *
import copy
from chromosome import *
import Test
import view


initPopulationSize = 20
breakPoint = 4
mutationRatio = 0.01
generation = 100

population = Population() #Test.makePopulation()



def init():
	global initPopulationSize
	global population

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
	genes = [0, 1, 2, 3, 4, 5, 6, 7]

	child = Chromosome([-1, -1, -1, -1, -1, -1, -1, -1])
	for i in range(0 , breakPoint):
		child[i] = chromosome1[i]

	j = breakPoint
	for i in range(breakPoint, genes.__len__()):


		if chromosome2[i] not in child:
			child[j] = chromosome2[i]
			j = j + 1

	gencopy = copy.deepcopy(genes)
	availabeGens = subList(gencopy, child)
	for i in range(j, child.__len__()):
		child[i] = availabeGens[i-j]

	return child


def generate_random_chromosome():

	chromosome = Chromosome([0, 0, 0, 0, 0, 0, 0, 0])
	genes = [0, 1, 2, 3, 4, 5, 6, 7]
	for i in range(0,8):
		randGenIndex = randint(0,genes.__len__() - 1)
		randGen = genes[randGenIndex]
		genes.remove(randGen)
		chromosome[i] = randGen

	return chromosome


def main():
	global population
	global mutationRatio
	global generation

	bests = Population()
	bests.append(population.bestChromosome())

	fitAnswer = 0
	generation_counter = 0
	while fitAnswer != 28 and generation_counter < generation:
		new_generation = Population()
		for j in range(0, initPopulationSize):
			parent1, parent2 = selection(mutation_pool())
			child = crossover(parent1, parent2)
			new_generation.append(child)

		population.mutating(mutationRatio)

		new_generation.append(population.bestChromosome())
		population = new_generation
		new_generation_best_answer = population.bestChromosome()
		bests.append(new_generation_best_answer)

		fitAnswer = new_generation_best_answer.fitness()
		print("Generation " + str(generation_counter) + ": " + str(new_generation_best_answer) + " fitness: " + str(
			new_generation_best_answer.fitness()))

		generation_counter = generation_counter + 1

	# for i in range(0, generation):	#generations


	# for item in bests:
	# 	print(str(item) + " : " + str(item.fitness()))
	answer = bests.bestChromosome()
	print("-----------------------------------------------------")
	print("|  Best answer: " + str(answer) + " fitness:" + str(answer.fitness()) + "  |")
	print("-----------------------------------------------------")
	view.showChromosome(answer)
	print(answer)

init()
main()
# print(population.bestChromosome())
# print(mutation_pool())
# print(fitness([0, 1, 2, 3, 4, 5, 6, 7]))
# print(population[0].fitness())
# print(population[4])
# print(crossover(population[0], population[4]))


