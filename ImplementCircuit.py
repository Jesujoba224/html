"""ImplementCircuit.py

Represents the logic shown in the attached circuit diagram and prints
the truth table and simplified expression.

From the diagram: Q = (A AND B) OR (B AND C)
which simplifies to Q = B AND (A OR C).

The script prints the truth table for all combinations of A,B,C and
accepts optional command-line arguments to evaluate a specific input.
"""

from typing import Iterable, Tuple
import sys


def circuit_output(a: int, b: int, c: int) -> int:
    """Compute Q for inputs a,b,c where each is 0 or 1."""
    # Ensure inputs are 0 or 1
    A = 1 if a else 0
    B = 1 if b else 0
    C = 1 if c else 0

    q = (A and B) or (B and C)
    return 1 if q else 0


def truth_table() -> Iterable[Tuple[int,int,int,int]]:
    """Yield (A,B,C,Q) for all 8 combinations."""
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                yield (a,b,c,circuit_output(a,b,c))


def print_truth_table():
    print("A B C | Q")
    print("-----------")
    for a,b,c,q in truth_table():
        print(f"{a} {b} {c} | {q}")


def simplify_expression() -> str:
    return "Q = (A AND B) OR (B AND C)  =>  Q = B AND (A OR C)"


if __name__ == '__main__':
    # If three arguments provided, evaluate that single combination
    if len(sys.argv) == 4:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            c = int(sys.argv[3])
        except ValueError:
            print("Arguments must be 0 or 1")
            sys.exit(1)
        if any(bit not in (0,1) for bit in (a,b,c)):
            print("Arguments must be 0 or 1")
            sys.exit(1)
        q = circuit_output(a,b,c)
        print(simplify_expression())
        print(f"Input: A={a}, B={b}, C={c}  =>  Q={q}")
    else:
        print(simplify_expression())
        print()
        print_truth_table()