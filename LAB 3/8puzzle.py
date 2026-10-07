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
    
    directions = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]
    
    for dr, dc, action in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
            moves.append((tuple(new_state), action))
            
    return moves

def depth_limited_dfs(current_state, goal_state, depth, visited, path):
    if current_state == goal_state:
        return path
    
    if depth <= 0:
        return None
        
    visited.add(current_state)
    
    for next_state, action in get_moves(current_state):
        if next_state not in visited:
            result = depth_limited_dfs(next_state, goal_state, depth - 1, visited, path + [action])
            if result is not None:
                return result
                
    visited.remove(current_state)
    return None

def iterative_deepening_dfs(initial_state, goal_state, max_depth=50):
    for depth in range(max_depth + 1):
        visited = set()
        path = depth_limited_dfs(initial_state, goal_state, depth, visited, [])
        if path is not None:
            return path
    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(f"{state[i]} {state[i+1]} {state[i+2]}")
    print()

def main():
    print("--- 8-Puzzle Solver (Iterative Deepening DFS) ---")
    initial_state = get_state("Define the INITIAL state:")
    goal_state = get_state("Define the GOAL state:")
    
    print("\nInitial Board Layout:")
    print_board(initial_state)
    print("Goal Board Layout:")
    print_board(goal_state)
    
    print("Searching for a solution...")
    solution = iterative_deepening_dfs(initial_state, goal_state)
    
    if solution is list and len(solution) == 0:
        print("The initial state is already the goal state!")
    elif solution:
        print(f"Success! Solution found in {len(solution)} moves.")
        print("Sequence of moves:", " -> ".join(solution))
    else:
        print("No solution found within the depth limit or the puzzle is unsolvable.")

if __name__ == "__main__":
    main()
