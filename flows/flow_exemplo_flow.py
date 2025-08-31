#!/usr/bin/env python
"""
GUIA DE CONSTRUÇÃO DE FLOWS NO CREWAI

Este arquivo serve como um guia didático para a construção de flows no CrewAI,
demonstrando as melhores práticas e padrões de implementação.

Um flow no CrewAI representa um fluxo de trabalho assíncrono que:
1. Define um estado estruturado para compartilhar informações entre etapas
2. Organiza a execução em etapas sequenciais ou paralelas
3. Integra diferentes componentes (crews, agentes, tarefas, ferramentas)
4. Processa informações de forma modular e escalável

Este exemplo demonstra a integração completa entre todos os componentes do projeto.
"""

# [BLOCO 1] - IMPORTS E CONFIGURAÇÃO INICIAL
# ------------------------------------------------------
# Sempre organize seus imports em blocos lógicos:
# 1. Bibliotecas padrão do Python
# 2. Bibliotecas de terceiros
# 3. Módulos locais do projeto

# Bibliotecas padrão do Python
import os
import sys
import random
from typing import Dict, Any

# Bibliotecas de terceiros
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from crewai.flow.flow import Flow, listen, start, or_, and_, router

# Configuração de caminhos para imports relativos
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Imports locais do projeto
from crews.crew_exemplo.crew_exemplo_crew import metodo_de_execucao_da_crew
from crews.crew_exemplo_2.crew_exemplo_2_crew import metodo_de_execucao_da_crew_2
from crews.crew_relatorio.crew_relatorio_crew import executar_crew_relatorio

# Carrega variáveis de ambiente
load_dotenv()

# [BLOCO 2] - MODELAGEM DO ESTADO DO FLOW
# ------------------------------------------------------
# O estado do flow é fundamental para compartilhar informações entre etapas.
# Use Pydantic para criar um modelo estruturado com validação automática.

class FlowExemploState(BaseModel):
    """Estado estruturado para o Flow de Exemplo.
    
    Um bom modelo de estado deve:
    1. Documentar claramente cada campo
    2. Definir valores padrão quando apropriado
    3. Usar tipos específicos para garantir validação
    4. Incluir todos os dados que precisam ser compartilhados entre etapas
    """
    # Dados de entrada do flow
    topico: str = Field(description="Tópico principal para pesquisa e análise")
    info_externa_1: str = Field(description="Informação externa adicional para contexto")
    info_externa_2: str = Field(default="", description="Segunda informação externa para contexto")
    info_externa_3: str = Field(default="", description="Terceira informação externa para contexto")
    
    # Resultados das crews
    resultado_crew_exemplo: dict = Field(default={}, description="Resultado da execução da crew exemplo")
    resultado_crew_exemplo_2: dict = Field(default={}, description="Resultado da execução da crew exemplo 2")
    relatorio_final: str = Field(default="", description="Relatório final gerado pela crew de relatório")
    
    # Controle de fluxo condicional
    processamento_complexo: bool = Field(default=False, description="Flag para determinar se deve usar processamento complexo")
    validacao_aprovada: bool = Field(default=False, description="Flag para indicar se a validação foi aprovada")
    tipo_processamento: str = Field(default="", description="Tipo de processamento escolhido pelo router")
    
    # Logs de controle de fluxo
    logs_or: list = Field(default_factory=list, description="Logs dos métodos executados via OR")
    logs_and: list = Field(default_factory=list, description="Logs dos métodos executados via AND")
    logs_router: list = Field(default_factory=list, description="Logs das decisões do router")

# [BLOCO 3] - IMPLEMENTAÇÃO DO FLOW
# ------------------------------------------------------
# A classe do flow herda de Flow e implementa os métodos necessários
# para definir o fluxo de execução.

