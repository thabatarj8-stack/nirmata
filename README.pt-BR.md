# Nirmata

**Idioma:** [English](README.md) · Português (Brasil)

**Nirmata é um programa independente de pesquisa que avalia agentes de IA pelo que fazem — não apenas pelo que dizem.**

Quando um agente usa ferramentas, altera estados ou atua em um sistema externo, uma resposta final plausível é evidência incompleta. A trajetória pode conter um erro de autorização, um ataque bloqueado, um controle quebrado ou um efeito que a resposta nunca menciona. O Nirmata torna esse caminho inspecionável e mantém avaliações fracassadas no registro da pesquisa.

> **Estado das evidências:** piloto em estágio inicial. Verificações de desenvolvimento e integração passaram, mas nenhum resultado confirmatório cego é reivindicado. O primeiro holdout planejado foi invalidado antes da pontuação porque seu gabarito entrou no contexto do avaliador. [Consulte o registro de evidências.](docs/EVIDENCE-STATUS.pt-BR.md)

## Comece aqui

| Se você quer... | Leia... |
|---|---|
| Entender a ideia em cinco minutos | [Por que a resposta final não basta](articles/pt-BR/por-que-a-resposta-final-nao-basta.md) |
| Inspecionar o desenho de avaliação | [Metodologia](docs/METHODOLOGY.pt-BR.md) |
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
| Autoridade delegada | Um agente consegue agir sem confundir conselho, aprovação, fila e publicação? | 12 verificações conhecidas passaram; isolamento real pendente |
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

## Mapa do repositório

```text
articles/       Ensaios acessíveis em português e inglês
case-studies/   Casos operacionais aplicados
docs/           Método, evidências, literatura e agenda
experiments/    Registro e estado dos experimentos
reproducibility/ Schema, trajetórias sintéticas, avaliador, pontuação e testes
```

## Citação e licença

Use [`CITATION.cff`](CITATION.cff) para citar o projeto. Uma versão arquivada com DOI está planejada após a preparação do pacote público de pesquisa.

Software, quando publicado aqui, usa Apache-2.0. Documentação, protocolos, taxonomias, diagramas, artigos e datasets públicos usam CC BY 4.0. Consulte [LICENSE.md](LICENSE.md).

## Autoria

Nirmata é uma pesquisa independente de [Tabata Jahoda](https://github.com/thabatarj8-stack). Conecte-se pelo [LinkedIn](https://www.linkedin.com/in/tabata-j-226b6123/).
