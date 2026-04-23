# AV Technology Patent Mining

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

A sophisticated data-driven pipeline for mining, analyzing, and visualizing trends in Autonomous Vehicle (AV) patents. This project transforms raw patent data into actionable innovation intelligence through semantic clustering, temporal forecasting, and LLM-powered structured extraction.

## The Hook: Why This Project?

The autonomous vehicle industry is a dense thicket of complex intellectual property. Identifying emerging technologies, dominant applicants, and novel outliers requires more than simple keyword searches. This project provides a production-ready analytical framework that leverages:

- **Semantic Embedding Clusters**: Grouping patents by technological concept rather than just keywords.
- **Temporal Trend Forecasting**: Predicting the trajectory of innovation areas using Facebook Prophet.
- **Outlier Detection**: Uncovering niche or unique innovations using Isolation Forests.
- **LLM Synthesis**: Converting long-form patent claims into structured technical summaries.

## System Architecture

```mermaid
graph TD
    %% Node Definitions
    A[/Raw Patent Data: JSONL/] --> B(Data Ingestion & Normalization)
    B --> C(Text Corpus Construction)
    C --> D{Analysis Engines}
    
    D --> E[Semantic Clustering: SBERT/UMAP]
    D --> F[Temporal Trend Analysis: Prophet]
    D --> G[Emergence Scoring]
    D --> H[Outlier Detection: Isolation Forest]
    D --> I[LLM Extraction: Gemini API]
    
    E --> J[(Innovation Intelligence)]
    F --> J
    G --> J
    H --> J
    I --> J
    
    J --> K>Final Analytical Insights]
    K --> L[/Summary Visuals & Reports/]

    %% Styling
    style A fill:#2d3436,stroke:#000,color:#fff
    style B fill:#0984e3,stroke:#000,color:#fff
    style C fill:#0984e3,stroke:#000,color:#fff
    style D fill:#6c5ce7,stroke:#000,color:#fff
    style E fill:#00b894,stroke:#000,color:#fff
    style F fill:#fdcb6e,stroke:#000,color:#000
    style G fill:#e17055,stroke:#000,color:#fff
    style H fill:#d63031,stroke:#000,color:#fff
    style I fill:#fdcb6e,stroke:#000,color:#000
    style J fill:#00b894,stroke:#000,color:#fff
    style K fill:#2d3436,stroke:#000,color:#fff
    style L fill:#2d3436,stroke:#000,color:#fff
```

## Getting Started

### Prerequisites
- Python 3.10 or higher
- [Optional] Google Gemini API Key (for structured extraction)

### Installation
```bash
# Clone the repository
git clone https://github.com/aniketqxp/av-tech-trends-patent-mining.git
cd av-tech-trends-patent-mining

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Quick Start
You can run the core pipeline via the root-level entry point:
```bash
python main.py
```

## Project Structure

- `src/`: Modularized core execution logic and data loaders.
- `notebooks/`: Narrative exploration for each stage of the analysis.
- `data/`: Curated dataset of ~700 AV patents (2020–2025).
- `assets/figures/`: Generated analytical visualizations.
- `reports/`: Consolidated project reports and review presentations.

## Visual Insights

![Patent Volume by Publication Year](assets/figures/patents_by_year.png)

![Top Autonomous Vehicle Patent Applicants](assets/figures/top_applicants.png)

<!-- Placeholder for Semantic Cluster Plot -->
<!-- ![Semantic Clustering Visualization](assets/figures/semantic_clusters.png) -->

## License
This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.
