# AV Technology Patent Mining

A data-driven analysis of autonomous vehicle patents. This repository contains curated patent data, reusable pipeline code, and analytical notebooks for semantic clustering, trend extraction, emergence detection, and outlier analysis.

## Overview

The project converts raw patent text into actionable innovation intelligence by combining:
- curated patent data ingestion and normalization
- semantic embedding-based clustering
- temporal trend analysis of patent terminology
- emergence scoring for promising technology areas
- outlier detection for unusual or novel patents

## Repository structure

- `data/`
  - `av_patentdata.jsonl` — curated patent dataset
  - `av_patent_data.json` — alternate JSON export
  - `README.md` — dataset details and usage notes
- `notebooks/` — narrative notebooks for each analysis stage
- `src/` — reusable pipeline modules and helpers
- `assets/figures/` — generated summary charts
- `reports/` — final presentation and report artifacts
- `requirements.txt` — Python dependencies
- `LICENSE` — MIT license

## Dataset

The dataset includes 667 U.S. patents focused on autonomous vehicle technology published between 2020 and 2025. Each record includes key text fields and metadata necessary for NLP analysis.

Fields include:
- `lens_id`
- `date_published`
- `claims`
- `description`
- `earliest_claim_date`
- `applicant_name`
- `cpc_symbols`
- `invention_title_text`
- `abstract_text`

## Analysis workflow

The notebooks are arranged to guide the analysis from ingestion through insight generation:

1. `notebooks/01-data-ingest-preprocessing.ipynb`
2. `notebooks/02-exploratory-analysis.ipynb`
3. `notebooks/03-semantic-clustering.ipynb`
4. `notebooks/04-innovation-trend-analysis.ipynb`
5. `notebooks/05-emergence-analysis.ipynb`
6. `notebooks/06-outlier-detection.ipynb`
7. `notebooks/07-structured-extraction-llm.ipynb`
8. `notebooks/08-project-exploration.ipynb`

## Quick summary visuals

![Patent Volume by Publication Year](assets/figures/patents_by_year.png)

![Top Autonomous Vehicle Patent Applicants](assets/figures/top_applicants.png)

## Setup

Create a Python environment and install dependencies:

```bash
python -m venv .venv
.\.venv\Scriptsctivate
pip install --upgrade pip
pip install -r requirements.txt
```

## Running the analysis

1. Launch Jupyter Lab:

   ```bash
   jupyter lab
   ```

2. Open the notebooks in `notebooks/`.

3. Use `src/data_loader.py` and `src/pipeline.py` to load data and run reusable pipeline steps.

## Reusable code

- `src/data_loader.py` loads JSONL patent records.
- `src/pipeline.py` provides a reusable pipeline for loading the dataset, building a text corpus, and generating a base DataFrame.

## License

This repository is licensed under the MIT License. See `LICENSE` for details.
