# Trabalhos relacionados e posicionamento

**Idioma:** [English](RELATED-WORK.md) · Português (Brasil)

O Nirmata está inserido em uma área crescente de pesquisa sobre agentes com ferramentas, segurança durante a execução, monitoramento de trajetórias e autonomia delegada. Esta página mapeia proximidade conceitual; ela não reivindica prioridade nem equivalência.

## Pesquisas próximas

- **ToolEmu** apresenta um sandbox emulado por LM para identificar em escala riscos de agentes que usam ferramentas. O Nirmata compartilha o interesse em riscos durante a execução, mas atualmente se concentra em trajetórias pequenas e auditáveis e em transições de autoridade, não em geração ampla de cenários. [Ruan et al., ICLR 2024](https://openreview.net/forum?id=GEcwtMk1uA)
- **AgentDojo** avalia ataques de prompt injection e defesas para agentes operando sobre dados não confiáveis vindos de ferramentas. Os casos de injeção de aprovação e integridade de controle do Nirmata são próximos desse modelo de ameaça, mas o Nirmata ainda não é um benchmark competitivo de prompt injection. [Debenedetti et al., NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html)
- **Monitoring LLM Agents for Sequentially Contextual Harm** estuda danos visíveis somente em sequências de ações individualmente plausíveis. O Nirmata também trata sequências e efeitos externos como evidência principal, com ênfase adicional em autorização da proprietária e transições de estado de publicação. [Korbak et al., OpenReview](https://openreview.net/forum?id=PGsM81SWHt)
- **TraceSafe** avalia guardrails sobre trajetórias de múltiplas chamadas de ferramentas. Seu foco em escala de benchmark é diretamente relevante para a pergunta piloto do Nirmata; a contribuição atual do Nirmata é um protocolo que preserva falhas e um desenho de avaliação fatorado, não uma cobertura comparável. [Chen et al., arXiv 2026](https://arxiv.org/abs/2604.07223)
- **ATBench** propõe um benchmark de segurança em trajetórias longas organizado por fonte de risco, modo de falha e dano real. O Nirmata deve utilizá-lo como ponto de comparação ao ampliar sua taxonomia e dataset. [Li et al., arXiv 2026](https://arxiv.org/abs/2604.02022)
- **Specifying the Delegated-Autonomy Boundary** trata autoridade, supervisão e retorno do controle como compromissos no nível de requisitos. Isso se alinha à distinção do Nirmata entre aprovação de conteúdo, entrada na fila, autorização de publicação e efeitos externos. [Arora, Vogelsang e Sharma, arXiv 2026](https://arxiv.org/abs/2607.17225)

## Posicionamento atual

O Nirmata deve ser descrito como um **programa piloto independente de pesquisa e laboratório de casos reproduzíveis**, não como benchmark maduro ou produto de segurança validado. Sua ênfase combina:

1. evidência do resultado final e da trajetória;
2. transições explícitas de autoridade delegada;
3. preservação de avaliações falhas e evidências invalidadas;
4. passagem entre experimentos controlados e sistemas reais aplicados.

Determinar se essa combinação constitui contribuição científica nova exige revisão formal de literatura e avaliação externa.

## Lacunas da revisão de literatura

- Comparação formal com supervisão de processo e process-reward modeling.
- Pesquisa de interação humano-computador sobre consentimento, aprovação e fronteiras de automação.
- Métodos de safety case e assurance case de sistemas críticos.
- Padrões de proveniência e schemas de eventos para trajetórias de agentes.
- Desenho estatístico para pilotos pequenos com trajetórias pareadas.

Esta página deve ser ampliada antes de qualquer artigo reivindicar novidade.