class FlowExemplo(Flow):
    """
    Flow didático que demonstra como integrar todos os componentes do CrewAI.
    
    Estrutura do flow:
    1. Inicialização e configuração do estado (@Flow.start)
    2. Preparação de informações para a crew (@Flow.listen)
    3. Execução da crew_exemplo (@Flow.listen)
    4. Geração de relatório final com agente e ferramenta (@Flow.listen)
    5. Finalização e entrega do resultado (@Flow.listen)
    
    Cada etapa é implementada como um método assíncrono decorado adequadamente.
    """
    
    def __init__(self):
        """Inicializa o flow de exemplo integrado com crew_exemplo."""
        super().__init__()
        
    @start()
    async def iniciar_flow(self) -> Dict[str, Any]:
        """
        Ponto de entrada do flow.
        
        O método decorado com @start() é sempre o primeiro a ser executado.
        Ele acessa o estado através de self.state e deve retornar um estado 
        atualizado para as próximas etapas.
        
        Returns:
            Estado estruturado convertido para dicionário.
        """
        # [DICA 1] - ACESSO AO ESTADO
        # Métodos @start() acessam o estado através de self.state
        # O estado já foi inicializado pelo método kickoff() com os inputs fornecidos
        current_state = self.state if isinstance(self.state, dict) else self.state.__dict__
        
        # [DICA 2] - CONVERSÃO DE ESTADO
        # Converta o estado não estruturado (dicionário) para um objeto Pydantic
        # Isso garante validação automática e acesso estruturado aos dados
        flow_state = FlowExemploState(
            # Use get() com valores padrão para lidar com entradas ausentes
            topico=current_state.get("topico", "[Tópico não especificado]"),
            # Você pode usar valores de entrada para construir outros campos
            info_externa_1=current_state.get("info_externa_1", f"Contexto inicial sobre {current_state.get('topico', '[Tópico]')}")
        )
        
        # [DICA 3] - LOGGING CLARO
        # Use emojis e mensagens claras para facilitar o acompanhamento do flow
        print(f"🚀 [FLOW EXEMPLO] Iniciando com tópico: '{flow_state.topico}'")
        
        # [DICA 4] - RETORNO DE ESTADO
        # Sempre converta o objeto Pydantic de volta para dicionário ao retornar
        return flow_state.model_dump()
    
    @listen("iniciar_flow")
    async def preparar_informacoes_externas(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepara informações externas para a crew_exemplo.
        
        O decorador @listen("metodo_anterior") indica que este método
        deve ser executado após a conclusão do método especificado.
        
        Args:
            state: Estado atual do flow (dicionário).
            
        Returns:
            Estado atualizado com informações externas preparadas.
        """
        # [DICA 4] - RECONSTRUÇÃO DE ESTADO
        # Reconstrua o objeto Pydantic a partir do dicionário recebido
        flow_state = FlowExemploState(**state)
        
        print(f"📋 [FLOW EXEMPLO] Preparando informações para: '{flow_state.topico}'")
        
        # [DICA 5] - PROCESSAMENTO DE DADOS
        # Aqui você pode realizar qualquer processamento necessário antes de chamar a crew
        # Por exemplo: buscar dados externos, formatar informações, etc.
        
        # Neste exemplo, estamos apenas criando informações de demonstração
        # Em um caso real, estas informações viriam de fontes externas ou processamento
        flow_state.info_externa_1 = f"Contexto principal sobre '{flow_state.topico}'"
        flow_state.info_externa_2 = f"Dados complementares relacionados a '{flow_state.topico}'"
        flow_state.info_externa_3 = f"Informações adicionais relevantes para '{flow_state.topico}'"
        
        print("✅ [FLOW EXEMPLO] Informações preparadas com sucesso")
        
        # Sempre retorne o estado atualizado como dicionário
        return flow_state.model_dump()
    
    @listen("preparar_informacoes_externas")
    async def executar_crew_exemplo(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa a crew_exemplo com as informações preparadas.
        
        Esta etapa demonstra como integrar uma crew existente dentro de um flow,
        permitindo a composição de fluxos complexos a partir de componentes reutilizáveis.
        
        Args:
            state: Estado atual do flow com informações externas.
            
        Returns:
            Estado atualizado com os resultados da crew_exemplo.
        """
        # Reconstrua o objeto de estado
        flow_state = FlowExemploState(**state)
        
        print(f"🤖 [FLOW EXEMPLO] Executando crew_exemplo para: '{flow_state.topico}'")
        
        # [DICA 6] - INTEGRAÇÃO COM CREWS
        # Ao integrar crews em flows, você pode:
        # 1. Chamar um método de execução da crew (como neste exemplo)  
        # 2. Instanciar e executar a crew diretamente
        # 3. Usar uma abordagem híbrida com configuração dinâmica
        
        try:
            # Executa a crew_exemplo com as informações preparadas
            resultado_crew = metodo_de_execucao_da_crew(
                info_externa_1=flow_state.info_externa_1,
                info_externa_2=flow_state.info_externa_2,
                info_externa_3=flow_state.info_externa_3
            )
            
            # Atualiza o estado com os resultados da crew
            flow_state.resultado_crew_exemplo = resultado_crew
            
            print("✅ [FLOW EXEMPLO] Crew exemplo executada com sucesso")
            
        except Exception as e:
            # [DICA 7] - TRATAMENTO DE ERROS
            # Sempre trate possíveis erros para evitar que o flow inteiro falhe
            print(f"❌ [FLOW EXEMPLO] Erro ao executar crew exemplo: {str(e)}")
            # Em caso de erro, podemos fornecer um resultado padrão ou alternativo
            flow_state.resultado_crew_exemplo = {"erro": str(e), "resultado_alternativo": "Dados de fallback"}
        
        return flow_state.model_dump()
    
    @listen("executar_crew_exemplo")
    async def executar_crew_exemplo_2(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa a crew_exemplo_2 com análise complexa dos dados.
        
        Esta etapa demonstra como executar múltiplas crews em sequência,
        permitindo processamento mais complexo e especializado dos dados.
        
        Args:
            state: Estado atual do flow com os resultados da crew_exemplo.
            
        Returns:
            Estado atualizado com os resultados da crew_exemplo_2.
        """
        flow_state = FlowExemploState(**state)
        
        print(f"🔬 [FLOW EXEMPLO] Executando crew_exemplo_2 para análise complexa: '{flow_state.topico}'")
        
        try:
            # Executa a crew_exemplo_2 com dados complexos baseados nos resultados anteriores
            resultado_crew_2 = metodo_de_execucao_da_crew_2(
                dados_complexos=str(flow_state.resultado_crew_exemplo),
                contexto_adicional=flow_state.info_externa_1,
                parametros_tecnicos=f"Análise técnica de: {flow_state.topico}"
            )
            
            # Atualiza o estado com os resultados da segunda crew
            flow_state.resultado_crew_exemplo_2 = resultado_crew_2
            
            print("✅ [FLOW EXEMPLO] Crew exemplo 2 executada com sucesso")
            
        except Exception as e:
            print(f"❌ [FLOW EXEMPLO] Erro ao executar crew exemplo 2: {str(e)}")
            flow_state.resultado_crew_exemplo_2 = {"erro": str(e), "resultado_alternativo": "Análise complexa indisponível"}
        
        return flow_state.model_dump()
    
    @listen("executar_crew_exemplo_2")
    async def gerar_relatorio_final(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gera um relatório final consolidando os resultados de múltiplas crews.
        
        Esta etapa demonstra como integrar crews especializadas dentro de um flow,
        consolidando resultados de múltiplas execuções em um relatório final.
        
        Args:
            state: Estado atual do flow com os resultados de ambas as crews.
            
        Returns:
            Estado atualizado com o relatório final consolidado.
        """
        flow_state = FlowExemploState(**state)
        
        print(f"📝 [FLOW EXEMPLO] Gerando relatório final consolidado para: '{flow_state.topico}'")
        
        try:
            # [DICA 8] - INTEGRAÇÃO COM CREW ESPECIALIZADA
            # Consolida os resultados de múltiplas crews para o relatório final
            dados_consolidados = {
                "crew_exemplo": flow_state.resultado_crew_exemplo,
                "crew_exemplo_2": flow_state.resultado_crew_exemplo_2,
                "topico": flow_state.topico
            }
            
            resultado_relatorio = executar_crew_relatorio(
                dados_entrada=str(dados_consolidados),
                topico=flow_state.topico
            )
            
            # Extrai o conteúdo do relatório do resultado da crew
            if hasattr(resultado_relatorio, 'raw'):
                flow_state.relatorio_final = resultado_relatorio.raw
            else:
                flow_state.relatorio_final = str(resultado_relatorio)
            
            print("✅ [FLOW EXEMPLO] Relatório final gerado com sucesso")
            
        except Exception as e:
            print(f"❌ [FLOW EXEMPLO] Erro ao gerar relatório: {str(e)}")
            flow_state.relatorio_final = f"Não foi possível gerar o relatório: {str(e)}"
        
        return flow_state.model_dump()
    
    # [BLOCO 3.5] - OPERADORES LÓGICOS AVANÇADOS
    # ------------------------------------------------------
    # Demonstração dos operadores OR, AND e ROUTER do CrewAI
    
    @listen("gerar_relatorio_final")
    async def avaliar_complexidade(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Avalia se o processamento deve ser complexo baseado no conteúdo.
        
        Esta etapa demonstra como usar lógica condicional para determinar
        o fluxo de execução baseado nos resultados anteriores.
        
        Args:
            state: Estado atual do flow com o relatório gerado.
            
        Returns:
            Estado atualizado com flags de controle de fluxo.
        """
        flow_state = FlowExemploState(**state)
        
        print("🔍 [FLOW EXEMPLO] Avaliando complexidade do processamento...")
        
        # [DICA 13] - LÓGICA CONDICIONAL BASEADA EM CONTEÚDO
        # Analisa o conteúdo para determinar se precisa de processamento complexo
        relatorio_length = len(flow_state.relatorio_final)
        crew_1_length = len(str(flow_state.resultado_crew_exemplo))
        crew_2_length = len(str(flow_state.resultado_crew_exemplo_2))
        
        # Determina complexidade baseada no tamanho do conteúdo
        total_content = relatorio_length + crew_1_length + crew_2_length
        flow_state.processamento_complexo = total_content > 1000  # Threshold arbitrário
        
        # Simula uma validação aleatória para demonstrar o router
        flow_state.validacao_aprovada = random.choice([True, False])
        
        print(f"📊 Conteúdo total: {total_content} caracteres")
        print(f"🔧 Processamento complexo: {flow_state.processamento_complexo}")
        print(f"✅ Validação aprovada: {flow_state.validacao_aprovada}")
        
        return flow_state.model_dump()
    
    @router("avaliar_complexidade")
    async def decidir_tipo_processamento(self, state: Dict[str, Any]) -> str:
        """
        Router que decide o tipo de processamento baseado na avaliação.
        
        O decorator @router permite criar fluxos condicionais dinâmicos,
        direcionando a execução para diferentes caminhos baseado na lógica de negócio.
        
        Args:
            state: Estado atual do flow.
            
        Returns:
            String indicando o caminho a seguir.
        """
        flow_state = FlowExemploState(**state)
        
        print("🎯 [ROUTER] Decidindo tipo de processamento...")
        
        # [DICA 14] - LÓGICA DO ROUTER
        # O router permite criar múltiplos caminhos de execução
        if flow_state.processamento_complexo and flow_state.validacao_aprovada:
            flow_state.tipo_processamento = "complexo_aprovado"
            flow_state.logs_router.append("Escolhido: processamento complexo aprovado")
            print("📈 Direcionando para processamento complexo aprovado")
            return "complexo_aprovado"
        elif flow_state.processamento_complexo and not flow_state.validacao_aprovada:
            flow_state.tipo_processamento = "complexo_rejeitado"
            flow_state.logs_router.append("Escolhido: processamento complexo rejeitado")
            print("📉 Direcionando para processamento complexo rejeitado")
            return "complexo_rejeitado"
        elif not flow_state.processamento_complexo and flow_state.validacao_aprovada:
            flow_state.tipo_processamento = "simples_aprovado"
            flow_state.logs_router.append("Escolhido: processamento simples aprovado")
            print("✨ Direcionando para processamento simples aprovado")
            return "simples_aprovado"
        else:
            flow_state.tipo_processamento = "simples_rejeitado"
            flow_state.logs_router.append("Escolhido: processamento simples rejeitado")
            print("⚡ Direcionando para processamento simples rejeitado")
            return "simples_rejeitado"
    
    # [DEMONSTRAÇÃO DO OPERADOR OR]
    # O operador or_ executa quando QUALQUER um dos métodos especificados emite saída
    
    @listen("complexo_aprovado")
    async def processamento_avancado(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processamento avançado para casos complexos aprovados.
        """
        flow_state = FlowExemploState(**state)
        
        print("🚀 [PROCESSAMENTO AVANÇADO] Executando análise detalhada...")
        flow_state.logs_or.append("Processamento avançado executado")
        
        # Simula processamento avançado
        import time
        time.sleep(0.5)  # Simula processamento
        
        return flow_state.model_dump()
    
    @listen("simples_aprovado")
    async def processamento_rapido(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processamento rápido para casos simples aprovados.
        """
        flow_state = FlowExemploState(**state)
        
        print("⚡ [PROCESSAMENTO RÁPIDO] Executando análise básica...")
        flow_state.logs_or.append("Processamento rápido executado")
        
        return flow_state.model_dump()
    
    @listen(or_("processamento_avancado", "processamento_rapido"))
    async def logger_processamento_aprovado(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Logger que executa quando QUALQUER processamento aprovado é concluído.
        
        O operador or_ permite que este método seja executado quando
        processamento_avancado OU processamento_rapido emitir uma saída.
        
        Args:
            state: Estado atual do flow.
            
        Returns:
            Estado atualizado com logs.
        """
        flow_state = FlowExemploState(**state)
        
        print("📝 [LOGGER OR] Processamento aprovado concluído!")
        flow_state.logs_or.append("Logger OR: processamento aprovado registrado")
        
        return flow_state.model_dump()
    
    # [DEMONSTRAÇÃO DO OPERADOR AND]
    # O operador and_ executa apenas quando TODOS os métodos especificados emitiram saída
    
    @listen("complexo_rejeitado")
    async def analise_rejeicao_complexa(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Análise específica para rejeições em casos complexos.
        """
        flow_state = FlowExemploState(**state)
        
        print("🔍 [ANÁLISE REJEIÇÃO] Analisando motivos da rejeição complexa...")
        flow_state.logs_and.append("Análise de rejeição complexa executada")
        
        return flow_state.model_dump()
    
    @listen("simples_rejeitado")
    async def analise_rejeicao_simples(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Análise específica para rejeições em casos simples.
        """
        flow_state = FlowExemploState(**state)
        
        print("📋 [ANÁLISE REJEIÇÃO] Analisando motivos da rejeição simples...")
        flow_state.logs_and.append("Análise de rejeição simples executada")
        
        return flow_state.model_dump()
    
    @listen(and_("analise_rejeicao_complexa", "analise_rejeicao_simples"))
    async def consolidar_analises_rejeicao(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Consolida análises apenas quando AMBAS as análises de rejeição foram executadas.
        
        O operador and_ garante que este método só execute quando
        analise_rejeicao_complexa E analise_rejeicao_simples tiverem emitido saída.
        
        Args:
            state: Estado atual do flow.
            
        Returns:
            Estado atualizado com consolidação.
        """
        flow_state = FlowExemploState(**state)
        
        print("📊 [CONSOLIDADOR AND] Consolidando todas as análises de rejeição...")
        flow_state.logs_and.append("Consolidação AND: todas as análises de rejeição processadas")
        
        return flow_state.model_dump()
    
    @listen(or_("logger_processamento_aprovado", "consolidar_analises_rejeicao"))
    async def finalizar_flow(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Finaliza o flow e prepara a saída final.
        
        Esta é a última etapa do flow, responsável por finalizar o processamento
        e preparar os dados para retorno ao chamador.
        
        Args:
            state: Estado atual do flow com o relatório final.
            
        Returns:
            Estado final do flow, pronto para ser retornado ao chamador.
        """
        flow_state = FlowExemploState(**state)
        
        # [DICA 11] - FINALIZAÇÃO DO FLOW
        # Use esta etapa para:
        # 1. Realizar limpezas necessárias
        # 2. Formatar os dados de saída
        # 3. Registrar métricas ou logs finais
        # 4. Preparar o estado para retorno
        
        print(f"🏁 [FLOW EXEMPLO] Finalizando flow para: '{flow_state.topico}'")
        
        # Exibe um resumo dos resultados (opcional)
        print("\n" + "="*50)
        print(f"RESUMO DO FLOW: '{flow_state.topico}'")
        print("="*50)
        print(f"Crew exemplo processada: {len(str(flow_state.resultado_crew_exemplo))} caracteres")
        print(f"Crew exemplo 2 processada: {len(str(flow_state.resultado_crew_exemplo_2))} caracteres")
        print(f"Tamanho do relatório: {len(str(flow_state.relatorio_final))} caracteres")
        print(f"Tipo de processamento: {flow_state.tipo_processamento}")
        print(f"Processamento complexo: {flow_state.processamento_complexo}")
        print(f"Validação aprovada: {flow_state.validacao_aprovada}")
        print(f"Logs OR executados: {len(flow_state.logs_or)}")
        print(f"Logs AND executados: {len(flow_state.logs_and)}")
        print(f"Decisões do Router: {len(flow_state.logs_router)}")
        print("="*50)
        
        # [DICA 15] - LOGS DETALHADOS DOS OPERADORES
        if flow_state.logs_or:
            print("\n🔀 LOGS DO OPERADOR OR:")
            for i, log in enumerate(flow_state.logs_or, 1):
                print(f"  {i}. {log}")
        
        if flow_state.logs_and:
            print("\n🔗 LOGS DO OPERADOR AND:")
            for i, log in enumerate(flow_state.logs_and, 1):
                print(f"  {i}. {log}")
        
        if flow_state.logs_router:
            print("\n🎯 LOGS DO ROUTER:")
            for i, log in enumerate(flow_state.logs_router, 1):
                print(f"  {i}. {log}")
        
        print("="*50)
        
        # [DICA 12] - RETORNO FINAL
        # O estado final deve conter todos os dados relevantes para o chamador
        return flow_state.model_dump()

# [BLOCO 4] - FUNÇÕES AUXILIARES E PONTO DE ENTRADA
# ------------------------------------------------------
# Estas funções facilitam a execução e teste do flow

async def executar_flow_async(topico: str, **kwargs) -> Dict[str, Any]:
    """
    Função auxiliar assíncrona para executar o flow com parâmetros específicos.
    
    Esta função facilita a execução do flow a partir de outros módulos
    ou scripts, encapsulando a criação e execução do flow.
    
    Args:
        topico: O tópico principal a ser processado pelo flow.
        **kwargs: Parâmetros adicionais para o flow.
        
    Returns:
        Resultado da execução do flow.
    """
    # Instancia o flow
    flow = FlowExemplo()
    
    # Prepara os parâmetros de entrada como state
    state = {"topico": topico}
    state.update(kwargs)  # Adiciona parâmetros opcionais
    
    # Executa o flow e retorna o resultado
    return await flow.kickoff(state)

def executar_flow(topico: str, **kwargs) -> Dict[str, Any]:
    """
    Função síncrona para executar o flow.
    
    Args:
        topico: O tópico principal a ser processado pelo flow.
        **kwargs: Parâmetros adicionais para o flow.
        
    Returns:
        Resultado da execução do flow.
    """
    # Instancia o flow
    flow = FlowExemplo()
    
    # Prepara os parâmetros de entrada como state
    state = {"topico": topico}
    state.update(kwargs)  # Adiciona parâmetros opcionais
    
    # Executa o flow usando o método síncrono kickoff
    # O CrewAI gerencia internamente o event loop
    return flow.kickoff(state)

def plot():
    """
    Gera uma visualização HTML interativa do flow usando o método plot() do CrewAI.
    
    Esta função cria uma representação gráfica do workflow que mostra:
    - Nós representando cada método/etapa do flow
    - Setas direcionadas indicando o fluxo de execução
    - Conexões entre métodos baseadas nos decoradores @listen, @router, or_, and_
    - Estrutura visual dos operadores lógicos avançados implementados
    
    O arquivo HTML gerado é interativo, permitindo:
    - Zoom in/out para explorar detalhes
    - Hover sobre nós para ver informações adicionais
    - Navegação visual do fluxo de dados entre etapas
    
    Saída:
        Cria o arquivo "FlowExemploPlot.html" no diretório atual que pode ser
        aberto em qualquer navegador web para visualizar o flow completo.
        
    Uso:
        Esta visualização é especialmente útil para:
        - Entender a estrutura complexa dos operadores lógicos (or_, and_, @router)
        - Debugar fluxos condicionais
        - Documentar workflows para apresentações
        - Identificar gargalos ou caminhos de execução
    """
    flow = FlowExemplo()
    flow.plot("FlowExemploPlot")

# Ponto de entrada para execução direta do script
if __name__ == "__main__":
    # [DICA 14] - EXECUÇÃO STANDALONE
    # Defina parâmetros de exemplo para teste rápido do flow
    
    print("\n" + "="*70)
    print("GUIA DE CONSTRUÇÃO DE FLOWS NO CREWAI - EXEMPLO DIDÁTICO")
    print("="*70)
    
    # Parâmetros de exemplo para teste
    TOPICO_EXEMPLO = "Construção de Flows no CrewAI"
    INFO_ADICIONAL = "Foco em integração de componentes e boas práticas"
    
    # Executa o flow
    try:
        resultado = executar_flow(
            topico=TOPICO_EXEMPLO,
            info_externa_1=INFO_ADICIONAL
        )
        print("✅ Flow executado com sucesso!")
        plot()
    except Exception as e:
        print(f"❌ Erro ao executar o flow: {str(e)}")
        import traceback
        traceback.print_exc()
        resultado = {"relatorio_final": f"Erro na execução: {str(e)}"}
    
    # Exibe o resultado final formatado
    print("\n" + "="*70)
    print(f"RESULTADO DO FLOW: '{TOPICO_EXEMPLO}'")
    print("="*70)
    print(resultado["relatorio_final"][:500] + "..." if len(resultado["relatorio_final"]) > 500 else resultado["relatorio_final"])
    print("\n[Relatório completo disponível no resultado do flow]")
    print("="*70)
    
    print("\n💡 DICA: Este flow serve como um guia didático para construção de flows no CrewAI.")
    print("💡 Estude o código-fonte para entender as melhores práticas e padrões de implementação.")
    print("="*70)
