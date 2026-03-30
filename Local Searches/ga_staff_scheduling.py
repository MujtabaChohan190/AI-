# ==========================================================
# QUESTION: Staff Scheduling using Genetic Algorithm
# ==========================================================
# Write a program to generate an optimal staff schedule
# using a Genetic Algorithm.

# ----------------------------------------------------------
# Problem Description:
# A company needs to assign staff members to different shifts
# while satisfying the following constraints:
# 1. Each shift must have at least a minimum number of staff.
# 2. A staff member should not work consecutive shifts.
# 3. Each staff member should not exceed a maximum number of shifts.
# ----------------------------------------------------------

# Requirements:
# - Number of staff: 5
# - Number of shifts: 7
# - Minimum staff per shift: 2
# - Maximum shifts per staff: 4

# ----------------------------------------------------------
# Tasks:
# 1. Representation:
#    - Represent schedule as a 2D list
#    - Rows = staff, Columns = shifts
#    - 1 = assigned, 0 = not assigned
#
# 2. Fitness Function:
#    - Add penalty if shift has fewer staff than required
#    - Add penalty if a staff works consecutive shifts
#    - Add penalty if staff exceeds max shifts
#
# 3. Genetic Algorithm Steps:
#    - Generate initial random population
#    - Evaluate fitness of each schedule
#    - Select best schedules as parents
#    - Apply crossover to create new schedules
#    - Apply mutation randomly
#    - Repeat for multiple generations
#
# 4. Output:
#    - Display best schedule found
#    - Display fitness (penalty value)
#    - Display shift coverage
# ----------------------------------------------------------

# Expected Outcome:
# - Minimize penalty
# - Perfect schedule has fitness = 0
# ==========================================================



import random

n = 8
population_size = 10
mutation_rate = 0.1


# Fitness function
def calculate_fitness(individual):

    non_attacking_pairs = 0
    total_pairs = n * (n - 1) // 2

    for i in range(n):
        for j in range(i + 1, n):

            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking_pairs += 1

    return non_attacking_pairs / total_pairs


# Create random chromosome
def create_random_individual():
    return random.sample(range(n), n)


# Selection
def select_parents(population, fitness_scores):

    sorted_population = [board for _, board in sorted(zip(fitness_scores, population), reverse=True)]
    return sorted_population[:len(population)//2]


# Crossover
def crossover(parent1, parent2):

    point = random.randint(1, n - 2)
    child = parent1[:point] + parent2[point:]

    missing = set(range(n)) - set(child)
    for i in range(len(child)):
        if child.count(child[i]) > 1:
            child[i] = missing.pop()

    return child


# Mutation
def mutate(individual):

    idx1, idx2 = random.sample(range(n), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

    return individual


# Genetic Algorithm
def genetic_algorithm():

    population = [create_random_individual() for _ in range(population_size)]

    generation = 0
    best_fitness = 0

    while best_fitness < 1.0 and generation < 100:

        fitness_scores = [calculate_fitness(ind) for ind in population]
        best_fitness = max(fitness_scores)

        print("Generation", generation, "Best Fitness:", best_fitness)

        if best_fitness == 1.0:
            break

        parents = select_parents(population, fitness_scores)

        new_population = [
            crossover(random.choice(parents), random.choice(parents))
            for _ in range(population_size)
        ]

        for i in range(len(new_population)):
            if random.random() < mutation_rate:
                new_population[i] = mutate(new_population[i])

        population = new_population
        generation += 1

    best_individual = max(population, key=calculate_fitness)

    return best_individual, calculate_fitness(best_individual)


# Run Genetic Algorithm
solution, fitness = genetic_algorithm()

print("Best Solution:", solution)
print("Best Fitness:", fitness)
