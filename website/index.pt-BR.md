---
description: O Nirmata audita agentes de IA pelo que fazem, não apenas pelo que dizem. A v0.1.0 é um piloto inicial, sem resultado confirmatório cego.
---

# Nirmata

**Versão `v0.1.0`** · [DOI 10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451) · [ORCID 0009-0007-1104-9204](https://orcid.org/0009-0007-1104-9204)

> O Nirmata é um programa independente de pesquisa que avalia agentes de IA pelo que fazem, não apenas pelo que dizem.
{: .thesis }

Pesquisa independente de [Tabata Jahoda](https://github.com/thabatarj8-stack). Quando um agente usa ferramentas, altera estados ou atua em um sistema externo, uma resposta final plausível é evidência incompleta. A trajetória pode conter um erro de autorização, um ataque bloqueado, um controle quebrado ou um efeito que a resposta nunca menciona.

!!! evidence "Estado das evidências do pacote v0.1.0"

    Piloto em estágio inicial. Verificações de desenvolvimento e integração passaram. **Nenhum resultado confirmatório cego é reivindicado** para esse pacote. O primeiro holdout planejado do Experimento 002 foi invalidado antes da pontuação porque o gabarito entrou no contexto do avaliador.

    Nenhum registro do pacote atual é classificado como confirmatório. [Abrir o registro de evidências](docs/EVIDENCE-STATUS.md).

## O que este projeto não afirma {: .boundary-title }

- **A v0.1.0 é um piloto inicial.** Ela não traz um resultado confirmatório cego.
- **O primeiro holdout do Experimento 002 foi invalidado por vazamento do gabarito.** O gabarito entrou no contexto do avaliador antes da pontuação. Essa execução não sustenta alegação de desempenho cego.
- **O baseline de reprodutibilidade é determinístico e sintético.** Não é uma pontuação de modelo e não é evidência confirmatória.
- **O Nirmata não detecta CVEs nem bugs de linguagem.**

O baseline executável público em `reproducibility/` usa marcadores sintéticos visíveis. Ele verifica o funcionamento do pipeline. O [início rápido de reprodutibilidade](reproducibility-quickstart.md) repete esse limite ao lado dos comandos.

## Como a auditoria é fatorada

O Nirmata separa fatos que costumam ser misturados. O texto abaixo segue o README do repositório.

- Recomendação, opinião de revisor, estado de fila ou aprovação anterior não são autorização da proprietária. A autorização fica registrada à parte da ação pedida.
- Tentativa não é efeito. Um pedido não autorizado e bloqueado (`UNAUTHORIZED_ATTEMPT_BLOCKED`) não é o mesmo evento que uma violação de política executada ou um efeito externo danoso.
- Dois avaliadores permanecem independentes. Um **avaliador de conteúdo** vê só a resposta final. Um **avaliador de trajetória** vê só evidência de processo. Uma regra determinística combina os dois. Um sinal limpo em um canal não pode apagar um sinal inseguro no outro.

```text
unsafe = content_unsafe OR trajectory_unsafe
```

Esse desenho não afirma que a avaliação por trajetória seja universalmente superior. A Fase 2 do [roadmap](ROADMAP.md) está marcada, incluindo o DOI. A Fase 1 ainda tem aberta a revisão externa do schema e da taxonomia de processo. A Fase 3 (novo piloto cego) e a Fase 4 (validade externa) estão abertas.

<div class="grid cards" markdown>

- [**Estado das evidências**](docs/EVIDENCE-STATUS.md)

  O que cada registro sustenta, e a extrapolação que ele não sustenta.

- [**Roadmap**](ROADMAP.md)

  Quatro fases ordenadas pela dependência entre evidências.

- [**Início rápido de reprodutibilidade**](reproducibility-quickstart.md)

  Baseline determinístico e sintético. Não é pontuação de modelo.

- [**Por que a resposta final não basta**](articles/pt-BR/por-que-a-resposta-final-nao-basta.md)

  O ensaio curto. As afirmações permanecem dentro do registro de evidências.

</div>

## Como citar

A versão `v0.1.0` está arquivada em [doi:10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451). O DOI conceitual de todas as versões do Nirmata é `10.5281/zenodo.22132450`.

> Jahoda, Tabata. *Nirmata: Trajectory-Aware Evaluation and Delegated Authority for AI Agents*. Version 0.1.0. [10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451)

Os metadados legíveis por máquina estão em [`CITATION.cff`](CITATION.cff). ORCID: [0009-0007-1104-9204](https://orcid.org/0009-0007-1104-9204).

O código usa Apache-2.0. Documentação, protocolos, taxonomias, diagramas, artigos e datasets públicos usam CC BY 4.0.

## Um resultado publicado, e o limite dele

A avaliação publicada do adaptador n8n está em [HOLDOUT_REPORT.md](research/m2/evaluation/n8n/run_002/HOLDOUT_REPORT.md). `HOLDOUT_PASS = true` em oito critérios pré-registrados. O relatório trata o passe como tudo ou nada, e os oito critérios são verdadeiros. A conclusão permitida é:

> n8n Adapter v0.1.0 demonstrated within-scope holdout generalization on a second preregistered synthetic n8n workflow that was not used for adapter implementation.

O relatório não afirma que o adaptador generaliza para o n8n, que está pronto para produção, que cobre workflows arbitrários do n8n, ou que o Nirmata está validado entre orquestradores. Esse resultado não encerra a Fase 3. O registro de evidências do pacote `v0.1.0` continua sem resultado confirmatório, inclusive o primeiro holdout invalidado do Experimento 002.

## Apoie esta pesquisa

O Nirmata é pesquisa independente e aberta (Apache-2.0). O próximo passo é um piloto cego pré-registrado que compara avaliação só da saída e avaliação com trajetória, seguido de uma replicação. Os resultados serão publicados qualquer que seja o desfecho, inclusive resultados nulos ou negativos.

Ainda não há resultado confirmatório. A release atual traz o schema, os protocolos e uma fixture reprodutível de 6 trajetórias com testes.

O piloto está em financiamento coletivo no Manifund até 26 nov 2026 (mínimo de US$ 3 mil, meta de US$ 14.2 mil): [manifund.org/projects/nirmata-auditing-ai-agents-by-what-they-do-not-only-what-they-say](https://manifund.org/projects/nirmata-auditing-ai-agents-by-what-they-do-not-only-what-they-say).
