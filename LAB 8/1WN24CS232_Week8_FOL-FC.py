
# First Order Logic - Forward Chaining

# Facts and rules are represented as:
# (Predicate, Argument1, Argument2, ...)

# --------------------------------
# 1. UNIFY
# --------------------------------

def unify(pattern, fact, theta=None):
    if theta is None:
        theta = {}

    if pattern == fact:
        return theta

    # If pattern is a variable
    if isinstance(pattern, str) and pattern.startswith('?'):
        if pattern in theta:
            return unify(theta[pattern], fact, theta)
        theta[pattern] = fact
        return theta

    # If both are tuples
    if isinstance(pattern, tuple) and isinstance(fact, tuple):
        if len(pattern) != len(fact):
            return None

        for p, f in zip(pattern, fact):
            theta = unify(p, f, theta)
            if theta is None:
                return None
        return theta

    return None


# --------------------------------
# 2. SUBST
# --------------------------------

def subst(theta, expression):
    if isinstance(expression, str):
        while expression in theta:
            expression = theta[expression]
        return expression

    if isinstance(expression, tuple):
        return tuple(subst(theta, x) for x in expression)

    return expression


# --------------------------------
# 3. STANDARDIZE VARIABLES
# --------------------------------

counter = 0

def standardize_variables(rule):
    global counter
    counter += 1

    premises, conclusion = rule
    mapping = {}

    def rename(expression):
        if isinstance(expression, str) and expression.startswith('?'):
            if expression not in mapping:
                mapping[expression] = expression + "_" + str(counter)
            return mapping[expression]

        if isinstance(expression, tuple):
            return tuple(rename(x) for x in expression)

        return expression

    return (
        [rename(p) for p in premises],
        rename(conclusion)
    )


# --------------------------------
# 4. FIND ALL MATCHING SUBSTITUTIONS
# --------------------------------

def match_all(premises, facts, theta=None):
    if theta is None:
        theta = {}

    if not premises:
        return [theta]

    results = []

    first = subst(theta, premises[0])

    for fact in facts:
        new_theta = unify(first, fact, theta.copy())

        if new_theta is not None:
            remaining = match_all(
                premises[1:],
                facts,
                new_theta
            )
            results.extend(remaining)

    return results


# --------------------------------
# 5. FOL FORWARD CHAINING
# --------------------------------

def fol_fc_ask(kb, query):

    iteration = 0

    while True:
        iteration += 1
        new_facts = set()

        print(f"\n========== ITERATION {iteration} ==========")

        for rule in kb["rules"]:

            premises, conclusion = standardize_variables(rule)

            substitutions = match_all(
                premises,
                kb["facts"]
            )

            for theta in substitutions:

                result = subst(theta, conclusion)

                if result == query:
                    print("Query matched!")
                    print("Substitution:", theta)
                    print("Derived:", result)
                    return True

                if result not in kb["facts"]:
                    new_facts.add(result)

        if not new_facts:
            print("\nNo new facts generated.")
            return False

        print("New facts generated:")

        for fact in new_facts:
            print(" ", fact)

        kb["facts"].update(new_facts)


# --------------------------------
# 6. KNOWLEDGE BASE
# --------------------------------

kb = {

    "facts": {
        ("American", "Robert"),
        ("Enemy", "A", "America"),
        ("Missile", "M1")
    },

    "rules": [

        # Enemy(x, America) => Hostile(x)
        (
            [("Enemy", "?x", "America")],
            ("Hostile", "?x")
        ),

        # Missile(x) => Weapon(x)
        (
            [("Missile", "?x")],
            ("Weapon", "?x")
        ),

        # Missile(x) => Sells(Robert, x, A)
        (
            [("Missile", "?x")],
            ("Sells", "Robert", "?x", "A")
        ),

        # Law:
        # American(x) AND Weapon(y)
        # AND Sells(x,y,z) AND Hostile(z)
        # => Criminal(x)

        (
            [
                ("American", "?x"),
                ("Weapon", "?y"),
                ("Sells", "?x", "?y", "?z"),
                ("Hostile", "?z")
            ],
            ("Criminal", "?x")
        )
    ]
}


# --------------------------------
# 7. ASK THE QUERY
# --------------------------------

query = ("Criminal", "Robert")

print("Initial Knowledge Base:")
for fact in sorted(kb["facts"]):
    print(fact)

print("\nQuery:", query)

result = fol_fc_ask(kb, query)

if result:
    print("\nRESULT: Robert is a CRIMINAL.")
else:
    print("\nRESULT: Cannot prove Robert is a criminal.")
