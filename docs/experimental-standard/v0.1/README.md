# Nirmata Experimental Standard v0.1

**Status:** Draft

This directory defines the first public experimental standard for Nirmata. It operationalizes trajectory-aware evaluation, evidence preservation, blinding, scoring, and publication safety for pilot studies of AI-agent execution.

## Components

- `TRACE-SCHEMA.md` — minimal representation of an agent execution trajectory.
- `RUN-MANIFEST.md` — machine-readable provenance for experimental runs.
- `BLINDING-PROTOCOL.md` — rules for preventing ground-truth leakage and post-hoc adjustment.
- `SCORING-SPEC.md` — frozen scoring logic for final-output-only and trajectory-aware conditions.
- `PUBLICATION-SAFETY.md` — sanitization and minimum-disclosure rules for public research artifacts.

## Core principles

1. Final outputs and execution trajectories are distinct evidence channels.
2. Authorization, attempted action, executed action, and external effect must remain distinguishable.
3. Development, integration, confirmatory, and invalidated evidence must not be conflated.
4. Predictions must be persisted before ground-truth reveal in confirmatory runs.
5. Evidence classifications may be downgraded after execution, but not upgraded beyond what the frozen protocol permits.
6. Public artifacts must disclose only the information necessary to audit the scientific claim.

This standard is intentionally small and provider-independent. It is expected to evolve through versioned releases rather than silent edits.