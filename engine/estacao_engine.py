from models.estacao import Estacao

def get_estacao(dia_absoluto, estacoes):
    for estacao in estacoes:

        if estacao.inicio <= estacao.fim:
            if estacao.inicio <= dia_absoluto <= estacao.fim:
                return estacao.nome

        else:  # atravessa o ano
            if dia_absoluto >= estacao.inicio or dia_absoluto <= estacao.fim:
                return estacao.nome

    return None


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


def criar_estacoes(total_dias):
    estacoes = []

    quantidade = perguntar_numero("Quantas estações existem? ", minimo=1)

    for i in range(quantidade):

        # validar nome
        while True:
            nome = input(f"Nome da estação {i+1}: ")

            if nome.strip() == "":
                print("Nome inválido")
                continue

            if any(e.nome == nome for e in estacoes):
                print("Essa estação já existe")
                continue

            break

        # validar inicio e fim corretamente
        while True:
            inicio = perguntar_numero(...)
            fim = perguntar_numero(...)

            if inicio > total_dias or fim > total_dias:
                print("Dias fora do limite do ano")
                continue

            if tem_sobreposicao(inicio, fim, estacoes, total_dias):
                print("Essa estação sobrepõe outra já existente")
                continue

            break

        estacao = Estacao(nome, inicio, fim)
        estacoes.append(estacao)

    return estacoes


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
