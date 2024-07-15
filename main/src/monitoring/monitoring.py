import psutil
import netifaces
import logging
import scapy.all as scapy
from scapy.layers.inet import IP

class NetworkMonitor:
    def __init__(self):
        self.anomalies = []
        self.logger = self._setup_logger()
        self.network_interface = self._get_wifi_interface()
        self.network_traffic_data = {}
        self.live_feed_data = {'messages': []}
        self.sniffer = None
        self.console_open = False

    def _setup_logger(self):
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(__name__)

    def _get_wifi_interface(self):
        # Function to get the active WiFi interface
        wifi_interface = None
        for iface in netifaces.interfaces():
            if 'wlan' in iface.lower():  # Assuming WiFi interface starts with 'wlan'
                wifi_interface = iface
                break
        return wifi_interface

    def get_live_updates(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        interfaces_status = self._get_interfaces_status()
        network_traffic = self._get_network_traffic()
        live_feed = self._get_live_feed()

        return {
            'cpu_percent': cpu_percent,
            'memory_percent': memory_percent,
            'interfaces_status': interfaces_status,
            'network_traffic': network_traffic,
            'live_feed': live_feed,
            'anomalies': self.anomalies,
            'console_open': self.console_open
        }

    def open_console(self):
        if not self.console_open:
            self.console_open = True
            self.logger.info("Opening Network Traffic Console.")
            self.start_sniffing()

    def close_console(self):
        if self.console_open:
            self.console_open = False
            self.logger.info("Closing Network Traffic Console.")
            self.stop_sniffing()

    def is_console_open(self):
        return self.console_open

    def _get_interfaces_status(self):
        interfaces_status = {}
        for iface in netifaces.interfaces():
            ip_address = self._get_ip_address(iface)
            status = 'UP' if ip_address else 'DOWN'
            interfaces_status[iface] = {'ip_address': ip_address, 'status': status}
        return interfaces_status

    def _get_ip_address(self, iface):
        try:
            return netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
        except (KeyError, IndexError):
            return None

    def _get_network_traffic(self):
        network_traffic = {}
        for iface in netifaces.interfaces():
            stats = psutil.net_io_counters(pernic=True).get(iface)
            if stats:
                network_traffic[iface] = {
                    'bytes_sent': stats.bytes_sent,
                    'bytes_recv': stats.bytes_recv
                }
        return network_traffic

    def _get_live_feed(self):
        return self.live_feed_data

    def start_sniffing(self):
        if self.network_interface:
            self.logger.info(f"Starting packet sniffing on interface {self.network_interface}")
            self.sniffer = scapy.AsyncSniffer(iface=self.network_interface, prn=self._process_packet, store=False)
            self.sniffer.start()
        else:
            self.logger.warning("No active WiFi interface found. Cannot start sniffing.")

    def stop_sniffing(self):
        if self.sniffer and self.sniffer.running:
            self.sniffer.stop()
            self.logger.info("Stopped packet sniffing.")
            self.sniffer = None

    def _process_packet(self, packet):
        try:
            if packet.haslayer(IP):
                ip_layer = packet[IP]
                self.logger.info(f"New Packet: {ip_layer.src} -> {ip_layer.dst}")
                packet_info = {
                    'src': ip_layer.src,
                    'dst': ip_layer.dst,
                    'proto': ip_layer.proto,
                    'len': ip_layer.len,
                    'ttl': ip_layer.ttl
                }
                self.network_traffic_data.setdefault(ip_layer.src, []).append(packet_info)
                # Uncomment the next line if `_detect_anomaly` method is implemented
                # self._detect_anomaly(packet_info)
                self._update_live_feed(f"New packet from {ip_layer.src} to {ip_layer.dst}")
        except Exception as e:
            self.logger.error(f"Error processing packet: {e}")

    def _update_live_feed(self, message):
        self.live_feed_data['messages'].append(message)
        if len(self.live_feed_data['messages']) > 10:
            self.live_feed_data['messages'].pop(0)  # Keep live feed limited to 10 messages

    def _detect_anomaly(self, packet_info):
        # Placeholder method to detect anomalies based on packet data
        pass

    # Add more methods as needed for anomaly detection, logging, etc.

# Example usage:
# monitor = NetworkMonitor()
# monitor.open_console()
# monitor.close_console()
