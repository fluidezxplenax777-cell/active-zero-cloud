import hashlib
import time

class ZKPGatekeeper:
    def __init__(self):
        # Hash da senha 'password'
        self.master_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

    def verificar_acesso(self, token_input):
        # Simula processamento pesado
        time.sleep(0.5) 
        input_hash = hashlib.sha256(token_input.encode()).hexdigest()
        return input_hash == self.master_hash
