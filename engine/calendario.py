from models.data import Data
from engine.estacao_engine import get_estacao
from engine.lua_engine import fase_da_lua
from utils.calendario_utils import calcular_dia_absoluto


def calcular_dia_absoluto(data, config):
    total = 0

    for i in range(data.mes):
        total += config.dias_por_mes[i]
    total += data.dia

    return total

def proximo_dia(data, config):

    novo_dia = data.dia
    novo_mes = data.mes
    novo_ano = data.ano

    if novo_mes >= len(config.dias_por_mes):
        raise ValueError("Mês inválido")

    dias_no_mes = config.dias_por_mes[novo_mes]

    if novo_dia < dias_no_mes:
        novo_dia += 1

    if novo_dia > config.dias_por_mes[novo_mes]:
        raise ValueError("Dia inválido para o mês")

    else:
        novo_dia = 1
        novo_mes += 1

        if novo_mes >= len(config.meses):
            novo_mes = 0
            novo_ano += 1

    return Data(novo_ano, novo_mes, novo_dia)

def avancar_n_dias(data, n, config):

    if n < 0:
        raise ValueError("n deve ser >= 0")

    nova_data = Data(data.ano, data.mes, data.dia)

    for _ in range(n):
        nova_data = proximo_dia(nova_data, config)

    return nova_data


def get_info_dia(data, config):

    dia_abs = calcular_dia_absoluto(data, config)

    estacao_atual = get_estacao(dia_abs, config.estacoes)

    if data.mes >= len(config.meses):
        raise ValueError("Mês inválido")

    fases_luas = []

    for lua in config.luas:
        fases_luas.append({
            "nome": lua.nome,
            "fase": fase_da_lua(dia_abs, lua.ciclo)
        })

    return {
        "ano": data.ano,
        "mes": data.mes,
        "mes_nome": config.meses[data.mes],
        "dia": data.dia,
        "dia_absoluto": dia_abs,
        "estacao": estacao_atual,
        "luas": fases_luas,
    }