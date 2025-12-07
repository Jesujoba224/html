def fibonacci_terms(n: int):
    """Return a list with first n Fibonacci terms (starting 0, 1...)."""
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    for _ in range(3, n + 1):
        seq.append(seq[-1] + seq[-2])
    return seq


def main():
    try:
        n = int(input("Enter number of terms (n >= 0): ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    series = fibonacci_terms(n)
    if not series:
        print("No terms to display.")
    else:
        print(f"Fibonacci series ({n} terms):")
        print(" ".join(str(x) for x in series))


if __name__ == "__main__":
    main()