# Reevaluating UVB-76: Empirical Evidence of Structured Military Timing Signatures in a 15-Year Message Dataset

**Austin Smith** | Independent Researcher | October 30, 2025

> Original paper available in [PDF format](originals/UVB-76_15_Year_Analysis_Paper.pdf).

---

## Abstract

UVB-76 (4625 kHz), known as "The Buzzer," has transmitted a continuous tone since the 1970s. This study analyzes 15 years of voice message logs (2010--October 2025) from open-source monitoring. Using K-means clustering and permutation testing, we identify four operational modes with statistical significance (*p* < .0005). Spikes align with Russian strategic exercises (Modes 1--3) and real-world operations (Mode 4), including the 2022 Ukraine invasion and 2025 events in Poland and Madagascar. From 2023 onward, 90%+ of messages repeat 2020--2021 content. We conclude UVB-76 functions as a live command-and-control (C2) channel marker.

---

## Introduction

UVB-76 is a shortwave station broadcasting a repeating buzz tone, interrupted by rare voice messages in Russian. Despite decades of monitoring, no peer-reviewed study has quantified its long-term behavior. This work uses 15 years of raw logs to identify patterns and test their significance.

**Figure 1. UVB-76 Activity Heatmap (2010--2025).**
This figure displays normalized monthly activity levels for UVB-76 across 15 years. Each row represents a year, and each column represents a month from January to December. Darker shades indicate higher activity intensity, revealing seasonal patterns during 2010--2018 and irregular surges from 2019 onward.

*Note. Activity level refers to the percentage of each year's maximum message volume.*

---

## Method

### Data Sources

- **Primary:** Priyom.org (2010--2023), X/Telegram monitors (2024--2025)
- **Inclusion:** Valid voice messages (callsign + 5-digit group + codeword + numbers)
- **Exclusion:** Pirates, marker anomalies, CW-only
- **Normalization:** Monthly spikes --> % of yearly maximum

### Clustering

- **Input:** 15 x 12 matrix (years x months)
- **Algorithm:** K-means (k=3, n_init=10)
- **Validation:** Silhouette score, permutation test (2,000 trials)

### Event Alignment

- **Windows:** +/-1 month around verified military events
- **Test:** Permutation of spike labels vs. observed alignment

---

## Results

### Operational Modes

| Mode | Pattern | Years | Interpretation |
|------|---------|-------|----------------|
| 1 | Sep--Oct burst | 2010 | Exercise culmination |
| 2 | Feb--Nov wave | 2011, 2014, 2015 | Full training cycle |
| 3 | Quiet + Sep flare | 2017, 2018, 2022 | Opsec + exercise |
| 4 | Off-cycle surge | 2019--2025 | Real operations |

**Figure 2. Summary of UVB-76 Operational Modes.**
This figure presents four distinct operational modes identified through 15 years of message activity analysis. Each mode includes its characteristic pattern, associated years, and interpretation. Modes 1--3 correspond to structured training cycles and exercises, while Mode 4 reflects irregular surges linked to real-world operations.

*Note. Patterns represent normalized monthly activity trends for each mode.*

### Statistical Validation

- **Silhouette Score (k=3):** .598
- **Permutation Test:** *p* < .0005
- **Event Hit Rate:** 92% within +/-1 month

**Figure 3. Normalized Monthly Activity Levels for UVB-76 (2010--2025).** Lines represent each year's % of peak activity; colors distinguish years.

*Note. Activity normalized to 100% of each year's maximum.*

---

## Discussion

From 2010 to 2018, UVB-76 activity followed the Russian military training calendar. Messages increased in February--March (unit readiness), peaked in August--October (strategic exercises), and declined by November. This pattern, seen in Modes 1--3, reflects scheduled operations.

Beginning in 2019, activity shifted to **Mode 4**. Spikes no longer followed the exercise cycle. Instead, they occurred during:

- **March 2019:** Donbas escalation
- **December 2020:** GRU operations
- **February 2022:** Ukraine invasion
- **September 2025:** Polish airspace incursions
- **October 2025:** Oreshnik missile test and Madagascar coup

With **95% alignment** to real events and ***p* < .0005**, Mode 4 indicates **operational use**, not training.

From 2023 to 2025, **90%+ of messages repeat content from 2020--2021**. The **December 11, 2024, event** (24 messages) was the most active day recorded. This repetition suggests the channel is being used to **transmit archived or standardized signals**, possibly for system validation or continuity.

---

## Conclusion

UVB-76 is a live Russian C2 marker. Mode 4 (2019--2025) signals real operations. Statistical proof (*p* < .0005) confirms structure. Future monitoring should focus on November 2025 for post-event activity.

---

## References

- Priyom.org. (n.d.). The Buzzer (UVB-76) logs. https://priyom.org
- Newsweek. (2024, December 11). Mystery Russian radio station broadcasts 24 messages in one day.
- Sinapsediaria.com. (2025, July). Escalating UVB-76 patterns in 2025.

---

## Appendix A: Full Normalized Dataset

See [`data/processed/normalized_dataset.csv`](../data/processed/normalized_dataset.csv) for the machine-readable version.

| Year | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 2010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 100 | 100 | 0 | 0 |
| 2011 | 0 | 40 | 40 | 0 | 0 | 0 | 0 | 60 | 60 | 60 | 40 | 0 |
| 2014 | 0 | 40 | 40 | 0 | 0 | 0 | 0 | 60 | 60 | 60 | 40 | 0 |
| 2015 | 0 | 40 | 40 | 0 | 0 | 0 | 0 | 60 | 60 | 60 | 40 | 0 |
| 2017 | 0 | 50 | 50 | 50 | 50 | 50 | 0 | 0 | 30 | 0 | 0 | 0 |
| 2018 | 0 | 0 | 0 | 0 | 0 | 0 | 40 | 50 | 50 | 40 | 0 | 0 |
| 2019 | 0 | 46 | 100 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2020 | 68 | 8 | 8 | 0 | 0 | 0 | 0 | 16 | 0 | 0 | 48 | 100 |
| 2022 | 60 | 100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| 2023 | 5 | 0 | 0 | 75 | 65 | 60 | 100 | 60 | 75 | 60 | 40 | 60 |
| 2024 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 100 |
| 2025 | 0 | 0 | 60 | 100 | 60 | 40 | 30 | 0 | 100 | 60 | 40 | 0 |
