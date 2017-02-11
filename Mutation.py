import random


class Mutation:

    def __init__(self, chromosome):
        # list will contain 4 element from crossover
        self.chromosome = chromosome
        # create list that contain the list from crossover and after mutation  will contain 8 elements
        self.final_chromosome = chromosome

    def mutation(self):
        for i in range(0, 4):
            # convert string to list
            temp_list = list(self.chromosome[i])

            # generate random number
            mutate_bit = random.randint(0, len(self.chromosome[i]) - 1)

            if temp_list[mutate_bit] == "1":
                temp_list[mutate_bit] = "0"

            elif temp_list[mutate_bit] == "0":
                temp_list[mutate_bit] = "1"

            # convert list to string and add to final_chromosome
            self.final_chromosome.append("".join(temp_list))

    def get_chromosomes(self):
        return self.final_chromosome
