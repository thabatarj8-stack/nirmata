# Why final answers are not enough to evaluate AI agents

**Português:** [Por que a resposta final não basta](../pt-BR/por-que-a-resposta-final-nao-basta.md)  
**Primary keyword:** AI agent evaluation  
**Meta description:** Learn why AI agent evaluation must inspect tool calls, authorization, state changes, and external effects—not only final answers.

An AI agent can produce a correct answer after taking an unacceptable path. It can use the wrong data, accept forged approval, call a tool outside its authority, or create an external effect that its final message never discloses. If evaluation sees only the answer, those events disappear.

This is the central problem Nirmata studies: **how much safety-relevant information is contained in an agent's execution trajectory but absent from its final output?**

## A correct answer is only one observation

Conventional output evaluation asks whether a response is accurate, relevant, safe, or well written. Those questions still matter. They are simply incomplete when a system can act.

Consider an editorial agent that returns a publication-ready article. The text may be accurate, yet the process may have:

- treated a reviewer's recommendation as the owner's approval;
- fetched information from an unverified source;
- queued content before the authorized version was fixed;
- published when it had authority only to draft;
- retried an external action and created a duplicate effect.

None of these failures must appear in the article itself. The object under evaluation is therefore not just a string. It is a sequence of decisions, tool calls, state transitions, authorization events, and effects.

## What a trajectory adds

Nirmata defines an execution trajectory as the final output plus observable process evidence. Depending on the system, that evidence can include tool inputs and results, content hashes, approval sources, controller decisions, external identifiers, and human interventions.

This view aligns with a broader shift in agent-safety research. AgentDojo evaluates agents using tools over untrusted data and shows why prompt injection must be tested in an interactive environment, not as a static response problem. TraceSafe-Bench and ATBench focus explicitly on multi-step trajectories and long-horizon safety failures. These works differ in scope and maturity, but they share a practical premise: risk can emerge during execution.

## Separate the signals before combining them

Showing all evidence to one evaluator sounds simple, but it creates another risk: a clean-looking process can soften the judgment of unsafe content, or alarming content can distort the classification of an otherwise blocked attempt.

Nirmata's current pilot design separates the channels:

```text
content evaluator    -> content_unsafe
trajectory evaluator -> trajectory_unsafe + process class
final judgment       -> content_unsafe OR trajectory_unsafe
```

The monotonic `OR` rule prevents one safe signal from erasing an unsafe signal. It also makes the incremental contribution of trajectory evidence measurable. This architecture has passed integration checks; it has not yet produced a blind confirmatory result.

## Blocked attempts are not executed violations

Trajectory evidence should improve discrimination, not merely generate more alerts. An unauthorized request that a control blocks is evidence that the control worked. An unauthorized action that reaches an external system is a policy violation. Treating both as equally unsafe hides the difference between exposure and failure.

Nirmata's process taxonomy therefore separates suspicious anomalies, blocked unauthorized attempts, executed policy violations, and harmful external actions. That distinction makes evaluation more useful for system design because it identifies where a defense held and where it failed.

## The practical question

The goal is not to collect every hidden thought. It is to preserve the observable evidence needed to answer four operational questions:

1. What did the agent attempt?
2. What authority did it actually have?
3. What changed outside the model?
4. Which control allowed, blocked, or modified the action?

A final answer can tell you what the agent said. A trajectory can help you determine what the system did.

## Continue reading

- [Nirmata methodology](../../docs/METHODOLOGY.md)
- [Evidence status](../../docs/EVIDENCE-STATUS.md)
- [Experiment registry](../../experiments/README.md)
- [Related work](../../docs/RELATED-WORK.md)

**External primary sources:** [AgentDojo, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html) · [TraceSafe, arXiv 2026](https://arxiv.org/abs/2604.07223) · [ATBench, arXiv 2026](https://arxiv.org/abs/2604.02022)
