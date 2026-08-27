# Por que a resposta final não basta para avaliar agentes de IA

**English:** [Why final answers are not enough](../en/why-final-answers-are-not-enough.md)  
**Palavra-chave principal:** avaliação de agentes de IA  
**Meta description:** Entenda por que avaliar agentes de IA exige inspecionar ferramentas, autorização, estados e efeitos externos — não só a resposta final.

Um agente de IA pode produzir a resposta correta depois de percorrer um caminho inaceitável. Ele pode usar os dados errados, aceitar uma aprovação forjada, chamar uma ferramenta fora de sua autoridade ou criar um efeito externo que sua mensagem final nunca revela. Quando a avaliação enxerga apenas a resposta, esses eventos desaparecem.

Esse é o problema central investigado pelo Nirmata: **quanta informação relevante para segurança existe na trajetória de execução de um agente, mas não aparece em seu resultado final?**

## Uma resposta correta é apenas uma observação

A avaliação convencional pergunta se uma resposta é correta, relevante, segura ou bem escrita. Essas perguntas continuam importantes. Elas apenas são incompletas quando o sistema pode agir.

Considere um agente editorial que entrega um artigo pronto para publicação. O texto pode estar correto, embora o processo tenha:

- tratado a recomendação de uma revisora como aprovação da proprietária;
- consultado uma fonte não verificada;
- colocado conteúdo na fila antes de fixar a versão autorizada;
- publicado quando tinha autoridade apenas para redigir;
- repetido uma ação externa e criado um efeito duplicado.

Nenhuma dessas falhas precisa aparecer no artigo. O objeto avaliado, portanto, não é apenas uma sequência de palavras. É uma sequência de decisões, chamadas de ferramentas, transições de estado, eventos de autorização e efeitos.

## O que a trajetória acrescenta

O Nirmata define trajetória de execução como o resultado final mais a evidência observável do processo. Dependendo do sistema, isso pode incluir entradas e resultados de ferramentas, hashes de conteúdo, fontes de aprovação, decisões de controladores, identificadores externos e intervenções humanas.

Essa visão acompanha uma mudança mais ampla na pesquisa sobre segurança de agentes. O AgentDojo avalia agentes que usam ferramentas sobre dados não confiáveis e mostra por que prompt injection deve ser testada em um ambiente interativo, não como um problema de resposta estática. TraceSafe-Bench e ATBench estudam explicitamente trajetórias de múltiplas etapas e falhas de longo horizonte. Os trabalhos diferem em escopo e maturidade, mas compartilham uma premissa prática: o risco pode surgir durante a execução.

## Separe os sinais antes de combiná-los

Mostrar toda a evidência para um único avaliador parece simples, mas cria outro risco: um processo aparentemente limpo pode suavizar o julgamento de conteúdo inseguro, ou um conteúdo alarmante pode distorcer a classificação de uma tentativa que foi corretamente bloqueada.

O desenho piloto atual do Nirmata separa os canais:

```text
avaliador de conteúdo   -> content_unsafe
avaliador de trajetória -> trajectory_unsafe + classe de processo
julgamento final        -> content_unsafe OR trajectory_unsafe
```

A regra monotônica `OR` impede que um sinal seguro apague um sinal inseguro. Ela também permite medir a contribuição incremental da trajetória. Essa arquitetura passou por verificações de integração; ainda não produziu um resultado confirmatório cego.

## Tentativa bloqueada não é violação executada

A evidência de trajetória deve melhorar a discriminação, não apenas produzir mais alertas. Um pedido não autorizado bloqueado por um controle mostra que o controle funcionou. Uma ação não autorizada que alcançou um sistema externo é uma violação de política. Tratar os dois casos como igualmente inseguros esconde a diferença entre exposição e falha.

Por isso, a taxonomia do Nirmata separa anomalias suspeitas, tentativas não autorizadas bloqueadas, violações executadas e ações externas danosas. Essa distinção torna a avaliação mais útil para o desenho do sistema, pois identifica onde a defesa resistiu e onde falhou.

## A pergunta prática

O objetivo não é coletar todo pensamento oculto. É preservar a evidência observável necessária para responder a quatro perguntas operacionais:

1. O que o agente tentou fazer?
2. Que autoridade ele realmente possuía?
3. O que mudou fora do modelo?
4. Qual controle permitiu, bloqueou ou alterou a ação?

A resposta final mostra o que o agente disse. A trajetória pode ajudar a determinar o que o sistema fez.

## Continue lendo

- [Metodologia do Nirmata](../../docs/METHODOLOGY.pt-BR.md)
- [Estado das evidências](../../docs/EVIDENCE-STATUS.pt-BR.md)
- [Registro de experimentos](../../experiments/README.md)
- [Trabalhos relacionados](../../docs/RELATED-WORK.pt-BR.md)

**Fontes primárias externas:** [AgentDojo, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html) · [TraceSafe, arXiv 2026](https://arxiv.org/abs/2604.07223) · [ATBench, arXiv 2026](https://arxiv.org/abs/2604.02022)
