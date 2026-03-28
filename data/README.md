# Patent Dataset

This directory contains the curated autonomous vehicle patent dataset used for this project.

Files
- `av_patentdata.jsonl`: 667 patent records extracted from Lens.org, filtered for US autonomous vehicle technology patents published between 2020 and 2025.
- `av_patent_data.json`: a secondary JSON export of the same dataset.

Fields in `av_patentdata.jsonl`
- `lens_id`
- `date_published`
- `claims`
- `description`
- `earliest_claim_date`
- `applicant_name`
- `cpc_symbols`
- `invention_title_text`
- `abstract_text`

Notes
- The dataset is preprocessed for NLP and trend analysis.
- Use `src/data_loader.py` to load the JSONL file reliably in Python.
