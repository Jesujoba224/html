def reverse_bits(n):
    if n == 0:
        return 0, '0'
    # Get binary representation without '0b'
    bits = bin(n)[2:]
    bit_length = len(bits)
    # Reverse the bits
    reversed_bits = bits[::-1]
    # Convert back to integer
    reversed_num = int(reversed_bits, 2)
    return reversed_num, reversed_bits.zfill(bit_length)

# Main program
if __name__ == "__main__":
    try:
        # Take input from user
        original_number = int(input("Enter your original number: "))
        if original_number == 0:
            print("Original number: 0 (0)")
            print("Reversed Number: 0 (0)")
        else:
            bits = bin(original_number)[2:]
            bit_length = len(bits)
            reversed_number, reversed_bits = reverse_bits(original_number)
            print(f"Original number: {original_number} ({bits})")
            print(f"Reversed Number: {reversed_number} ({reversed_bits})")
    except ValueError:
        print("Please enter a valid integer.")