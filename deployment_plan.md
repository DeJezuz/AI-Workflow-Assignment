# Deployment Plan

1. Package model and preprocessing pipeline.
2. Deploy a feature extraction pipeline near EHR (batch or stream).
3. Serve model behind authenticated API.
4. Start with shadow mode; validate with clinicians.
5. Monitor metrics and drift; schedule retraining.
