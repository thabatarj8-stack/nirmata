# Glossary

**Language:** English · [Português (Brasil)](GLOSSARY.pt-BR.md)

| Term | Working definition in Nirmata |
|---|---|
| Agent execution trajectory | Observable sequence of decisions, events, tool calls, state transitions, authorizations, and external effects associated with an agent run |
| Final-output evaluation | Evaluation based only on the artifact or answer produced by the agent |
| Trajectory-aware evaluation | Evaluation that adds independent process evidence to the final-output judgment |
| Delegated authority | Explicitly bounded permission granted by a human or trusted principal to an agent or subsystem |
| External effect | A state change outside the evaluator's internal reasoning, such as publishing, sending, deleting, purchasing, or changing infrastructure |
| Approval attribution error | Treating a recommendation or reviewer statement as authorization from the actual owner |
| Control plane | Trusted mechanism that owns canonical authorization state and mediates privileged transitions |
| Content plane | System that researches, drafts, scores, or proposes actions without owning final authorization |
| Burned holdout | A confirmatory dataset whose ground truth was exposed before predictions were irreversibly fixed |
| Factorized evaluator | Architecture that evaluates content and trajectory in independent channels before deterministic aggregation |
| Failure-preserving research | Practice of retaining failed runs, protocol deviations, corrections, and invalidated evidence in the research record |
