"""
Tuple to List conversion examples.

Provides a simple function `tuple_to_list` that converts a tuple to a list,
with simple demonstration and basic tests.
"""

from typing import Any, Tuple, List


def tuple_to_list(tup: Tuple[Any, ...]) -> List[Any]:
    """Convert a tuple to a list and return it."""
    return list(tup)


def main() -> None:
    """Demonstrate converting tuples to lists and run basic tests."""
    examples = [
        (1, 2, 3),
        ("a", "b", "c"),
        (1, "two", 3.0, [4, 5]),
        (),
        ((1, 2), (3, 4)),  # nested tuples -> list of tuples
    ]

    for i, t in enumerate(examples, 1):
        l = tuple_to_list(t)
        print(f"Example {i}: tuple={t} -> list={l}")

    # Basic tests
    assert tuple_to_list((1, 2, 3)) == [1, 2, 3]
    assert tuple_to_list(()) == []
    assert tuple_to_list(("x",)) == ["x"]

    # Ensure returned object is a new list, not the same object as the tuple
    t = (1, 2, 3)
    l = tuple_to_list(t)
    assert l == [1, 2, 3] and l is not t

    print("\nAll tests passed ✅")


if __name__ == "__main__":
    main()