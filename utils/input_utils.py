def perguntar_numero(msg, minimo=None):
    while True:
        try:
            valor = int(input(msg))

            if minimo is not None and valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}")
                continue

            return valor

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")