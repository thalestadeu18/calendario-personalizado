class Lua:
    def __init__(self, nome, ciclo):
        self.nome = nome
        self.ciclo = ciclo
    
    def __str__(self):
        return f"{self.nome} (ciclo de {self.ciclo} dias)"