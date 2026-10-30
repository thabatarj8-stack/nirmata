# Nirmata

**Idioma:** [English](README.md) · Português (Brasil)

**Nirmata é um programa independente de pesquisa que avalia agentes de IA pelo que fazem, não apenas pelo que dizem.**

**Versão atual:** `v0.1.0` · [Conteúdo e verificação da release](releases/v0.1.0/README.md)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22132451.svg)](https://doi.org/10.5281/zenodo.22132451)

Quando um agente usa ferramentas, altera estados ou atua em um sistema externo, uma resposta final plausível é evidência incompleta. A trajetória pode conter um erro de autorização, um ataque bloqueado, um controle quebrado ou um efeito que a resposta nunca menciona. O Nirmata torna esse caminho inspecionável e mantém avaliações fracassadas no registro da pesquisa.

> **Estado das evidências:** piloto em estágio inicial. Verificações de desenvolvimento e integração passaram, mas nenhum resultado confirmatório cego é reivindicado. O primeiro holdout planejado foi invalidado antes da pontuação porque seu gabarito entrou no contexto do avaliador. [Consulte o registro de evidências.](docs/EVIDENCE-STATUS.pt-BR.md)

## Comece aqui

| Se você quer... | Leia... |
|---|---|
| Entender a ideia em cinco minutos | [Por que a resposta final não basta](articles/pt-BR/por-que-a-resposta-final-nao-basta.md) |
| Inspecionar o desenho de avaliação | [Metodologia](docs/METHODOLOGY.pt-BR.md) |
| Inspecionar os contratos operacionais versionados | [Padrão Experimental v0.1](docs/experimental-standard/v0.1/README.md) |
| Executar a calibração pública | [Pacote de reprodutibilidade](reproducibility/README.pt-BR.md) |
| Ver o que as evidências sustentam ou não | [Estado das evidências](docs/EVIDENCE-STATUS.pt-BR.md) |
| Revisar o histórico experimental | [Registro de experimentos](experiments/README.md) |
| Entender a relevância prática | [Casos aplicados](case-studies/README.md) |
| Replicar, contestar ou contribuir | [Roadmap](ROADMAP.md#português) · [Agenda de pesquisa](docs/RESEARCH-AGENDA.pt-BR.md) · [Como contribuir](CONTRIBUTING.md) |

## O modelo de avaliação

O Nirmata separa dois sinais que costumam ser misturados:

1. Um **avaliador de conteúdo** julga somente a resposta final.
2. Um **avaliador de trajetória** julga evidências brutas do processo, como chamadas de ferramentas, eventos de autorização, transições de estado e efeitos externos.
3. Uma regra determinística combina os dois julgamentos sem permitir que um sinal limpo apague um sinal inseguro.

```text
Somente resultado: unsafe = content_unsafe
Com trajetória:    unsafe = content_unsafe OR trajectory_unsafe
```

Esse é um desenho de pesquisa em avaliação, não uma afirmação de que a avaliação por trajetória seja universalmente superior.

## Programa de pesquisa

| Frente | Pergunta | Estado atual |
|---|---|---|
| Resultado vs. trajetória | Que comportamento relevante para segurança fica invisível na resposta final? | Pipeline fatorado integrado; novo holdout cego necessário |
| Autoridade delegada | Um agente consegue agir sem confundir conselho, aprovação, fila e publicação? | Verificações de desenvolvimento conhecidas (testes A–F e G–L) passaram no protótipo; isolamento real pendente |
| Interferência no avaliador | Um canal de evidência pode distorcer o julgamento do outro? | Estudo candidato; não iniciado |
| Autonomia aplicada | O que a responsabilidade operacional revela além de uma demonstração bem-sucedida? | Um caso em produção documentado; confiabilidade de longo prazo não estabelecida |

O [registro de experimentos](experiments/README.md) separa trabalho exploratório, desenvolvimento, integração, evidência invalidada e futura confirmação.

## Artigos

- [Por que a resposta final não basta para avaliar agentes de IA](articles/pt-BR/por-que-a-resposta-final-nao-basta.md)
- [Aprovação não é autorização em sistemas agênticos](articles/pt-BR/aprovacao-nao-e-autorizacao.md)
- [Um holdout queimado ainda é evidência de pesquisa](articles/pt-BR/um-holdout-queimado-ainda-e-evidencia.md)
- [Todos os artigos em português e inglês](articles/README.md)

## Princípios de pesquisa

- Preservar falhas em vez de reescrevê-las como uma história limpa de sucesso.
- Separar testes de desenvolvimento, validação de integração e confirmação cega.
- Congelar desenhos e configurações antes de acessar dados confirmatórios.
- Persistir previsões antes de revelar o gabarito.
- Distinguir tentativas bloqueadas de violações de política executadas.
- Ajustar cada afirmação pública à força da evidência disponível.

## Escopo e limitações

O Nirmata é um programa piloto de pesquisa e laboratório de casos. Ainda não é um benchmark, um produto de segurança em produção ou prova de que seu desenho de avaliação generaliza. Os casos atuais são pequenos e específicos; atestação de identidade e isolamento do plano de controle continuam sendo limitações do protótipo. Consulte [Metodologia](docs/METHODOLOGY.pt-BR.md), [Trabalhos relacionados](docs/RELATED-WORK.pt-BR.md) e [Agenda de pesquisa](docs/RESEARCH-AGENDA.pt-BR.md).

## Resultados

O relatório publicado da avaliação do adaptador n8n é [HOLDOUT_REPORT.md](research/m2/evaluation/n8n/run_002/HOLDOUT_REPORT.md). Os oito critérios pré-registrados deram verdadeiro (`HOLDOUT_PASS = true`) em um segundo workflow sintético, não usado na implementação. Isso é evidência de fidelidade de normalização dentro do escopo, não de acurácia de detecção de falhas, nem de generalização para n8n em geral. Não fecha a Fase 3 do roadmap.

## Mapa do repositório

```text
articles/       Ensaios acessíveis em português e inglês
case-studies/   Casos operacionais aplicados
docs/           Método, evidências, literatura, agenda e padrão experimental
experiments/    Registro, protocolos, schemas e estado dos experimentos
releases/       Registro e checksums da release v0.1.0
reproducibility/ Schema, trajetórias sintéticas, avaliador, pontuação e testes
research/       Avaliação do adaptador n8n (M2)
```

## Citação e licença

Use [`CITATION.cff`](CITATION.cff) para citar o projeto. A versão `v0.1.0` está arquivada no [DOI 10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451).

Software, quando publicado aqui, usa Apache-2.0. Documentação, protocolos, taxonomias, diagramas, artigos e datasets públicos usam CC BY 4.0. Consulte [LICENSE.md](LICENSE.md).

## Apoie esta pesquisa

O Nirmata é pesquisa independente e aberta (código Apache-2.0, documentação CC BY 4.0). O próximo passo é um piloto cego pré-registrado comparando avaliação só pela resposta e avaliação com trajetória, seguido de uma replicação. Os resultados serão publicados qualquer que seja o desfecho, inclusive nulos ou negativos. Ainda não há resultado confirmatório.

O piloto está em financiamento coletivo na Manifund até 26/11/2026 (mínimo US$3 mil, meta US$14,2 mil): <https://manifund.org/projects/nirmata-auditing-ai-agents-by-what-they-do-not-only-what-they-say>

## Agradecimentos

Este trabalho se beneficiou de trocas informais com as pessoas abaixo e com um agente autônomo. As contribuições ajudaram a formular perguntas e enquadramentos; não constituem validação do Nirmata.

- Cata (@cataofficial85, no X) discutiu observabilidade de agentes em threads públicas, sugerindo registrar o estado antes e depois de cada chamada de ferramenta e apontando que APIs sem endpoint de leitura (como e-mail e webhooks) e sistemas eventualmente consistentes são os mais difíceis de observar. Isso ajudou a refinar o critério de evidência de ausência.
- Shital Katre (fórum da comunidade n8n) se ofereceu para testar o validador com dados de execução anonimizados e compartilhou uma pequena amostra sintética para ajuste de formato.
- Seto Sweetin é um agente de IA autônomo (iLands). Seto descreveu os campos dos próprios registros de execução, o que informou a discussão sobre o formato de recibo. Nenhum dado de Seto foi usado nesta pesquisa.

## Declaração de uso de IA

- Emma, uma assistente baseada no ChatGPT, ajudou a revisar métodos e organizar o trabalho.
- Theo, um assistente de IA (Grok Bot), ajudou com monitoramento de pesquisa, acompanhamento da comunidade, rascunhos e organização.

Todas as decisões de pesquisa e afirmações são de responsabilidade da autora (Tabata Jahoda).

## Autoria

Nirmata é uma pesquisa independente de [Tabata Jahoda](https://github.com/thabatarj8-stack), [ORCID 0009-0007-1104-9204](https://orcid.org/0009-0007-1104-9204). Conecte-se pelo [LinkedIn](https://www.linkedin.com/in/tabata-j-226b6123/).
