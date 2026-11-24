import itertools

# Helper function for logical implication (P -> Q)
def implies(p, q):
    return not p or q

# Evaluates the full Knowledge Base across its 3 sentences
def evaluate_kb(p, q, r):
    s1 = implies(q, p)       # Q -> P
    s2 = implies(p, not q)   # P -> ~Q
    s3 = q or r              # Q v R
    return s1 and s2 and s3

def run_logic_verification():
    # 1. Define the queries from questions ii, iii, and iv
    queries = {
        "ii) R": lambda p, q, r: r,
        "iii) R -> P": lambda p, q, r: implies(r, p),
        "iv) Q -> R": lambda p, q, r: implies(q, r)
    }
    
    # Track models and tracking for entailment results
    kb_models = []
    entailment_results = {name: True for name in queries}
    
    # 2. Print Truth Table Header
    print(f"{'P':<6}{'Q':<6}{'R':<6}{'~Q':<6}{'Q->P':<7}{'P->~Q':<8}{'QvR':<6}{'KB Status':<15}")
    print("-" * 65)
    
    # 3. Generate all 8 combinations of T/F for P, Q, R
    for p, q, r in itertools.product([True, False], repeat=3):
        # Calculate sub-expressions
        not_q = not q
        q_to_p = implies(q, p)
        p_to_not_q = implies(p, not_q)
        q_or_r = q or r
        
        # Calculate overall KB status
        kb_true = evaluate_kb(p, q, r)
        
        # Format strings for clean printing
        p_str, q_str, r_str = ('T' if x else 'F' for x in (p, q, r))
        not_q_str = 'T' if not_q else 'F'
        q_to_p_str = 'T' if q_to_p else 'F'
        p_to_not_q_str = 'T' if p_to_not_q else 'F'
        q_or_r_str = 'T' if q_or_r else 'F'
        
        if kb_true:
            model_num = len(kb_models) + 1
            kb_models.append((p, q, r))
            status_str = f"True (Model {model_num})"
        else:
            status_str = "False"
            
        print(f"{p_str:<6}{q_str:<6}{r_str:<6}{not_q_str:<6}{q_to_p_str:<7}{p_to_not_q_str:<8}{q_or_r_str:<6}{status_str:<15}")
        
        # 4. Check Entailment for each query
        for name, query_fn in queries.items():
            query_val = query_fn(p, q, r)
            # Entailment fails if KB is True but the query evaluates to False
            if kb_true and not query_val:
                entailment_results[name] = False

    # 5. Print Summary of KB Models
    print("\n" + "="*45)
    print(f"Total KB Models found: {len(kb_models)}")
    for i, (p, q, r) in enumerate(kb_models, 1):
        print(f"  Model {i}: P={p}, Q={q}, R={r}")
    print("="*45)

    # 6. Print Entailment Answers
    print("\nEN-TAIL-MENT VERIFICATION ANSWERS:")
    print("-" * 45)
    for name, entails in list(entailment_results.items()):
        status = "YES (KB entails the query)" if entails else "NO (Not entailed / Counterexample exists)"
        print(f"Does KB entail {name}?\n -> {status}\n")

if __name__ == "__main__":
    run_logic_verification()
