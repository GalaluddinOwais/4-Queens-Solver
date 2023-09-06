import random
import copy
import time

                                
print('   __ __        ____                            ')
print('  / // /       / __ \__  _____  ___  ____  _____')
print(' / // /_______/ / / / / / / _ \/ _ \/ __ \/ ___/')
print('/__  __/_____/ /_/ / /_/ /  __/  __/ / / (__  ) ')
print('  /_/        \___\_\__,_/\___/\___/_/ /_/____/  ')


print('                                                                     ')
print('  _____             __  _       ___   __              _ __  __       ') 
print(' / ___/__ ___  ___ / /_(_)___  / _ | / /__ ____  ____(_) /_/ /  __ ___')
print("/ (_ / -_) _ \/ -_) __/ / __/ / __ |/ / _ `/ _ \/ __/ / __/ _ \/  '  /")
print('\___/\__/_//_/\__/\__/_/\__/ /_/ |_/_/\_, /\___/_/ /_/\__/_//_/_/_/_/')
print('                                     /___/                           ')

print('                                                                     ')
print('IMPLEMENTED FROM SCRATCH')
print('                                                                     ')
print('                                                                     ')


POPULATION = 20
FIRST_CHROMOSOMES_TO_VIEW = 20
GENERATIONS = int(input('number of generations: '))+1
CROSS_OVERS_A_GENERATION = 5
MUTATIONS_A_GENERATION = 5
def manifest(w,x,y,z):
    matrix = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    binaryString = bin(w)[2:].zfill(4)
    matrix[0][0] = int(binaryString[0])
    matrix[0][1] = int(binaryString[1])
    matrix[0][2] = int(binaryString[2])
    matrix[0][3] = int(binaryString[3])
    binaryString = bin(x)[2:].zfill(4)
    matrix[1][0]= int(binaryString[0])
    matrix[1][1]= int(binaryString[1])
    matrix[1][2]= int(binaryString[2])
    matrix[1][3]= int(binaryString[3])
    binaryString = bin(y)[2:].zfill(4)
    matrix[2][0] = int(binaryString[0])
    matrix[2][1] = int(binaryString[1])
    matrix[2][2] = int(binaryString[2])
    matrix[2][3] = int(binaryString[3])
    binaryString = bin(z)[2:].zfill(4)
    matrix[3][0] = int(binaryString[0])
    matrix[3][1] = int(binaryString[1])
    matrix[3][2] = int(binaryString[2])
    matrix[3][3] = int(binaryString[3])
    return matrix


def fitness(w,x,y,z):
    matrix = manifest(w,x,y,z)
    score = 0

    for i in range(0,4):
        numOfOnes = 0
        for ii in range(0,4):
            numOfOnes = numOfOnes+ matrix[i][ii]
        if numOfOnes == 1:
            score = score + 10
        elif numOfOnes == 0:
            score = score - 10
        else:
            score = score - numOfOnes*10

    for i in range(0,4):
        numOfOnes = 0
        for ii in range(0,4):
            numOfOnes = numOfOnes+ matrix[ii][i]
        if  numOfOnes == 1:
            score=score+10
        elif numOfOnes == 0:
            score = score-10
        else:
            score = score - numOfOnes*10

    list =[0,1,2,3]
    for p in range(1,8):
        if p <= 4:
           list_portion= list[:p]
        else:
           list_portion=list[p-4:]
        list_to_reverse = list_portion.copy()
        list_to_reverse.reverse()
        numOfOnes = 0
        for i, ii in zip(list_portion, list_to_reverse):
            numOfOnes = numOfOnes + matrix[i][ii]
        if numOfOnes == 1:
            score = score + 10
        elif numOfOnes == 0:
            score = score - 10
        else:
            score = score - numOfOnes*10

    list = [0, 1, 2, 3]
    for p in range(1, 8):
        if p <= 4:
            list_portion = list[:p]
            list_to_oppose = list_portion.copy()
            list_to_oppose = [i + (4 - len(list_to_oppose)) for i in list_to_oppose]
        else:
            list_portion = list[p - 4:]
            list_to_oppose = list_portion.copy()
            list_to_oppose = [i-(4-len(list_to_oppose)) for i in list_to_oppose]


        numOfOnes = 0
        for i, ii in zip(list_portion, list_to_oppose):
            numOfOnes = numOfOnes + matrix[i][ii]
        if numOfOnes == 1:
            score = score + 10
        elif numOfOnes == 0:
            score = score - 10
        else:
            score = score - numOfOnes * 10

    return score

