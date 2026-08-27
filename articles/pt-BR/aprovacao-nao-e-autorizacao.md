# Aprovação não é autorização em sistemas agênticos

**English:** [Approval is not authorization](../en/approval-is-not-authorization.md)  
**Palavra-chave principal:** autoridade delegada em agentes de IA  
**Meta description:** Entenda por que conselho, aprovação, fila e permissão para agir precisam ser estados separados em sistemas com agentes de IA.

“Parece bom” não é um modelo seguro de permissão.

Em um fluxo agêntico, uma revisora pode recomendar um rascunho, a proprietária pode aprovar seu conteúdo, um agendador pode colocá-lo na fila e um publicador pode criar um efeito externo. São quatro eventos diferentes. Reduzi-los a uma única ideia de aprovação dá ao agente espaço para atravessar uma fronteira que ninguém delegou de forma explícita.

## A ambiguidade escondida na aprovação humana

A colaboração em linguagem natural depende de contexto. Pessoas normalmente entendem se “pode seguir” significa “continue editando”, “agende” ou “publique agora”. Um sistema que age por ferramentas não pode depender dessa ambiguidade com segurança.

O problema cresce quando a autoridade vem de várias pessoas:

- uma pesquisadora recomenda uma fonte;
- uma editora aceita a recomendação;
- a proprietária aprova o conteúdo final;
- um controlador verifica a versão aprovada;
- um publicador a envia para uma plataforma externa.

Se o agente converte a recomendação da pesquisadora em aprovação da proprietária, o conteúdo final pode continuar excelente. O caminho de autorização continua errado.

## Modele autoridade como estado, não como tom

Autoridade delegada precisa ser explícita, limitada e inspecionável. No mínimo, uma ação relevante deve vincular:

- **principal:** quem concedeu a autoridade;
- **ação:** o que pode ser feito;
- **objeto:** qual conteúdo ou recurso exato está coberto;
- **escopo:** onde e em qual conta a ação pode ocorrer;
- **tempo:** quando a autorização começa e expira;
- **precondições:** quais verificações precisam passar;
- **evidência:** como a concessão e o efeito resultante são registrados.

Isso transforma “a conversa pareceu positiva” em uma decisão verificável de controle. Um trabalho recente de engenharia de requisitos chama o conceito mais amplo de fronteira de autonomia delegada: as decisões sobre o que pode ser delegado, sob qual autoridade graduada, com qual supervisão e como o controle retorna a uma pessoa.

## Aprovação de conteúdo não é autoridade para publicar

Um fluxo robusto separa pelo menos estes estados:

```text
RASCUNHO -> REVISADO -> CONTEUDO_APROVADO -> FILA -> PUBLICACAO_AUTORIZADA -> PUBLICADO
```

A passagem de `CONTEUDO_APROVADO` para `PUBLICACAO_AUTORIZADA` não deve ser implícita. Ela deve exigir uma concessão distinta que mencione a versão exata a publicar. Um hash de conteúdo pode impedir que uma edição posterior herde silenciosamente uma aprovação anterior.

O publicador também deve ter menos autoridade que o planejador. Ele precisa de permissão para executar uma ação específica e aprovada, não de liberdade para redesenhar o plano. Isso reduz o raio de impacto se o contexto de planejamento for manipulado.

## O controle deve separar tentativa de efeito

Um agente pode tentar publicar sem autoridade. Se o controlador bloquear a chamada, o evento é importante, mas não é uma violação executada. Se a chamada alcançar a plataforma, o efeito externo muda a classificação.

Por isso, o registro de auditoria deve guardar tanto o pedido quanto o resultado:

- transição solicitada;
- autorização apresentada;
- decisão do controlador;
- invocação da ferramenta;
- identificador externo ou erro;
- estado final.

Sem o resultado, a equipe não consegue distinguir um ataque, uma defesa que funcionou ou uma violação real de política.

## O que o Nirmata mostrou — e o que não mostrou

O protótipo do Nirmata passou por 12 verificações conhecidas de desenvolvimento e integridade de controle, cobrindo injeção de aprovação, identidade forjada, adulteração de estado, substituição de conteúdo, manipulação de fila, replay e publicação em duas fases. Esses testes sustentam o comportamento da implementação nos casos conhecidos.

Eles não demonstram isolamento em nível de produção nem robustez contra ataques inéditos. Controlador e publicador ainda precisam de credenciais independentes e isolamento mais forte entre processos antes que o sistema possa sustentar uma afirmação mais forte de segurança.

A conclusão desconfortável é simples: aprovação humana não é uma mensagem. É uma transição de estado apoiada por evidência, escopo e uma fronteira aplicável.

## Continue lendo

- [Experimento 001](../../experiments/README.md#experiment-001)
- [Metodologia e taxonomia de processo](../../docs/METHODOLOGY.pt-BR.md)
- [Estado das evidências](../../docs/EVIDENCE-STATUS.pt-BR.md)
- [Agenda de pesquisa](../../docs/RESEARCH-AGENDA.pt-BR.md)

**Fonte primária externa:** [Specifying the Delegated-Autonomy Boundary, arXiv 2026](https://arxiv.org/abs/2607.17225)
