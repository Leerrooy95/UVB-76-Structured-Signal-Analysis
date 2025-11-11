# Limitations & Assumptions

## Data Source (Priyom.org)
- **Coverage**: Logs depend on global volunteer monitoring. Gaps likely in low-activity periods or non-English regions.
- **Verification**: Transmissions are user-submitted; no centralized ground truth.
- **Bias**: Higher reporting during voice messages or anomalies.

## Spike-Day Definition
- ≥1 transmission = spike day
- **Risk**: Low-volume days may be underreported
- **Mitigation**: Used only *confirmed* logs; excluded ambiguous entries

## Event Alignment
- Military calendar from open sources (mil.ru, state media)
- **Window**: ±6 hours (voice), ±24 hours (spikes)
- **Rationale**: Allows for reporting lag; tested 1h–48h windows (6h optimal)

## Statistical Claims
- p < 0.01 via 10k permutations
- **Interpretation**: Strong evidence *against random*, not proof of causation
- **Alternative explanations**: Monitoring bias, seasonal reporting, geopolitical noise
