def gerar_calendario(config):
    calendario = []

    for mes_index, mes_nome in enumerate(config.meses):
        for dia in range(1, config.dias_por_mes[mes_index] + 1):

            data = Data(ano=0, mes=mes_index, dia=dia)

            info = get_info_dia(data, config)

            calendario.append(info)

    return calendario