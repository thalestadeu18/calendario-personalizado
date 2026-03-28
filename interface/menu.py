from engine.calendario import get_info_dia, avancar_n_dias
from engine.biblioteca import salvar_calendario
from utils.input_utils import perguntar_numero

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
        luas_str = ', '.join([f"{l['nome']} ({l['fase']})" for l in dia['luas']])
        print(f"Mês {dia['data'].mes} - Dia {dia['data'].dia} | Estação: {dia['estacao']} | Luas: {luas_str}")
    print("--------------------------")

def iniciar_menu(nome_save, data_atual, config, calendario_completo):
    """
    Loop principal de interação com o utilizador.
    Mantém o programa a rodar até o utilizador escolher sair.
    """
    while True:
        exibir_opcoes()
        opcao = input("Escolha o que deseja fazer: ").strip()

        if opcao == '1':
            # Usa o "coração" da Fase 3 para montar o relatório do dia
            info = get_info_dia(data_atual, config)
            print("\n" + "-"*35)
            print(f"📅 DATA: Dia {info['data'].dia} | Mês {info['data'].mes} | Ano {info['data'].ano}")
            print(f"🍂 Estação: {info['estacao']}")
            print(f"🔢 Dia absoluto do ano: {info['dia_absoluto']}")
            
            print("🌕 Fases das Luas:")
            for lua in info['luas']:
                print(f"   - {lua['nome']}: {lua['fase']}")
            print("-" * 35)

        elif opcao == '2':
            qtd = perguntar_numero("\nQuantos dias deseja avançar no tempo? ", minimo=1)
            data_atual = avancar_n_dias(data_atual, qtd, config)
            
            # A magia da biblioteca: guarda sempre que o tempo avança!
            salvar_calendario(nome_save, data_atual, config)
            
            print(f"✅ Tempo avançado em {qtd} dias! (Progresso escrito na biblioteca)")

        elif opcao == '3':
            mostrar_calendario_completo(calendario_completo)

        elif opcao == '4':
            print("\nFechando os pergaminhos do calendário... Até a próxima! ⏳")
            break

        else:
            print("\n❌ Opção não reconhecida. Tente novamente.")