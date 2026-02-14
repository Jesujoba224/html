def binary_to_decimal(b: str):
    b = b.strip()
    if not b:
        return None
    if any(ch not in "01" for ch in b):
        return None
    return int(b, 2)


def main():
    while True:
        s = input("Enter your Binary (or 'q' to quit): ").strip()
        if s.lower() in ("q", "quit", "exit"):
            break
        dec = binary_to_decimal(s)
        if dec is None:
            print("Invalid binary. Use only 0 and 1.")
        else:
            print(f"Decimal :  {dec}")


if __name__ == "__main__":
    main()

