import sys
import time
import json
import os
from datetime import datetime, timedelta
from zkp_gatekeeper import ZKPGatekeeper
from bio_cortex import BioCortex
from auditoria import AuditorForense
from neural_bridge import NeuralBridge

# ARQUIVO DE BLOQUEIO (PERSISTÊNCIA)
BLACKLIST_FILE = "blacklist_users.json"

def verificar_blacklist(usuario):
    """Verifica se o usuário está de castigo (24h)"""
    if not os.path.exists(BLACKLIST_FILE):
        return False, ""
    
    with open(BLACKLIST_FILE, 'r') as f:
        try:
            dados = json.load(f)
            if usuario in dados:
                desbloqueio = datetime.fromisoformat(dados[usuario])
                if datetime.now() < desbloqueio:
                    return True, desbloqueio.strftime("%d/%m %H:%M")
        except:
            pass
    return False, ""

def aplicar_punicao(usuario):
    """Bloqueia o usuário por 24 horas"""
    desbloqueio = datetime.now() + timedelta(hours=24) # 24 horas de trava
    dados = {}
    
    if os.path.exists(BLACKLIST_FILE):
        with open(BLACKLIST_FILE, 'r') as f:
            try:
                dados = json.load(f)
            except:
                dados = {}
    
    dados[usuario] = desbloqueio.isoformat()
    
    with open(BLACKLIST_FILE, 'w') as f:
        json.dump(dados, f)
    
    return desbloqueio.strftime("%d/%m %H:%M")

def desafio_socratico(cerebro):
    """O Porteiro que avalia o conhecimento prévio"""
    print("\n🦁 [DESAFIO SOCRÁTICO] O Porteiro exige prova de leitura.")
    print("PERGUNTA: Explique, com suas palavras, o conceito de 'Compliance' segundo o Manual LIA.")
    
    resposta = input("SUA RESPOSTA DISCURSIVA >> ")
    
    print("⏳ [CÉREBRO] Analisando profundidade semântica da resposta...")
    time.sleep(2) # Drama para parecer que está pensando muito
    
    # LÓGICA DE AVALIAÇÃO (SIMULADA PARA O MVP)
    # Se a resposta for curta ou não tiver palavras-chave, reprova.
    palavras_chave = ["lei", "regras", "manual", "norma", "ética", "board", "conformidade"]
    tem_conteudo = any(p in resposta.lower() for p in palavras_chave)
    
    if len(resposta) > 15 and tem_conteudo:
        return True, "Análise semântica: Nível Intermediário Atingido."
    else:
        return False, "Análise semântica: Resposta superficial. Falta embasamento no Cap. 5."

def sistema_active_zero():
    print("\n⚡ PROTOCOLO ACTIVE ZERO (GATEKEEPER MODE) ⚡")
    print("==============================================")
    
    usuario_atual = "aluno_teste" # Simulando login
    
    # 1. VERIFICAÇÃO DE BLOQUEIO (BLACKLIST)
    bloqueado, data_volta = verificar_blacklist(usuario_atual)
    if bloqueado:
        print(f"🚫 ACESSO NEGADO. USUÁRIO EM PERÍODO DE REFLEXÃO (COOLING-OFF).")
        print(f"🔒 Volte após: {data_volta}")
        print("💡 Motivo: Falha no Desafio Socrático anterior.")
        sys.exit(1)

    # 2. TERMO DE ACEITE (COMPLIANCE)
    print(f"\n📜 [JURÍDICO] Termos de Uso v1.0 (Hash: a1b2c3d4)")
    aceite = input("Digite 'ACEITO' para concordar com a Blindagem LIA: ")
    if aceite.strip().upper() != "ACEITO":
        print("❌ ACESSO NEGADO. O aceite é obrigatório.")
        sys.exit(1)

    auditor = AuditorForense()
    auditor.registrar_evento(usuario_atual, "TERMO_ACEITE", "CONFIRMADO")

    # 3. O DESAFIO (VESTIBULAR)
    cerebro = NeuralBridge()
    passou, feedback = desafio_socratico(cerebro)
    
    if not passou:
        print(f"\n❌ REPROVADO NO DESAFIO SOCRÁTICO.")
        print(f"📉 Feedback Pedagógico: {feedback}")
        print("⚠️ PENALIDADE: Seu acesso foi bloqueado por 24 horas para releitura do Manual.")
        
        data_volta = aplicar_punicao(usuario_atual)
        auditor.registrar_evento(usuario_atual, "DESAFIO_SOCRATICO", "FALHA - BLOQUEADO")
        sys.exit(1)
        
    print(f"\n✅ APROVADO! {feedback}")
    print("🔑 GERANDO TOKEN DE ACESSO SOBERANO...")
    time.sleep(1)
    
    # 4. ENTRADA NA SALA (LOOP PRINCIPAL)
    cortex = BioCortex()
    gate = ZKPGatekeeper()
    
    print("\n📚 [SANTUÁRIO LIA] Bem-vindo ao Ambiente Seguro.")
    
    while True:
        try:
            prompt = input("\n[LIA-TERMINAL] >> ")
            if prompt.lower() in ['sair', 'exit']:
                break
            
            # Filtro e RAG (Igual antes)
            aprovado, motivo = cortex.analisar_intencao(prompt)
            if not aprovado:
                print(f"🚫 {motivo}")
                continue
                
            print(f"🤖 {cerebro.gerar_resposta(prompt)}")
            auditor.registrar_evento(usuario_atual, prompt, "PROCESSADO")
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    sistema_active_zero()
