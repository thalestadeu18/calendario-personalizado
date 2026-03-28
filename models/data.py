class Data:
    def __init__(self, ano, mes, dia):
        self.ano = ano
        self.mes = mes
        self.dia = dia

    def __str__(self):
        return f"Data({self.dia}, {self.mes}, {self.ano})"
