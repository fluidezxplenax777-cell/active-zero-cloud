import hashlib
import datetime
import os

class AuditorForense:
    def registrar_evento(self, usuario, prompt, resposta):
        timestamp = datetime.datetime.now().isoformat()
        evento = f"{timestamp}|{usuario}|{prompt}|{resposta}"
        h = hashlib.sha256(evento.encode()).hexdigest()
        
        # Em produção, salvaria no banco. No GitHub Action, apenas printa.
        print(f"📝 [LOG] {timestamp} - HASH: {h}")
        return h
