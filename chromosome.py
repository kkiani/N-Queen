import random
import copy


class Chromosome(list):

	def __new__(cls, *args, **kwargs):
		obj = super(Chromosome, cls).__new__(cls, *args, **kwargs)
		return obj

	def __init__(self, *args):
		super(Chromosome, self).__init__(*args)

	def fitness(self):

		error = 0

		for i in range(0, self.__len__()):
			for j in range(i + 1, self.__len__()):
				if abs(self[i] - self[j]) == abs(i - j):
					error += 1

		return 28 - error


class Population(list):

	def __init__(self, *args):
		super(Population, self).__init__(*args)

	def Efitness(self):
		ef = 0

		for item in self:
			ef = ef + item.fitness()

		return ef

	def bestChromosome(self):
		best = self[0]

		for item in self:
			# print(item.fitness())
			if item.fitness() > best.fitness():
				best = item
		# print(best.fitness())
		return best

	def __mutan_chromosome(self, chromosome):
		indexes = random.sample(range(0, chromosome.__len__() - 1), 2)
		chromosome[indexes[0]], chromosome[indexes[1]] = chromosome[indexes[1]], chromosome[indexes[0]]

	def mutating(self, ratio = 0.01):
		numberOfMutans = int(ratio * self.__len__())

		if numberOfMutans <= 0 : numberOfMutans = 1

		selected_mutens_index = random.sample(range(0, self.__len__()), numberOfMutans)
		for index in selected_mutens_index:
			self.__mutan_chromosome(self[index])

	def __sortByFitness(self):
		for i in range(0, self.__len__()):
			for j in range(i, self.__len__()):
				if self[i].fitness() < self[j].fitness():
					self[i], self[j] = self[j], self[i]


	def NextGeneration(self, SelectionRatio, childs):

		mergedGeneration = copy.deepcopy(self)
		mergedGeneration.extend(childs)
		nextGeneration = Population()

		mergedGeneration.__sortByFitness()
		selectingSize = int(mergedGeneration.__len__() * SelectionRatio)

		for i in range(0, selectingSize):
			nextGeneration.append(mergedGeneration.pop(i))

		for i in range(0, self.__len__() - nextGeneration.__len__()):
			index = random.randint(0, mergedGeneration.__len__() - 1)
			nextGeneration.append(mergedGeneration.pop(index))

		return nextGeneration

