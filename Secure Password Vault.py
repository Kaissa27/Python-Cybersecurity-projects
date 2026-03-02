import hashlib
import os
import uuid

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        # Generate a unique "Salt" for this specific user
        self.__salt = os.urandom(32) 
        # Store only the hashed version
        self.__hashed_password = self._hash_func(password)

    def _hash_func(self, password):
        """PBKDF2 (Password-Based Key Derivation Function 2) logic."""
        # We combine the password with the salt and hash it 100,000 times
        
        return hashlib.pbkdf2_hmac(
            'sha256', 
            password.encode('utf-8'), 
            self.__salt, 
            100000
        )

    def verify_password(self, input_password):
        """Compare the hash of the input with the stored hash."""
        new_hash = self._hash_func(input_password)
        return new_hash == self.__hashed_password

def main():
    print("--- Security Lab: Salted Hashing & PBKDF2 ---")
    
    # 1. Registration
    user = UserAccount("admin_user", "CorrectHorseBatteryStaple!")
    print(f"User '{user.username}' registered successfully.")
    print("[INFO] Plaintext password discarded. Salted hash stored.")

    # 2. Login Attempt
    print("\n--- Login Simulation ---")
    attempts = ["wrong_pass", "CorrectHorseBatteryStaple!"]
    
    for attempt in attempts:
        print(f"Attempting login with: {attempt}")
        if user.verify_password(attempt):
            print("  [SUCCESS] Access Granted.")
        else:
            print("  [FAILURE] Invalid Credentials.")

if __name__ == "__main__":

    main()
