import functools
import time

# 1. The Security Decorator: Wraps any function with an MFA check
def require_mfa(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        print(f"\n[SECURITY CHECK] Challenging user '{user}' for MFA...")
        # Simulate a One-Time Password (OTP) check
        otp_attempt = "123456" # In reality, this comes from an input or app
        authorized_otp = "123456" 
        
        if otp_attempt == authorized_otp:
            print(f"[SUCCESS] MFA Verified. Executing {func.__name__}...")
            return func(user, *args, **kwargs)
        else:
            print(f"[BLOCK] MFA Failed for user '{user}'. Access Denied.")
            return None
    return wrapper

# 2. Sensitive Functions: "Decorated" with our security layer
@require_mfa
def access_vault(user):
    print(f"--- VAULT OPENED for {user} ---")
    print("Secret Data: The launch codes are 0000.")

@require_mfa
def delete_database(user, db_name):
    print(f"--- DATABASE '{db_name}' DELETED BY {user} ---")

def main():
    print("--- Functional Security: Decorator Logic ---")
    
    # Attempting sensitive actions
    access_vault("Admin_Alice")
    
    time.sleep(1)
    
    delete_database("SysOp_Bob", "Production_Server")

if __name__ == "__main__":

    main()
