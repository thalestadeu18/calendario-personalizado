def perguntar_numero(msg, minimo=None, maximo=None):
    while True:
        entrada = input(msg)

        try:
            valor = int(entrada)
        except ValueError:
            print("❌ Valor inválido.")
            continue

        if minimo is not None and valor < minimo:
            print(f"Digite um valor ≥ {minimo}")
            continue

        if maximo is not None and valor > maximo:
            print(f"Digite um valor ≤ {maximo}")
            continue

        return valor