def prettyPrint(matrix):
    print(matrix[0][0],matrix[0][1],matrix[0][2],matrix[0][3])
    print(matrix[1][0],matrix[1][1],matrix[1][2],matrix[1][3])
    print(matrix[2][0],matrix[2][1],matrix[2][2],matrix[2][3])
    print(matrix[3][0],matrix[3][1],matrix[3][2],matrix[3][3])

def unique(list):
    unique_list = []

    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


def apply_rank_based_selection(chromosomes_ranked_by_fitness):
    unique_chromosomes_ranked_by_fitness = unique(chromosomes_ranked_by_fitness)
    sum = 0
    list_of_ranges = []
    for i in range(1, len(unique_chromosomes_ranked_by_fitness) + 1):
        sum = sum + 1 / i
        list_of_ranges.append(sum)

    new_chromosomes = []
    for _ in range(len(chromosomes_ranked_by_fitness)):
        random_spin_number = random.uniform(0, sum)
        for i in range(0, len(unique_chromosomes_ranked_by_fitness)):
            if random_spin_number <= list_of_ranges[i]:
                new_chromosomes.append(copy.deepcopy(unique_chromosomes_ranked_by_fitness[i]))
                break

    new_chromosomes.sort()
    new_chromosomes.reverse()
    return new_chromosomes


def apply_fitness_proportionate_selection(chromosomes_ranked_by_fitness):
    unique_chromosomes_ranked_by_fitness = unique(chromosomes_ranked_by_fitness)
    sum = 0
    list_of_ranges = []
    for i in range(len(unique_chromosomes_ranked_by_fitness)):
        sum = sum + unique_chromosomes_ranked_by_fitness[i][0]
        list_of_ranges.append(sum)

    new_chromosomes = []
    for _ in range(len(chromosomes_ranked_by_fitness)):
        random_spin_number = random.uniform(0, sum)
        for i in range(0, len(unique_chromosomes_ranked_by_fitness)):
            if random_spin_number <= list_of_ranges[i]:
                new_chromosomes.append(copy.deepcopy(unique_chromosomes_ranked_by_fitness[i]))
                break

    new_chromosomes.sort()
    new_chromosomes.reverse()
    return new_chromosomes


def crossover(fitness_and_chromosome1,fitness_and_chromosome2,fitness_and_chromosome1_to_replace,fitness_and_chromosome2_to_replace):
    random_gene_number = int(random.uniform(1,4))
    #copy to crossover
    chromosome_1_copy =   copy.deepcopy(fitness_and_chromosome1)
    chromosome_2_copy =  copy.deepcopy(fitness_and_chromosome2)

    #swap a randomized part
    holder = chromosome_1_copy[1][random_gene_number:]
    chromosome_1_copy[1][random_gene_number:] = chromosome_2_copy[1][random_gene_number:]
    chromosome_2_copy[1][random_gene_number:] = holder



    #recalculate fitness value
    chromosome_1_copy[0] = fitness(chromosome_1_copy[1][0], chromosome_1_copy[1][1], chromosome_1_copy[1][2],chromosome_1_copy[1][3])
    chromosome_2_copy[0] = fitness(chromosome_2_copy[1][0], chromosome_2_copy[1][1], chromosome_2_copy[1][2],chromosome_2_copy[1][3])

    # replace in low fitting
    print('offsprings:')
    print(fitness_and_chromosome1)
    print('X')
    print(fitness_and_chromosome2)
    print('↓')
    fitness_and_chromosome1_to_replace[0] = chromosome_1_copy[0]
    fitness_and_chromosome1_to_replace[1] = chromosome_1_copy[1]
    print(fitness_and_chromosome1_to_replace)
    print('||')
    fitness_and_chromosome2_to_replace[0] = chromosome_2_copy[0]
    fitness_and_chromosome2_to_replace[1] = chromosome_2_copy[1]
    print(fitness_and_chromosome2_to_replace)


