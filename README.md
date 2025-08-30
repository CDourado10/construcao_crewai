# 🏗️ Guia de Construção CrewAI

Um projeto didático completo demonstrando as melhores práticas para construção de **Crews**, **Flows** e **Tools** no CrewAI.

## 📋 Visão Geral

Este repositório serve como um guia prático para desenvolvedores que desejam aprender a implementar soluções robustas usando o framework CrewAI, incluindo:

- **Crews estruturadas** com agentes especializados
- **Flows assíncronos** para orquestração de processos
- **Tools personalizadas** para funcionalidades específicas
- **Integração completa** entre todos os componentes

## 🚀 Início Rápido

### 1. Configuração do Ambiente

```bash
# Clone o repositório
git clone https://github.com/CDourado10/construcao_crewai.git
cd construcao_crewai

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt
```

### 2. Configuração das APIs

```bash
# Copie o arquivo de exemplo
copy .env.example .env

# Edite o .env e adicione suas chaves de API
# Mínimo necessário: OPENAI_API_KEY
```

### 3. Execução dos Exemplos

```bash
# Executar crew exemplo
python crews/crew_exemplo/crew_exemplo_crew.py

# Executar flow exemplo
python flows/flow_exemplo_flow.py

# Executar crew de relatório
python crews/crew_relatorio/crew_relatorio_crew.py
```

## 📁 Estrutura do Projeto

```
guia_construcao/
├── crews/                      # Crews especializadas
│   ├── crew_exemplo/           # Crew de demonstração
│   │   ├── config/            # Configurações YAML
│   │   │   ├── agents.yaml    # Definição dos agentes
│   │   │   └── tasks.yaml     # Definição das tarefas
│   │   └── crew_exemplo_crew.py
│   └── crew_relatorio/         # Crew para relatórios
│       ├── config/
│       └── crew_relatorio_crew.py
├── flows/                      # Flows de orquestração
│   └── flow_exemplo_flow.py    # Flow exemplo integrado
├── tools/                      # Tools personalizadas
│   └── tool_examplo.py         # Tool de demonstração
├── knowledge/                  # Base de conhecimento
│   └── exemplo_knowledge.md    # Conhecimento exemplo
├── resultados/                 # Saídas das execuções
│   ├── crew_exemplo/
│   └── crew_relatorio/
├── .env.example               # Template de configuração
├── .gitignore                 # Arquivos ignorados
└── requirements.txt           # Dependências Python
```

## 🔧 Componentes Principais

### **Crews**
- **crew_exemplo**: Demonstra estrutura completa com 2 agentes e 2 tarefas
- **crew_relatorio**: Especializada em geração de relatórios finais

### **Flows**
- **flow_exemplo**: Orquestra execução de crews e processamento de dados
- Demonstra integração entre componentes e gerenciamento de estado

### **Tools**
- **ExemploTool**: Template para criação de ferramentas personalizadas
- Estrutura modular com métodos internos reutilizáveis

## 📚 Conceitos Demonstrados

### **Estrutura de Crews**
- Configuração via arquivos YAML
- Agentes especializados com roles, goals e backstories
- Tarefas com validação Pydantic e saídas estruturadas
- Integração com tools e fontes de conhecimento

### **Flows Assíncronos**
- Estado estruturado com Pydantic
- Decoradores `@start()` e `@listen()` para controle de fluxo
- Integração entre crews e processamento sequencial
- Tratamento de erros e fallbacks

### **Tools Personalizadas**
- Herança de `BaseTool` do CrewAI
- Schema de entrada com validação
- Métodos internos modulares
- Documentação rica para LLMs

## 🛠️ APIs Necessárias

### **Obrigatórias**
- **OpenAI API**: Para execução dos agentes (GPT-4o-mini)

### **Opcionais**
- **Serper API**: Para buscas na web
- **GitHub Token**: Para acesso a repositórios
- **Langtrace**: Para observabilidade de LLMs
- **Alpha Vantage**: Para dados financeiros
- **News API**: Para notícias

## 📖 Como Usar Este Guia

### **Para Iniciantes**
1. Comece com `crews/crew_exemplo/` para entender a estrutura básica
2. Estude `tools/tool_examplo.py` para criar ferramentas personalizadas
3. Execute `flows/flow_exemplo_flow.py` para ver a integração completa

### **Para Desenvolvedores Avançados**
- Use as crews como templates para projetos específicos
- Adapte os flows para casos de uso complexos
- Estenda as tools com funcionalidades personalizadas

## 🔍 Observabilidade

O projeto inclui integração com ferramentas de observabilidade:

- **Langtrace**: Monitoramento de chamadas LLM
- **OpenTelemetry**: Tracing distribuído
- **Logs estruturados**: Acompanhamento detalhado da execução

## 🤝 Contribuição

Este é um projeto didático. Contribuições são bem-vindas para:
- Melhorar a documentação
- Adicionar novos exemplos
- Corrigir bugs ou otimizar código

## 📄 Licença

MIT License - veja o arquivo LICENSE para detalhes.

## 🆘 Suporte

Para dúvidas ou problemas:
1. Consulte a documentação oficial do CrewAI
2. Verifique os logs de execução em `resultados/`
3. Abra uma issue no repositório
