class BioCortex:
    def __init__(self):
        self.proibidos = ["poesia", "piada", "receita", "futebol", "ignorar"]

    def analisar_intencao(self, prompt):
        prompt_lower = prompt.lower()
        for p in self.proibidos:
            if p in prompt_lower:
                return False, f"VIOLAÇÃO DE MANUAL: Termo '{p}' proibido."
        return True, "Aprovado LIA Compliance."
