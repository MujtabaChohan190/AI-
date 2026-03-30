import random

# ==========================================================
# FITNESS FUNCTION
# Maximize number of 1s in chromosome
# ==========================================================
def fitness(chromosome):
    return sum(chromosome)


# ==========================================================
# SELECTION (Roulette Wheel Selection)
# ==========================================================
def roulette_wheel_selection(population, fitness_values):

    total_fitness = sum(fitness_values)

    # Avoid division by zero
    if total_fitness == 0:
        return random.sample(population, 2)

    probabilities = [f / total_fitness for f in fitness_values]

    # Select 2 parents
    selected = random.choices(population, weights=probabilities, k=2)
    return selected


# ==========================================================
# CROSSOVER (Single-Point)
# ==========================================================
def crossover(parent1, parent2):

    point = random.randint(1, len(parent1) - 1)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2


# ==========================================================
# CROSSOVER (Two-Point)
# ==========================================================
def two_point_crossover(parent1, parent2):

    cp1 = random.randint(1, len(parent1) - 2)
    cp2 = random.randint(1, len(parent1) - 1)

    if cp1 > cp2:
        cp1, cp2 = cp2, cp1

    child1 = parent1[:cp1] + parent2[cp1:cp2] + parent1[cp2:]
    child2 = parent2[:cp1] + parent1[cp1:cp2] + parent2[cp2:]

    return child1, child2


# ==========================================================
# MUTATION (Bit Flip)
# ==========================================================
def mutate(chromosome, mutation_rate):

    new_chromosome = chromosome[:]  # copy to avoid modifying original

    for i in range(len(new_chromosome)):
        if random.random() < mutation_rate:
            new_chromosome[i] = 1 - new_chromosome[i]

    return new_chromosome


# ==========================================================
# GENETIC ALGORITHM
# ==========================================================
def genetic_algorithm(initial_population, generations, mutation_rate):

    population = initial_population

    for generation in range(generations):

        # Evaluate fitness
        fitness_values = [fitness(ch) for ch in population]

        print(f"Generation {generation+1} | Best Fitness: {max(fitness_values)}")

        new_population = []

        # Generate new population
        while len(new_population) < len(population):

            # Selection
            parent1, parent2 = roulette_wheel_selection(population, fitness_values)

            # Crossover (you can switch to two_point_crossover if needed)
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)

            new_population.append(child1)
            new_population.append(child2)

        population = new_population[:len(population)]  # keep size fixed

    # Return best solution
    best = max(population, key=fitness)
    return best


# ==========================================================
# INITIAL POPULATION
# ==========================================================
initial_population = [
    [0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1]
]

generations = 50
mutation_rate = 0.1   # (0.70 is too high, 0.1 is better)

# ==========================================================
# RUN GA
# ==========================================================
best_solution = genetic_algorithm(initial_population, generations, mutation_rate)

print("\nBest Solution:", best_solution)
print("Best Fitness:", fitness(best_solution))
