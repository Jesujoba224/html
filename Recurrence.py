"""
Recurrence Relation and Time Complexity Analysis
Analyzing Shubhangi's Code Functions
"""

def myfunction1(n):
    """
    Code 1 - Function with loop and multiple recursive calls
    """
    if n <= 0:  # Base case: corrected from n > 0
        return
    
    # For loop: O(n) operations
    for i in range(0, int(n)+1):
        print("Codingal")
    
    # Recursive calls: T(n/2) and T(n/3)
    if n > 1:
        myfunction1(n//2)
        myfunction1(n//3)


def myfunction2(n):
    """
    Code 2 - Function with single recursive call (linear recursion)
    """
    if n <= 1:  # Base case
        return
    
    # O(1) operation
    print("Codingal")
    
    # Recursive call: T(n-1)
    myfunction2(n - 1)


def analyze_recurrence_relations():
    """Analyze and print recurrence relations for both functions"""
    
    print("=" * 70)
    print("RECURRENCE RELATION AND TIME COMPLEXITY ANALYSIS")
    print("=" * 70)
    
    # Code 1 Analysis
    print("\n" + "=" * 70)
    print("CODE 1: myfunction1(n)")
    print("=" * 70)
    
    print("\nCode Structure:")
    print("""
    def myfunction1(n):
        if n <= 0:
            return                    # Base case
        
        for i in range(0, n+1):       # Loop: O(n)
            print("Codingal")
        
        myfunction1(n/2)              # Recursive call 1
        myfunction1(n/3)              # Recursive call 2
    """)
    
    print("\n" + "-" * 70)
    print("RECURRENCE RELATION FOR CODE 1:")
    print("-" * 70)
    print("T(n) = O(n) + T(n/2) + T(n/3)")
    print("\nWhere:")
    print("  - O(n) represents the for loop (runs n+1 times)")
    print("  - T(n/2) represents the first recursive call with n/2")
    print("  - T(n/3) represents the second recursive call with n/3")
    print("  - Base case: T(n) = 1 when n <= 0")
    
    print("\n" + "-" * 70)
    print("TIME COMPLEXITY ANALYSIS (Using Master Theorem):")
    print("-" * 70)
    print("T(n) = O(n) + T(n/2) + T(n/3)")
    print("\nApplying Master Theorem / Recursion Tree Method:")
    print("  Level 0: n operations")
    print("  Level 1: n/2 + n/3 = 5n/6 operations")
    print("  Level 2: (n/4 + n/6) + (n/6 + n/9) = 25n/36 operations")
    print("  ...")
    print("\nThe sum converges to: n * (1 + 5/6 + (5/6)² + ... ) = O(n)")
    print("\nFINAL TIME COMPLEXITY: O(n)")
    
    # Code 2 Analysis
    print("\n" + "=" * 70)
    print("CODE 2: myfunction2(n)")
    print("=" * 70)
    
    print("\nCode Structure:")
    print("""
    def myfunction2(n):
        if n <= 1:
            return                    # Base case
        
        print("Codingal")             # O(1) operation
        
        myfunction2(n - 1)            # Recursive call with n-1
    """)
    
    print("\n" + "-" * 70)
    print("RECURRENCE RELATION FOR CODE 2:")
    print("-" * 70)
    print("T(n) = O(1) + T(n-1)")
    print("\nWhere:")
    print("  - O(1) represents the print statement (constant time)")
    print("  - T(n-1) represents the recursive call with n-1")
    print("  - Base case: T(n) = 1 when n <= 1")
    
    print("\n" + "-" * 70)
    print("TIME COMPLEXITY ANALYSIS (Linear Recursion):")
    print("-" * 70)
    print("T(n) = O(1) + T(n-1)")
    print("     = O(1) + O(1) + T(n-2)")
    print("     = O(1) + O(1) + O(1) + T(n-3)")
    print("     = ... (n times)")
    print("     = n * O(1)")
    print("\nFINAL TIME COMPLEXITY: O(n)")
    
    # Comparison Summary
    print("\n" + "=" * 70)
    print("SUMMARY AND COMPARISON TABLE")
    print("=" * 70)
    print(f"\n{'Metric':<35} {'Code 1':<20} {'Code 2':<20}")
    print("-" * 70)
    print(f"{'Recurrence Relation':<35} {'T(n)=O(n)+T(n/2)+T(n/3)':<20} {'T(n)=O(1)+T(n-1)':<20}")
    print(f"{'Recursion Type':<35} {'Tree Recursion':<20} {'Linear Recursion':<20}")
    print(f"{'Number of Branches':<35} {'2':<20} {'1':<20}")
    print(f"{'Depth of Recursion':<35} {'O(log n)':<20} {'O(n)':<20}")
    print(f"{'Time Complexity':<35} {'O(n)':<20} {'O(n)':<20}")
    print(f"{'Space Complexity':<35} {'O(log n)':<20} {'O(n)':<20}")
    print("-" * 70)


def execution_example():
    """Show example execution"""
    print("\n" + "=" * 70)
    print("EXAMPLE EXECUTION")
    print("=" * 70)
    
    print("\n--- CODE 1 EXECUTION (myfunction1(3)) ---")
    print("Output:")
    myfunction1(3)
    
    print("\n--- CODE 2 EXECUTION (myfunction2(4)) ---")
    print("Output:")
    myfunction2(4)


if __name__ == "__main__":
    analyze_recurrence_relations()
    execution_example()
    
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
