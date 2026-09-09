# Calendário Personalizado

Sistema interativo em **Python** para criar, salvar e simular calendários personalizados de mundos fictícios. O projeto foi desenvolvido para praticar **orientação a objetos, modularização, regras de negócio e persistência de dados em JSON**.

## Funcionalidades

- Criação de calendários com quantidade e duração de meses personalizadas
- Configuração de estações com intervalos próprios
- Suporte a estações que atravessam a virada do ano
- Cadastro de múltiplas luas com ciclos e fases calculadas automaticamente
- Persistência dos mundos criados em `saves.json`
- Carregamento e exclusão de mundos salvos
- Simulação da passagem do tempo
- Geração de relatório completo do ano

## Organização do projeto

```text
calendario-personalizado/
├── main.py
├── models/
│   ├── data.py
│   ├── estacao.py
│   └── lua.py
├── config/
│   └── calendario_config.py
├── engine/
│   ├── biblioteca.py
│   └── lua_engine.py
├── interface/
│   ├── menu.py
│   └── setup.py
└── utils/
    ├── calendario_utils.py
    └── input_utils.py
```

A separação entre `models`, `engine`, `interface`, `config` e `utils` mantém as responsabilidades do sistema organizadas e facilita a manutenção do código.

## Tecnologias

- Python 3.x
- Programação Orientada a Objetos (POO)
- JSON para persistência
- Biblioteca padrão do Python (`os` e `json`)

Não são necessárias dependências externas.

## Como executar

1. Clone o repositório.
2. Acesse a pasta do projeto:

```bash
cd calendario-personalizado
```

3. Execute o programa:

```bash
python main.py
```

Os mundos criados são armazenados localmente em `saves.json`.

## Destaques técnicos

O projeto trabalha com regras próprias para cálculo de datas, duração de meses, períodos de estações e fases lunares. A aplicação também utiliza uma estrutura modular para separar modelos de dados, processamento, interface e utilitários.

## Objetivo

Projeto pessoal desenvolvido durante a formação em Análise e Desenvolvimento de Sistemas, com foco em consolidar fundamentos de Python e organização de software.
