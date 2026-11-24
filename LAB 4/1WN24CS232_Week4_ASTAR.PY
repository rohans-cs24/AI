
import heapq

# Heuristic: number of misplaced tiles
def heuristic(state, goal):
    return sum(
        1 for i in range(9)
        if state[i] != 0 and state[i] != goal[i]
    )


# Generate neighboring states
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_pos = nr * 3 + nc
            new_state = state.copy()

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(new_state)

    return neighbors


# A* algorithm
def astar(start, goal):
    # Priority queue entries: (f, g, state)
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), 0, start))

    parent = {}
    g_cost = {tuple(start): 0}
    visited = set()
    explored = 0

    while pq:
        f, g, current = heapq.heappop(pq)
        key = tuple(current)

        if key in visited:
            continue

        visited.add(key)
        explored += 1

        h = heuristic(current, goal)

        print(f"\nState {explored}:")
        print_state(current)
        print(f"g(n) = {g}, h(n) = {h}, f(n) = {g + h}")

        if current == goal:
            print("\nGoal reached!")
            print("Total explored states:", explored)
            print("\nSolution path:")
            path = []
            while key in parent:
                path.append(list(key))
                key = parent[key]
            path.append(start)
            path.reverse()

            for i, state in enumerate(path):
                print(f"Step {i}: {state}")
            return

        for neighbor in get_neighbors(current):
            nkey = tuple(neighbor)
            new_g = g + 1

            if nkey not in g_cost or new_g < g_cost[nkey]:
                g_cost[nkey] = new_g
                parent[nkey] = tuple(current)
                new_h = heuristic(neighbor, goal)
                new_f = new_g + new_h

                heapq.heappush(
                    pq, (new_f, new_g, neighbor)
                )

    print("No solution found.")


# Print a 3 x 3 puzzle
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])


# Take input from user
print("Enter initial state (9 numbers, use 0 for blank):")
start = list(map(int, input().split()))

print("Enter goal state (9 numbers, use 0 for blank):")
goal = list(map(int, input().split()))

if (len(start) != 9 or len(goal) != 9
        or sorted(start) != list(range(9))
        or sorted(goal) != list(range(9))):
    print("Invalid input! Enter each number from 0 to 8 once.")
else:
    astar(start, goal)
