import sys
import time
from zkp_gatekeeper import ZKPGatekeeper
from bio_cortex import BioCortex
from auditoria import AuditorForense
from neural_bridge import NeuralBridge

def sistema_active_zero():
    print("\n⚡ INICIANDO PROTOCOLO ACTIVE ZERO (VERSÃO FINAL) ⚡")
    print("====================================================")
    
    # 1. INICIALIZAÇÃO DOS MÓDULOS
    try:
        gate = ZKPGatekeeper()
        cortex = BioCortex()
        auditor = AuditorForense()
        cerebro = NeuralBridge() # Já inclui o RAG
    except Exception as e:
        print(f"❌ ERRO CRÍTICO NA INICIALIZAÇÃO: {e}")
        sys.exit(1)

    # 2. AUTENTICAÇÃO (SIMULADA PARA TESTE RÁPIDO)
    # Em produção, removeriamos o valor padrão ou pediriamos input
    senha_teste = "password" 
    print(f"🔐 [GATEKEEPER] Verificando credenciais de Admin...")
    
    if not gate.verificar_acesso(senha_teste):
        print("❌ ACESSO NEGADO. SISTEMA TRAVADO.")
        sys.exit(1)
    
    print("✅ ACESSO CONCEDIDO. AMBIENTE SEGURO.")
    print("📚 [KNOWLEDGE BASE] Módulo RAG carregado e pronto.")

    # 3. LOOP DE INTERAÇÃO
    while True:
        try:
            prompt = input("\n[LIA-TERMINAL] >> ")
            
            # Comandos de Saída
            if prompt.lower() in ['sair', 'exit', 'q']:
                print("Desligando protocolo...")
                break
                
            if not prompt.strip():
                continue

            # A. FILTRO ÉTICO (BIO-CORTEX)
            aprovado, motivo = cortex.analisar_intencao(prompt)
            
            if not aprovado:
                print(f"🚫 BLOQUEIO LIA: {motivo}")
                auditor.registrar_evento("admin", prompt, "BLOQUEADO")
                continue

            # B. GERAÇÃO COM RAG (NEURAL BRIDGE)
            print("⏳ Processando via RAG...")
            resposta = cerebro.gerar_resposta(prompt)
            
            print(f"🤖 {resposta}")
            
            # C. AUDITORIA FINAL
            h = auditor.registrar_evento("admin", prompt, resposta)
            print(f"⚖️ HASH: {h}")

        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
            break
        except Exception as e:
            print(f"⚠️ ERRO NO LOOP: {e}")

if __name__ == "__main__":
    sistema_active_zero()
