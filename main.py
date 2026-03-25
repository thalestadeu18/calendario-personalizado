from engine.calendario import gerar_calendario
from engine.calendario import criar_meses
from engine.estacao_engine import criar_estacoes
from engine.lua_engine import criar_luas


def main():

    # meses
    meses, dias_por_mes = criar_meses()

    total_dias = sum(dias_por_mes)

    # estações
    estacoes = criar_estacoes(total_dias)

    # luas
    luas = criar_luas()

    # gerar calendário
    calendario = gerar_calendario(meses, dias_por_mes, estacoes, luas)

    # exibir
    mostrar_calendario(calendario)


def mostrar_calendario(calendario):

    for dia in calendario:
        print(
            f"{dia['mes']} - Dia {dia['dia']} | "
            f"Estação: {dia['estacao']} | "
            f"Luas: {', '.join(dia['luas'])}"
        )


if __name__ == "__main__":
    main()
