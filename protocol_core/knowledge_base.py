import json

class KnowledgeBase:
    def __init__(self):
        # Simulação de Vetores (Banco de Dados em Memória)
        # Em produção, isso leria o chroma.db
        self.db = {
            "juros": "Manual Financeiro Cap. 3: Juros compostos devem seguir a tabela SAC...",
            "compliance": "Manual Jurídico Seção 5: O oficial de compliance deve reportar ao board...",
            "lei": "Constituição Federal Art. 5: Todos são iguais perante a lei...",
            "bifi": "Metodologia LIA: O Letramento em IA exige 3 níveis de cognição..."
        }

    def buscar_contexto(self, query):
        """Busca semântica simulada (Keyword Search para MVP)"""
        print(f"📚 [RAG] Buscando conhecimento sobre: '{query}'...")
        query_lower = query.lower()
        
        resultados = []
        for chave, conteudo in self.db.items():
            if chave in query_lower:
                resultados.append(conteudo)
        
        if resultados:
            return "\n".join(resultados)
        else:
            return "NENHUM DADO ENCONTRADO NO MANUAL LIA."
