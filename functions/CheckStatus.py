from ping3 import ping

class CheckStatus:
    def __init__(self, ip):
        self.ip = ip
    
    def check(self):
        response = ping(self.ip, timeout=2, unit="ms")
        if response is not None:
            return True
        else:
            return False