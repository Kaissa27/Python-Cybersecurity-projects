import hashlib
import time
import uuid

# Base Class: Represents a Cryptographic Key
class CryptoKey:
    def __init__(self, owner):
        self.key_id = str(uuid.uuid4())[:8]
        self.owner = owner
        self.created_at = time.time()
        self.__secret_value = hashlib.sha256(str(time.time()).encode()).hexdigest()
        self.is_active = True

    def get_key_value(self, requester):
        if requester == self.owner and self.is_active:
            return self.__secret_value
        return "ACCESS DENIED"

# The KMS Engine: Demonstrates Composition and Lifecycle Management
class KeyManager:
    def __init__(self):
        self.__vault = {} # Dictionary of CryptoKey objects
        self.audit_logs = []

    def generate_new_key(self, user):
        new_key = CryptoKey(user)
        self.__vault[user] = new_key
        self._log(f"New key {new_key.key_id} generated for {user}")
        return new_key.key_id

    def rotate_key(self, user):
        """Disables old key and creates a new one (Security Best Practice)"""
        if user in self.__vault:
            self.__vault[user].is_active = False
            old_id = self.__vault[user].key_id
            new_id = self.generate_new_key(user)
            self._log(f"Key Rotation: {old_id} -> {new_id}")
            return new_id

    def _log(self, action):
        entry = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {action}"
        self.audit_logs.append(entry)

    def retrieve_key(self, user):
        if user in self.__vault:
            return self.__vault[user].get_key_value(user)
        return "No key found."

def main():
    kms = KeyManager()

    # 1. User registers a key
    print("--- KMS Operations: Key Generation ---")
    user_a = "CloudServer_01"
    kms.generate_new_key(user_a)
    print(f"Initial Key: {kms.retrieve_key(user_a)[:15]}...")

    # 2. Key Rotation (Simulating a security policy update)
    print("\n--- KMS Operations: Key Rotation ---")
    time.sleep(1)
    kms.rotate_key(user_a)
    print(f"Rotated Key: {kms.retrieve_key(user_a)[:15]}...")

    # 3. Unauthorized access attempt
    print("\n--- KMS Operations: Security Audit ---")
    print(f"Intruder attempt: {kms.retrieve_key('Hacker_IP')}")

    print("\n--- Official Audit Trail ---")
    for entry in kms.audit_logs:
        print(entry)

if __name__ == "__main__":
    main()