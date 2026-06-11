# Hurricane Catastrophe Loss Model

multi-basin monte carlo simulation of global hurricane activity built in python. models storm frequency and intensity across 5 ocean basins using real historical data from NOAA.

---

## what it does

simulates 10,000 years of hurricane activity per basin and calculates key risk metrics used in the insurance industry — AAL, 100-year PML, and 250-year PML. built this to demonstrate actuarial modeling concepts like frequency-severity models and catastrophe risk quantification.

---

## data

- **source:** IBTrACS v04r01 — NOAA National Centers for Environmental Information
- **coverage:** 1980–2025
- **storms used:** 2,197 hurricane-strength storms (≥64 knots, per WMO classification)
- **basins modeled:** Western Pacific, Eastern Pacific, South Indian, South Pacific, North Indian
- SA basin excluded — only 1 storm on record, not enough to model

---

## methodology

- **frequency:** poisson distribution — models how many storms hit per year per basin
- **severity:** lognormal distribution — models peak wind intensity per storm
- **severity metric:** max sustained wind speed (knots) used instead of dollar losses since global insured loss data is inconsistent across countries
- **parameters:** λ, μ, σ derived directly from IBTrACS data per basin
- **simulation:** 10,000 years per basin = 50,000 total simulated basin-years

---

## results

| Basin | Full Name | AAL | 100-Year PML | 250-Year PML |
|-------|-----------|-----|--------------|--------------|
| WP | Western Pacific | 1,588 | 2,663 | 2,859 |
| EP | Eastern Pacific | 907 | 1,703 | 1,816 |
| SI | South Indian | 889 | 1,674 | 1,780 |
| SP | South Pacific | 471 | 1,051 | 1,159 |
| NI | North Indian | 159 | 504 | 561 |

*all values in accumulated annual wind intensity (knots)*

WP dominates because it averages 15+ storms/year. NI has the worst tail risk relative to its average — its 100yr PML is 3.2x its AAL vs 1.7x for WP.

---

## how to run

1. clone the repo
2. install dependencies: `pip install -r requirements.txt`
3. drop the IBTrACS CSV in the same folder as the notebook (too large to upload here — download it from [NOAA](https://www.ncei.noaa.gov/products/international-best-track-archive))
4. open `hurricane_model.ipynb` in jupyter and run all cells

---

## files

```
├── hurricane_model.ipynb     # main notebook
├── requirements.txt          # python dependencies
├── charts.png                # simulated loss distribution charts
└── Hurricane_Catastrophe_Model_Summary.pdf   # full project writeup
```

---

## limitations

- wind speed is a proxy for loss, not actual dollar damage
- 46 years of data means rare events may be underrepresented
- no landfall adjustment — open ocean storms are included
- basins modeled independently, real correlation (ex. el nino effects) not captured
- parameters assumed stable over time — climate change may affect this

---

built with python — numpy, scipy, pandas, matplotlib
