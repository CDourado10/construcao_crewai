#!/usr/bin/env python
"""
Script principal de execução da CrewExemplo.

Este módulo define a estrutura completa de uma crew no CrewAI, incluindo:
- Configuração de agentes e tarefas a partir de arquivos YAML.
- Integração com ferramentas externas (tools).
- Uso de fontes de conhecimento personalizadas.
- Geração de saídas em múltiplos formatos (Markdown, JSON).
- Observabilidade com Langtrace e Openlit.

A função `metodo_de_execucao_da_crew` é o ponto de entrada para executar a crew,
permitindo a injeção de informações externas que serão usadas nas tasks.
"""

from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task, tool
from dotenv import load_dotenv
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource
from pydantic import BaseModel

import sys
import os
import datetime

# Adiciona o diretório raiz do projeto ao sys.path para facilitar imports relativos
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)


# Importa tools personalizadas que serão utilizadas pelos agentes ou tasks
from tools.tool_examplo import ExemploTool

# Carrega variáveis de ambiente do arquivo .env (chaves de API, configs sensíveis, etc.)
load_dotenv()

# Configuração de observabilidade (monitoramento da execução da crew)
import openlit

openlit.init(disable_metrics=True)

# Fonte de conhecimento adicional utilizada pelos agentes
# Aqui, é um arquivo markdown com informações relevantes para enriquecer o contexto
exemplo_knowledge = CrewDoclingSource(
    file_paths=[
        "exemplo_knowledge.md"
    ]
)


# -----------------------------
# MODELOS DE SAÍDA DAS TASKS
# -----------------------------

class SAIDATASK1(BaseModel):
    """Modelo de saída esperado para a Task 1."""
    chave_1: str
    chave_2: int
    chave_3: float
    chave_4: list
    chave_5: dict


class SAIDATASK2(BaseModel):
    """Modelo de saída esperado para a Task 2."""
    chave_1: str
    chave_2: int
    chave_3: float
    chave_4: list
    chave_5: dict


# -----------------------------
# DEFINIÇÃO DA CREW
# -----------------------------

@CrewBase
class CrewExemplo:
    """
    Exemplo de implementação de uma Crew no CrewAI.

    Esta classe utiliza o decorator `@CrewBase`, que transforma
    a classe em uma crew configurável com:
    - Agentes carregados a partir de `config/agents.yaml`.
    - Tarefas carregadas a partir de `config/tasks.yaml`.
    - Suporte a ferramentas personalizadas e fontes de conhecimento.
    """

    # Caminhos para as configurações dos agentes e tasks
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # -----------------------------
    # AGENTES
    # -----------------------------

    @agent
    def agent_1(self) -> Agent:
        """Define o primeiro agente da crew, com tool e conhecimento associado."""
        return Agent(
            config=self.agents_config['agent_1'],
            verbose=True,
            tools=[ExemploTool()],
            llm="gpt-4o-mini",
            knowledge_sources=[exemplo_knowledge]
        )

    @agent
    def agent_2(self) -> Agent:
        """Define o segundo agente da crew, com tool e conhecimento associado."""
        return Agent(
            config=self.agents_config['agent_2'],
            verbose=True,
            tools=[ExemploTool()],
            llm="gpt-4o-mini",
            knowledge_sources=[exemplo_knowledge]
        )

    # -----------------------------
    # TASKS
    # -----------------------------

    @task
    def task_1(self) -> Task:
        """
        Define a primeira tarefa da crew.

        Saída será validada contra o modelo SAIDATASK1
        e salva em formato Markdown com timestamp único.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        output_filename = f'resultados/crew_exemplo/tasks/task_1_{timestamp}.md'
        
        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        
        return Task(
            config=self.tasks_config['task_1'],
            agent=self.agent_1(),
            output_pydantic=SAIDATASK1,
            markdown=True,
            output_file=output_filename
        )

    @task
    def task_2(self) -> Task:
        """
        Define a segunda tarefa da crew.

        - Usa o `agent_2`.
        - Recebe o contexto da execução da `task_1`.
        - Saída validada contra o modelo SAIDATASK2.
        - Resultado salvo em Markdown.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        output_filename = f'resultados/crew_exemplo/tasks/task_2_{timestamp}.md'
        
        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        
        return Task(
            config=self.tasks_config['task_2'],
            agent=self.agent_2(),
            context=[self.task_1()],
            output_pydantic=SAIDATASK2,
            markdown=True,
            output_file=output_filename
        )

    # -----------------------------
    # CREW (EXECUÇÃO)
    # -----------------------------

    @crew
    def crew(self) -> Crew:
        """
        Define a crew completa.

        - Contém os agentes e tasks registrados.
        - Executa em processo sequencial.
        - Gera log detalhado em arquivo JSON.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        output_filename = f'resultados/crew_exemplo/crew/crew_{timestamp}.json'
        
        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        
        return Crew(
            name="Crew Exemplo",
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            planning=True,
            output_log_file=output_filename
        )


# -----------------------------
# MÉTODO DE EXECUÇÃO DA CREW
# -----------------------------

def metodo_de_execucao_da_crew(info_externa_1: str = "", info_externa_2: str = "", info_externa_3: str = "") -> dict:
    """
    Executa a CrewExemplo com informações externas fornecidas como input.

    Args:
        info_externa_1 (str): Primeira informação externa contextual.
        info_externa_2 (str): Segunda informação externa contextual.
        info_externa_3 (str): Terceira informação externa contextual.

    Retorna:
        dict: Resultado final da execução da crew.
    """
    crew = CrewExemplo()
    inputs = {
        "info_externa_1": info_externa_1,
        "info_externa_2": info_externa_2,
        "info_externa_3": info_externa_3
    }
    resultado = crew.crew().kickoff(inputs=inputs)
    return resultado


# -----------------------------
# ENTRYPOINT
# -----------------------------

if __name__ == "__main__":
    # Exemplo de execução manual da crew com informações externas
    info_externa_1 = "Primeiras informações externas"
    info_externa_2 = "Segundas informações externas"
    info_externa_3 = "Terceiras informações externas"

    resultado = metodo_de_execucao_da_crew(
        info_externa_1=info_externa_1,
        info_externa_2=info_externa_2,
        info_externa_3=info_externa_3
    )
