from dataclasses import dataclass
from typing import List, Set, Union

# --- 1. AST Node Definitions ---
@dataclass(frozen=True)
class Term:
    name: str
    args: tuple = ()
    def __str__(self):
        return f"{self.name}({', '.join(map(str, self.args))})" if self.args else self.name

@dataclass(frozen=True)
class Predicate:
    name: str
    args: tuple
    def __str__(self):
        return f"{self.name}({', '.join(map(str, self.args))})"

@dataclass(frozen=True)
class Not:
    operand: 'Formula'
    def __str__(self):
        return f"¬{self.operand}"

@dataclass(frozen=True)
class And:
    left: 'Formula'
    right: 'Formula'
    def __str__(self):
        return f"({self.left} ∧ {self.right})"

@dataclass(frozen=True)
class Or:
    left: 'Formula'
    right: 'Formula'
    def __str__(self):
        return f"({self.left} ∨ {self.right})"

@dataclass(frozen=True)
class Implies:
    left: 'Formula'
    right: 'Formula'
    def __str__(self):
        return f"({self.left} → {self.right})"

@dataclass(frozen=True)
class ForAll:
    var: str
    body: 'Formula'
    def __str__(self):
        return f"∀{self.var} [{self.body}]"

@dataclass(frozen=True)
class Exists:
    var: str
    body: 'Formula'
    def __str__(self):
        return f"∃{self.var} ({self.body})"

Formula = Union[Predicate, Not, And, Or, Implies, ForAll, Exists]


# --- 2. Conversion Pipeline ---
def eliminate_implications(f: Formula) -> Formula:
    if isinstance(f, Implies):
        return Or(Not(eliminate_implications(f.left)), eliminate_implications(f.right))
    if isinstance(f, Not):
        return Not(eliminate_implications(f.operand))
    if isinstance(f, And):
        return And(eliminate_implications(f.left), eliminate_implications(f.right))
    if isinstance(f, Or):
        return Or(eliminate_implications(f.left), eliminate_implications(f.right))
    if isinstance(f, ForAll):
        return ForAll(f.var, eliminate_implications(f.body))
    if isinstance(f, Exists):
        return Exists(f.var, eliminate_implications(f.body))
    return f

def move_negations_inward(f: Formula) -> Formula:
    if isinstance(f, Not):
        inner = f.operand
        if isinstance(inner, Not):
            return move_negations_inward(inner.operand)
        if isinstance(inner, And):
            return Or(move_negations_inward(Not(inner.left)), move_negations_inward(Not(inner.right)))
        if isinstance(inner, Or):
            return And(move_negations_inward(Not(inner.left)), move_negations_inward(Not(inner.right)))
        if isinstance(inner, ForAll):
            return Exists(inner.var, move_negations_inward(Not(inner.body)))
        if isinstance(inner, Exists):
            return ForAll(inner.var, move_negations_inward(Not(inner.body)))
        return Not(move_negations_inward(inner))
    if isinstance(f, And):
        return And(move_negations_inward(f.left), move_negations_inward(f.right))
    if isinstance(f, Or):
        return Or(move_negations_inward(f.left), move_negations_inward(f.right))
    if isinstance(f, ForAll):
        return ForAll(f.var, move_negations_inward(f.body))
    if isinstance(f, Exists):
        return Exists(f.var, move_negations_inward(f.body))
    return f

def substitute_term(t: Term, var: str, replacement: Term) -> Term:
    if not t.args and t.name == var:
        return replacement
    return Term(t.name, tuple(substitute_term(arg, var, replacement) for arg in t.args))

