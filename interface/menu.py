from engine.calendario import get_info_dia, avancar_n_dias

def exibir_opcoes():
    print("\n" + "="*35)
    print(" 📜 MENU DO CALENDÁRIO 📜 ")
    print("="*35)
    print("1. Ver dia atual")
    print("2. Avançar dias")
    print("3. Ver calendário completo")
    print("4. Sair")
    print("="*35)

def mostrar_calendario_completo(calendario):
    print("\n--- VISÃO GERAL DO ANO ---")
    for dia in calendario:
        luas_str = ', '.join(
            f"{lua['nome']} ({lua['fase']})" for lua in dia['luas']
)

def iniciar_menu(data_atual, config, calendario_completo):
    """
    Loop principal de interação com o usuário.
    Mantém o programa rodando até o usuário escolher sair.
    """
    while True:
        exibir_opcoes()
        opcao = input("Escolha o que deseja fazer: ").strip()

        if opcao == '1':
            info = get_info_dia(data_atual, config)

            print("\n" + "-"*35)
            print(f"📅 DATA: Dia {info['dia']} | Mês {info['mes_nome']} | Ano {info['ano']}")
            print(f"🍂 Estação: {info['estacao']}")
            print(f"🔢 Dia absoluto do ano: {info['dia_absoluto']}")

            print("🌕 Fases das Luas:")
            for lua in info['luas']:
                print(f"   - {lua['nome']}: {lua['fase']}")
            print("-" * 35)

        elif opcao == '2':
            try:
                qtd = perguntar_numero("\nQuantos dias deseja avançar? ", minimo=1)
                if qtd <= 0:
                    print("❌ Digite um valor maior que zero.")
                    continue
                data_atual = avancar_n_dias(data_atual, qtd, config)
            except ValueError:
                print("❌ Entrada inválida. Digite um número inteiro.")

        elif opcao == '3':
            calendario = gerar_calendario(config)
            mostrar_calendario_completo(calendario)

        elif opcao == '4':
            print("\nFechando os pergaminhos do calendário... Até a próxima! ⏳")
            break

        else:
            print("\n❌ Opção não reconhecida. Tente novamente.")