import hashlib
import datetime
import os

class AuditorForense:
    def __init__(self):
        self.log_file = "audit_trail_immutable.log"

    def registrar_evento(self, usuario, prompt, resposta):
        timestamp = datetime.datetime.now().isoformat()
        
        # Cria a string única do evento
        evento_raw = f"{timestamp}|{usuario}|{prompt}|{resposta}"
        
        # Assina digitalmente (SHA-256)
        evento_hash = hashlib.sha256(evento_raw.encode()).hexdigest()
        
        # Formata a linha para o arquivo
        linha_log = f"[{timestamp}] HASH:{evento_hash} | USR:{usuario} | CMD:{prompt[:20]}...\n"
        
        # GRAVA NO DISCO (PERSISTÊNCIA)
        with open(self.log_file, "a") as f:
            f.write(linha_log)
            
        # MOSTRA NA TELA (FEEDBACK)
        print(f"📝 [LOG DISCO] Salvo em {self.log_file}")
        return evento_hash
