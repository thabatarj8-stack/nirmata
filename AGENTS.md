# Agentes no repositório Nirmata

Este arquivo orienta o Cursor e outros agentes a continuar o trabalho da Tabata Jahoda sem ultrapassar a evidência publicada e sem publicar nada no lugar dela.

## Leia nesta ordem

1. [`.cursor/rules/nirmata-core.mdc`](.cursor/rules/nirmata-core.mdc): o que o Nirmata é, os limites do `v0.1.0` (DOI [10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451)), ficção rotulada, português sem travessão, e o que só a Tabata autoriza.
2. [`studio/PLANO.md`](studio/PLANO.md): onde o estúdio parou em 23/10/2026 e as etapas A a D.
3. [`studio/PROMPTS.md`](studio/PROMPTS.md): prompts prontos para colar.
4. Site: [`.cursor/rules/nirmata-website.mdc`](.cursor/rules/nirmata-website.mdc), mesmo que `mkdocs.yml` ainda não esteja neste branch.
5. Filme: [`.cursor/rules/nirmata-film.mdc`](.cursor/rules/nirmata-film.mdc).

O registro de evidência é [`docs/EVIDENCE-STATUS.md`](docs/EVIDENCE-STATUS.md). Não afirme além dele.

## Como a Tabata retoma

Ela abre este repositório, faz checkout deste branch ou o incorpora em `main`, e diz por exemplo: "continue a Etapa A". O agente lê o plano e o prompt dessa etapa, trabalha e para antes de merge, publicação, postagem, pagamento ou mudança de configuração.

A Etapa A mora no branch `cursor/nirmata-docs-site-00c6` (PR #20). Não misture o diff do site com o branch das regras e não faça o merge desse PR sem um sim explícito.

## Limites em uma página

- `v0.1.0` é piloto inicial. Não há resultado confirmatório cego.
- O primeiro holdout do Experimento 002 foi invalidado porque a chave de respostas entrou no contexto do avaliador.
- A baseline sintética não é pontuação de modelo.
- O Nirmata não detecta CVEs nem bugs de linguagem. Auditar não é prevenir.
- Ficção fica rotulada e separada de incidentes reais. A Dra. Lia é inventada.
- Texto em português não usa travessão.
- Não manipule senhas, tokens nem `.env`.

## Mídia

Quadros-chave e clipes não estão neste repositório. Ficam no computador da assistente, em `/workspace/nirmata_ep1/keyframes_v2/` e `/workspace/nirmata_ep1/clips/`. Não adicione binários.
