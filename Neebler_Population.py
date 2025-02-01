"""Simulates natural selection in the fictional Neebler population."""

import random

# Starting population with each trait variation.
green_neeblers = 100
yellow_neeblers = 100

# Loop to simulate generations of neeblers
generation = 0
while generation < 20 and green_neeblers > 0 and yellow_neeblers > 0:
    for neebler in range(green_neeblers):
        # Low chance of being spotted by predators
        # because they're well camouflaged in the forest.
        chance_of_being_spotted = random.randint(0, 4)
        if chance_of_being_spotted == 4:
            green_neeblers = green_neeblers - 1
    
    for neebler in range(yellow_neeblers):
        # Higher chance of being spotted by predators
        # because they're not well camouflaged in the forest.
        chance_of_being_spotted = random.randint(0, 3)
        if chance_of_being_spotted == 3:
            yellow_neeblers = yellow_neeblers - 1
    
    baby_green_neeblers = 0
    for neebler in range(green_neeblers):
        # Greenness trait gets passed to their babies.
        num_babies = random.randint(0, 3)
        baby_green_neeblers = baby_green_neeblers + num_babies
    
    baby_yellow_neeblers = 0
    for neebler in range(yellow_neeblers):
        # Yellowness trait gets passed to their babies.
        num_babies = random.randint(0, 3)
        baby_yellow_neeblers = baby_yellow_neeblers + num_babies
    
    # Babies become the starting population of the next generation.
    green_neeblers = baby_green_neeblers
    yellow_neeblers = baby_yellow_neeblers
   
    generation += 1
    
    print("Generation " + str(generation))
    print("  " + str(green_neeblers) + " green Neeblers")
    print("  " + str(yellow_neeblers) + " yellow Neeblers")
