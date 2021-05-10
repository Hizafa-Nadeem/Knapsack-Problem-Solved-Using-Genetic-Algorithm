
import random



def calculate_fitness(solution):
    fitness_of_sol = 0
    for item in range(len(solution)):
        if solution[item] * weights[item] < kw:
            fitness_of_sol += solution[item] * values[item]
    return fitness_of_sol
def cross_over(parent_solution1, parent_solution2):
    parent_solution1[5:10], parent_solution2[0:5] = parent_solution2[0:5], parent_solution1[5:10]

def mutation(parent_solution):
    r = random.sample(range(0, 9), 3)
    #print("random", r)
    for i in r:
        parent_solution[i] ^= 1


def generate_offspring(parent_solution1 , parent_solution2) -> object:

    # crossover
    # print("parent solution before", parent_solution1, parent_solution2)
    cross_over(parent_solution1, parent_solution2)

    # print("parent solution after", parent_solution1, parent_solution2)
    mutation(parent_solution1)
    mutation(parent_solution2)
    print("parent solution after mutation ", parent_solution1, parent_solution2)
    
    return parent_solution1 ,parent_solution2

def Get_Best_Solution():
    ind = list(fitness.keys())[0]
    print("Best Solution!")
    Total_Amount = 0
    for i in range(10):
        if population[ind][i] == 1:
            print("Item no " + str(i) +" Value " + str(values[i]) + " Weight" + str(weights[i]))
            Total_Amount += values[i]
    print("Total Amount Collected By Thief:", Total_Amount)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

    values = [266, 442, 671, 526, 388, 245, 210, 145, 126, 322]
    weights = [3, 13, 10, 9, 7, 1, 8, 8, 2, 9]
    kw = 35
    fitness = {}
    population = [
        [0, 1, 0, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0]]

    print("Initial Population", population)
    # Initializing fitness of population
    for solution in range(len(population)):
        fitness[solution] = calculate_fitness(population[solution])
    fitness = dict(sorted(fitness.items(), key=lambda item: item[1]))
    print("Fitness of Initial Population :", fitness)

    # loop
    for i in range(10000):
        parent = []
        parent1_index = list(fitness.keys()).pop(0)
        parent2_index = list(fitness.keys()).pop(1)

        # Generating new population
        bad_child1 = list(fitness.keys()).pop(len(fitness.keys()) - 1)
        bad_child2 = list(fitness.keys()).pop(len(fitness.keys()) - 2)

        population[bad_child1], population[bad_child2] = generate_offspring(population[parent2_index], population[parent1_index])

        fitness[bad_child1] = calculate_fitness(population[parent1_index])
        fitness[bad_child2] = calculate_fitness(population[parent2_index])

        print("New Population", population)
        fitness = dict(sorted(fitness.items(), key=lambda item: item[1]))
        print("Fitness of new Population:", fitness)

    Get_Best_Solution()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
