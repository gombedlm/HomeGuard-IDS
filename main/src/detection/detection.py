class Detection:
    def __init__(self):
        self.anomalies = []

    def detect_anomalies(self, data):
        self.anomalies.clear()  # Clear previous anomalies
        for packet in data:
            if self.detect_malicious_traffic(packet) or self.detect_unusual_behavior(packet) or self.detect_large_packets(packet) or self.detect_suspicious_domains(packet):
                self.anomalies.append(packet)
        
        return self.anomalies

    def detect_malicious_traffic(self, packet):
        # Detect known attack signatures or patterns
        attack_signatures = [
            "malware", "virus", "exploit", "ransomware",
            "trojan", "backdoor", "command injection", "SQL injection"
        ]
        for signature in attack_signatures:
            if signature in packet.lower():  # Case-insensitive matching
                return True
        return False

    def detect_unusual_behavior(self, packet):
        # Detect unusual patterns or behaviors
        # Example: Detects unusual packet size or structure
        if len(packet) > 2000 or packet.startswith("AAA"):
            return True
        return False

    def detect_large_packets(self, packet):
        # Detect unusually large packets
        # Example: Packets exceeding the standard MTU size
        if len(packet) > 1500:  # Typical Ethernet MTU size
            return True
        return False

    def detect_suspicious_domains(self, packet):
        # Detect communication with suspicious domains or IPs
        suspicious_domains = [
            "malicious.com", "hackers.net", "phishingdomain.com",
            "spyware.org", "botnetserver.net"
        ]
        for domain in suspicious_domains:
            if domain in packet:
                return True
        return False

    def detect_anomalies_advanced(self, data, detection_methods=None):
        self.anomalies.clear()  # Clear previous anomalies
        if not detection_methods:
            detection_methods = [
                self.detect_malicious_traffic,
                self.detect_unusual_behavior,
                self.detect_large_packets,
                self.detect_suspicious_domains
            ]

        for packet in data:
            for method in detection_methods:
                if method(packet):
                    self.anomalies.append(packet)
                    break  # Exit loop if any method detects an anomaly
        
        return self.anomalies
