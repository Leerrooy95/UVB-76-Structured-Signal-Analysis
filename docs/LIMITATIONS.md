# Limitations & Assumptions

This document outlines known constraints of the dataset, methodology, and conclusions presented in this analysis. These should be considered when interpreting or extending the findings.

---

## Data Source (Priyom.org)

| Dimension | Detail |
|-----------|--------|
| **Coverage** | Logs depend on global volunteer monitoring. Gaps are likely in low-activity periods or non-English-speaking regions. |
| **Verification** | Transmissions are user-submitted with no centralized ground truth or automated validation. |
| **Reporting bias** | Higher reporting frequency during voice messages or anomalous events. Routine buzzer activity is underrepresented. |
| **Supplementary sources** | 2024--2025 data supplemented via X/Telegram monitors, which may carry different reporting biases than Priyom.org. |

---

## Spike-Day Definition

- A spike-day is defined as any day with **one or more** confirmed voice transmissions.
- **Risk:** Low-volume days may be underreported due to monitoring gaps, leading to undercounting.
- **Mitigation:** Only confirmed logs were used; ambiguous or unverified entries were excluded.
- **Trade-off:** This binary approach (spike vs. no spike) sacrifices volume granularity in favor of consistency across years with varying monitoring coverage.

---

## Event Alignment

- Military event calendars were sourced from open materials (mil.ru, state media reports).
- **Alignment windows:** +/-6 hours for voice messages, +/-24 hours for spike-days.
- **Window selection rationale:** Allows for reporting lag between transmission and log entry. Windows from 1h to 48h were tested; 6h was selected as optimal based on hit-rate vs. false-positive balance.
- **Limitation:** Open-source military calendars may be incomplete or subject to state information controls.

---

## Statistical Claims

| Claim | Context |
|-------|---------|
| *p* < .0005 | Via 2,000 permutation reshuffles of spike labels against event windows |
| **Interpretation** | Strong evidence *against random timing*, not proof of direct causation |
| **Alternative explanations** | Monitoring bias, seasonal reporting patterns, geopolitical noise, coincidental temporal overlap |

The permutation test establishes that the observed alignment between spike-days and military events is unlikely under a null model of random timing. It does not establish a causal mechanism. Correlation with military calendars could reflect shared seasonal drivers (e.g., weather, political cycles) rather than direct command-and-control signaling.
