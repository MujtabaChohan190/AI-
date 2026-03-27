import random

# =========================
# Fitness Function
# =========================
# Counts number of attacking queen pairs (lower is better)
def calculate_conflicts(state):
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# =========================
# Create Initial Population
# =========================
def create_population(n, size):
    population = []
    for _ in range(size):
        individual = [random.randint(0, n - 1) for _ in range(n)]
        population.append(individual)
    return population


# =========================
# Selection (Tournament)
# =========================
def select_parent(population):
    # pick 3 random individuals
    sample = random.sample(population, 3)

    # return the best (least conflicts)
    best = min(sample, key=calculate_conflicts)  #gets the best parent ,we do it twice in GA algo
    return best


# =========================
# Crossover
# =========================
def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 1)

    child = parent1[:point] + parent2[point:]  
    return child


# =========================
# Mutation
# =========================
def mutate(state, rate):
    n = len(state)
    new_state = list(state)

    for i in range(n):
        if random.random() < rate:   #The if random.random() < rate: condition ensures that mutation happens randomly with a controlled probability, keeping GA effective.
            new_state[i] = random.randint(0, n - 1) #we replace that particular row index of that state with random value

    return new_state


# =========================
# Genetic Algorithm
# =========================
def genetic_algorithm(n):

    population_size = 50
    mutation_rate = 0.1
    max_generations = 500

    # Step 1: create population
    population = create_population(n, population_size)

    for generation in range(max_generations):

        # Step 2: check best solution
        best = min(population, key=calculate_conflicts)  #gets the best parent and check if conflict is 0 thats best case so we return 
        best_conflicts = calculate_conflicts(best)

        if best_conflicts == 0:
            print("Solution found at generation", generation)
            return best, best_conflicts

        # Step 3: create new population
        new_population = []

        while len(new_population) < population_size:  #This while loop fills the new generation by repeatedly creating children until we have as many boards as the population size.
            parent1 = select_parent(population)
            parent2 = select_parent(population)

            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)

            new_population.append(child)

        population = new_population

    # if no perfect solution found
    return best, best_conflicts


# =========================
# Run Genetic Algorithm
# =========================
n = 8
solution, conflicts = genetic_algorithm(n)

if conflicts == 0:
    print("Solution:", solution)
else:
    print("Best found:", solution)
    print("Conflicts:", conflicts)




























# GENETIC ALGORITHM - N-QUEENS PROBLEM
# This code solves N-Queens using Genetic Algorithm

import random

POPULATION_SIZE = 100
MUTATION_RATE = 0.1
MAX_GENERATIONS = 1000
N = 8

def create_individual(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def calculate_fitness(individual):
    n = len(individual)
    attacks = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if individual[i] == individual[j]:
                attacks += 1
            if abs(individual[i] - individual[j]) == abs(i - j):
                attacks += 1
    
    return attacks

def selection(population, fitness_scores):
    tournament_size = 5
    tournament = random.sample(list(zip(population, fitness_scores)), tournament_size)
    winner = min(tournament, key=lambda x: x[1])
    return winner[0]

def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 1)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(individual, mutation_rate):
    n = len(individual)
    mutated = individual.copy()
    
    for i in range(n):
        if random.random() < mutation_rate:
            mutated[i] = random.randint(0, n - 1)
    
    return mutated

def genetic_algorithm(n, population_size, mutation_rate, max_generations):
    population = [create_individual(n) for _ in range(population_size)]
    
    best_solution = None
    best_fitness = float('inf')
    
    for generation in range(max_generations):
        fitness_scores = [calculate_fitness(ind) for ind in population]
        
        min_fitness = min(fitness_scores)
        if min_fitness < best_fitness:
            best_fitness = min_fitness
            best_solution = population[fitness_scores.index(min_fitness)]
        
        if generation % 100 == 0:
            print(f"Generation {generation}: Best Fitness = {best_fitness}")
        
        if best_fitness == 0:
            print(f"\n✓ Solution found in generation {generation}!")
            break
        
        new_population = []
        
        while len(new_population) < population_size:
            parent1 = selection(population, fitness_scores)
            parent2 = selection(population, fitness_scores)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population
    
    return best_solution, best_fitness

def print_board(board):
    n = len(board)
    print("\nBoard Configuration:")
    print("  " + " ".join(str(i) for i in range(n)))
    for row in range(n):
        line = f"{row} "
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

# Run the code
print(f"Solving {N}-Queens Problem using Genetic Algorithm")
print(f"Population Size: {POPULATION_SIZE}")
print(f"Mutation Rate: {MUTATION_RATE}")
print(f"Max Generations: {MAX_GENERATIONS}\n")

solution, fitness = genetic_algorithm(N, POPULATION_SIZE, MUTATION_RATE, MAX_GENERATIONS)

print(f"\n{'='*50}")
print("FINAL RESULT:")
print(f"{'='*50}")
print(f"Best Fitness: {fitness} (0 = perfect solution)")
print(f"Solution: {solution}")

if fitness == 0:
    print("\n✓ Perfect solution found!")
    print_board(solution)
else:
    print(f"\n✗ Near-optimal solution ({fitness} conflicts remaining)")
    print_board(solution)






