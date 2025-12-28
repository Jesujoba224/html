"""Simple Robot class example

Harsh has two robots (Tom and Jerry). Each robot can introduce its name using
the `introduce` method.
"""

from __future__ import annotations


class Robot:
    """A simple robot that can introduce itself by name."""

    def __init__(self, name: str) -> None:
        """Initialize the robot with a name."""
        self.name = name

    def introduce(self) -> None:
        """Print a friendly introduction that includes the robot's name."""
        print(f"Hello, I'm {self.name}.")

    def set_name(self, new_name: str) -> None:
        """Update the robot's name (useful if the robot's memory was reset)."""
        self.name = new_name


def main() -> None:
    """Create two robots (Tom and Jerry) and make them introduce themselves."""
    tom = Robot("Tom")
    jerry = Robot("Jerry")

    tom.introduce()
    jerry.introduce()


if __name__ == "__main__":
    main()
