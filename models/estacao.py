class Estacao:

    def __init__(self, nome, inicio, fim):
        self.nome = nome
        self.inicio = inicio
        self.fim = fim
    
    def __str__(self):
        return f"{self.nome} (dias {self.inicio} a {self.fim})"