#!/usr/bin/env python
"""
Segunda crew de exemplo para demonstrar complexidade e integração múltipla.

Esta crew demonstra como implementar workflows mais complexos com:
- Múltiplos agentes especializados em diferentes domínios
- Tarefas interdependentes com validação rigorosa
- Integração com ferramentas avançadas
- Processamento de dados em pipeline
"""

from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource
from pydantic import BaseModel
import openlit
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
openlit.init(disable_metrics=True)

# Fonte de conhecimento adicional utilizada pelos agentes
exemplo_knowledge = CrewDoclingSource(
    file_paths=[
        "exemplo_knowledge.md"
    ]
)


# -----------------------------
# MODELOS DE SAÍDA DAS TASKS
# -----------------------------

class AnaliseComplexaOutput(BaseModel):
    """Modelo de saída para análise complexa de dados."""
    categoria_principal: str
    nivel_complexidade: int
    fatores_criticos: list
    metricas_relevantes: dict
    recomendacoes_tecnicas: list


class SinteseFinalOutput(BaseModel):
    """Modelo de saída para síntese final integrada."""
    resumo_integrado: str
    pontos_convergencia: list
    areas_divergencia: list
    conclusoes_consolidadas: dict
    proximos_passos: list


# -----------------------------
# DEFINIÇÃO DA CREW
# -----------------------------

@CrewBase
class CrewExemplo2:
    """
    Segunda crew de exemplo demonstrando workflows complexos.

    Esta crew implementa um pipeline mais sofisticado com:
    - Agente especialista em análise técnica complexa
    - Agente integrador para síntese de múltiplas fontes
    - Processamento sequencial com dependências entre tasks
    - Validação rigorosa de saídas estruturadas
    """

    # Caminhos para as configurações dos agentes e tasks
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # -----------------------------
    # AGENTES
    # -----------------------------

    @agent
    def especialista_analise(self) -> Agent:
        """Agente especializado em análise técnica complexa de dados."""
        return Agent(
            config=self.agents_config['especialista_analise'],
            verbose=True,
            tools=[ExemploTool()],
            llm="gpt-4o-mini",
            knowledge_sources=[exemplo_knowledge]
        )

    @agent
    def integrador_sintese(self) -> Agent:
        """Agente responsável por integrar e sintetizar múltiplas análises."""
        return Agent(
            config=self.agents_config['integrador_sintese'],
            verbose=True,
            tools=[ExemploTool()],
            llm="gpt-4o-mini",
            knowledge_sources=[exemplo_knowledge]
        )

    # -----------------------------
    # TASKS
    # -----------------------------

    @task
    def analise_complexa(self) -> Task:
        """
        Primeira tarefa: análise técnica complexa dos dados de entrada.

        Esta task recebe informações externas e realiza uma análise
        aprofundada, identificando padrões, métricas e fatores críticos.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        output_filename = f'resultados/crew_exemplo_2/tasks/analise_complexa_{timestamp}.md'
        
        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        
        return Task(
            config=self.tasks_config['analise_complexa'],
            agent=self.especialista_analise(),
            output_pydantic=AnaliseComplexaOutput,
            markdown=True,
            output_file=output_filename
        )

    @task
    def sintese_integrada(self) -> Task:
        """
        Segunda tarefa: síntese integrada baseada na análise complexa.

        Esta task recebe o contexto da análise complexa e integra
        com informações externas para gerar uma síntese consolidada.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        output_filename = f'resultados/crew_exemplo_2/tasks/sintese_integrada_{timestamp}.md'
        
        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        
        return Task(
            config=self.tasks_config['sintese_integrada'],
            agent=self.integrador_sintese(),
            context=[self.analise_complexa()],
            output_pydantic=SinteseFinalOutput,
            markdown=True,
            output_file=output_filename
        )

    # -----------------------------
    # CREW (EXECUÇÃO)
    # -----------------------------

    @crew
    def crew(self) -> Crew:
        """
        Define a crew exemplo 2 com pipeline complexo.

        - Executa análise técnica seguida de síntese integrada
        - Processo sequencial com dependências entre tasks
        - Logging detalhado para acompanhamento do pipeline
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        output_filename = f'resultados/crew_exemplo_2/crew/crew_exemplo_2_{timestamp}.json'
        
        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        
        return Crew(
            name="Crew Exemplo 2",
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

def metodo_de_execucao_da_crew_2(dados_complexos: str = "", contexto_adicional: str = "", parametros_tecnicos: str = "") -> dict:
    """
    Executa a CrewExemplo2 com dados complexos e contexto técnico.

    Args:
        dados_complexos (str): Dados técnicos para análise aprofundada.
        contexto_adicional (str): Contexto adicional para enriquecer a análise.
        parametros_tecnicos (str): Parâmetros técnicos específicos.

    Retorna:
        dict: Resultado final da execução da crew com análise e síntese.
    """
    crew = CrewExemplo2()
    inputs = {
        "dados_complexos": dados_complexos,
        "contexto_adicional": contexto_adicional,
        "parametros_tecnicos": parametros_tecnicos
    }
    resultado = crew.crew().kickoff(inputs=inputs)
    return resultado


# -----------------------------
# ENTRYPOINT
# -----------------------------

if __name__ == "__main__":
    # Exemplo de execução manual da crew com dados complexos
    dados_complexos = "Dados técnicos complexos para análise aprofundada"
    contexto_adicional = "Contexto adicional relevante para a análise"
    parametros_tecnicos = "Parâmetros técnicos específicos do domínio"

    resultado = metodo_de_execucao_da_crew_2(
        dados_complexos=dados_complexos,
        contexto_adicional=contexto_adicional,
        parametros_tecnicos=parametros_tecnicos
    )

    print("Resultado da Crew Exemplo 2:")
    print(resultado)
