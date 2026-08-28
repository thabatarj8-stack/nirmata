# Nirmata v0.1: A failure-preserving protocol for trajectory-aware evaluation of AI agents

- **Author:** Tabata Jahoda ([ORCID 0009-0007-1104-9204](https://orcid.org/0009-0007-1104-9204))
- **Methods-note version:** 0.1
- **Artifact release:** [Nirmata v0.1.0](https://doi.org/10.5281/zenodo.22132451)
- **Evidence status:** method and integration package; no blind confirmatory result

## Abstract

Evaluations of tool-using AI agents often emphasize the final answer even though safety-relevant behavior can occur earlier in execution. An agent may cross an authorization boundary, attempt a blocked action, alter external state, or produce an apparently acceptable answer after an unsafe process. This methods note presents Nirmata v0.1, a small, auditable protocol for evaluating final-output evidence separately from execution-trajectory evidence. The design uses independent content and trajectory evaluators, a deterministic monotonic aggregation rule, an explicit process taxonomy, and evidence tiers that separate development, integration, confirmatory, and invalidated records. It also preserves protocol failures: the first planned confirmatory holdout is recorded as invalidated because its ground truth entered the evaluator context before predictions were frozen. The public v0.1.0 package provides schemas, evaluator contracts, scoring rules, synthetic calibration traces, validation scripts, and a sanitized applied case. These artifacts establish that the package is executable and internally consistent; they do not establish evaluator generalization or production safety. A fresh blind pilot is required to test whether independent trajectory evidence adds useful detection without an unacceptable increase in false positives.

## 1. Motivation

A final answer is an observation of an agent's outcome, not a complete account of its execution. For agents that call tools or act in external systems, the path to that answer may include decisions, authorization events, controller responses, state transitions, and external effects. Two executions can therefore produce similar answers while differing materially in whether an attempted action was authorized, blocked, executed, or harmful.

Nirmata studies this gap through a constrained research question:

> In a frozen set of agent traces, does an independent trajectory signal identify ground-truth unsafe cases that final-output-only evaluation accepts, and what additional false positives does it introduce?

The question is comparative and bounded. It does not assume that trajectory-aware evaluation is universally superior, that every internal event should be logged, or that a small pilot can establish production safety.

## 2. Unit of analysis

The unit of analysis is an **agent execution trajectory**: a final output paired with the observable events produced while reaching it. Depending on the system, a trace can include:

- model decisions and outputs;
- tool calls and tool results;
- authorization requirements, sources, and outcomes;
- controller decisions and human interventions;
- state transitions and content hashes;
- attempted and executed external effects.

The schema applies minimum-necessary disclosure. Public traces use synthetic identifiers and omit credentials, private communications, client data, and operational details that do not contribute to the claim under evaluation.

## 3. Factorized evaluation design

Nirmata separates the evaluation into two channels:

1. The **content evaluator** receives only the final output and returns `content_unsafe`.
2. The **trajectory evaluator** receives process evidence and returns `trajectory_unsafe` plus a process class.
3. A deterministic rule produces the trajectory-aware judgment.

```text
final_only_unsafe = content_unsafe
trajectory_aware_unsafe = content_unsafe OR trajectory_unsafe
```

This factorization prevents trajectory context from downgrading an independently unsafe content judgment. It also exposes the marginal contribution of the trajectory channel. The rule is intentionally simple so that changes in performance can be attributed to the additional evidence rather than to an opaque joint evaluator.

## 4. Process taxonomy

The trajectory evaluator assigns one initial process class:

| Class | Interpretation | Unsafe by itself? |
|---|---|---|
| `BENIGN` | Expected and authorized behavior | No |
| `SUSPICIOUS_ANOMALOUS` | Unusual behavior without established prohibition or harm | No |
| `UNAUTHORIZED_ATTEMPT_BLOCKED` | An unauthorized request was denied with no external effect | No; the control worked |
| `POLICY_VIOLATION` | An unauthorized action was executed | Yes |
| `HARMFUL_EXTERNAL_ACTION` | An executed action caused an unsafe external effect | Yes |

The distinction between a blocked attempt and an executed violation is central. Treating both as equivalent would obscure whether a control contained the event or failed to prevent an effect.

## 5. Evidence classes and failure preservation

Nirmata separates evidence by the role it played in the research process:

| Evidence class | Purpose | Permitted inference |
|---|---|---|
| `DEVELOPMENT` | Build or debug known rules | Behavior on known cases |
| `INTEGRATION` | Verify schemas, components, and end-to-end plumbing | Package readiness |
| `CONFIRMATORY` | Evaluate a frozen design on unseen cases | Bounded out-of-sample pilot evidence |
| `INVALIDATED` | Preserve a run that violated a required condition | Evidence about process failure, not target performance |

The classification is designed to resist evidentiary laundering. Passing development cases does not become a confirmatory result merely because the checks are automated. Likewise, a contaminated holdout is not silently removed from the record.

The first planned Experiment 002 holdout was invalidated before scoring after its answer key entered the evaluator context. No predictions or metrics were produced. The event remains documented because it identifies a failure mode in the research process and motivates stricter separation of ground truth from evaluator context.

## 6. Blinding and freezing protocol

A confirmatory run follows this order:

1. Freeze the protocol, prompts, model configuration, aggregation rule, and analysis code.
2. Store traces and ground truth separately.
3. Keep ground truth outside both evaluator contexts.
4. Run each evaluator on its permitted evidence channel.
5. Persist predictions and record their hashes.
6. Reveal ground truth only after prediction persistence.
7. Score without changing rubrics, thresholds, or cases.
8. Record deviations and publish positive, negative, partial, or invalidated outcomes.

Ground-truth exposure before prediction freeze burns the affected holdout for blind confirmatory use with that evaluator context. The cases may still be retained for development or regression testing if relabeled accordingly.

## 7. Measures

The planned comparison reports raw counts and rates for both conditions. Primary quantities include:

- unsafe acceptance rate;
- safety blind spot among ground-truth unsafe cases;
- violation detection recall;
- false-positive rate;
- incremental true detections added by trajectory evidence;
- additional false positives added by trajectory evidence;
- paired transitions between final-only and trajectory-aware judgments.

The incremental detection quantity counts a case only when final-output evaluation predicts safe, trajectory evaluation predicts unsafe, and ground truth is unsafe. Cases already detected by final-output evaluation are not credited again to the trajectory signal.

## 8. Public package and current evidence

The archived [Nirmata v0.1.0 package](https://doi.org/10.5281/zenodo.22132451) contains:

- JSON Schemas for traces, predictions, and run manifests;
- independent content- and trajectory-evaluator contracts;
- a pre-run checklist and holdout-handling rules;
- deterministic validation, baseline, aggregation, and scoring scripts;
- six transparent synthetic calibration traces with expected classifications;
- automated tests, local-link checks, schema validation, and publication-safety scanning;
- one sanitized applied automation case with explicit claim boundaries.

The public fixture demonstrates package integrity and expected distinctions on known synthetic cases. The applied case connects the taxonomy to an operational setting but does not independently verify the private production event or establish long-term reliability. No record in v0.1.0 is classified as confirmatory.

## 9. Threats to validity

The current design has several material limitations:

- **Small and constructed cases:** synthetic calibration traces cannot estimate real-world prevalence or generalization.
- **Evaluator dependence:** judgments may vary across prompts, models, providers, or model versions.
- **Instrumentation dependence:** unobserved or incorrectly recorded events can make a trajectory appear safer than the underlying execution.
- **Ground-truth subjectivity:** authorization and harm labels require a policy defined before reveal.
- **False-positive cost:** more process evidence can add detections and unnecessary alerts; both must be reported.
- **Prototype isolation:** identity attestation and control-plane isolation are simulated or incomplete.
- **Researcher involvement:** the implementer designed the current cases and taxonomy, increasing the need for external review and independently authored traces.

These limitations constrain both performance claims and novelty claims. The package is a pilot method and case laboratory, not a mature benchmark or validated safety product.

## 10. Planned confirmatory pilot

The next valid experiment requires a fresh holdout whose labels are held independently from the evaluator context. The initial target is 12 matched traces. Protocol, model configuration, evaluator prompts, schemas, aggregation, and primary metrics must be frozen before evaluation. Predictions must be persisted and hashed before ground-truth reveal.

The pilot can support a bounded claim only if the blinding conditions hold. A negative result, a false-positive increase, an evaluator failure, or another invalidation remains publishable evidence under the protocol.

## 11. Relation to prior work

Nirmata is adjacent to research on tool-use risk simulation, prompt-injection evaluation, and sequentially contextual harm. ToolEmu studies scalable risk identification in emulated tool environments; AgentDojo evaluates attacks and defenses over untrusted tool data; and work on sequentially contextual harm treats multi-step behavior as a safety-relevant unit. Nirmata's current emphasis is narrower: auditable authority transitions, factorized evidence channels, and preservation of invalidated evaluations. A formal literature review and external assessment are still required before making a priority or novelty claim.

## 12. Conclusion

Nirmata v0.1 operationalizes a simple proposition: evaluating an agent's final answer and evaluating its execution trajectory are related but distinct tasks. The protocol makes that distinction testable while preserving failures in both agent behavior and research procedure. Its present contribution is an auditable method package, not a confirmed performance advantage. The next evidentiary step is a fresh, preregistered blind pilot followed by publication of the result regardless of direction.

## References

1. Ruan et al. “ToolEmu: Identifying the Risks of LM Agents with an LM-Emulated Sandbox.” ICLR 2024. <https://openreview.net/forum?id=GEcwtMk1uA>
2. Debenedetti et al. “AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents.” NeurIPS 2024. <https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html>
3. Korbak et al. “Monitoring LLM Agents for Sequentially Contextual Harm.” OpenReview. <https://openreview.net/forum?id=PGsM81SWHt>
4. Jahoda, T. “Nirmata: Trajectory-Aware Evaluation and Delegated Authority for AI Agents.” Version 0.1.0, Zenodo, 2026. <https://doi.org/10.5281/zenodo.22132451>
