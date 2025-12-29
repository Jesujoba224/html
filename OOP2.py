"""A simple OOP-based expression solver.

This module implements two classes:
- ExpressionSolver: safely evaluates arithmetic expressions using AST
- Expression: represents an expression string and stores the computed result

Supported operators: +, -, *, /, %, //, ** and unary +/-. Only numeric literals are allowed.
Functions are reusable blocks of code
Variables are storage place for data
Library is a collection of functions

Uses of fuctions, library, etc:
* To make coding faster and easier
"""

import ast
import operator
from typing import Union, Optional

Number = Union[int, float]

class ExpressionSolver:
    """Evaluate arithmetic expressions safely using Python's AST module."""

    _bin_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }

    _unary_ops = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def evaluate(self, expression: str) -> Number:
        """Evaluate the given expression string and return its numeric result.

        Raises ValueError for unsupported syntax or types.
        """
        try:
            parsed = ast.parse(expression, mode="eval")
        except SyntaxError as exc:
            raise ValueError(f"Invalid expression: {exc}") from exc
        return self._eval(parsed.body)

    def _eval(self, node) -> Number:
        if isinstance(node, ast.BinOp):
            left = self._eval(node.left)
            right = self._eval(node.right)
            op_type = type(node.op)
            func = self._bin_ops.get(op_type)
            if func is None:
                raise ValueError(f"Unsupported binary operator: {op_type.__name__}")
            return func(left, right)

        if isinstance(node, ast.UnaryOp):
            operand = self._eval(node.operand)
            op_type = type(node.op)
            func = self._unary_ops.get(op_type)
            if func is None:
                raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
            return func(operand)

        # numeric literal (Python 3.8+: ast.Constant)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Only int/float constants are allowed")

        # legacy numeric node
        if hasattr(ast, 'Num') and isinstance(node, ast.Num):
            return node.n

        raise ValueError(f"Unsupported expression node: {type(node).__name__}")


class Expression:
    """Represents an expression and its computed result."""

    def __init__(self, expr: str):
        self.expr = expr
        self.result: Optional[Number] = None

    def compute(self, solver: ExpressionSolver) -> Number:
        """Compute and store the result using the provided solver."""
        self.result = solver.evaluate(self.expr)
        return self.result


def main() -> None:
    solver = ExpressionSolver()

    samples = [
        "2 + 3 * 4",
        "(1 + 2) / (3 - 1)",
        "5 - 2 * (3 + 1)",
        "2 ** 3 + 1",
        "-5 + 3",
    ]

    print("Example evaluations:")
    for s in samples:
        expr = Expression(s)
        try:
            print(f"{s} = {expr.compute(solver)}")
        except Exception as exc:
            print(f"{s} -> Error: {exc}")

    # simple interactive loop
    while True:
        try:
            user = input("Enter expression (or 'q' to quit): ").strip()
            if user.lower() in {"q", "quit", "exit"}:
                print("Goodbye!")
                break
            expr = Expression(user)
            print("Result:", expr.compute(solver))
        except Exception as exc:
            print("Error:", exc)


if __name__ == "__main__":
    main()
