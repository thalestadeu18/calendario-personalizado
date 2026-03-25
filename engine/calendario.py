def calcular_dia_absoluto(dia, mes, dias_por_mes):
    total = 0

    for i in range(mes):
        total += dias_por_mes[i]
    total += dia
    return total


def perguntar_numero(msg, minimo=None):
    while True:
        try:
            valor = int(input(msg))

            if minimo is not None and valor < minimo:
                print(f"Digite um valor >= {minimo}")
                continue

            return valor

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def criar_meses():
    meses = []
    dias_por_mes = []

    quantidade = perguntar_numero("Quantos meses terá o ano? ", minimo=1)

    for i in range(quantidade):

        # validar nome
        while True:
            nome = input(f"Nome do mês {i+1}: ")

            if nome.strip() == "":
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
