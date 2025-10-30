# Reevaluating UVB-76: Empirical Evidence of Structured Military Timing Signatures in a 15-Year Transmission Dataset

This repository contains the datasets, analytical workflow, and supporting materials for a longitudinal study of UVB-76 / MDZhB transmission activity spanning 2010–2025. The analysis focuses not on message content, but on **unique spike-day frequency** and **seasonal transmission clustering**, treated as a proxy for operational and training-cycle timing.

## Overview

UVB-76 (also known as “The Buzzer”) is a long-standing Russian shortwave station transmitting on 4625 kHz. While culturally associated with speculation and folklore, the operational behavior of the signal has received limited structured academic examination.

This project provides:

- A **15-year normalized spike-day dataset**
- **Cross-year seasonal comparison**
- **K-means and hierarchical clustering**
- **Permutation testing against known Russian military event calendars**
- A **time-resolved operational mode classification model**

The study demonstrates statistically significant and recurring timing structures aligned with Russian strategic exercise cycles (2010–2018) and operational event periods (2019–2025).

## Repository Contents

| File / Folder | Description |
|--------------|-------------|
| `paper/` | Final research paper in PDF and DOCX formats |
| `datasets/` | Processed monthly spike-day datasets (2010–2025) |
| `normalized/` | Normalized (percent-of-year) dataset used for clustering and heatmaps |
| `heatmaps/` | Visual representations of seasonal timing patterns |
| `cluster_analysis/` | Outputs from K-means and hierarchical clustering |
| `methodology/` | Notes on extraction, cleaning, and normalization procedures |

## Method Summary

1. **Spike-Day Extraction**  
   Each day with ≥1 documented transmission is counted as a single “spike-day,” regardless of total message volume.

2. **Normalization**  
   For cross-year comparability, each year’s monthly spike-day counts are scaled to **percent of yearly maximum frequency**.

3. **Clustering Techniques**  
   - **K-means (k=3)** identifies three dominant operational timing modes.  
   - **Hierarchical clustering** validates separation between training-cycle years and operational-intensification years.

4. **Statistical Testing**  
   A **permutation test** (10,000 random reshuffles) confirms that temporal clustering aligns with documented military readiness and exercise periods at **p < 0.01**.

## Key Finding

Transmission timing is **structured and cyclic**, not random.  
Years group into **four operational modes**, reflecting shifts from annual training readiness cycles to operational and conflict-driven signaling periods.

## Citation

If referencing this repository or the associated paper:

**APA:**
Smith, A. (2025). *Reevaluating UVB-76: Empirical Evidence of Structured Military Timing Signatures in a 15-Year Transmission Dataset.* GitHub. https://github.com/<your-username>/UVB-76-Structured-Signal-Analysis

## Contact / Correspondence

For academic correspondence or data replication inquiries, please open a GitHub issue.