def mutate(fitness_and_chromosome,fitness_and_chromosome_to_replace):
    # copy
    chromosome_copy = copy.deepcopy(fitness_and_chromosome)
    # mutate a randomized gen
    list_of_random_genes_to_mutate = []
    for _ in range(int(random.uniform(1, 4))):
        list_of_random_genes_to_mutate.append(int(random.uniform(0, 4)))

    for random_gene_number in list_of_random_genes_to_mutate:
        chromosome_copy[1][random_gene_number] = int(random.uniform(0, 16))

    #recalcuate fitness
    chromosome_copy[0] = fitness(chromosome_copy[1][0], chromosome_copy[1][1], chromosome_copy[1][2],chromosome_copy[1][3])

    # replace
    print('mutant:')
    print(fitness_and_chromosome)
    print('↓')
    fitness_and_chromosome_to_replace[0] = chromosome_copy[0]
    fitness_and_chromosome_to_replace[1] = chromosome_copy[1]
    print(fitness_and_chromosome_to_replace)


# generate random chromosomes
chromosomes = []
for _ in range(POPULATION):
    chromosomes.append([int(random.uniform(0,8)),int(random.uniform(0,8)),int(random.uniform(0,8)),int(random.uniform(0,8))])

# calculate fitness for each chromosome and sort them by
chromosomes_ranked_by_fitness = []
fitnessValue = None

print('fitness values for each chromosome in the initial random population:')
for chromosome in chromosomes:
    fitnessValue = fitness(chromosome[0], chromosome[1], chromosome[2], chromosome[3])
    chromosomes_ranked_by_fitness.append([fitnessValue, chromosome])
    print(fitnessValue)

chromosomes_ranked_by_fitness.sort()
chromosomes_ranked_by_fitness.reverse()

fittest_found = chromosomes_ranked_by_fitness[0].copy()

print('Gen', 0, '  (fittest ', FIRST_CHROMOSOMES_TO_VIEW, ' solutions)')

for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
    print(chromosome)

print(
    '____________________________________________________________________________________________________________________________________________________________')
print('fittest solution found until the moment:')
print(fittest_found)
prettyPrint(manifest(fittest_found[1][0],fittest_found[1][1],fittest_found[1][2],fittest_found[1][3]))
print(
    '____________________________________________________________________________________________________________________________________________________________')

for i in range(1, GENERATIONS):

    chromosomes_ranked_by_fitness = apply_rank_based_selection(chromosomes_ranked_by_fitness)

    print('right after selection process:')
    for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
        print(chromosome)

    for _ in range(CROSS_OVERS_A_GENERATION):
        random_chromosome_1 = int(random.uniform(0, POPULATION))
        random_chromosome_2 = int(random.uniform(0, POPULATION))
        crossover(chromosomes_ranked_by_fitness[random_chromosome_1],
                  chromosomes_ranked_by_fitness[random_chromosome_2],
                  chromosomes_ranked_by_fitness[random_chromosome_1],
                  chromosomes_ranked_by_fitness[random_chromosome_2],
                  )

    print('right after cross-over process:')
    for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
        print(chromosome)

    for _ in range(MUTATIONS_A_GENERATION):
        random_chromosome = int(random.uniform(0, POPULATION))
        mutate(chromosomes_ranked_by_fitness[random_chromosome],
               chromosomes_ranked_by_fitness[random_chromosome]
               )

    print('right after mutation process:')
    for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
        print(chromosome)

    chromosomes_ranked_by_fitness.sort()
    chromosomes_ranked_by_fitness.reverse()

    if chromosomes_ranked_by_fitness[0][0] > fittest_found[0]:
        fittest_found = chromosomes_ranked_by_fitness[0].copy()

    print('Gen', i, '  (fittest ', FIRST_CHROMOSOMES_TO_VIEW, ') solutions')

    for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
        print(chromosome)
    print(
        '____________________________________________________________________________________________________________________________________________________________')
    print('fittest solution found until the moment:')

    print(fittest_found)
    prettyPrint(manifest(fittest_found[1][0],fittest_found[1][1],fittest_found[1][2],fittest_found[1][3]))

    print(
        '____________________________________________________________________________________________________________________________________________________________')

time.sleep(10)