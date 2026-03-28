from models.data import Data
from interface.setup import criar_meses
from engine.lua_engine import criar_luas
from interface.menu import iniciar_menu
from utils.calendario_utils import gerar_calendario
from config.calendario_config import Config
from interface.setup import criar_estacoes

def main():
    print("=== 🛠️ FORJA DO MUNDO 🛠️ ===")
    
    # Criação
    meses, dias_por_mes = criar_meses()
    total_dias = sum(dias_por_mes)

    estacoes = criar_estacoes(total_dias)
    luas = criar_luas()
    
    # Config
    config = Config(meses, dias_por_mes, estacoes, luas)
    
    # Estado inicial
    data_inicial = Data(ano=1, mes=0, dia=1)
    
    # Pré-cálculo
    calendario_completo = gerar_calendario(config)

    print("\n✨ Mundo criado com sucesso!")
    
    iniciar_menu(data_inicial, config, calendario_completo)


if __name__ == "__main__":
    main()