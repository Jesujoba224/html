# Program to swap three numbers from a list

def swap_three_numbers(numbers, index1, index2, index3):
    """
    Swap three numbers in a list at given indices
    
    Args:
        numbers: List of numbers
        index1, index2, index3: Indices of elements to swap
    
    Returns:
        List with swapped elements
    """
    # Create a copy to avoid modifying original list
    temp_list = numbers.copy()
    
    # Swap three numbers: position1 -> position2 -> position3 -> position1
    temp = temp_list[index1]
    temp_list[index1] = temp_list[index2]
    temp_list[index2] = temp_list[index3]
    temp_list[index3] = temp
    
    return temp_list


def swap_three_values(a, b, c):
    """
    Swap three individual values
    
    Args:
        a, b, c: Three numbers to swap
    
    Returns:
        Tuple of swapped values (b, c, a)
    """
    return b, c, a


def main():
    print("=" * 50)
    print("SWAP THREE NUMBERS PROGRAM")
    print("=" * 50)
    
    # Method 1: Swap from a list
    print("\n--- Method 1: Swap from List ---")
    numbers = [10, 20, 30, 40, 50]
    print(f"Original list: {numbers}")
    
    # Swap elements at index 0, 2, 4
    result = swap_three_numbers(numbers, 0, 2, 4)
    print(f"After swapping indices 0, 2, 4: {result}")
    print(f"Original list (unchanged): {numbers}")
    
    # Method 2: Swap three individual numbers
    print("\n--- Method 2: Swap Three Individual Numbers ---")
    first = 100
    second = 200
    third = 300
    
    print(f"Before swap:")
    print(f"  first = {first}")
    print(f"  second = {second}")
    print(f"  third = {third}")
    
    first, second, third = swap_three_values(first, second, third)
    print(f"After swap:")
    print(f"  first = {first}")
    print(f"  second = {second}")
    print(f"  third = {third}")
    
    # Method 3: User input
    print("\n--- Method 3: User Input ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        
        print(f"\nBefore swap: {num1}, {num2}, {num3}")
        
        # Swap using tuple unpacking
        num1, num2, num3 = num2, num3, num1
        print(f"After swap: {num1}, {num2}, {num3}")
    
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")
    
    # Method 4: Swap list elements
    print("\n--- Method 4: Swap List Elements ---")
    my_list = [5, 15, 25, 35, 45]
    print(f"Original list: {my_list}")
    print("Swapping indices 1, 2, 3...")
    
    my_list[1], my_list[2], my_list[3] = my_list[2], my_list[3], my_list[1]
    print(f"After swap: {my_list}")


if __name__ == "__main__":
    main()