def substitute(f: Formula, var: str, replacement: Term) -> Formula:
    if isinstance(f, Predicate):
        return Predicate(f.name, tuple(substitute_term(arg, var, replacement) for arg in f.args))
    if isinstance(f, Not):
        return Not(substitute(f.operand, var, replacement))
    if isinstance(f, And):
        return And(substitute(f.left, var, replacement), substitute(f.right, var, replacement))
    if isinstance(f, Or):
        return Or(substitute(f.left, var, replacement), substitute(f.right, var, replacement))
    if isinstance(f, ForAll):
        return f if f.var == var else ForAll(f.var, substitute(f.body, var, replacement))
    if isinstance(f, Exists):
        return f if f.var == var else Exists(f.var, substitute(f.body, var, replacement))
    return f

def skolemize(f: Formula, universal_vars: List[str] = None, counter: List[int] = None) -> Formula:
    if universal_vars is None:
        universal_vars = []
    if counter is None:
        counter = [0]

    if isinstance(f, ForAll):
        return ForAll(f.var, skolemize(f.body, universal_vars + [f.var], counter))
    if isinstance(f, Exists):
        skolem_name = f"f{counter[0] if counter[0] > 0 else ''}"
        counter[0] += 1
        skolem_term = Term(skolem_name, tuple(Term(v) for v in universal_vars))
        substituted_body = substitute(f.body, f.var, skolem_term)
        return skolemize(substituted_body, universal_vars, counter)
    if isinstance(f, And):
        return And(skolemize(f.left, universal_vars, counter), skolemize(f.right, universal_vars, counter))
    if isinstance(f, Or):
        return Or(skolemize(f.left, universal_vars, counter), skolemize(f.right, universal_vars, counter))
    return f

def drop_universal_quantifiers(f: Formula) -> Formula:
    if isinstance(f, ForAll):
        return drop_universal_quantifiers(f.body)
    if isinstance(f, And):
        return And(drop_universal_quantifiers(f.left), drop_universal_quantifiers(f.right))
    if isinstance(f, Or):
        return Or(drop_universal_quantifiers(f.left), drop_universal_quantifiers(f.right))
    return f

def distribute_or_over_and(f: Formula) -> Formula:
    if isinstance(f, And):
        return And(distribute_or_over_and(f.left), distribute_or_over_and(f.right))
    if isinstance(f, Or):
        left = distribute_or_over_and(f.left)
        right = distribute_or_over_and(f.right)
        if isinstance(left, And):
            return And(
                distribute_or_over_and(Or(left.left, right)),
                distribute_or_over_and(Or(left.right, right))
            )
        if isinstance(right, And):
            return And(
                distribute_or_over_and(Or(left, right.left)),
                distribute_or_over_and(Or(left, right.right))
            )
        return Or(left, right)
    return f

def extract_clauses(f: Formula) -> List[Set[str]]:
    if isinstance(f, And):
        return extract_clauses(f.left) + extract_clauses(f.right)
    
    def get_literals(node: Formula) -> Set[str]:
        if isinstance(node, Or):
            return get_literals(node.left) | get_literals(node.right)
        return {str(node)}
    
    return [get_literals(f)]


# --- 3. Build and Convert the Given Formula ---
if __name__ == "__main__":
    x = Term("x")
    y = Term("y")

    # Goal: ∀x [P(x) → ∃y (Q(x, y) ∧ ¬R(y))]
    formula = ForAll(
        "x",
        Implies(
            Predicate("P", (x,)),
            Exists("y", And(Predicate("Q", (x, y)), Not(Predicate("R", (y,)))))
        )
    )

    print("Original FOL:          ", formula)
    step1 = eliminate_implications(formula)
    print("1. Eliminate →:        ", step1)
    step2 = move_negations_inward(step1)
    print("2. Negations inward:   ", step2)
    step3 = skolemize(step2)
    print("3. Skolemize (∃y→f(x)):", step3)
    step4 = drop_universal_quantifiers(step3)
    print("4. Drop ∀:             ", step4)
    cnf = distribute_or_over_and(step4)
    print("5. Final CNF:          ", cnf)
    print("6. Clause Set:         ", extract_clauses(cnf))
