import psutil
import netifaces
import pywifi
from pywifi import const
import socket

class NetworkMonitor:
    def __init__(self):
        self.wifi = pywifi.PyWiFi()

    def get_live_updates(self):
        # Example: Retrieve CPU usage and network interfaces status
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent

        # Example: Retrieve network interfaces and their status
        interfaces = netifaces.interfaces()
        interfaces_status = {}
        for iface in interfaces:
            try:
                addresses = netifaces.ifaddresses(iface)
                ip_address = addresses[netifaces.AF_INET][0]['addr']
            except (KeyError, ValueError):
                ip_address = "Unknown"

            status = self.get_interface_status(iface)
            interfaces_status[iface] = {
                'ip_address': ip_address,
                'status': status
            }

        return {
            'cpu_percent': cpu_percent,
            'memory_percent': memory_percent,
            'interfaces_status': interfaces_status
        }

    def get_interface_status(self, interface):
        try:
            socket.setdefaulttimeout(2)  # Set a timeout for the connection attempt
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((socket.gethostbyname("www.google.com"), 80))
            return 'Connected'
        except Exception:
            return 'Disconnected'

    def get_connected_wifi(self):
        interfaces = self.wifi.interfaces()
        connected_wifi = []

        for iface in interfaces:
            iface.scan()
            scan_results = iface.scan_results()

            for profile in iface.network_profiles():
                try:
                    if profile.akm and len(profile.akm) > 0 and profile.akm[0] == const.AKM_TYPE_WPA2PSK:
                        connected_wifi.append({
                            'interface': iface.name(),
                            'ssid': profile.ssid
                        })
                except Exception as e:
                    print(f"Error processing profile: {e}")
                    continue

        return connected_wifi

    def get_all_interfaces(self):
        # Method to return all network interfaces
        return netifaces.interfaces()

    def monitor_networks(self):
        all_interfaces = netifaces.interfaces()
        interfaces_with_internet = [iface for iface in all_interfaces if self.get_interface_status(iface) == 'Connected']
        connected_wifi = self.get_connected_wifi()

        return all_interfaces, interfaces_with_internet, connected_wifi

    def start_sniffing(self, iface):
        # Placeholder method to start sniffing on a specific interface
        pass
