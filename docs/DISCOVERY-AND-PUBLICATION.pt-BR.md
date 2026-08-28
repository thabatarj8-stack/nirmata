# Checklist de descoberta e publicação

**Idioma:** [English](DISCOVERY-AND-PUBLICATION.md) · Português (Brasil)

## Metadados do GitHub

### Descrição sugerida para o repositório

> Pesquisa independente sobre avaliação de agentes de IA por trajetória, autoridade delegada, integridade de controle e reprodutibilidade que preserva falhas.

### Tópicos sugeridos

`ai-agents`, `agent-evaluation`, `agent-trajectories`, `agentic-ai`, `ai-safety`, `ai-governance`, `delegated-authority`, `human-in-the-loop`, `tool-use`, `control-integrity`, `reproducible-research`, `llm-evaluation`

## Portões de publicação

- [x] Escolher licenças para código, documentação e futuros datasets.
- [x] Confirmar quais artefatos-fonte dos experimentos podem ser públicos ([auditoria de publicação](PUBLICATION-AUDIT-2026-08-27.md)).
- [x] Sanitizar identificadores de produção, dados pessoais, material de clientes, tokens e dados privados de holdout.
- [x] Publicar `thabatarj8-stack/nirmata` como repositório público.
- [ ] Adicionar descrição, tópicos e imagem de compartilhamento.
- [x] Criar o repositório público de perfil `thabatarj8-stack/thabatarj8-stack`.
- [x] Publicar uma fixture sintética e executável de integração com limites explícitos das afirmações.
- [x] Adicionar verificações automatizadas da documentação e do pipeline de reprodutibilidade.
- [ ] Fixar Nirmata e seu caso aplicado mais forte no perfil do GitHub.
- [x] Adicionar o ORCID da autora aos metadados de citação e do projeto.
- [x] Ativar integração GitHub–Zenodo e emitir uma release versionada com DOI ([10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451)).
- [ ] Registrar futuros protocolos confirmatórios em serviço externo com timestamp antes da execução.
- [x] Publicar nota de método ou preprint ligado à versão com DOI ([nota de método v0.1](../papers/nirmata-methods-note-v0.1.pt-BR.md)).

## Perguntas para descoberta em buscas e IA

O repositório deve responder de forma direta e factual:

- Como avaliar agentes de IA por trajetórias de execução?
- O que a avaliação somente do resultado final não percebe em agentes que usam ferramentas?
- Como representar autoridade delegada e aprovação humana em agentes de IA?
- Como distinguir tentativas bloqueadas de violações de política executadas?
- Como relatar holdouts invalidados e avaliações falhas de agentes?

## Caminho para autoridade científica

1. Repositório canônico com escopo e limitações claros.
2. Artefatos públicos versionados e DOI citável.
3. Artigo curto de método ou preprint.
4. Revisão externa da taxonomia e do desenho do holdout.
5. Replicação independente em outro sistema agêntico.
6. Referências de terceiros em comunidades, workshops e relatórios técnicos.

Metadados ajudam na descoberta, mas citações externas e replicação independente são sinais científicos mais fortes.
