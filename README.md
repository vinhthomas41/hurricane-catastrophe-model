# Hurricane Catastrophe Loss Model

Multi-basin Monte Carlo simulation of global hurricane activity built in Python. Models storm frequency and intensity across 5 ocean basins using real historical data from NOAA.

---

## What it does

Simulates 10,000 years of hurricane activity per basin and calculates key risk metrics used in the insurance industry — AAL, 100-year PML, and 250-year PML. Built this to demonstrate actuarial modeling concepts like frequency-severity models and catastrophe risk quantification.

---

## Data

- **Source:** IBTrACS v04r01 — NOAA National Centers for Environmental Information
- **Coverage:** 1980–2025
- **Storms used:** 2,197 hurricane-strength storms (≥64 knots, per WMO classification)
- **Basins modeled:** Western Pacific, Eastern Pacific, South Indian, South Pacific, North Indian
- SA basin excluded — only 1 storm on record, not enough to model

---

## Methodology

- **Frequency:** Poisson distribution — models how many storms hit per year per basin
- **Severity:** Lognormal distribution — models peak wind intensity per storm
- **Severity metric:** Max sustained wind speed (knots) used instead of dollar losses since global insured loss data is inconsistent across countries
- **Parameters:** λ, μ, σ derived directly from IBTrACS data per basin
- **Simulation:** 10,000 years per basin = 50,000 total simulated basin-years

---

## Results

| Basin | Full Name | AAL | 100-Year PML | 250-Year PML |
|-------|-----------|-----|--------------|--------------|
| WP | Western Pacific | 1,588 | 2,663 | 2,859 |
| EP | Eastern Pacific | 907 | 1,703 | 1,816 |
| SI | South Indian | 889 | 1,674 | 1,780 |
| SP | South Pacific | 471 | 1,051 | 1,159 |
| NI | North Indian | 159 | 504 | 561 |

*All values in accumulated annual wind intensity (knots)*

WP dominates because it averages 15+ storms/year. NI has the worst tail risk relative to its average — its 100-year PML is 3.2x its AAL vs 1.7x for WP.

---

## How to run

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run `python download_data.py` — pulls the IBTrACS CSV (~50MB) directly from NOAA
4. Open `hurricane_model.ipynb` in Jupyter and run all cells

---

## Files

```
├── hurricane_model.ipynb                     # main notebook
├── download_data.py                          # downloads IBTrACS data from NOAA
├── requirements.txt                          # python dependencies
├── charts.png                                # simulated loss distribution charts
└── Hurricane_Catastrophe_Model_Summary.pdf   # full project writeup
```

---

## Limitations

- Wind speed is a proxy for loss, not actual dollar damage
- 46 years of data means rare events may be underrepresented
- No landfall adjustment — open ocean storms are included
- Basins modeled independently, real correlation (ex. El Nino effects) not captured
- Parameters assumed stable over time — climate change may affect this

---

Built with Python — numpy, scipy, pandas, matplotlib
