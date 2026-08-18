# Related work and positioning

**Language:** English · [Português (Brasil)](RELATED-WORK.pt-BR.md)

Nirmata sits within a growing research area on tool-using agents, execution-time safety, trajectory monitoring, and delegated autonomy. This page maps conceptual proximity; it does not claim priority or equivalence.

## Closely related research

- **ToolEmu** introduces an LM-emulated sandbox for scalable identification of risks in tool-using language-model agents. Nirmata shares its interest in risks that arise during tool execution, but currently focuses on small, auditable trajectories and authority transitions rather than broad scenario generation. [Ruan et al., ICLR 2024](https://openreview.net/forum?id=GEcwtMk1uA)
- **AgentDojo** evaluates prompt-injection attacks and defenses for agents operating over untrusted tool data. Nirmata's approval-injection and control-integrity cases are adjacent to this threat model, but Nirmata is not currently a competitive prompt-injection benchmark. [Debenedetti et al., NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html)
- **Monitoring LLM Agents for Sequentially Contextual Harm** studies harms that become visible only across sequences of individually plausible actions. Nirmata similarly treats sequences and external effects as first-class evidence, with additional emphasis on owner authorization and publication-state transitions. [Korbak et al., OpenReview](https://openreview.net/forum?id=PGsM81SWHt)
- **TraceSafe** evaluates guardrails over multi-step tool-calling trajectories. Its benchmark-scale trajectory focus is directly relevant to Nirmata's pilot question; Nirmata's current contribution is a failure-preserving protocol and factorized evaluation design, not comparable benchmark coverage. [Chen et al., arXiv 2026](https://arxiv.org/abs/2604.07223)
- **ATBench** proposes a long-horizon agent-safety benchmark organized by risk source, failure mode, and real-world harm. Nirmata should use it as a comparison point when expanding its taxonomy and dataset beyond a pilot. [Li et al., arXiv 2026](https://arxiv.org/abs/2604.02022)
- **Specifying the Delegated-Autonomy Boundary** frames authority, oversight, and return of control as requirements-level commitments. This is strongly aligned with Nirmata's distinction between content approval, queueing, publication authorization, and external effects. [Arora, Vogelsang, and Sharma, arXiv 2026](https://arxiv.org/abs/2607.17225)

## Current positioning

Nirmata is best described as an **independent pilot research program and reproducible case laboratory**, not as a mature benchmark or a validated safety product. Its distinctive emphasis is the combination of:

1. final-output and trajectory evidence;
2. explicit delegated-authority state transitions;
3. preservation of failed evaluations and invalidated evidence;
4. movement between controlled experiments and real applied systems.

Whether that combination constitutes a novel research contribution remains a question for a formal literature review and external peer assessment.

## Literature-review gaps

- Formal comparison with process supervision and process-reward modeling.
- Human-computer interaction research on consent, approval, and automation boundaries.
- Safety-case and assurance-case methods from safety-critical systems.
- Provenance and event-schema standards for agent traces.
- Statistical design for small matched-trajectory pilots.

This page should be expanded before any paper claims novelty.
