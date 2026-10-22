main README 

# Hail Risk and Crop Insurance Pricing: Nashik Grapes

## Overview

This project models the annual hail loss for a 1-hectare grape orchard in Nashik, Maharashtra, and estimates the fair insurance premium using frequency-severity-aggregate (FSA) simulation.

**Research question:** Given historical hail frequency and damage patterns, what is the expected annual loss, the 1-in-100 worst case, and a loaded premium that covers expected loss plus risk margin?

---

## Problem statement

Nashik grows ~60% of India's table grapes. Hail during the fruiting season (April–June) causes widespread crop loss, sometimes wiping out 50–80% of production in affected talukas. Farmers lack affordable insurance mechanisms, partly because insurers lack reliable hail risk models.

This project demonstrates a quantitative approach to hail risk using frequency-severity modelling, a core actuarial technique.

---

## Data sources

| Dataset | Variable | Source | Status |
|---------|----------|--------|--------|
| Convective environment | CAPE, CIN, precip, temp | ERA5 (Copernicus CDS) | Downloaded |
| Hail events (1995–2023) | Date, taluka, damage ratio | News archives, disaster reports | In progress |
| Crop value | Cost of cultivation, yield | ICAR-NRC Grapes, Maharashtra Ag Dept | To gather |
| Insurance context | Sum insured, premiums | PMFBY, National Horticulture Board | To gather |

---

## Methodology

### Frequency model
- Count hail days per season → Poisson/Negative Binomial fit
- Assess overdispersion, choose model via AIC
- Output: λ (mean events per year)

### Severity model
- Damage ratio (0–1) per event → Beta or mixture distribution
- Fit using event data; validate against PMFBY loss ratios
- Output: distribution of losses per event

### Aggregate loss
- Monte Carlo: 10,000–100,000 simulations
- Each: draw # events ~ Freq model, draw damage ~ Severity model, aggregate
- Output: E[Loss], Var[Loss], 95% VaR, 99% VaR

### Premium calculation
- Pure premium = E[Loss]
- Loaded = Pure × (1 + expense ratio) × (1 + risk loading)
- Sanity check against PMFBY rates

---

## Key assumptions & limitations

- **Data sparsity:** Hail is underreported in local records. Small event table (expect ~10–30 events) increases parameter uncertainty.
- **ERA5 limitations:** Reanalysis struggles with convective precipitation; used as environment proxy, not rainfall truth.
- **No spatial dependence:** Model treats each farm independently; no correlation across orchards.
- **Constant exposure:** Assumes orchard value and hail vulnerability are constant over time; ignores climate trends.
- **Damage proxy:** Severity inferred from limited sources; sensitivity analysis shows impact.

---

## Usage

### Setup
```r
# Install packages
install.packages(c("tidyverse", "fitdistrplus", "EnvStats"))

# Set working directory
setwd("path/to/hail-risk-nashik-grapes")

# Source setup
source("R/01_setup.R")
```

### Run the pipeline
```r
source("R/02_event_table.R")    # Load hail events
source("R/03_frequency_fit.R")  # Fit frequency dist
source("R/04_severity_fit.R")   # Fit severity dist
source("R/05_simulation.R")     # Monte Carlo
source("R/06_plotting.R")       # Generate charts
```

---

## Results 

- Expected annual loss per hectare: ₹[X]
- 1-in-100 annual loss: ₹[Y]
- Pure premium (fair price): ₹[Z]
- Loaded premium (with risk loading): ₹[Z × 1.X]
- Premium reduction with 40% risk mitigation: [%]

See `outputs/` for charts.

---

## Files & structure

- `notes/`: Study notes on distributions, estimation, compound loss, premium principles
- `data/raw/`: ERA5 downloads, event table (original, unedited)
- `data/processed/`: Cleaned event data, fitted parameters
- `R/`: Modular scripts (numbered in order)
- `outputs/`: Charts (frequency fit, severity fit, loss distribution, premium comparison)

---

## References

- IRI Data Library: IMD gridded rainfall data
- Copernicus Climate Data Store: ERA5 reanalysis documentation
- Mausam journal: Hail climatology in India
- PMFBY (Pradhan Mantri Fasal Bima Yojana): Crop insurance scheme

---

## Author

Samruddhi S | Oct 2026

