import datetime

# Base Class: Represents a generic Network Packet
class Packet:
    def __init__(self, source_ip, destination_ip, port, payload):
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.port = port
        self.payload = payload

# Base Class for Rules: Demonstrates Abstraction
class FirewallRule:
    def __init__(self, description):
        self.description = description

    def is_allowed(self, packet):
        # To be overridden by specific rule types
        return True

# Specific Rule: Filtering by IP (Inheritance)
class IPBlockRule(FirewallRule):
    def __init__(self, description, blocked_ip):
        super().__init__(description)
        self.blocked_ip = blocked_ip

    def is_allowed(self, packet):
        return packet.source_ip != self.blocked_ip

# Specific Rule: Filtering by Port (Inheritance)
class PortFilterRule(FirewallRule):
    def __init__(self, description, allowed_ports):
        super().__init__(description)
        self.allowed_ports = allowed_ports

    def is_allowed(self, packet):
        return packet.port in self.allowed_ports

# The Firewall: Demonstrates Composition (it "has a" list of rules)
class Firewall:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def process_packet(self, packet):
        for rule in self.rules:
            if not rule.is_allowed(packet):
                print(f"[BLOCK] Rule: {rule.description} | {packet.source_ip} -> {packet.port}")
                return False
        print(f"[ALLOW] Packet from {packet.source_ip} to port {packet.port} accepted.")
        return True

def main():
    # Initialize Firewall and Rules
    my_fw = Firewall()
    my_fw.add_rule(IPBlockRule("Block Malicious Bot", "192.168.1.100"))
    my_fw.add_rule(PortFilterRule("Allow Web Traffic Only", [80, 443]))

    # Simulated incoming traffic
    traffic = [
        Packet("10.0.0.5", "10.0.0.1", 443, "Secure Data"),
        Packet("192.168.1.100", "10.0.0.1", 80, "Malicious payload"),
        Packet("10.0.0.8", "10.0.0.1", 22, "SSH Attempt")
    ]

    print("--- OOPS Firewall Rule Engine Active ---")
    for p in traffic:
        my_fw.process_packet(p)

if __name__ == "__main__":
    main()