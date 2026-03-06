# Create a program
# This script reads an integer from the user and prints the position
# of the rightmost set bit (first set bit from the right).
# If the number is 0 (no set bits) it will report that there is none.

import sys


def rightmost_set_bit_position(n: int) -> int:
    """Return the 1-based position of the rightmost set bit in n.

    If n is 0, return 0 to indicate no set bit.
    """
    if n == 0:
        return 0
    # isolate lowest set bit: n & -n
    low_bit = n & -n
    # compute position by taking log2 or counting trailing zeros
    pos = (low_bit.bit_length())
    return pos


def main() -> None:
    try:
        num_str = input("Enter number: ")
        num = int(num_str.strip(), 0)
    except ValueError:
        print("Invalid integer input.")
        sys.exit(1)

    position = rightmost_set_bit_position(num)
    if position == 0:
        print(f"{num} has no set bits.")
    else:
        print(f"Position of the first set bit:  {position}")


if __name__ == "__main__":
    main()
