import hashlib
import datetime

class SecureMessage:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        # Generate a signature at the moment of creation
        self.__signature = self._generate_signature()

    def _generate_signature(self):
        """Creates a unique hash based on the sender, content, and time."""
        raw_data = f"{self.sender}{self.content}{self.timestamp}"
        return hashlib.sha256(raw_data.encode()).hexdigest()

    def verify_integrity(self):
        """Re-calculates the hash to see if the message was altered."""
        current_hash = self._generate_signature()
        return current_hash == self.__signature

    def get_details(self):
        return f"[{self.timestamp}] {self.sender}: {self.content}"

class MessagingServer:
    def __init__(self):
        self.inbox = []

    def receive_message(self, message_obj):
        print(f"\nIncoming message from {message_obj.sender}...")
        
        # Security Check: Verify the signature before showing it
        if message_obj.verify_integrity():
            print("[VERIFIED] Digital Signature matches. Message is authentic.")
            self.inbox.append(message_obj)
        else:
            print("[!!] ALERT: MESSAGE TAMPERING DETECTED! Signature mismatch.")

def main():
    server = MessagingServer()

    # 1. Create a legitimate message
    msg1 = SecureMessage("Alice", "Transfer $500 to Bob.")
    server.receive_message(msg1)

    # 2. Simulate a "Man-in-the-Middle" attack
    # An attacker intercepts the object and changes the content
    msg2 = SecureMessage("Charlie", "Meet at the park.")
    print("\n--- ATTACK IN PROGRESS ---")
    msg2.content = "Meet at the dark alley." # Direct modification of the object
    
    server.receive_message(msg2)

    # 3. View legitimate inbox
    print("\n--- Secure Inbox ---")
    for m in server.inbox:
        print(m.get_details())

if __name__ == "__main__":
    main()