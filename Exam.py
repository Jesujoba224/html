def check_exam_eligibility(age, attendance, gpa):
    """
    Check if a user is eligible for exam based on criteria
    
    Args:
        age: User's age (must be >= 18)
        attendance: Attendance percentage (must be >= 75%)
        gpa: Grade Point Average (must be >= 2.0)
    
    Returns:
        Tuple (eligible: bool, message: str)
    """
    eligibility_checks = []
    
    # Check age
    if age < 18:
        eligibility_checks.append(f"❌ Age requirement failed: Must be 18+, you are {age}")
    else:
        eligibility_checks.append(f"✅ Age requirement passed: {age} years old")
    
    # Check attendance
    if attendance < 75:
        eligibility_checks.append(f"❌ Attendance requirement failed: Must be 75%+, you have {attendance}%")
    else:
        eligibility_checks.append(f"✅ Attendance requirement passed: {attendance}%")
    
    # Check GPA
    if gpa < 2.0:
        eligibility_checks.append(f"❌ GPA requirement failed: Must be 2.0+, you have {gpa}")
    else:
        eligibility_checks.append(f"✅ GPA requirement passed: {gpa}")
    
    # Determine eligibility
    is_eligible = age >= 18 and attendance >= 75 and gpa >= 2.0
    
    return is_eligible, eligibility_checks


def display_eligibility(name, age, attendance, gpa):
    """
    Display exam eligibility status with details
    
    Args:
        name: User's name
        age: User's age
        attendance: Attendance percentage
        gpa: Grade Point Average
    """
    print("\n" + "=" * 60)
    print(f"EXAM ELIGIBILITY CHECK - {name.upper()}")
    print("=" * 60)
    
    print(f"\nStudent Details:")
    print(f"  Name: {name}")
    print(f"  Age: {age} years")
    print(f"  Attendance: {attendance}%")
    print(f"  GPA: {gpa}")
    
    print(f"\nEligibility Criteria:")
    is_eligible, checks = check_exam_eligibility(age, attendance, gpa)
    
    for check in checks:
        print(f"  {check}")
    
    print("\n" + "-" * 60)
    if is_eligible:
        print(f"✅ RESULT: {name} is ELIGIBLE to appear for the exam!")
    else:
        print(f"❌ RESULT: {name} is NOT ELIGIBLE to appear for the exam.")
    print("-" * 60 + "\n")


def get_user_input():
    """
    Get user input for eligibility check
    
    Returns:
        Tuple (name, age, attendance, gpa) or None if invalid
    """
    try:
        name = input("Enter your name: ").strip()
        if not name:
            print("❌ Name cannot be empty!")
            return None
        
        age = int(input("Enter your age: "))
        if age < 0:
            print("❌ Age cannot be negative!")
            return None
        
        attendance = float(input("Enter your attendance percentage (0-100): "))
        if not (0 <= attendance <= 100):
            print("❌ Attendance must be between 0-100%!")
            return None
        
        gpa = float(input("Enter your GPA (0.0-4.0): "))
        if not (0 <= gpa <= 4.0):
            print("❌ GPA must be between 0.0-4.0!")
            return None
        
        return name, age, attendance, gpa
    
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")
        return None


def main():
    print("\n" + "=" * 60)
    print("EXAM ELIGIBILITY CHECKER SYSTEM")
    print("=" * 60)
    print("\nEligibility Requirements:")
    print("  • Minimum Age: 18 years")
    print("  • Minimum Attendance: 75%")
    print("  • Minimum GPA: 2.0")
    
    while True:
        print("\nOptions:")
        print("  1. Check Your Eligibility")
        print("  2. Check Pre-defined Cases")
        print("  3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == "1":
            data = get_user_input()
            if data:
                name, age, attendance, gpa = data
                display_eligibility(name, age, attendance, gpa)
        
        elif choice == "2":
            print("\n--- Pre-defined Test Cases ---")
            
            # Test Case 1: Eligible student
            display_eligibility("Alice Johnson", 20, 85, 3.5)
            
            # Test Case 2: Age too low
            display_eligibility("Bob Smith", 17, 90, 3.0)
            
            # Test Case 3: Low attendance
            display_eligibility("Carol White", 22, 70, 2.8)
            
            # Test Case 4: Low GPA
            display_eligibility("David Brown", 19, 80, 1.9)
            
            # Test Case 5: All criteria failed
            display_eligibility("Eve Davis", 16, 60, 1.5)
            
            # Test Case 6: Edge case - exactly meets criteria
            display_eligibility("Frank Miller", 18, 75, 2.0)
        
        elif choice == "3":
            print("\n✅ Thank you for using Exam Eligibility Checker!")
            print("=" * 60 + "\n")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()