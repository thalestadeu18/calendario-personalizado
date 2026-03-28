from models.estacao import Estacao
from utils.input_utils import perguntar_numero


def get_estacao(dia_absoluto, config):
    total_dias = sum(config.dias_por_mes)
    dia = ((dia_absoluto - 1) % total_dias) + 1

    for estacao in config.estacoes:
        inicio = estacao.inicio
        fim = estacao.fim

        if inicio <= fim:
            if inicio <= dia <= fim:
                return estacao.nome
        else:  # atravessa o ano
            if dia >= inicio or dia <= fim:
                return estacao.nome

    raise ValueError("Nenhuma estação encontrada para o dia informado")

def quebrar_intervalo(inicio, fim, total_dias):
    if inicio <= fim:
        return [(inicio, fim)]
    else:
        return [(inicio, total_dias), (1, fim)]


def tem_sobreposicao(inicio, fim, estacoes, total_dias):
    novo_intervalos = quebrar_intervalo(inicio, fim, total_dias)

    for estacao in estacoes:
        existentes = quebrar_intervalo(estacao.inicio, estacao.fim, total_dias)

        for a_inicio, a_fim in novo_intervalos:
            for b_inicio, b_fim in existentes:
                if a_inicio <= b_fim and a_fim >= b_inicio:
                    return True

    return False