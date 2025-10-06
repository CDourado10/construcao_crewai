# 🏗️ Guia de Construção CrewAI

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.175.0-orange.svg)](https://github.com/joaomdmoura/crewAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Um guia didático completo e prático para dominar a construção de Crews, Flows e Tools no CrewAI**

Este repositório é um **recurso educacional abrangente** que demonstra as melhores práticas, padrões arquiteturais e técnicas avançadas para desenvolvimento com o framework CrewAI. Cada componente foi cuidadosamente documentado e estruturado para servir como referência tanto para iniciantes quanto para desenvolvedores experientes.

---

## 📋 Visão Geral

O projeto oferece implementações completas e production-ready de:

### 🤖 **3 Crews Especializadas**
- **crew_exemplo**: Arquitetura base com 2 agentes, 2 tasks e outputs Pydantic validados
- **crew_exemplo_2**: Pipeline complexo com análise técnica e síntese integrada
- **crew_relatorio**: Crew especializada em geração de relatórios executivos

### 🔄 **1 Flow Completo**
- Flow integrado demonstrando operadores lógicos avançados (`or_`, `and_`, `@router`)
- Orquestração de múltiplas crews com estado estruturado
- Visualização interativa do fluxo de execução

### 🛠️ **Tools Personalizadas**
- Template modular para criação de ferramentas
- Schema de validação com Pydantic
- Documentação otimizada para LLMs

### 📚 **Base de Conhecimento**
- Fonte de conhecimento integrada via Docling
- Guia completo de boas práticas para criação de arquivos knowledge

---

## 🚀 Início Rápido

### 1️⃣ Configuração do Ambiente

```bash
# Clone o repositório
git clone https://github.com/CDourado10/construcao_crewai.git
cd construcao_crewai

# Crie e ative o ambiente virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 2️⃣ Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
# Obrigatória
OPENAI_API_KEY=sk-sua-chave-aqui

# Opcionais (para features avançadas)
SERPER_API_KEY=sua-chave-serper
GITHUB_TOKEN=seu-token-github
LANGTRACE_API_KEY=sua-chave-langtrace
```

### 3️⃣ Executando os Exemplos

#### **Executar Crew Exemplo 1**
```bash
python crews/crew_exemplo/crew_exemplo_crew.py
```
Demonstra a estrutura básica com agentes, tasks e saídas validadas.

#### **Executar Crew Exemplo 2**
```bash
python crews/crew_exemplo_2/crew_exemplo_2_crew.py
```
Pipeline complexo com análise técnica e síntese integrada.

#### **Executar Crew de Relatório**
```bash
python crews/crew_relatorio/crew_relatorio_crew.py
```
Geração de relatórios executivos estruturados.

#### **Executar Flow Completo**
```bash
python flows/flow_exemplo_flow.py
```
Orquestra múltiplas crews com operadores lógicos avançados e gera visualização HTML.

---

## 📁 Estrutura do Projeto

```
guia_construcao/
│
├── 🤖 crews/                           # Crews especializadas
│   │
│   ├── crew_exemplo/                   # Crew base de demonstração
│   │   ├── config/
│   │   │   ├── agents.yaml             # Configuração dos agentes
│   │   │   └── tasks.yaml              # Configuração das tarefas
│   │   └── crew_exemplo_crew.py        # Implementação principal
│   │
│   ├── crew_exemplo_2/                 # Crew com pipeline complexo
│   │   ├── config/
│   │   │   ├── agents.yaml             # Agentes especializados
│   │   │   └── tasks.yaml              # Tasks interdependentes
│   │   └── crew_exemplo_2_crew.py
│   │
│   └── crew_relatorio/                 # Crew para relatórios
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── crew_relatorio_crew.py
│
├── 🔄 flows/                           # Flows de orquestração
│   └── flow_exemplo_flow.py            # Flow completo com 600+ linhas de documentação
│
├── 🛠️ tools/                           # Ferramentas personalizadas
│   └── tool_examplo.py                 # Template modular para tools
│
├── 📚 knowledge/                       # Base de conhecimento
│   └── exemplo_knowledge.md            # Guia de estruturação de conhecimento
│
├── 📊 resultados/                      # Outputs das execuções
│   ├── crew_exemplo/
│   │   ├── tasks/                      # Saídas de tasks individuais
│   │   └── crew/                       # Logs da crew completa
│   ├── crew_exemplo_2/
│   │   ├── tasks/
│   │   └── crew/
│   └── crew_relatorio/
│
├── 📄 requirements.txt                 # Dependências Python completas
├── 📖 README.md                        # Este arquivo
└── 🎨 FlowExemploPlot.html            # Visualização interativa do flow
```

---

## 🎯 Componentes Principais

### 🤖 **Crews**

#### **crew_exemplo** - Arquitetura Base
Demonstra a estrutura fundamental de uma crew no CrewAI:
- 2 agentes com roles, goals e backstories bem definidos
- 2 tasks sequenciais com contexto compartilhado
- Validação de outputs com modelos Pydantic
- Integração com tools personalizadas e knowledge sources
- Geração de outputs em Markdown e JSON
- Sistema de logging estruturado

**Principais features:**
- Configuração via YAML para fácil manutenção
- Outputs timestamped automaticamente
- Observabilidade com OpenLit integrado
- Estrutura modular para reutilização

#### **crew_exemplo_2** - Pipeline Complexo
Implementação avançada demonstrando workflows sofisticados:
- Agente `especialista_analise` para análise técnica profunda
- Agente `integrador_sintese` para síntese de múltiplas fontes
- Tasks interdependentes com validação rigorosa
- Modelos de saída complexos (`AnaliseComplexaOutput`, `SinteseFinalOutput`)

**Principais features:**
- Processamento de dados em pipeline
- Análise quantitativa e qualitativa integrada
- Identificação de convergências e divergências
- Recomendações técnicas acionáveis

#### **crew_relatorio** - Relatórios Executivos
Crew especializada em transformar dados em relatórios estruturados:
- Agente `analista_relatorio` otimizado para síntese
- Geração de relatórios com estrutura executiva
- Modelo `RelatorioFinal` com 5 seções obrigatórias
- Foco em insights acionáveis e tomada de decisão

**Principais features:**
- Resumo executivo conciso (2-3 parágrafos)
- Análise detalhada baseada em evidências
- Insights principais priorizados
- Recomendações práticas e implementáveis
- Conclusão consolidada

### 🔄 **Flows**

#### **flow_exemplo_flow.py** - Orquestração Completa

Um flow didático de **642 linhas** ricamente documentado que demonstra:

**Operadores de Controle de Fluxo:**
- `@start()`: Ponto de entrada do flow
- `@listen()`: Execução após conclusão de outro método
- `@router()`: Decisões condicionais com múltiplos caminhos
- `or_()`: Executa quando QUALQUER método especificado completa
- `and_()`: Executa apenas quando TODOS os métodos completam

**Estrutura do Flow:**
```
iniciar_flow
    ↓
preparar_informacoes_externas
    ↓
executar_crew_exemplo
    ↓
executar_crew_exemplo_2
    ↓
gerar_relatorio_final
    ↓
avaliar_complexidade
    ↓
decidir_tipo_processamento (@router)
    ├── complexo_aprovado → processamento_avancado
    ├── simples_aprovado → processamento_rapido
    ├── complexo_rejeitado → analise_rejeicao_complexa
    └── simples_rejeitado → analise_rejeicao_simples
        ↓
logger_processamento_aprovado (or_) / consolidar_analises_rejeicao (and_)
    ↓
finalizar_flow
```

**Estado Estruturado:**
- Modelo Pydantic `FlowExemploState` com 13 campos
- Validação automática de tipos
- Compartilhamento de estado entre etapas
- Logs detalhados de decisões do router e operadores lógicos

**Visualização:**
```python
# Gera visualização HTML interativa
flow.plot("FlowExemploPlot")
```

### 🛠️ **Tools**

#### **ExemploTool** - Template Modular

Demonstra a estrutura ideal para criação de ferramentas personalizadas:

**Componentes:**
- `ExemploToolInput`: Schema Pydantic para validação de entrada
- `name`: Identificador da tool
- `description`: Documentação rica para LLMs (incluindo exemplos)
- `args_schema`: Definição do schema de entrada
- `_metodo_interno_*`: Métodos privados modulares
- `_run()`: Método principal de execução

**Boas Práticas Demonstradas:**
- Documentação estruturada (propósito, casos de uso, exemplos)
- Separação de lógica em métodos internos reutilizáveis
- Validação automática de inputs
- Mensagens de erro claras e descritivas
- Arquitetura fachada para simplificar uso

### 📚 **Knowledge Base**

#### **exemplo_knowledge.md**

Guia completo para estruturação de arquivos de conhecimento:
- Uso de cabeçalhos hierárquicos para chunking otimizado
- Chunks curtos (1-3 parágrafos) para recuperação precisa
- Listas e tabelas para estruturação visual
- Repetição estratégica de termos-chave
- Checklist de boas práticas
- Integração com `CrewDoclingSource` do Docling

---

## 📚 Conceitos e Técnicas Demonstradas

### 🏗️ **Arquitetura de Crews**

#### **Separação de Configuração e Código**
```yaml
# config/agents.yaml
agent_1:
  role: "Pesquisador de Mercado"
  goal: "Analisar tendências emergentes"
  backstory: "Com anos de experiência..."
```

#### **Validação de Outputs com Pydantic**
```python
class SAIDATASK1(BaseModel):
    chave_1: str
    chave_2: int
    chave_3: float
    chave_4: list
    chave_5: dict
```

#### **Integração com Knowledge Sources**
```python
exemplo_knowledge = CrewDoclingSource(
    file_paths=["exemplo_knowledge.md"]
)
```

### 🔄 **Padrões de Flow**

#### **Estado Estruturado**
```python
class FlowExemploState(BaseModel):
    topico: str = Field(description="...")
    resultado_crew: dict = Field(default={})
    processamento_complexo: bool = Field(default=False)
```

#### **Operadores Lógicos Avançados**
```python
# OR: Executa quando QUALQUER método completa
@listen(or_("processamento_avancado", "processamento_rapido"))
async def logger_processamento_aprovado(self, state):
    ...

# AND: Executa quando TODOS os métodos completam
@listen(and_("analise_rejeicao_complexa", "analise_rejeicao_simples"))
async def consolidar_analises_rejeicao(self, state):
    ...
```

#### **Roteamento Condicional**
```python
@router("avaliar_complexidade")
async def decidir_tipo_processamento(self, state) -> str:
    if flow_state.processamento_complexo and flow_state.validacao_aprovada:
        return "complexo_aprovado"
    elif flow_state.processamento_complexo:
        return "complexo_rejeitado"
    # ... outros caminhos
```

### 🛠️ **Design de Tools**

#### **Schema de Entrada Tipado**
```python
class ExemploToolInput(BaseModel):
    argument_1: str = Field(
        ...,
        description="Contexto principal com exemplos..."
    )
```

#### **Métodos Internos Modulares**
```python
class ExemploTool(BaseTool):
    def _metodo_interno_1(self) -> str:
        return "resultado parcial"
    
    def _metodo_interno_3(self) -> str:
        metodo_1 = self._metodo_interno_1()
        metodo_2 = self._metodo_interno_2()
        return f"Resultado consolidado: {metodo_1} {metodo_2}"
```

---

## 🔧 Dependências e APIs

### **Stack Tecnológica**

| Categoria | Tecnologia | Versão | Propósito |
|-----------|-----------|--------|-----------|
| **Core** | CrewAI | 0.175.0 | Framework principal |
| **LLM** | OpenAI | 1.102.0 | Modelos de linguagem |
| **Validação** | Pydantic | 2.11.7 | Validação de dados |
| **Processamento** | Docling | 2.48.0 | Processamento de documentos |
| **Observabilidade** | OpenLit | 1.35.1 | Monitoramento de LLMs |
| **Visualização** | PyVis | 0.3.2 | Visualização de flows |

### **APIs Necessárias**

#### **Obrigatórias**
- **OpenAI API** (`OPENAI_API_KEY`): Execução dos agentes com GPT-4o-mini
  - [Obter chave](https://platform.openai.com/api-keys)

#### **Opcionais**
- **Serper API** (`SERPER_API_KEY`): Buscas na web
- **Langtrace** (`LANGTRACE_API_KEY`): Observabilidade avançada de LLMs
- **GitHub Token** (`GITHUB_TOKEN`): Acesso a repositórios privados

---

## 📖 Guia de Uso

### 🎓 **Para Iniciantes**

#### **Caminho de Aprendizado Recomendado:**

1. **Comece com Tools** (`tools/tool_examplo.py`)
   - Entenda a estrutura básica de uma ferramenta
   - Veja como validar inputs e estruturar outputs
   - Aprenda sobre métodos internos modulares

2. **Estude Crews Básicas** (`crews/crew_exemplo/`)
   - Analise a configuração YAML de agentes e tasks
   - Entenda como integrar tools e knowledge sources
   - Veja validação de outputs com Pydantic
   - Execute e observe os resultados em `resultados/`

3. **Explore Knowledge Base** (`knowledge/exemplo_knowledge.md`)
   - Aprenda a estruturar conhecimento para LLMs
   - Entenda chunking hierárquico e recuperação semântica
   - Veja boas práticas de documentação

4. **Avance para Flows** (`flows/flow_exemplo_flow.py`)
   - Leia os comentários detalhados (guia didático)
   - Execute e visualize com `flow.plot()`
   - Entenda operadores lógicos (`or_`, `and_`, `@router`)

### 🚀 **Para Desenvolvedores Experientes**

#### **Adaptação para Produção:**

1. **Use as Crews como Templates**
   ```python
   # Adapte os agentes para seu domínio
   @agent
   def seu_agente_customizado(self) -> Agent:
       return Agent(
           config=self.agents_config['seu_agente'],
           tools=[SuaToolPersonalizada()],
           llm="gpt-4o",  # Use modelo mais poderoso em prod
           knowledge_sources=[sua_knowledge_base]
       )
   ```

2. **Estenda os Flows para Casos Complexos**
   ```python
   # Adicione processamento paralelo
   @listen(or_("task_a", "task_b", "task_c"))
   async def processar_paralelo(self, state):
       # Lógica para processar múltiplas fontes
       ...
   ```

3. **Crie Tools Especializadas**
   ```python
   # Integre com APIs externas
   class APIClientTool(BaseTool):
       def _run(self, query: str) -> str:
           response = requests.post(API_URL, json={"query": query})
           return self._processar_resposta(response)
   ```

---

## 🔍 Observabilidade e Monitoramento

### **OpenLit Integration**

Todas as crews incluem monitoramento automático de:
- Chamadas LLM com latência e tokens
- Performance de agentes e tasks
- Erros e exceções em tempo real

```python
import openlit
openlit.init(disable_metrics=True)
```

### **Logs Estruturados**

Cada execução gera:
- **Task outputs**: `resultados/[crew]/tasks/[task]_[timestamp].md`
- **Crew logs**: `resultados/[crew]/crew/crew_[timestamp].json`
- **Console logs**: Acompanhamento em tempo real com emojis

### **Visualização de Flows**

```bash
# Gere visualização HTML interativa
python -c "from flows.flow_exemplo_flow import plot; plot()"
```

Abre `FlowExemploPlot.html` mostrando:
- Nós representando cada etapa do flow
- Setas indicando fluxo de execução
- Conexões dos operadores lógicos
- Estrutura visual dos routers

---

## 🎨 Outputs e Resultados

### **Formato dos Outputs**

Cada task gera dois outputs:

1. **Markdown** (`.md`): Formato legível para humanos
2. **JSON** (através do log): Dados estruturados para processamento

### **Estrutura dos Resultados**

```
resultados/
├── crew_exemplo/
│   ├── tasks/
│   │   ├── task_1_20251005_2045.md
│   │   └── task_2_20251005_2045.md
│   └── crew/
│       └── crew_20251005_2045.json
├── crew_exemplo_2/
│   ├── tasks/
│   │   ├── analise_complexa_20251005_2046.md
│   │   └── sintese_integrada_20251005_2046.md
│   └── crew/
│       └── crew_exemplo_2_20251005_2046.json
└── crew_relatorio/
    └── relatorio_final_20251005_2047.md
```

---

## 🧪 Testando o Projeto

### **Teste Rápido - Crew Básica**
```bash
python crews/crew_exemplo/crew_exemplo_crew.py
```
✅ Verifica: configuração básica, integração com OpenAI, geração de outputs

### **Teste Intermediário - Pipeline Complexo**
```bash
python crews/crew_exemplo_2/crew_exemplo_2_crew.py
```
✅ Verifica: tasks interdependentes, validação Pydantic, análise técnica

### **Teste Avançado - Flow Completo**
```bash
python flows/flow_exemplo_flow.py
```
✅ Verifica: orquestração de crews, operadores lógicos, roteamento condicional, visualização

---

## 🤝 Contribuindo

Este é um projeto educacional aberto a contribuições! Formas de contribuir:

### **Documentação**
- Melhorar exemplos e explicações
- Traduzir documentação
- Adicionar diagramas e visualizações

### **Exemplos**
- Criar novas crews especializadas
- Adicionar flows para casos de uso específicos
- Desenvolver tools para integrações populares

### **Código**
- Otimizar performance
- Adicionar testes automatizados
- Melhorar tratamento de erros

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🆘 Suporte e Recursos

### **Documentação Oficial**
- [CrewAI Documentation](https://docs.crewai.com)
- [Pydantic Documentation](https://docs.pydantic.dev)
- [OpenAI API Reference](https://platform.openai.com/docs)

### **Comunidade**
- [CrewAI GitHub](https://github.com/joaomdmoura/crewAI)
- [CrewAI Discord](https://discord.gg/crewai)

### **Suporte deste Projeto**
- 📖 Consulte os logs em `resultados/` para debugging
- 🐛 Abra uma [issue](https://github.com/CDourado10/construcao_crewai/issues) para reportar bugs
- 💬 Inicie uma [discussão](https://github.com/CDourado10/construcao_crewai/discussions) para perguntas

---

## 🌟 Agradecimentos

Este projeto foi desenvolvido como recurso educacional para a comunidade CrewAI.

**Principais influências:**
- Framework CrewAI por João Moura
- Padrões de documentação da comunidade Python
- Boas práticas de engenharia de prompt da OpenAI

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!**

[Reportar Bug](https://github.com/CDourado10/construcao_crewai/issues) · [Solicitar Feature](https://github.com/CDourado10/construcao_crewai/issues) · [Documentação](https://github.com/CDourado10/construcao_crewai)

</div>
