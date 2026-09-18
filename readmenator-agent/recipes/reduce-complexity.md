# Recipe: Reduce File Complexity

Target hotspot: `realtime_train.py`
(complexity 1.0, centrality 0.8)

1. Read dependents: `grep -n 'realtime_train.py' readmenator-agent/ARCHITECTURE.md`
2. Extract functions/classes into new files in the same subsystem
3. Update imports
4. Regenerate: `readmenator .`
