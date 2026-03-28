from models.estacao import Estacao
from utils.input_utils import perguntar_numero
from engine.estacao_engine import tem_sobreposicao


def criar_meses():
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


def criar_estacoes(total_dias):
    estacoes = []

    quantidade = perguntar_numero("Quantas estações existem? ", minimo=1)

    for i in range(quantidade):

        while True:
            nome = input(f"Nome da estação {i+1}: ").strip()

            if not nome:
                print("Nome inválido")
                continue

            if any(e.nome == nome for e in estacoes):
                print("Essa estação já existe")
                continue

            break

        while True:
            inicio = perguntar_numero(f"Que dia inicia {nome}? ", minimo=1)
            fim = perguntar_numero(f"Que dia termina {nome}? ", minimo=1)

            if inicio > total_dias or fim > total_dias:
                print("Dias fora do limite do ano")
                continue

            if tem_sobreposicao(inicio, fim, estacoes, total_dias):
                print("Essa estação sobrepõe outra já existente")
                continue

            break

        estacoes.append(Estacao(nome, inicio, fim))

    return estacoes