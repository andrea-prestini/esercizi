import random
"""
Dimostriamo il paradosso di Monty Hall
sul cambio di scelta nel gioco di Monty Hall
"""

# Calculate the probabilities in the Monty Hall paradox


def calculate_monty_hall_probabilities():
    # Total number of trials
    total_trials = 1_000_000

    # Initialize counters for each scenario
    stay_wins = 0
    switch_wins = 0

    # Run the trials
    for _ in range(total_trials):
        # Randomly choose the door with the prize
        prize_door = random.randint(1, 3)

        # Randomly choose the door selected by the player
        player_door = random.randint(1, 3)

        # Randomly choose the door opened by Monty
        monty_door = random.choice([door for door in range(
            1, 4) if door != prize_door and door != player_door])

        # Determine the outcome if the player stays
        if player_door == prize_door:
            stay_wins += 1

        # Determine the outcome if the player switches
        switch_door = [door for door in range(
            1, 4) if door != player_door and door != monty_door][0]
        if switch_door == prize_door:
            switch_wins += 1

    # Calculate the probabilities
    stay_probability = stay_wins / total_trials
    switch_probability = switch_wins / total_trials

    # Print the results
    print("Probability of winning if you stay:", stay_probability)
    print("Probability of winning if you switch:", switch_probability)


# Call the function to calculate the probabilities
calculate_monty_hall_probabilities()
