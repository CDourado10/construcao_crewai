from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class ExemploToolInput(BaseModel):
    """Define os parâmetros de entrada necessários para a execução da ExemploTool."""

    argument_1: str = Field(
        ...,
        description=(
            "Primeiro argumento que estabelece o contexto principal da execução.\n"
            "Exemplos válidos: 'relatório financeiro', 'tendências em IA', 'resumo de artigo acadêmico'."
        ),
    )
    argument_2: str = Field(
        ...,
        description=(
            "Segundo argumento que complementa ou refina o primeiro argumento.\n"
            "Exemplos válidos: 'curto prazo', 'para leigos', 'com foco em oportunidades de negócio'."
        ),
    )


class ExemploTool(BaseTool):
    # Nome da ferramenta (como será referenciada pelo CrewAI)
    name: str = "Exemplo Tool"

    # Descrição geral da ferramenta — deve ser clara para humanos e LLMs
    description: str = (
        "Uma ferramenta de demonstração que combina diferentes métodos internos "
        "para gerar um resultado final organizado e compreensível.\n\n"
        "📌 Propósito:\n"
        "- Demonstrar a estrutura de implementação de uma Tool no CrewAI.\n"
        "- Ilustrar como dividir a lógica em métodos internos reutilizáveis.\n\n"
        "📂 Casos de uso:\n"
        "- Servir como modelo para novos desenvolvedores.\n"
        "- Testar a integração de ferramentas personalizadas.\n\n"
        "✅ Exemplos de entrada:\n"
        "- argument_1='relatório financeiro', argument_2='curto prazo'\n"
        "- argument_1='tendências em IA', argument_2='para leigos'\n\n"
        "📤 Exemplo de saída:\n"
        "'Organizar as informações retornadas pelos métodos internos: metodo interno 1 metodo interno 2'"
    )

    # Schema de entrada esperado
    args_schema: Type[BaseModel] = ExemploToolInput

    def _metodo_interno_1(self) -> str:
        """
        Executa a primeira etapa da lógica da ferramenta.

        Retorno:
            str: Um resultado parcial da primeira operação.
        """
        return "metodo interno 1"

    def _metodo_interno_2(self) -> str:
        """
        Executa a segunda etapa da lógica da ferramenta.

        Retorno:
            str: Um resultado parcial da segunda operação.
        """
        return "metodo interno 2"

    def _metodo_interno_3(self) -> str:
        """
        Combina os resultados dos métodos internos anteriores,
        organizando-os em uma saída final clara e estruturada.

        Retorno:
            str: Resultado consolidado da execução da ferramenta.
        """
        metodo_1 = self._metodo_interno_1()
        metodo_2 = self._metodo_interno_2()
        resultado = (
            f"Organizar as informações retornadas pelos métodos internos: {metodo_1} {metodo_2}"
        )
        return resultado

    def _run(self, argument_1: str, argument_2: str) -> str:
        """
        Método principal de execução da Tool.

        Atua como fachada, chamando os métodos internos na ordem correta
        e retornando o resultado consolidado.

        Args:
            argument_1 (str): Contexto principal da execução.
            argument_2 (str): Complemento ou refinamento do argumento principal.

        Retorno:
            str: Resultado final da ferramenta, em formato de string legível.
        """
        return self._metodo_interno_3()
