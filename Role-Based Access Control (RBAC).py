import hashlib

# Base Class: Demonstrates Abstraction and Encapsulation
class User:
    def __init__(self, username, password):
        self.username = username
        # Encapsulation: Prefixing with __ makes it "Private"
        self.__password_hash = self._hash_password(password)
        self.role = "Guest"

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_access(self, resource):
        print(f"[ACCESS DENIED] {self.username} ({self.role}) cannot access {resource}")

# Inheritance: Admin inherits from User
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = "Admin"

    # Polymorphism: Overriding the access check for elevated privileges
    def check_access(self, resource):
        print(f"[ACCESS GRANTED] Admin {self.username} is accessing {resource}...")
        print(f"[*] Modifying system logs... Done.")

# Inheritance: Auditor inherits from User
class Auditor(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = "Auditor"

    def check_access(self, resource):
        print(f"[READ-ONLY ACCESS] Auditor {self.username} is viewing {resource}.")

def main():
    # Creating a list of different user objects
    users = [
        User("jdoe_99", "password123"),
        Admin("root_sys", "S3cure_P@ss!"),
        Auditor("audit_team", "Checking123")
    ]

    target_resource = "SECURE_DATABASE_V1"

    print("--- Cyber-Security RBAC Simulation ---")
    for user in users:
        print(f"\nRequesting Access for: {user.username}")
        user.check_access(target_resource)

if __name__ == "__main__":
    main()