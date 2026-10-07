def get_state(prompt):
    print(prompt)
    print("Enter 9 numbers (0-8) separated by spaces (0 represents the blank space):")

    while True:
        try:
            inputs = list(map(int, input().split()))

            if len(inputs) == 9 and sorted(inputs) == list(range(9)):
                return tuple(inputs)

            print("Invalid input! Please enter exactly 9 unique numbers from 0 to 8.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


def get_moves(state):
    moves = []

    blank_idx = state.index(0)
    row, col = blank_idx // 3, blank_idx % 3

    directions = [
        (-1, 0, 'Up'),
        (1, 0, 'Down'),
        (0, -1, 'Left'),
        (0, 1, 'Right')
    ]

    for dr, dc, action in directions:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with the adjacent tile
            new_state[blank_idx], new_state[new_idx] = \
                new_state[new_idx], new_state[blank_idx]

            moves.append((tuple(new_state), action))

    return moves


def depth_limited_dfs(current_state, goal_state, depth, visited, path):
    # Goal reached
    if current_state == goal_state:
        return path

    if depth <= 0:
        return None

    visited.add(current_state)

    for next_state, action in get_moves(current_state):

        if next_state not in visited:

            # Store both action and resulting state
            result = depth_limited_dfs(
                next_state,
                goal_state,
                depth - 1,
                visited,
                path + [(action, next_state)]
            )

            if result is not None:
                return result

    visited.remove(current_state)

    return None


def iterative_deepening_dfs(initial_state, goal_state, max_depth=50):

    # Initial state is already the goal
    if initial_state == goal_state:
        return []

    for depth in range(max_depth + 1):

        visited = set()

        path = depth_limited_dfs(
            initial_state,
            goal_state,
            depth,
            visited,
            []
        )

        if path is not None:
            return path

    return None


def print_board(state):
    print("+---+---+---+")

    for i in range(0, 9, 3):
        print(
            f"| {state[i] if state[i] != 0 else ' '} "
            f"| {state[i+1] if state[i+1] != 0 else ' '} "
            f"| {state[i+2] if state[i+2] != 0 else ' '} |"
        )

        print("+---+---+---+")


def print_solution(initial_state, solution):
    print("\n========== SOLUTION ==========")

    # State before any move
    current_state = initial_state

    print("\nMove 0")
    print("State: Initial")
    print_board(current_state)

    # Print every move and resulting state
    for move_number, (action, state) in enumerate(solution, start=1):
        print_board(state)
        print("===================")


    print("==============================")


def main():

    print("--- 8-Puzzle Solver (Iterative Deepening DFS) ---")

    initial_state = get_state("\nDefine the INITIAL state:")

    goal_state = get_state("\nDefine the GOAL state:")

    print("\nInitial Board Layout:")
    print_board(initial_state)

    print("Goal Board Layout:")
    print_board(goal_state)

    print("\nSearching for a solution...")

    solution = iterative_deepening_dfs(
        initial_state,
        goal_state
    )

    if solution == []:

        print("\nThe initial state is already the goal state!")

        print("\nState:")
        print_board(initial_state)

    elif solution:

        print(f"\nSuccess! Solution found in {len(solution)} moves.")

        print_solution(initial_state, solution)

    else:

        print("\nNo solution found within the depth limit")
        print("or the puzzle is unsolvable.")


if __name__ == "__main__":
    main()
