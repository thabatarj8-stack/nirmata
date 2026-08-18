# Nirmata

**Idioma:** [English](README.md) · Português (Brasil)

Nirmata é um programa independente de pesquisa para avaliar agentes de IA por suas **trajetórias de execução**, não apenas por suas respostas finais.

Uma resposta pode parecer correta enquanto o caminho que a produziu contém um erro de autorização, uma chamada insegura de ferramenta, um controle quebrado ou um efeito externo invisível no resultado final. O Nirmata torna esse caminho inspecionável.

> **Estado da pesquisa:** trabalho independente em estágio inicial. O pipeline de avaliação passou por verificações de desenvolvimento e integração, mas não há atualmente um resultado confirmatório cego reivindicado. Um primeiro holdout foi invalidado antes da pontuação porque seu gabarito foi exposto ao contexto do avaliador.

## Ideia central

O Nirmata trata uma execução do agente como uma sequência auditável de:

- decisões e seleção de candidatos;
- verificação de fontes e afirmações;
- chamadas de ferramentas e transições de estado;
- eventos de aprovação e autorização;
- efeitos externos;
- falhas, correções e intervenções humanas.

O projeto investiga se essa trajetória contém informação relevante para segurança que permanece invisível quando a avaliação considera apenas o resultado final.

## Perguntas de pesquisa

1. Quais comportamentos inseguros não são percebidos quando avaliadores inspecionam somente a resposta final?
2. Quanto sinal adicional de segurança é acrescentado pela trajetória bruta?
3. Protocolos de aprovação conseguem preservar a autoridade humana diante de entradas adversariais ou ambíguas?
4. Avaliar conteúdo e trajetória de forma independente reduz interferência entre sinais?
5. Como preservar falhas de agentes para manter alegações futuras auditáveis e reproduzíveis?

## Pilares de pesquisa

| Pilar | Objeto de estudo | Evidência atual |
|---|---|---|
| Avaliação consciente da trajetória | Resultado final isolado vs. resultado mais sinal independente da trajetória | Integração do pipeline fatorado validada; confirmação cega pendente |
| Autoridade delegada | Aprovação, fila, autorização de publicação e efeitos externos | 12 verificações de desenvolvimento/integridade passaram; isolamento real continua sendo limitação |
| Metodologia que preserva falhas | Correções versionadas, execuções abortadas, holdouts invalidados e desenhos congelados | Manifestos e registros de falhas existem no laboratório-fonte |
| Autonomia aplicada | Substituição de dependências SaaS opacas por sistemas governados pela proprietária | Caso comentário→DM no Instagram concluído em produção |

## Experimentos

| Experimento | Pergunta | Estado |
|---|---|---|
| [#001 — Avaliação estratégica e autoridade delegada](experiments/README.md#experiment-001) | Um editor consegue selecionar, verificar e agir sem exceder a autoridade delegada? | Execução exploratória e verificações adversariais concluídas |
| [#002 — Resultado final vs. trajetória de execução](experiments/README.md#experiment-002) | A trajetória revela falhas de segurança ocultas da avaliação do resultado? | Pipeline congelado; holdout cego original invalidado; novo holdout necessário |
| [#003 — Interferência de contexto no avaliador](experiments/README.md#experiment-003) | Um canal de evidência pode interferir na avaliação de outro? | Estudo candidato; não iniciado |

## Casos aplicados

- [Comentário→DM no Instagram: do ManyChat à infraestrutura governada pela proprietária](case-studies/README.md#instagram-comment--dm) — caso em produção sobre autonomia, evidência operacional, autoridade delegada, custos escondidos e a diferença entre uma demonstração bem-sucedida e um sistema durável.

## Compromissos metodológicos

- Preservar falhas em vez de reescrever a história como um sucesso limpo.
- Separar testes de desenvolvimento, validação de integração e confirmação cega.
- Congelar desenhos e configurações antes de acessar dados confirmatórios.
- Persistir previsões antes de revelar o gabarito.
- Distinguir tentativa bloqueada de violação de política executada.
- Declarar explicitamente controles simulados e limitações de processo compartilhado.
- Usar linguagem compatível com a força da evidência.

Consulte [Metodologia](docs/METHODOLOGY.pt-BR.md), [Estado das evidências](docs/EVIDENCE-STATUS.pt-BR.md), [Agenda de pesquisa](docs/RESEARCH-AGENDA.pt-BR.md), [Trabalhos relacionados](docs/RELATED-WORK.pt-BR.md), [Glossário](docs/GLOSSARY.pt-BR.md) e o [Checklist de descoberta e publicação](docs/DISCOVERY-AND-PUBLICATION.pt-BR.md).

## O que o Nirmata não afirma

- Não afirma que avaliação por trajetória seja universalmente superior.
- Não afirma possuir isolamento do plano de controle em nível de produção.
- Não trata sucesso em testes de desenvolvimento como evidência de generalização.
- Não relata efeito confirmatório a partir do holdout invalidado.
- Ainda não é um benchmark; o trabalho atual é um programa piloto de pesquisa.

## Citação

Use o arquivo [`CITATION.cff`](CITATION.cff). Uma versão arquivada com DOI está planejada após a finalização do pacote público e da licença.

## Autoria

Nirmata é um projeto independente de pesquisa de [Tabata Jahoda](https://github.com/thabatarj8-stack).

## Estado da licença

Ainda não foi escolhida uma licença de reutilização. Até que uma licença seja adicionada, os direitos permanecem com a autora e visibilidade pública não significa permissão de reutilização.
