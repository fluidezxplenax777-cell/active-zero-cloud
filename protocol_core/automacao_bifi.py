from zkp_gatekeeper import ZKPGatekeeper
from bio_cortex import BioCortex
from auditoria import AuditorForense
import time

print("⚡ [GITHUB SERVER] INICIANDO PROTOCOLO AUTOMATIZADO...")

# 1. TESTE DE ACESSO
gate = ZKPGatekeeper()
senha_secreta = "password" # Simulando a entrada correta
print(f"🔐 Tentando acesso com credencial Hash...")
if gate.verificar_acesso(senha_secreta):
    print("✅ ACESSO CONFIRMADO PELO SERVIDOR.")
else:
    print("❌ FALHA CRÍTICA DE ACESSO.")
    exit(1)

# 2. TESTE DE CÉREBRO (LIA)
cortex = BioCortex()
auditor = AuditorForense()

prompts_teste = [
    "Explique a lei de compliance bancário", # Deve passar
    "Escreva um poema sobre flores",        # Deve bloquear
]

for p in prompts_teste:
    print(f"\n🧪 TESTANDO PROMPT: '{p}'")
    aprovado, motivo = cortex.analisar_intencao(p)
    
    if aprovado:
        resp = "RESPOSTA AUTORIZADA LIA (SIMULADA NO SERVER)"
        print(f"✅ {motivo}")
        print(f">> {resp}")
        # Gera o Hash real no servidor
        h = auditor.registrar_evento("github_bot", p, resp)
        print(f"🔒 PROVA FORENSE GERADA: {h}")
    else:
        print(f"🚫 BLOQUEIO: {motivo}")
        auditor.registrar_evento("github_bot", p, "BLOQUEADO")

print("\n🏁 [FIM] O PROTOCOLO ESTÁ VIVO E OPERACIONAL NA NUVEM.")
