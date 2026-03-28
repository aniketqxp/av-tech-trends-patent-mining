# AV Tech Trends Patent Mining

A professional portfolio-ready repository for autonomous vehicle patent mining, trend analysis, and innovation intelligence.

This project consolidates an end-to-end patent analytics workflow using a curated patent dataset, NLP-driven semantic clustering, technology trend extraction, and innovation outlier detection.

## Highlights
- `data/` contains a curated dataset of 667 AV patents from Lens.org.
- `notebooks/` contains polished Jupyter notebooks that explain the analysis story step by step.
- `src/` contains reusable data-loading helpers for clean, reproducible workflows.
- `reports/` contains the final project deck and written report.
- `assets/figures/` includes summary visuals embedded in this README.

## Portfolio-ready assets
- `README.md` — project overview and quickstart
- `requirements.txt` — reproducible Python environment
- `LICENSE` — MIT license for open use
- `notebooks/` — renamed and organized final analysis notebooks
- `data/` — curated AV patent dataset
- `reports/` — final presentation + report

## Quick preview

![Patent Volume by Publication Year](assets/figures/patents_by_year.png)

![Top Autonomous Vehicle Patent Applicants](assets/figures/top_applicants.png)

## Repository structure

- `notebooks/`
  - `01-data-ingest-preprocessing.ipynb`
  - `02-exploratory-analysis.ipynb`
  - `03-semantic-clustering.ipynb`
  - `04-innovation-trend-analysis.ipynb`
  - `05-emergence-analysis.ipynb`
  - `06-outlier-detection.ipynb`
  - `07-structured-extraction-llm.ipynb`
  - `08-project-exploration.ipynb`
- `data/`
  - `av_patentdata.jsonl`
  - `av_patent_data.json`
  - `README.md`
- `src/`
  - `data_loader.py`
  - `__init__.py`
- `assets/figures/`
  - `patents_by_year.png`
  - `top_applicants.png`
- `reports/`
  - `Final Review.pptx`
  - `Project Report.pdf`
- `requirements.txt`
- `LICENSE`

## How to use

1. Create a Python environment:
   ```bash
   python -m venv .venv
   ./.venv/Scripts/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. Launch Jupyter:
   ```bash
   jupyter lab
   ```

3. Open the notebooks in `notebooks/` in the order listed above.

## Data workflow

- `data_loader.py` provides a simple helper to load the `data/av_patentdata.jsonl` dataset.
- The notebooks build on this dataset to produce clustering, trend, emergence, and outlier insights.

## Notes

- The dataset is already curated for AV patents; the pipeline focuses on NLP, embedding-based analytics, and trend discovery.
- The notebooks were renamed and reorganized for clarity and storytelling.

## License

This repository is licensed under the MIT License. See `LICENSE` for details.
