class Lua:
    def __init__(self, nome, ciclo):
        self.nome = nome
        self. ciclo = ciclo
    
    def __repr__(self):
        return f"Lua({self.nome}, {self.ciclo})"