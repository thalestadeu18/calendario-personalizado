import json
import os
from models.data import Data
from models.estacao import Estacao
from models.lua import Lua
from config.calendario_config import Config

ARQUIVO_SAVES = "saves.json" # Os pergaminhos guardados

def salvar_calendario(nome_save, data, config):
    saves = carregar_todos_saves()
    
    # Converte os objetos complexos para dicionários simples
    saves[nome_save] = {
        "data_atual": {
            "ano": data.ano,
            "mes": data.mes,
            "dia": data.dia
        },
        "config": {
            "meses": config.meses,
            "dias_por_mes": config.dias_por_mes,
            "estacoes": [{"nome": e.nome, "inicio": e.inicio, "fim": e.fim} for e in config.estacoes],
            "luas": [{"nome": l.nome, "ciclo": l.ciclo} for l in config.luas]
        }
    }
    
    # Escreve no ficheiro JSON
    with open(ARQUIVO_SAVES, "w", encoding="utf-8") as f:
        json.dump(saves, f, indent=4, ensure_ascii=False)

def carregar_todos_saves():
    if not os.path.exists(ARQUIVO_SAVES):
        return {}
    try:
        with open(ARQUIVO_SAVES, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def carregar_calendario(nome_save):
    saves = carregar_todos_saves()
    if nome_save not in saves:
        return None, None
        
    dados = saves[nome_save]
    
    # Reconstrói o objeto Data
    data_dict = dados["data_atual"]
    data = Data(data_dict["ano"], data_dict["mes"], data_dict["dia"])
    
    # Reconstrói o Config, as Estações e as Luas
    cfg = dados["config"]
    estacoes = [Estacao(e["nome"], e["inicio"], e["fim"]) for e in cfg["estacoes"]]
    luas = [Lua(l["nome"], l["ciclo"]) for l in cfg["luas"]]
    
    config = Config(cfg["meses"], cfg["dias_por_mes"], estacoes, luas)
    
    return data, config

def excluir_calendario(nome_save):
    saves = carregar_todos_saves()
    if nome_save in saves:
        del saves[nome_save] # Remove o mundo do dicionário
        # Escreve o ficheiro novamente, agora sem o mundo apagado
        with open(ARQUIVO_SAVES, "w", encoding="utf-8") as f:
            json.dump(saves, f, indent=4, ensure_ascii=False)
        return True
    return False