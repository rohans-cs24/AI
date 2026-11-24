import random

N = 4

# Count pairs of queens attacking each other
def heuristic(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Generate all neighboring states
def get_neighbors(state):
    neighbors = []

    for col in range(N):
        for row in range(N):
            if row != state[col]:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)

    return neighbors


def hill_climbing():
    explored = 0

    current = [random.randint(0, N - 1) for _ in range(N)]

    while True:
        explored += 1
        h_current = heuristic(current)

        print(f"State {explored}: {current}, h = {h_current}")

        if h_current == 0:
            print("\nSolution found!")
            print("Total explored states:", explored)
            print("Final state:", current)
            return

        neighbors = get_neighbors(current)

        # Choose the neighbor with the lowest heuristic
        best = min(neighbors, key=heuristic)
        h_best = heuristic(best)

        print("  Best neighbor:", best, ", h =", h_best)

        if h_best >= h_current:
            print("  Local minimum reached. Restarting...\n")
            current = [random.randint(0, N - 1) for _ in range(N)]
        else:
            current = best


hill_climbing()
