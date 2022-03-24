import socket


def validate_ip(ip_address):
        try:
            socket.inet_aton(ip_address)
            return True
        except:
            return False