# 🌍 Calendário Personalizado (Biblioteca de Mundos)

Este é um sistema interativo em Python projetado para **forjar, gerenciar e simular calendários customizados** de mundos fictícios ou personalizados. Perfeito para escritores, mestres de RPG ou entusiastas de construção de mundos (*worldbuilding*), o programa permite definir dinamicamente a estrutura de tempo de um universo próprio (meses, estações e até múltiplas luas) e acompanhar a passagem dos dias.

## ✨ Funcionalidades

- **Forja de Mundos:** Crie um calendário do zero definindo:
  - Quantidade de meses e a quantidade exata de dias de cada um.
  - Estações do ano com intervalos customizados de dias (permitindo inclusive estações que atravessam a virada do ano).
  - Múltiplas luas, cada uma com seu próprio ciclo e cálculo automático de fases (Nova, Crescente, Quarto Crescente, Cheia e Minguante).
- **Biblioteca de Mundos (Persistência):** Os mundos criados são salvos automaticamente em um arquivo `saves.json`. Você pode criar novos mundos, carregar mundos existentes para continuar a simulação ou deletá-los permanentemente.
- **Simulador de Passagem do Tempo:** Avance o tempo em quantos dias desejar e veja o impacto imediato na data atual, na estação vigente e nas fases de cada lua.
- **Visão Completa do Ano:** Gera um relatório completo mostrando as características de cada dia do ano forjado.

## 🛠️ Estrutura do Projeto

O projeto segue uma arquitetura modular e organizada:
- `main.py`: Ponto de entrada do programa que gerencia o menu da biblioteca (carregar/criar mundos).
- `models/`: Contém as classes que definem as entidades do sistema (`Data`, `Estacao`, `Lua`).
- `config/`: Guarda as configurações de estrutura do calendário (`Config`).
- `engine/`: Contém a lógica principal de processamento de datas, avanço de tempo, cálculo de sobreposição de estações e engine lunar.
- `interface/`: Controla os menus interativos via terminal de configuração (`setup.py`) e de simulação diária (`menu.py`).
- `utils/`: Funções utilitárias para validação de entradas numéricas e geração de relatórios.

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Ter o **Python 3.x** instalado na sua máquina. Não são necessárias bibliotecas externas adicionais (usa apenas os módulos padrão `os` e `json`).

### Passo a Passo

1. **Clone ou baixe o repositório** para a sua máquina local.
2. **Abra o terminal** ou prompt de comando e navegue até a pasta raiz do projeto:
   ```bash
   cd caminho/para/o/projeto/calendario-personalizado
