import math
import random

def simulated_annealing(problem, schedule):

    current = problem["initial_state"]
    t = 1

    print("INITIAL STATE:", current["name"])
    print("INITIAL VALUE:", current["value"])
    print("-" * 60)

    while True:

        # Step 1: Calculate temperature
        T = schedule(t)

        print("\nIteration:", t)
        print("Temperature:", T)

        # Step 2: Check stopping condition
        if T == 0:
            print("\nTemperature is zero.")
            print("Algorithm Terminated!")
            return current

        # Step 3: Select random successor
        next_state = random.choice(
            problem["successors"](current)
        )

        print("Current State:", current["name"])
        print("Next State:", next_state["name"])

        # Step 4: Calculate change in value
        delta_E = next_state["value"] - current["value"]

        print("Current Value:", current["value"])
        print("Next Value:", next_state["value"])
        print("Delta E:", delta_E)

        # Step 5: Decide whether to accept successor
        if delta_E > 0:
            current = next_state
            print("Better Solution Found!")
            print("Accepted with probability 1")

        else:
            probability = math.exp(delta_E / T)
            random_value = random.random()

            print("Acceptance Probability:", round(probability, 4))
            print("Random Value:", round(random_value, 4))

            if random_value < probability:
                current = next_state
                print("Worse Solution Accepted!")
            else:
                print("Solution Rejected!")

        print("Updated Current State:", current["name"])
        print("Updated Current Value:", current["value"])
        print("-" * 60)

        t += 1


# Define problem
problem = {
    "initial_state": {"name": "A", "value": 10},

    "successors": lambda state: [
        {"name": "B", "value": 15},
        {"name": "C", "value": 8},
        {"name": "D", "value": 12}
    ]
}

# Temperature schedule
def schedule(t):
    return max(100 - t * 10, 0)


# Run algorithm
solution = simulated_annealing(problem, schedule)

print("\nFINAL SOLUTION:", solution["name"])
print("FINAL VALUE:", solution["value"])
