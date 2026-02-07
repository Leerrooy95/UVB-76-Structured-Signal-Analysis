# UVB-76 Structured Signal Analysis

[![UVB-76](https://img.shields.io/badge/UVB--76-4625_kHz-red)](https://en.wikipedia.org/wiki/UVB-76)
[![Data](https://img.shields.io/badge/Data-2010--2025-green)](data/)
[![Significance](https://img.shields.io/badge/Permutation_Test-p_%3C_.0005-blue)](#key-findings)
[![License](https://img.shields.io/badge/Cite-CITATION.cff-orange)](CITATION.cff)

**15-year empirical analysis of UVB-76 ("The Buzzer") transmission timing patterns using K-means clustering and permutation testing.**

---

## Executive Summary

UVB-76 is a Russian shortwave station on 4625 kHz that has broadcast a repeating buzz tone since the 1970s, interrupted by rare voice messages. Despite decades of public monitoring, no structured longitudinal study had quantified its operational behavior.

This project analyzes 15 years of transmission logs (2010--2025) sourced from [Priyom.org](https://priyom.org) and open-source monitors. Rather than examining message content, the analysis focuses on **when** transmissions occur -- treating spike-day frequency and seasonal clustering as proxies for operational timing.

The core finding: transmission timing is **structured and cyclic**, not random. Four distinct operational modes emerge, with statistically significant alignment to Russian military exercise schedules (2010--2018) and real-world operational events (2019--2025).

---

## Key Findings

| Metric | Value |
|--------|-------|
| **Permutation test** | *p* < .0005 (2,000 trials) |
| **Silhouette score** (k=3) | .598 |
| **Event alignment rate** | 92% within +/-1 month |
| **Dataset span** | 2010--2025 (12 years with confirmed logs) |
| **Operational modes identified** | 4 |

### Operational Modes

| Mode | Pattern | Years | Interpretation |
|------|---------|-------|----------------|
| 1 | Sep--Oct burst | 2010 | Exercise culmination |
| 2 | Feb--Nov wave | 2011, 2014, 2015 | Full training cycle |
| 3 | Quiet + Sep flare | 2017, 2018, 2022 | Opsec + exercise |
| 4 | Off-cycle surge | 2019--2025 | Real operations |

**Mode 4** (2019--present) marks a shift from training-cycle patterns to event-driven signaling. Spikes align with the Donbas escalation (2019), Ukraine invasion (2022), and 2025 escalation events. From 2023 onward, 90%+ of messages repeat 2020--2021 content, suggesting standardized C2 channel validation.

---

## Repository Structure

```
UVB-76-Structured-Signal-Analysis/
├── README.md
├── CITATION.cff
├── data/
│   ├── raw/                          # Original transmission logs from Priyom.org
│   │   ├── 2010_logs.txt
│   │   ├── 2011_logs.txt
│   │   ├── 2014_logs.txt
│   │   ├── 2015_logs.txt
│   │   ├── 2017_logs.txt
│   │   ├── 2018_logs.txt
│   │   ├── 2019_logs.txt
│   │   ├── 2020_logs.txt
│   │   └── 2022_logs.txt
│   └── processed/
│       └── normalized_dataset.csv    # Monthly spike-day counts (% of yearly max)
├── docs/
│   ├── report.md                     # Full analysis paper (Markdown)
│   ├── LIMITATIONS.md                # Data limitations & assumptions
│   └── originals/                    # Archival copies of original PDFs
│       ├── Normalized_Dataset.pdf
│       └── UVB-76_15_Year_Analysis_Paper.pdf
└── analysis/                         # Reserved for scripts and reproducible workflows
```

---

## Methodology

### 1. Spike-Day Extraction

Each day with one or more documented voice transmissions is counted as a single "spike-day," regardless of total message volume. This binary approach avoids weighting by reporting frequency.

### 2. Normalization

For cross-year comparability, each year's monthly spike-day counts are scaled to **percent of yearly maximum frequency**. This produces a 15 x 12 matrix suitable for clustering.

### 3. Clustering

- **K-means (k=3, n_init=10)** identifies three dominant operational timing modes
- **Hierarchical clustering** validates separation between training-cycle years and operational-intensification years
- **Silhouette score:** .598 (moderate-to-strong cluster separation)

### 4. Statistical Testing

A **permutation test** (2,000 random reshuffles of spike labels) confirms that temporal clustering aligns with documented military readiness and exercise periods at ***p* < .0005**.

### 5. Event Alignment

Military event calendars sourced from open materials (mil.ru, state media). Alignment windows: +/-6 hours for voice messages, +/-24 hours for spike-days. The 6-hour window was selected after testing 1h--48h ranges.

---

## Data Sources

| Source | Coverage | Role |
|--------|----------|------|
| [Priyom.org](https://priyom.org) | 2010--2023 | Primary log archive |
| X / Telegram monitors | 2024--2025 | Supplementary real-time logs |
| mil.ru / state media | 2010--2025 | Military event calendar |

**Inclusion criteria:** Valid voice messages containing callsign + 5-digit group + codeword + numbers.
**Exclusion criteria:** Pirate transmissions, marker anomalies, CW-only signals.

See [docs/LIMITATIONS.md](docs/LIMITATIONS.md) for a full discussion of data source constraints, reporting bias, and statistical caveats.

---

## Quick Start

The normalized dataset is available as a clean CSV for immediate use:

```
data/processed/normalized_dataset.csv
```

Each row is a year, each column is a month (Jan--Dec), and values represent the percentage of that year's maximum spike-day count (0--100 scale).

For the full research paper with figures and discussion, see [docs/report.md](docs/report.md).

---

## Citation

If referencing this repository or the associated analysis:

**APA:**
> Smith, A. (2025). *Reevaluating UVB-76: Empirical Evidence of Structured Military Timing Signatures in a 15-Year Transmission Dataset.* GitHub. https://github.com/Leerrooy95/UVB-76-Structured-Signal-Analysis

See [CITATION.cff](CITATION.cff) for machine-readable citation metadata.

---

## References

- Priyom.org. (n.d.). *The Buzzer (UVB-76) logs.* https://priyom.org
- Newsweek. (2024, December 11). Mystery Russian radio station broadcasts 24 messages in one day.
- Sinapsediaria.com. (2025, July). Escalating UVB-76 patterns in 2025.

---

## Contact

For academic correspondence or data replication inquiries, please [open a GitHub issue](https://github.com/Leerrooy95/UVB-76-Structured-Signal-Analysis/issues).
