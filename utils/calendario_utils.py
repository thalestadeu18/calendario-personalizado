from models.data import Data
from engine.calendario import get_info_dia, avancar_n_dias

def gerar_calendario(config, ano_inicial):
    calendario = []

    # Aqui também usamos a variável ano_inicial que veio do main
    data = Data(ano=ano_inicial, mes=0, dia=1)
    total_dias = sum(config.dias_por_mes)

    for _ in range(total_dias):
        info = get_info_dia(data, config)
        calendario.append(info)

        data = avancar_n_dias(data, 1, config)

    return calendario