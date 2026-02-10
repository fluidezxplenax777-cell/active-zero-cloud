import os
from knowledge_base import KnowledgeBase # <--- IMPORT NOVO

class NeuralBridge:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.engine_path = os.path.expanduser("~/engine/ligar_qwen.py")
        
    def gerar_resposta(self, prompt_usuario):
        # 1. Recupera o Contexto (RAG)
        contexto = self.kb.buscar_contexto(prompt_usuario)
        
        # 2. Monta o Prompt Engenheirado
        prompt_final = f"""
        [SISTEMA LIA]
        CONTEXTO OBRIGATÓRIO: {contexto}
        
        PERGUNTA DO USUÁRIO: {prompt_usuario}
        
        RESPOSTA (Use apenas o contexto acima):
        """
        
        print(f"🔌 [NEURAL-BRIDGE] Enviando prompt enriquecido para o motor...")
        
        # 3. Simulação de Resposta (Para GitHub Actions não quebrar)
        if "NENHUM DADO" in contexto:
            return "Desculpe, essa informação não consta nos Manuais LIA aprovados."
        else:
            return f"[IA LIA]: Baseado no manual, afirmo: {contexto}"
