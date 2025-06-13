from ipware import get_client_ip
from hashlib import sha256


def get_pure_ip(request):
    ip_address, _ = get_client_ip(request)
    return ip_address


def get_hash_ip_address(request):
    ip_address = get_pure_ip(request)
    hasher = sha256()
    hasher.update(ip_address.encode('utf-8'))
    return hasher.hexdigest()
