import math


def alpha_beta_pruning(
    node, depth, alpha, beta, maximizing_player, path="Root"
):
    # Base case: leaf node is reached (represented as an integer/float)
    if isinstance(node, (int, float)):
        print(f"Reached leaf [{path}] -> Value: {node}")
        return node

    if maximizing_player:
        max_eval = -math.inf
        for i, child in enumerate(node):
            child_path = f"{path} -> Max({i})"
            eval_val = alpha_beta_pruning(
                child, depth + 1, alpha, beta, False, child_path
            )
            max_eval = max(max_eval, eval_val)
            alpha = max(alpha, eval_val)

            # Prune remaining siblings if beta <= alpha
            if beta <= alpha:
                print(
                    f"✂️ PRUNED remaining branches at [{path}] (alpha={alpha} >="
                    f" beta={beta})"
                )
                break
        return max_eval

    else:  # Minimizing player
        min_eval = math.inf
        for i, child in enumerate(node):
            child_path = f"{path} -> Min({i})"
            eval_val = alpha_beta_pruning(
                child, depth + 1, alpha, beta, True, child_path
            )
            min_eval = min(min_eval, eval_val)
            beta = min(beta, eval_val)

            # Prune remaining siblings if beta <= alpha
            if beta <= alpha:
                print(
                    f"✂️ PRUNED remaining branches at [{path}] (alpha={alpha} >="
                    f" beta={beta})"
                )
                break
        return min_eval


# --- Simulation Setup ---
# Game tree represented as nested lists (depth = 3)
# Leaf values at the bottom:, [6, 9], [1, 2], [0, -1]
game_tree = [[[3, 5], [6, 9]], [[1, 2], [0, -1]]]

print("Starting Alpha-Beta Pruning Simulation...\n")
optimal_value = alpha_beta_pruning(
    node=game_tree, depth=0, alpha=-math.inf, beta=math.inf, maximizing_player=True
)
print(f"\n✅ Optimal Value for Root (Maximizer): {optimal_value}")
