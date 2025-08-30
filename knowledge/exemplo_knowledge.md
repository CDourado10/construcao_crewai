# 📘 Guia Prático para Construção de Arquivos de Conhecimento no CrewAI + Docling

## 🎯 Objetivo do Documento

Este guia tem como objetivo explicar **a forma ideal de criar arquivos de conhecimento em formato Markdown** para serem utilizados como fonte (`CrewDoclingSource`) dentro do CrewAI.

O **CrewAI**, em conjunto com o **Docling**, utiliza esses arquivos para:

- Converter documentos em representações estruturadas.
- Dividir o conteúdo em **chunks hierárquicos** para facilitar a busca semântica.
- Oferecer aos agentes os trechos mais relevantes durante a execução de **tasks**.

---

## 🏗️ Estrutura Recomendada

### 1. Use Cabeçalhos Hierárquicos

Os cabeçalhos (`#`, `##`, `###`) orientam o `HierarchicalChunker` do Docling a **dividir o documento de forma lógica**.

```markdown
# Tópico Principal
## Subtópico
### Detalhe
```

✅ Dica: quanto mais granularidade nos títulos, mais fácil para os agentes recuperarem apenas o trecho certo, sem carregar informação irrelevante.

### 2. Mantenha os Chunks Curtos

Cada seção deve ter 1 a 3 parágrafos no máximo.
Chunks curtos tornam a recuperação mais precisa e focada.

❌ Evite blocos longos com várias ideias misturadas.
✅ Prefira quebrar o conteúdo em seções pequenas e claras.

### 3. Use Listas e Tabelas

Listas e tabelas facilitam a leitura e a segmentação automática.

Exemplo de lista:

```markdown
- Vantagem 1: Melhora a organização.
- Vantagem 2: Ajuda na recuperação semântica.
- Vantagem 3: Reduz redundância nos embeddings.
```

Exemplo de tabela:

```markdown
| Termo       | Definição                   |
|-------------|-----------------------------|
| Chunk       | Unidade de informação       |
| Embedding   | Representação vetorial      |
```

### 4. Repita Termos Importantes

Palavras-chave relevantes devem ser estrategicamente repetidas para otimizar os embeddings.

Exemplo de termos úteis neste contexto:

- CrewAI
- Docling
- Knowledge Source
- Chunking

### 5. Evite Texto Excessivamente Longo

Não escreva capítulos inteiros sem subtítulos.

✅ Sempre divida conteúdos extensos em seções menores e focadas.
🔎 Isso aumenta a chance de o agente recuperar exatamente o que precisa.

## 📑 Exemplo de Estrutura de Documento

```markdown
# Introdução
Breve descrição do tema e contexto.

## Conceitos Principais

### Conceito A
Explicação curta e direta, destacando os pontos-chave.

### Conceito B
Explicação curta e direta, com foco em aplicabilidade.

## Exemplos de Aplicação
- Exemplo prático 1: como usar o conceito A em um caso real.
- Exemplo prático 2: situação onde o conceito B é útil.

## Referências
- Link ou citação 1
- Link ou citação 2
```

## ✅ Checklist de Boas Práticas

- [ ] Usar Markdown limpo e organizado.
- [ ] Garantir que cada seção tenha poucos parágrafos.
- [ ] Incluir palavras-chave importantes no texto.
- [ ] Estruturar com listas e tabelas sempre que possível.
- [ ] Dividir conteúdo longo em múltiplas seções.
- [ ] Revisar se o documento está fácil de ler tanto por humanos quanto por LLMs.

## 🔚 Conclusão

Seguindo este guia, qualquer documento Markdown estará pronto para ser processado pelo Docling e utilizado no CrewAI como uma fonte de conhecimento confiável, organizada e semanticamente otimizada.

Com isso, seus agentes terão acesso rápido e preciso às informações certas, aumentando a qualidade e a eficiência das respostas.
