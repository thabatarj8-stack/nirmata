# A burned holdout is still research evidence

**Português:** [Um holdout queimado ainda é evidência](../pt-BR/um-holdout-queimado-ainda-e-evidencia.md)  
**Primary keyword:** AI evaluation reproducibility  
**Meta description:** Why an invalidated holdout cannot prove model performance—but should remain visible as evidence about the research process.

The most credible result in an early evaluation project may be the result it refuses to report.

Nirmata planned a blind holdout to test whether execution trajectories add safety signal beyond final-output evaluation. Before predictions were produced, the answer key entered the evaluator context. The run stopped. No score was calculated. The holdout was invalidated for that context.

That event cannot support a performance claim. Hiding it would still make the research worse.

## What makes a holdout useful

A holdout estimates behavior on cases that did not shape the evaluator. Its value depends on separation: the design is frozen, the evaluator sees inputs without labels, predictions are persisted, and only then is ground truth revealed.

Once the answer key enters the development or evaluator context, the separation is broken. Even if nobody intentionally copies a label, future choices can be influenced by knowledge of the cases. Prompts, rubrics, thresholds, or error analysis may adapt to the supposedly unseen set.

The safe rule is strict: if ground truth was exposed before predictions were fixed, the holdout is burned for that context.

## Invalidated does not mean useless

The holdout no longer measures blind performance, but the failure still provides process evidence. It can reveal:

- that ground truth and trace inputs were stored too close together;
- that the evaluator context had broader file access than intended;
- that the protocol lacked a pre-run exposure check;
- that prediction persistence and label release were not separated by a strong enough boundary;
- that the team was willing to stop instead of converting contamination into a result.

These observations can improve the next protocol. They just cannot be relabeled as model accuracy.

## Preserve the layers of evidence

Nirmata uses separate evidence classes because “the test passed” is otherwise too vague:

| Evidence class | Legitimate use |
|---|---|
| Development | Check known rules and implementation behavior |
| Integration | Verify schemas, evaluator plumbing, and expected distinctions |
| Confirmatory | Estimate behavior on frozen, unseen cases |
| Invalidated | Document why an intended claim cannot be made |

Passing development tests does not demonstrate generalization. Passing integration cases does not create an effect size. An invalidated holdout does not become confirmatory because the pipeline was otherwise well built.

## A failure-preserving protocol

A stronger next run should make contamination difficult to achieve and easy to detect:

1. Freeze prompts, configurations, rubrics, aggregation, and analysis code.
2. Build trace inputs and labels in separate environments.
3. Record access boundaries and run a preflight exposure check.
4. Evaluate only the unlabeled traces.
5. Persist predictions in an append-only artifact and record hashes.
6. Reveal ground truth after predictions are fixed.
7. Score without changing cases, thresholds, or interpretation rules.
8. Record every deviation, including aborted runs.

Independent custody of the holdout would be stronger than procedural separation inside one shared context. Until that exists, the limitation should remain explicit.

## Why the public record matters

Repositories often show only the clean path: the final code, the successful run, and the chart worth sharing. That makes the artifact easier to read but harder to trust. Reviewers cannot see how many designs failed, which cases influenced the evaluator, or whether a “blind” result remained blind.

Preserving the invalidated run creates no positive performance result. It creates something more basic: a boundary around what the project is allowed to claim.

That boundary is not an embarrassment. It is part of the method.

## Continue reading

- [Blinding protocol](../../docs/METHODOLOGY.md#blinding-protocol)
- [Evidence ledger](../../docs/EVIDENCE-STATUS.md)
- [Experiment 002](../../experiments/README.md#experiment-002)
- [Research agenda](../../docs/RESEARCH-AGENDA.md)
