import random
import string

# --- Configuration ---
TARGET = "Hello World"
POPULATION_SIZE = 200    # How many "creatures" per generation
MUTATION_RATE = 0.01     # 1% chance a gene (letter) randomly changes

# --- Helper Functions ---

def random_char():
    """Return a random printable character."""
    return random.choice(string.ascii_letters + string.punctuation + " ")

def create_genome(length):
    """Create a random string of a specific length."""
    return [random_char() for _ in range(length)]

def calculate_fitness(genome):
    """
    Score the genome. 
    1 point for every character that matches the target in the right position.
    """
    score = 0
    for i in range(len(TARGET)):
        if genome[i] == TARGET[i]:
            score += 1
    return score

def crossover(parent1, parent2):
    """
    Create a child by taking some genes from parent1 and some from parent2.
    """
    # Pick a random crossover point
    midpoint = random.randint(0, len(TARGET) - 1)
    
    # Child gets Part A from Parent 1, Part B from Parent 2
    child_genome = parent1[:midpoint] + parent2[midpoint:]
    return child_genome

def mutate(genome):
    """
    Randomly change one character based on mutation rate.
    """
    for i in range(len(genome)):
        if random.random() < MUTATION_RATE:
            genome[i] = random_char()
    return genome

# --- Main Simulation ---

def main():
    # 1. Genesis: Create initial random population
    population = [create_genome(len(TARGET)) for _ in range(POPULATION_SIZE)]
    generation = 1
    
    found = False
    while not found:
        # Sort population by fitness (highest score first)
        # We wrap this in a list to keep the structure manageable
        scored_population = []
        for individual in population:
            fitness = calculate_fitness(individual)
            scored_population.append((fitness, individual))
        
        # Sort so the best fit are at the top
        scored_population.sort(key=lambda x: x[0], reverse=True)
        
        # Check if we won
        best_fitness = scored_population[0][0]
        best_str = "".join(scored_population[0][1])
        
        print(f"Gen {generation} | Best: {best_str} | Score: {best_fitness}/{len(TARGET)}")
        
        if best_str == TARGET:
            print("\nEvolution Complete!\n")
            break

        # 2. Natural Selection: Keep top 20% to be parents
        top_performers = [x[1] for x in scored_population[:int(POPULATION_SIZE * 0.2)]]
        
        # 3. Reproduction: Create new generation
        new_population = []
        
        # Elitism: Always keep the absolute best one unchanged
        new_population.append(scored_population[0][1])
        
        # Fill the rest of the population with children
        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(top_performers)
            parent2 = random.choice(top_performers)
            
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
            
        population = new_population
        generation += 1

if __name__ == "__main__":
    print("\n")
    main()