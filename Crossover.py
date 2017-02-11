import random
import copy


class Crossover:

    # two chromosomes to generate two children
    def __init__(self, chromosomes, crossover_rate):
        self.parent1 = chromosomes[0]
        self.parent2 = chromosomes[1]
        self.crossover_rate = crossover_rate
        self.crossed = []

    def crossover(self):

        # if random.random() <= self.crossover_rate:
        if self.crossover_rate <= 1:
            cross_point = random.randint(1, len(self.parent1) - 1)
            # [:x]-> from the beginning of array to x
            child1 = self.parent1[:cross_point] + self.parent2[cross_point:]
            # [x:]-> from x to the end
            child2 = self.parent2[:cross_point] + self.parent1[cross_point:]

        else:
            # Make copy of parents
            child1 = copy.deepcopy(self.parent1)
            child2 = copy.deepcopy(self.parent2)

        self.crossed = [self.parent1, self.parent2, child1, child2]

    def get_crossed(self):
        return self.crossed
