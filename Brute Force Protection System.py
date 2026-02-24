import time

def simulate_login(attempts_log, username, password):
    # Security Configuration
    MAX_ATTEMPTS = 3
    LOCKOUT_DURATION = 10 # Seconds
    CORRECT_PASSWORD = "CyberSafe2026!"

    current_time = time.time()
    
    # Check if user is already in the log
    if username not in attempts_log:
        attempts_log[username] = {"count": 0, "lockout_until": 0}

    user_state = attempts_log[username]

    # 1. Check Lockout Status
    if current_time < user_state["lockout_until"]:
        wait_time = int(user_state["lockout_until"] - current_time)
        return False, f"LOCKED: Too many attempts. Try again in {wait_time}s."

    # 2. Check Password
    if password == CORRECT_PASSWORD:
        user_state["count"] = 0 # Reset on success
        return True, "Access Granted."
    else:
        user_state["count"] += 1
        
        # 3. Trigger Lockout if threshold reached
        if user_state["count"] >= MAX_ATTEMPTS:
            user_state["lockout_until"] = current_time + LOCKOUT_DURATION
            return False, "ALERT: Threshold reached. Account LOCKED for 10s."
        
        remaining = MAX_ATTEMPTS - user_state["count"]
        return False, f"Invalid password. {remaining} attempts remaining."

def main():
    user_db = {} # Persistent log of attempts
    target_user = "admin_user"

    print("--- Security Gateway: Brute Force Protection ---")
    
    while True:
        print(f"\nUser: {target_user}")
        pwd = input("Enter Password (or 'q' to quit): ")
        if pwd.lower() == 'q': break

        success, message = simulate_login(user_db, target_user, pwd)
        print(f"Result: {message}")

if __name__ == "__main__":
    main()