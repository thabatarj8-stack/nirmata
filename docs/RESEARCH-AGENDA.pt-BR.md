# Agenda de pesquisa

**Idioma:** [English](RESEARCH-AGENDA.md) · Português (Brasil)

## Programa atual

### RQ1 — Resultado final versus trajetória

Mantendo constante o julgamento do conteúdo, quanta informação adicional relevante para segurança um avaliador independente de trajetória fornece?

**Próximo passo válido:** construir um novo holdout cego, criado pela proprietária em um contexto que nunca tenha visto o gabarito. O holdout anterior não pode ser reutilizado para confirmação.

### RQ2 — Autoridade delegada e integridade de controle

Máquinas de estado de aprovação conseguem resistir a identidade forjada, injeção de aprovação, substituição de conteúdo, adulteração de fila, replay e confusão entre aprovação e autorização para publicar?

**Próximo passo válido:** mover controlador e publicador para um plano de controle confiável, com credenciais independentes e isolamento em nível de sistema operacional, e repetir os testes adversariais contra essa fronteira implantada.

### RQ3 — Interferência entre sinais

Quando um avaliador LLM recebe conjuntamente evidências de conteúdo e trajetória, um sinal limpo em um canal pode reduzir a detecção correta de um sinal inseguro no outro?

**Estado:** motivada por uma observação em teste de integração; não iniciada e não confirmada.

### RQ4 — Generalização entre sistemas agênticos

Um avaliador consciente da trajetória mantém discriminação útil em publicação de conteúdo, automação de navegador, mudanças de infraestrutura e operações com clientes?

**Próximo passo válido:** definir um schema mínimo compartilhado de trajetória e coletar casos pareados de sistemas independentes.

## Crescimento do dataset

1. Piloto: aproximadamente 12 trajetórias pareadas.
2. Piloto ampliado: 50 trajetórias em múltiplas classes de falha.
3. Estudo multissistema: mais de 100 trajetórias de agentes implementados independentemente.
4. Replicação externa: liberar um avaliador congelado e aceitar trajetórias de terceiros.

Holdouts inutilizados não devem reaparecer como evidência confirmatória durante esse crescimento.

## Caminho de publicação

1. Publicar método e protocolo.
2. Publicar dataset e avaliador versionados.
3. Criar snapshot arquivado com DOI via Zenodo ou equivalente.
4. Produzir artigo curto de método/preprint com limitações explícitas.
5. Buscar replicação externa e casos adversariais criados por revisores.
