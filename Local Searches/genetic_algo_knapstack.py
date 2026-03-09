# TASK 3: GENETIC ALGORITHM - KNAPSACK PROBLEM (SURVIVAL ITEMS)
# Maximize survival points while staying within 30kg weight limit

import random

# Problem parameters from the table
items = [
    {"name": "SLEEPING BAG", "weight": 15, "points": 15},
    {"name": "ROPE", "weight": 3, "points": 7},
    {"name": "POCKET KNIFE", "weight": 2, "points": 10},
    {"name": "TORCH", "weight": 5, "points": 5},
    {"name": "BOTTLE", "weight": 9, "points": 8},
    {"name": "GLUCOSE", "weight": 20, "points": 17}
]

MAX_WEIGHT = 30

# GA Parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.2
MAX_GENERATIONS = 200

def create_individual():
    """
    Create a random individual (chromosome)
    Each bit represents whether item is included (1) or not (0)
    Returns: List of 0s and 1s, length = number of items
    """
    return [random.randint(0, 1) for _ in range(len(items))]

def calculate_fitness(individual):
    """
    Fitness function: Total survival points
    Penalty if weight exceeds limit
    
    Returns: Fitness score (higher is better)
    """
    total_weight = 0
    total_points = 0
    
    for i, selected in enumerate(individual):
        if selected == 1:
            total_weight += items[i]["weight"]
            total_points += items[i]["points"]
    
    # Heavy penalty if weight exceeds limit
    if total_weight > MAX_WEIGHT:
        return 0  # Invalid solution
    
    return total_points

def get_weight(individual):
    """
    Calculate total weight of selected items
    """
    total_weight = 0
    for i, selected in enumerate(individual):
        if selected == 1:
            total_weight += items[i]["weight"]
    return total_weight

def selection(population, fitness_scores):
    """
    Tournament selection
    """
    tournament_size = 5
    tournament = random.sample(list(zip(population, fitness_scores)), tournament_size)
    winner = max(tournament, key=lambda x: x[1])
    return winner[0]

def crossover(parent1, parent2):
    """
    Single-point crossover
    """
    point = random.randint(1, len(items) - 1)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(individual, mutation_rate):
    """
    Bit-flip mutation
    """
    mutated = individual.copy()
    for i in range(len(mutated)):
        if random.random() < mutation_rate:
            mutated[i] = 1 - mutated[i]  # Flip bit
    return mutated

def genetic_algorithm():
    """
    Main GA loop for Knapsack problem
    """
    # Initialize population
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    
    best_individual = None
    best_fitness = 0
    
    print(f"Starting Genetic Algorithm for Knapsack Problem")
    print(f"Max Weight: {MAX_WEIGHT} kg")
    print(f"Population Size: {POPULATION_SIZE}")
    print(f"Mutation Rate: {MUTATION_RATE}")
    print(f"Max Generations: {MAX_GENERATIONS}\n")
    
    for generation in range(MAX_GENERATIONS):
        # Calculate fitness
        fitness_scores = [calculate_fitness(ind) for ind in population]
        
        # Track best
        max_fitness = max(fitness_scores)
        if max_fitness > best_fitness:
            best_fitness = max_fitness
            best_individual = population[fitness_scores.index(max_fitness)]
        
        # Print progress
        if generation % 20 == 0:
            avg_fitness = sum(fitness_scores) / len(fitness_scores)
            print(f"Generation {generation}: Best={best_fitness}, Avg={avg_fitness:.2f}")
        
        # Create new population
        new_population = []
        
        while len(new_population) < POPULATION_SIZE:
            # Selection
            parent1 = selection(population, fitness_scores)
            parent2 = selection(population, fitness_scores)
            
            # Crossover
            child = crossover(parent1, parent2)
            
            # Mutation
            child = mutate(child, MUTATION_RATE)
            
            new_population.append(child)
        
        population = new_population
    
    return best_individual, best_fitness

def print_solution(individual):
    """
    Print selected items and statistics
    """
    print("\n" + "="*60)
    print("SELECTED ITEMS:")
    print("="*60)
    print(f"{'ITEM':<20} {'WEIGHT (kg)':<15} {'SURVIVAL POINTS'}")
    print("-"*60)
    
    total_weight = 0
    total_points = 0
    
    for i, selected in enumerate(individual):
        if selected == 1:
            item = items[i]
            print(f"{item['name']:<20} {item['weight']:<15} {item['points']}")
            total_weight += item['weight']
            total_points += item['points']
    
    print("-"*60)
    print(f"{'TOTAL':<20} {total_weight:<15} {total_points}")
    print("="*60)
    
    print(f"\nWeight Used: {total_weight}/{MAX_WEIGHT} kg")
    print(f"Remaining Capacity: {MAX_WEIGHT - total_weight} kg")
    print(f"Total Survival Points: {total_points}")
    
    if total_weight <= MAX_WEIGHT:
        print("✓ Valid solution (within weight limit)")
    else:
        print("✗ Invalid solution (exceeds weight limit)")

# Run Genetic Algorithm
print("="*60)
print("TASK 3: GENETIC ALGORITHM - KNAPSACK PROBLEM")
print("="*60)

print("\nAvailable Items:")
print(f"{'ITEM':<20} {'WEIGHT (kg)':<15} {'SURVIVAL POINTS'}")
print("-"*60)
for item in items:
    print(f"{item['name']:<20} {item['weight']:<15} {item['points']}")
print("-"*60)
print(f"Maximum Weight Capacity: {MAX_WEIGHT} kg\n")

print("="*60)
print("RUNNING GENETIC ALGORITHM")
print("="*60)

best_solution, best_points = genetic_algorithm()

print("\n" + "="*60)
print("FINAL RESULT")
print("="*60)

print_solution(best_solution)

print("\n" + "="*60)
print("ANALYSIS")
print("="*60)
print(f"Optimal Survival Points: {best_points}")
print(f"Chromosome: {best_solution}")
print("\nNote: 1 = Item selected, 0 = Item not selected")
