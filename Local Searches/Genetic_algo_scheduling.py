# GENETIC ALGORITHM - STAFF SCHEDULING PROBLEM
# This code creates an optimal staff schedule using GA

import random

num_staff = 5
num_shifts = 7
min_staff_per_shift = 2
max_shifts_per_staff = 4

population_size = 50
mutation_rate = 0.2
max_generations = 100

def create_random_schedule():
    schedule = [[0] * num_shifts for _ in range(num_staff)]
    
    for staff in range(num_staff):
        num_assignments = random.randint(3, max_shifts_per_staff)
        assigned_shifts = random.sample(range(num_shifts), num_assignments)
        
        for shift in assigned_shifts:
            schedule[staff][shift] = 1
    
    return schedule

def evaluate_fitness(schedule):
    penalty = 0
    
    for shift in range(num_shifts):
        staff_count = sum(schedule[staff][shift] for staff in range(num_staff))
        if staff_count < min_staff_per_shift:
            penalty += (min_staff_per_shift - staff_count) * 10
    
    for staff in range(num_staff):
        for shift in range(num_shifts - 1):
            if schedule[staff][shift] == 1 and schedule[staff][shift + 1] == 1:
                penalty += 5
    
    for staff in range(num_staff):
        total_shifts = sum(schedule[staff])
        if total_shifts > max_shifts_per_staff:
            penalty += (total_shifts - max_shifts_per_staff) * 3
    
    return penalty

def select_parents(population, fitness_scores):
    paired = list(zip(fitness_scores, population))
    paired.sort(key=lambda x: x[0])
    sorted_population = [schedule for _, schedule in paired]
    return sorted_population[:len(population) // 2]

def crossover(parent1, parent2):
    point = random.randint(0, num_shifts - 1)
    
    child = []
    for staff in range(num_staff):
        child_row = parent1[staff][:point] + parent2[staff][point:]
        child.append(child_row)
    
    return child

def mutate(schedule):
    mutated = [row.copy() for row in schedule]
    
    staff = random.randint(0, num_staff - 1)
    shift1, shift2 = random.sample(range(num_shifts), 2)
    
    mutated[staff][shift1], mutated[staff][shift2] = \
        mutated[staff][shift2], mutated[staff][shift1]
    
    return mutated

def genetic_algorithm():
    population = [create_random_schedule() for _ in range(population_size)]
    
    best_schedule = None
    best_fitness = float('inf')
    
    print(f"Starting Genetic Algorithm for Staff Scheduling")
    print(f"Staff: {num_staff}, Shifts: {num_shifts}")
    print(f"Population: {population_size}, Generations: {max_generations}\n")
    
    for generation in range(max_generations):
        fitness_scores = [evaluate_fitness(schedule) for schedule in population]
        
        current_best_fitness = min(fitness_scores)
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            best_schedule = population[fitness_scores.index(current_best_fitness)]
        
        print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")
        
        if best_fitness == 0:
            print(f"\n✓ Perfect schedule found at generation {generation + 1}!")
            break
        
        parents = select_parents(population, fitness_scores)
        
        new_population = []
        
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            
            if random.random() < mutation_rate:
                child = mutate(child)
            
            new_population.append(child)
        
        population = new_population
    
    return best_schedule, best_fitness

def print_schedule(schedule):
    print("\n" + "="*60)
    print("STAFF SCHEDULE (1 = Assigned, 0 = Off)")
    print("="*60)
    
    header = "       "
    for shift in range(num_shifts):
        header += f"Shift{shift+1} "
    print(header)
    print("-" * 60)
    
    for staff in range(num_staff):
        row = f"Staff{staff+1}:  "
        for shift in range(num_shifts):
            row += f"   {schedule[staff][shift]}    "
        print(row)
    
    print("-" * 60)
    
    print("\nShift Coverage:")
    for shift in range(num_shifts):
        count = sum(schedule[staff][shift] for staff in range(num_staff))
        status = "✓" if count >= min_staff_per_shift else "✗"
        print(f"  Shift {shift+1}: {count} staff {status}")
    
    print()

# Run the code
best_schedule, best_fitness = genetic_algorithm()

print("\n" + "="*60)
print("FINAL RESULT")
print("="*60)
print(f"Best Fitness (Penalty): {best_fitness}")

if best_fitness == 0:
    print("✓ Perfect schedule found (no constraint violations)!")
else:
    print(f"✗ Near-optimal schedule ({best_fitness} penalty points)")

print_schedule(best_schedule)
