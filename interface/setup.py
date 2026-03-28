def criar_meses(perguntar_numero):
    meses = []
    dias_por_mes = []

    quantidade = perguntar_numero("Quantos meses terá o ano? ", minimo=1)

    for i in range(quantidade):

        while True:
            nome = input(f"Nome do mês {i+1}: ").strip()

            if not nome:
                print("Nome inválido")
                continue

            if nome in meses:
                print("Esse mês já existe")
                continue

            break

        dias = perguntar_numero(f"Quantos dias tem {nome}? ", minimo=1)

        meses.append(nome)
        dias_por_mes.append(dias)

    return meses, dias_por_mes