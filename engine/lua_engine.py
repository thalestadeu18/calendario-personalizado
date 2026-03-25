from models.lua import Lua

def fase_da_lua(dia_absoluto, ciclo):
    posicao = dia_absoluto % ciclo

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


def criar_luas():
    luas = []

    quantidade = perguntar_numero("Quantas luas terá no calendário? ", minimo=1)

    for i in range(quantidade):

        # nome com validação
        while True:
            nome = input(f"Nome da Lua {i+1}: ")
            if nome.strip() == "":
                print("Nome inválido")
                continue
            if any(l.nome == nome for l in luas):
                print("Essa lua já existe")
                continue
            break

        ciclo = perguntar_numero(f"Quantos dias dura o ciclo de {nome}? ", minimo=1)

        lua = Lua(nome, ciclo)

        luas.append(lua)

    return luas
