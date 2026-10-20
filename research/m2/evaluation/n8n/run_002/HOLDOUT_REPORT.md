# HOLDOUT_REPORT — n8n run_002 / Adapter v0.1.0

The commit hashes cited in this report live in a private development repository; this report is published here for transparency.

<!-- markdownlint-disable-next-line MD036 -->
**HOLDOUT_PASS = true**

This is the first evaluation of frozen n8n Adapter v0.1.0 against independently
frozen run_002 gold. The evaluator was committed and pushed
(`78beb73162920617456025b6f5973a73f7fa1824`) **before** the first adapter
execution.

Adapter production code was not modified. Gold was not modified.
TRAJECTORY_SCHEMA_v0.1.1 was not modified. Proposal 005 was not implemented.
`main` was not merged.

---

## Frozen bindings

| Object | Value |
|---|---|
| Protocol commit | `b846d849c91760db08230ab706afd767d11cef8a` |
| Adapter commit | `59f732b99d45198030ff8b8c3ba87bb7319b13b3` |
| Adapter version | `0.1.0` |
| Gold commit | `e3afe6815dc6309c27d92b80f31e8ebe233d8224` |
| Gold SHA-256 | `309425ec3c95beece2ab864ae4ccdb13f6940c391b6724d0c48eed79fab57608` |
| Evaluator commit | `78beb73162920617456025b6f5973a73f7fa1824` |
| Evaluator file SHA-256 | `6ecaa04614d10622cefb74c8f1b472ae747e613e758f594e398660025f74d9b8` |
| Original public evidence SHA-256 | `2bf9d2895bec510a12ce7bc346a06a8edf50e2d99507a80296ed24dbebbfd66b` |
| First output SHA-256 | `075a3061ac30b85ab5feccc972baa0cfcad54e7a24ae44af34dc8625c5938ed6` |
| First report SHA-256 | `f8b6638851a7dff50af2cdf1098f75ca6008826bef1aeee91a67280e90c14b61` |
| Repeat output SHA-256 | `075a3061ac30b85ab5feccc972baa0cfcad54e7a24ae44af34dc8625c5938ed6` |
| Repeat report SHA-256 | `f8b6638851a7dff50af2cdf1098f75ca6008826bef1aeee91a67280e90c14b61` |

Original evidence remains **outside Git**.

---

## Eight criteria

| # | Criterion | Result |
|---|---|---|
| 1 | Normalization completed without capability abort | **true** (exit 0; no `A_N8N_*`) |
| 2 | Event/action agreement = 100% | **true** (9 events; actions and sequence fields agree) |
| 3 | Causal-topology agreement = 100% | **true** (linear parent positions `null,1,2,3,4,5,6,7,8`) |
| 4 | Material-field agreement = 100% | **true** (gold-required subset). Adapter-only `extensions.n8n` extra keys: **9** (descriptive; not a substitute for §1–§6) |
| 5 | Zero manufactured authorization claims | **true** (no serialized `authorization` on the wire) |
| 6 | Zero manufactured effects claims | **true** (no boolean `external_effect` on the wire) |
| 7 | Zero sensitive leakage, fully exercised | **true** (original SHA verified; ciphertext and `resumeToken` **values** absent; dropped **names** only) |
| 8 | Deterministic semantic output | **true** (also **byte-identical** first vs repeat) |

`HOLDOUT_PASS` is all-or-nothing. All eight are true.

Mismatch list: **empty**.

---

## Adapter run

First run (after evaluator freeze was already on `origin/m2/run002-evaluation`):

- exit code `0`
- stderr empty
- no capability abort

Repeat run: identical inputs, same frozen adapter tree, no code change.
Output and report SHA-256 each match the first run.

M1 validator on first output: **TRACE VALID**. Warnings (context only, not
holdout criteria): 7× `W_UNKNOWN_ACTION`, 1× `W_INTEGRITY_ABSENT`.

---

## Wire vs parser defaults

Serialized adapter events omit `authorization` and `effects`.

M1 may still materialize `authorization.state=not_required` after parse.
That default is **not** counted as an adapter-produced authorization claim.

---

## Out-of-protocol artifact

Hash beginning `53a30f28…` is `OUT_OF_PROTOCOL_ARTIFACT` /
`EXCLUDED_FROM_ANALYSIS`. It was not used.

---

## Interpretation

Allowed conclusion:

> n8n Adapter v0.1.0 demonstrated within-scope holdout generalization on a
> second preregistered synthetic n8n workflow that was not used for adapter
> implementation.

**Not** claimed: that the adapter generalizes to n8n; that it is
production-ready; that it supports arbitrary n8n workflows; that Nirmata is
validated across orchestrators.

Proposal 005 remains **OPEN / M2 EVIDENCE REQUIRED**.

This result does not prove source authenticity.
