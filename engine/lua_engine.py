from models.lua import Lua
from utils.input_utils import perguntar_numero

def fase_da_lua(dia_absoluto, ciclo):
    posicao = (dia_absoluto - 1) % ciclo

    if posicao == 0:
        return "Lua Nova"
    elif posicao < ciclo * 0.25:
        return "Crescente"
    elif posicao < ciclo * 0.5:
        return "Quarto Crescente"
    elif posicao < ciclo * 0.75:
        return "Cheia"
    else:
        return "Minguante"


def criar_luas():
    luas = []

    quantidade = perguntar_numero("Quantas luas terá no calendário? ", minimo=1)

    for i in range(quantidade):

        while True:
            nome = input(f"Nome da Lua {i+1}: ").strip()

            if not nome:
                print("Nome inválido")
                continue

            if any(l.nome == nome for l in luas):
                print("Essa lua já existe")
                continue

            break

        ciclo = perguntar_numero(f"Quantos dias dura o ciclo de {nome}? ", minimo=1)

        luas.append(Lua(nome, ciclo))

    return luas