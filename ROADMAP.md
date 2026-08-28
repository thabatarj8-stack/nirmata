# Nirmata roadmap

**Language:** English · [Português abaixo](#português)

The roadmap is ordered by evidentiary dependency, not by visibility. A DOI and a polished release are not useful if the archived package cannot be executed or audited.

## Phase 1 — Reproducibility foundation

- [x] Publish a minimal trajectory schema.
- [x] Publish synthetic calibration traces and expected classifications.
- [x] Provide deterministic validation, evaluation, scoring, manifests, and tests.
- [x] Run documentation and pipeline checks in continuous integration.
- [ ] Invite external review of the schema and process taxonomy.

## Phase 2 — Release candidate

- [x] Publish a sanitized applied-case package without production artifacts.
- [x] Review every public artifact for secrets, identifiers, client material, and holdout leakage ([audit](docs/PUBLICATION-AUDIT-2026-08-27.md)).
- [x] Add ORCID to citation and project metadata.
- [x] Freeze a `v0.1.0` release candidate and record artifact hashes ([release record](releases/v0.1.0/README.md)).
- [x] Connect GitHub to Zenodo and archive the release with a DOI ([10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451)).

## Phase 3 — Fresh blind pilot

- [ ] Pre-register the frozen protocol and primary metrics.
- [ ] Assign independent custody of new holdout labels.
- [ ] Persist and hash predictions before ground-truth release.
- [ ] Score without changing prompts, rubrics, thresholds, or cases.
- [ ] Publish positive, negative, partial, or invalidated outcomes.

## Phase 4 — External validity

- [ ] Add independently authored adversarial traces.
- [ ] Replicate on at least one separately implemented agentic system.
- [ ] Compare the taxonomy formally with adjacent benchmarks and assurance methods.
- [x] Prepare a methods note only after the public artifacts support it ([methods note v0.1](papers/nirmata-methods-note-v0.1.md)).

---

## Português

O roadmap segue a dependência entre evidências, não a visibilidade. Um DOI e uma release bem apresentada têm pouco valor se o pacote arquivado não puder ser executado ou auditado.

### Fase 1 — Base de reprodutibilidade

- [x] Publicar schema mínimo de trajetória.
- [x] Publicar trajetórias sintéticas de calibração e classificações esperadas.
- [x] Fornecer validação, avaliação, pontuação, manifestos e testes determinísticos.
- [x] Executar verificações da documentação e do pipeline em integração contínua.
- [ ] Convidar revisão externa do schema e da taxonomia de processo.

### Fase 2 — Candidata a release

- [x] Publicar um pacote sanitizado de caso aplicado sem artefatos de produção.
- [x] Revisar todos os artefatos públicos em busca de segredos, identificadores, material de clientes e vazamento de holdout ([auditoria](docs/PUBLICATION-AUDIT-2026-08-27.md)).
- [x] Adicionar ORCID aos metadados de citação e do projeto.
- [x] Congelar uma candidata `v0.1.0` e registrar hashes dos artefatos ([registro da release](releases/v0.1.0/README.md)).
- [x] Conectar GitHub ao Zenodo e arquivar a release com DOI ([10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451)).

### Fase 3 — Novo piloto cego

- [ ] Pré-registrar protocolo congelado e métricas primárias.
- [ ] Atribuir custódia independente dos novos rótulos de holdout.
- [ ] Persistir e registrar hashes das previsões antes de liberar o gabarito.
- [ ] Pontuar sem alterar prompts, rubricas, limiares ou casos.
- [ ] Publicar resultados positivos, negativos, parciais ou invalidados.

### Fase 4 — Validade externa

- [ ] Adicionar trajetórias adversariais escritas de forma independente.
- [ ] Replicar em pelo menos um sistema agêntico implementado separadamente.
- [ ] Comparar formalmente a taxonomia com benchmarks e métodos de garantia próximos.
- [x] Preparar uma nota de método somente quando os artefatos públicos a sustentarem ([nota de método v0.1](papers/nirmata-methods-note-v0.1.pt-BR.md)).
