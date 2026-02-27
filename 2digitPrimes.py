# Program to list all prime numbers with exactly two digits (10-99).
# Shubhangi's teacher wants primes but initially mentioned 3-digit; here
# we generate the 2-digit primes per the exercise description.


def is_prime(n: int) -> bool:
    """Return True if n is prime (n >= 2)."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    # check odd divisors up to sqrt
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def two_digit_primes() -> list[int]:
    """Return a list of all prime numbers with two digits."""
    primes = []
    for num in range(10, 100):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    primes = two_digit_primes()
    print("Two-digit prime numbers:", primes)
