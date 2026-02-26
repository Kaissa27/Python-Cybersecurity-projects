import re

# 1. Individual Validation Functions (The "Filters")
def check_length(pwd):
    return (len(pwd) >= 12, "Must be at least 12 characters")

def check_complexity(pwd):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])"
    return (bool(re.search(pattern, pwd)), "Missing required complexity (Upper, Lower, Digit, Special)")

def check_leaked_patterns(pwd):
    # Simulating a check against common/leaked words
    common_passwords = ["Password123", "Admin2026", "Qwerty!@#"]
    return (pwd not in common_passwords, "Password is too common/previously leaked")

# 2. The Auditor (The Pipeline Runner)
def audit_password(password):
    # A list of our function references
    validators = [check_length, check_complexity, check_leaked_patterns]
    
    failed_tests = []
    
    for validate in validators:
        passed, error_msg = validate(password)
        if not passed:
            failed_tests.append(error_msg)
            
    return failed_tests

def main():
    print("--- Pro-Grade Password Audit Pipeline ---")
    
    test_cases = ["weak", "Password123", "LongAndComplex!2026"]
    
    for pwd in test_cases:
        print(f"\nAuditing: {pwd}")
        errors = audit_password(pwd)
        
        if not errors:
            print("[SAFE] Password passed all security gates.")
        else:
            print("[RISK] Password rejected:")
            for e in errors:
                print(f"  - {e}")

if __name__ == "__main__":
    main()
