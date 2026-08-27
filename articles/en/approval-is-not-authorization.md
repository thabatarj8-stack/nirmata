# Approval is not authorization in agentic systems

**Português:** [Aprovação não é autorização](../pt-BR/aprovacao-nao-e-autorizacao.md)  
**Primary keyword:** delegated authority in AI agents  
**Meta description:** Learn why advice, approval, queueing, and permission to act must be separate states in systems built with AI agents.

“Looks good” is not a safe permission model.

In an agentic workflow, a reviewer may recommend a draft, an owner may approve its content, a scheduler may place it in a queue, and a publisher may create an external effect. Those are four different events. Collapsing them into a single notion of approval gives an agent room to cross a boundary that nobody explicitly delegated.

## The hidden ambiguity in human approval

Natural-language collaboration relies on context. People often understand whether “go ahead” means “continue editing,” “schedule this,” or “publish now.” A system that acts through tools cannot safely depend on that ambiguity.

The problem becomes sharper when authority comes from several actors:

- a researcher recommends a source;
- an editor accepts the recommendation;
- an owner approves the final content;
- a controller verifies the approved version;
- a publisher sends it to an external platform.

If an agent turns the researcher's recommendation into owner approval, the final content may still be excellent. The authorization path is still wrong.

## Model authority as state, not tone

Delegated authority should be explicit, scoped, and inspectable. At minimum, a consequential action should bind:

- **principal:** who granted authority;
- **action:** what may be done;
- **object:** which exact content or resource is covered;
- **scope:** where and under which account the action may occur;
- **time:** when the authorization starts and expires;
- **preconditions:** which checks must pass first;
- **evidence:** how the grant and resulting effect are recorded.

This converts “the conversation sounded positive” into a verifiable control decision. Recent requirements-engineering work calls the broader concept a delegated-autonomy boundary: the decisions about what may be delegated, under what graduated authority, with what oversight, and how control returns to a human.

## Content approval is not publication authority

A robust workflow separates at least these states:

```text
DRAFTED -> REVIEWED -> CONTENT_APPROVED -> QUEUED -> PUBLICATION_AUTHORIZED -> PUBLISHED
```

The transition from `CONTENT_APPROVED` to `PUBLICATION_AUTHORIZED` should not be implied. It should require a distinct grant that refers to the exact version being published. A content hash can prevent a later edit from silently inheriting earlier approval.

The publisher should also have less authority than the planner. It needs permission to execute a specific approved action, not freedom to redesign the plan. This reduces the blast radius if the planning context is manipulated.

## Controls must preserve the difference between attempt and effect

An agent may attempt to publish without authority. If the controller blocks the call, the event is important but it is not an executed policy violation. If the call reaches the platform, the external effect changes the classification.

This is why audit records should capture both the request and the outcome:

- requested transition;
- presented authorization;
- controller decision;
- tool invocation;
- external identifier or error;
- final state.

Without the outcome, teams cannot tell whether they observed an attack, a working defense, or a real breach of policy.

## What Nirmata has—and has not—shown

Nirmata's prototype passed 12 known development and control-integrity checks covering approval injection, forged identity, state tampering, content substitution, queue tampering, replay, and two-phase publication. Those tests support implementation behavior on known cases.

They do not establish production-grade isolation or robustness against unseen attacks. The controller and publisher still require independent credentials and stronger process-level isolation before the system can support a stronger security claim.

The uncomfortable conclusion is simple: human approval is not a message. It is a state transition backed by evidence, scope, and an enforceable boundary.

## Continue reading

- [Experiment 001](../../experiments/README.md#experiment-001)
- [Methodology and process taxonomy](../../docs/METHODOLOGY.md)
- [Evidence status](../../docs/EVIDENCE-STATUS.md)
- [Research agenda](../../docs/RESEARCH-AGENDA.md)

**External primary source:** [Specifying the Delegated-Autonomy Boundary, arXiv 2026](https://arxiv.org/abs/2607.17225)
