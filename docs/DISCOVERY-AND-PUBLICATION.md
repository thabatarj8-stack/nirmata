# Discovery and publication checklist

**Language:** English · [Português (Brasil)](DISCOVERY-AND-PUBLICATION.pt-BR.md)

## GitHub metadata

### Suggested repository description

> Independent research on trajectory-aware AI-agent evaluation, delegated authority, control integrity, and failure-preserving reproducibility.

### Suggested topics

`ai-agents`, `agent-evaluation`, `agent-trajectories`, `agentic-ai`, `ai-safety`, `ai-governance`, `delegated-authority`, `human-in-the-loop`, `tool-use`, `control-integrity`, `reproducible-research`, `llm-evaluation`

## Publication gates

- [x] Select licenses for code, documentation, and future datasets.
- [x] Confirm which source experiment artifacts may be public ([publication audit](PUBLICATION-AUDIT-2026-08-27.md)).
- [x] Sanitize production identifiers, personal data, client material, tokens, and private holdout data.
- [x] Publish `thabatarj8-stack/nirmata` as a public repository.
- [ ] Add repository description, topics, and social preview image.
- [x] Create the public profile repository `thabatarj8-stack/thabatarj8-stack`.
- [x] Publish a synthetic, executable integration fixture with explicit claim boundaries.
- [x] Add automated checks for documentation and the reproducibility pipeline.
- [ ] Pin Nirmata and its strongest applied case to the GitHub profile.
- [x] Add the author's ORCID to citation and project metadata.
- [x] Enable GitHub–Zenodo archiving and issue a versioned release/DOI ([10.5281/zenodo.22132451](https://doi.org/10.5281/zenodo.22132451)).
- [ ] Register future confirmatory protocols in an external timestamped service before execution.
- [x] Publish a methods note or preprint linking the DOI-backed release ([methods note v0.1](../papers/nirmata-methods-note-v0.1.md)).

## Search and AI-discovery questions

The repository should answer these phrases directly and factually:

- How can AI agents be evaluated from execution trajectories?
- What does final-output evaluation miss in tool-using agents?
- How should delegated authority and human approval be represented in AI agents?
- How can blocked attempts be distinguished from executed policy violations?
- How should invalidated holdouts and failed agent evaluations be reported?

## Authority-building path

1. Canonical repository with clear scope and limitations.
2. Public versioned artifacts and a citable DOI.
3. Short methods paper or preprint.
4. External review of the taxonomy and holdout design.
5. Independent replication on another agentic system.
6. Third-party references from research communities, workshops, and practitioner reports.

Repository metadata helps discovery, but external citations and independent replication are the stronger research signals.
