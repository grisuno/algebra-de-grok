# Second Brain

*Last synthesized: 2026-10-07 | 22 files | 4 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `config.py`, `training.py`, `app.py`. Architecturally it is 6 layers, dominant utility (15 files) across 4 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between new_experiment: checkpointing, root, new_experiment: purity_analysis: 1 extracted cross-community imports and 5 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (95% file coverage), 0 security findings, 0 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 22 |
| Symbols | 282 |
| Resolved imports | 35 |
| Languages | py, sh |
| Communities | 4 |
| Doc coverage | 95% (21/22 files) |
| Security findings | 0 |
| Estimated read cost | ~7393 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target readmenator_algebra-de-grok_7q3_3xp8
```

## Concept Wiki

- [new_experiment: checkpointing (8 files, cohesion 0.60)](./community_0_new_experiment_checkpointing.md)
- [root (7 files, cohesion 1.00)](./community_1_root.md)
- [new_experiment: purity_analysis (4 files, cohesion 0.29)](./community_2_new_experiment_purity_analysis.md)
- [orphans (3 files, cohesion 0.00)](./community_3_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `new_experiment/config.py` | 20.4 |
| `new_experiment/training.py` | 16.4 |
| `app.py` | 13.8 |
| `new_experiment/streamlit_app.py` | 13.0 |
| `new_experiment/test_framework.py` | 12.8 |

## Strongest Connections

- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: shares_context (strength 0.5, INFERRED)
- 0 -> 3: shares_context (strength 0.5, INFERRED)
- 1 -> 2: shares_context (strength 0.5, INFERRED)
- 1 -> 3: shares_context (strength 0.5, INFERRED)
- 2 -> 3: shares_context (strength 0.5, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
