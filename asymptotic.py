"""
Time Complexity Analysis Program
Analyzes the time complexity of Shubhangi's code
"""

def myfunction(n):
    """Original function with time complexity analysis"""
    # First Loop: O(n)
    for i in range(0, n+1):
        print("First Loop")
 
    # Second Loop: O(log n)
    j = 1
    while(j <= n+1):
        print("Second Loop ", j)
        j = j * 2
 
    # Third Loop: O(1)
    for i in range(0, 100):
        print("Third loop")


def analyze_time_complexity():
    """Analyze and print time complexity for each loop"""
    print("=" * 60)
    print("TIME COMPLEXITY ANALYSIS FOR SHUBHANGI'S CODE")
    print("=" * 60)
    
    print("\n1. FIRST LOOP ANALYSIS:")
    print("   Code: for i in range(0, n+1):")
    print("         print('First Loop')")
    print("   - Loop runs from 0 to n (inclusive)")
    print("   - Number of iterations: n+1")
    print("   - Each iteration: O(1)")
    print("   - Time Complexity: O(n)")
    
    print("\n2. SECOND LOOP ANALYSIS:")
    print("   Code: j = 1")
    print("         while(j <= n+1):")
    print("             print('Second Loop', j)")
    print("             j = j * 2")
    print("   - j starts at 1 and multiplies by 2 each iteration")
    print("   - Sequence: 1, 2, 4, 8, 16, ..., 2^k")
    print("   - Loop continues while 2^k <= n, so k <= log₂(n)")
    print("   - Number of iterations: log₂(n)")
    print("   - Time Complexity: O(log n)")
    
    print("\n3. THIRD LOOP ANALYSIS:")
    print("   Code: for i in range(0, 100):")
    print("         print('Third loop')")
    print("   - Loop runs exactly 100 times")
    print("   - Independent of n")
    print("   - Time Complexity: O(1)")
    
    print("\n" + "=" * 60)
    print("TOTAL TIME COMPLEXITY CALCULATION:")
    print("=" * 60)
    print("Total = O(n) + O(log n) + O(1)")
    print("\nSince O(n) dominates O(log n) and O(1):")
    print("OVERALL TIME COMPLEXITY = O(n)")
    print("=" * 60)


def complexity_summary():
    """Print a summary table"""
    print("\n\nSUMMARY TABLE:")
    print("-" * 60)
    print(f"{'Loop':<15} {'Type':<25} {'Complexity':<15}")
    print("-" * 60)
    print(f"{'First Loop':<15} {'Linear loop':<25} {'O(n)':<15}")
    print(f"{'Second Loop':<15} {'Exponential growth':<25} {'O(log n)':<15}")
    print(f"{'Third Loop':<15} {'Fixed iterations':<25} {'O(1)':<15}")
    print("-" * 60)
    print(f"{'TOTAL':<15} {'':<25} {'O(n)':<15}")
    print("-" * 60)


if __name__ == "__main__":
    # Display analysis
    analyze_time_complexity()
    complexity_summary()
    
    # Optional: Run the function with a small value of n
    print("\n\nEXAMPLE EXECUTION (with n=5):")
    print("=" * 60)
    myfunction(5)
