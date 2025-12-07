def is_armstrong(number: int) -> bool:
    """Return True if number is an Armstrong number."""
    if number < 0:
        return False
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return sum(d ** power for d in digits) == number


def main():
    try:
        val = input("Enter a non-negative integer to check for Armstrong: ").strip()
        n = int(val)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if is_armstrong(n):
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is NOT an Armstrong number.")


if __name__ == "__main__":
    main()