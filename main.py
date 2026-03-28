from models.data import Data
from interface.setup import criar_meses, criar_estacoes
from engine.lua_engine import criar_luas
from interface.menu import iniciar_menu
from utils.calendario_utils import gerar_calendario
from config.calendario_config import Config
from utils.input_utils import perguntar_numero

def main():
    print("=== 🛠️ FORJA DO MUNDO 🛠️ ===")
    
    # Criação
    meses, dias_por_mes = criar_meses()
    total_dias = sum(dias_por_mes)

    estacoes = criar_estacoes(total_dias)
    luas = criar_luas()
    
    # Config
    config = Config(meses, dias_por_mes, estacoes, luas)
    
    # Pergunta o ano inicial e usa-o logo de seguida!
    ano_inicial = perguntar_numero("\nEm qual ano o calendário deve começar? ", minimo=1)
    
    # Estado inicial com o ano dinâmico (aqui estava o erro se a linha antiga ficou)
    data_inicial = Data(ano=ano_inicial, mes=0, dia=1)
    
    # Pré-cálculo com o ano inicial
    calendario_completo = gerar_calendario(config, ano_inicial)

    print("\n✨ Mundo criado com sucesso!")
    
    iniciar_menu(data_inicial, config, calendario_completo)

if __name__ == "__main__":
    main()