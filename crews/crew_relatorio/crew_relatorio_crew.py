#!/usr/bin/env python
"""
Crew especializada em geração de relatórios finais.

Esta crew contém um único agente especializado em análise e síntese de informações,
responsável por transformar dados processados em relatórios estruturados e acionáveis.
"""

from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource
from dotenv import load_dotenv
from pydantic import BaseModel
from langtrace_python_sdk import langtrace
import openlit
import sys
import os
import datetime

# Adiciona o diretório raiz do projeto ao sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)

from tools.tool_examplo import ExemploTool

# Carrega variáveis de ambiente
load_dotenv()

# Configuração de observabilidade (monitoramento da execução da crew)
langtrace.init(api_key=os.getenv("LANGTRACE_API_KEY"))
openlit.init(disable_metrics=True)

# Fonte de conhecimento adicional utilizada pelos agentes
exemplo_knowledge = CrewDoclingSource(
    file_paths=[
        "exemplo_knowledge.md"
    ]
)


# Modelo de saída para o relatório
class RelatorioFinal(BaseModel):
    """Modelo de saída para o relatório final."""
    resumo_executivo: str
    analise_detalhada: str
    insights_principais: list
    recomendacoes: list
    conclusao: str


@CrewBase
class CrewRelatorio:
    """
    Crew especializada em geração de relatórios finais.
    
    Contém um único agente analista que recebe dados processados
    e gera relatórios estruturados e acionáveis.
    """

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def analista_relatorio(self) -> Agent:
        """Agente especializado em análise e geração de relatórios."""
        return Agent(
            config=self.agents_config['analista_relatorio'],
            verbose=True,
            tools=[ExemploTool()],
            llm="gpt-4o-mini",
            knowledge_sources=[exemplo_knowledge]
        )

    @task
    def gerar_relatorio(self) -> Task:
        """Tarefa de geração do relatório final."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        output_filename = f'resultados/crew_relatorio/relatorio_final_{timestamp}.md'
        
        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        
        return Task(
            config=self.tasks_config['gerar_relatorio'],
            agent=self.analista_relatorio(),
            output_pydantic=RelatorioFinal,
            markdown=True,
            output_file=output_filename
        )

    @crew
    def crew(self) -> Crew:
        """Define a crew de relatório."""
        return Crew(
            name="Crew Relatório",
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )


def executar_crew_relatorio(dados_entrada: str = "", topico: str = "") -> dict:
    """
    Executa a crew de relatório com os dados fornecidos.
    
    Args:
        dados_entrada: Dados processados para análise
        topico: Tópico principal do relatório
        
    Returns:
        Resultado da execução da crew
    """
    crew = CrewRelatorio()
    inputs = {
        "dados_entrada": dados_entrada,
        "topico": topico
    }
    resultado = crew.crew().kickoff(inputs=inputs)
    return resultado


if __name__ == "__main__":
    # Teste da crew
    resultado = executar_crew_relatorio(
        dados_entrada="Dados de exemplo para teste",
        topico="Teste da Crew Relatório"
    )
    print(resultado)
