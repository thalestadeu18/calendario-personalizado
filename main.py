from interface.setup import criar_meses, criar_estacoes
from engine.lua_engine import criar_luas
from interface.menu import iniciar_menu
from utils.calendario_utils import gerar_calendario
from config.calendario_config import Config
from models.data import Data
from utils.input_utils import perguntar_numero
from engine.biblioteca import carregar_todos_saves, carregar_calendario, salvar_calendario, excluir_calendario

def menu_inicial():
    while True:
        print("\n=== 🌍 BIBLIOTECA DE MUNDOS 🌍 ===")
        saves = carregar_todos_saves()
        
        if saves:
            print("1. Forjar Novo Mundo")
            print("2. Abrir Pergaminho Existente (Carregar Mundo)")
            print("3. 🔥 Queimar Pergaminho (Excluir Mundo)")
            opcao = input("Escolha (1, 2 ou 3): ").strip()
            
            if opcao == '2':
                nomes_saves = list(saves.keys())
                print("\n--- MUNDOS GUARDADOS ---")
                for i, nome in enumerate(nomes_saves):
                    print(f"{i+1}. {nome}")
                
                escolha = perguntar_numero("Qual mundo deseja visitar? ", minimo=1, maximo=len(nomes_saves))
                nome_escolhido = nomes_saves[escolha - 1]
                data, config = carregar_calendario(nome_escolhido)
                return nome_escolhido, data, config
                
            elif opcao == '3':
                nomes_saves = list(saves.keys())
                print("\n--- QUEIMAR PERGAMINHO ---")
                for i, nome in enumerate(nomes_saves):
                    print(f"{i+1}. {nome}")
                
                escolha = perguntar_numero("Qual mundo deseja excluir permanentemente? ", minimo=1, maximo=len(nomes_saves))
                nome_escolhido = nomes_saves[escolha - 1]
                
                certeza = input(f"Tem certeza que deseja apagar '{nome_escolhido}' para sempre? (s/n): ").strip().lower()
                if certeza == 's':
                    excluir_calendario(nome_escolhido)
                    print(f"🔥 O mundo de '{nome_escolhido}' virou cinzas...")
                else:
                    print("✅ O mundo foi poupado.")
                continue # Volta para o início do menu inicial
                
            elif opcao == '1':
                return criar_novo_mundo()
            
            else:
                print("❌ Opção inválida.")
                
        else:
            # Se não houver saves, vai direto para a criação
            return criar_novo_mundo()

def criar_novo_mundo():
    print("\n=== 🛠️ FORJA DO MUNDO 🛠️ ===")
    
    while True:
        nome_save = input("Qual o nome deste novo mundo? ").strip()
        if nome_save: break
        print("❌ O nome não pode estar vazio.")
    
    meses, dias_por_mes = criar_meses()
    total_dias = sum(dias_por_mes)
    estacoes = criar_estacoes(total_dias)
    luas = criar_luas()
    
    config = Config(meses, dias_por_mes, estacoes, luas)
    ano_inicial = perguntar_numero("\nEm qual ano o calendário deve começar? ", minimo=1)
    data_inicial = Data(ano=ano_inicial, mes=0, dia=1)
    
    # Salva o mundo na biblioteca pela primeira vez
    salvar_calendario(nome_save, data_inicial, config)
    return nome_save, data_inicial, config

def main():
    # Passa pelo ecrã inicial
    nome_save, data_inicial, config = menu_inicial()
    
    # Pré-cálculo com o ano inicial para visão global
    calendario_completo = gerar_calendario(config, data_inicial.ano)

    print(f"\n✨ Bem-vindo ao mundo de '{nome_save}'!")
    
    # Inicia o menu passando o nome_save
    iniciar_menu(nome_save, data_inicial, config, calendario_completo)

if __name__ == "__main__":
    main()