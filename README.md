## Methodology for Patent Data Acquisition and Processing Pipeline

### 1. Data Source Selection and Filtering
Patent data was sourced from Lens.org, a comprehensive global patent database. Strategic filters were applied to focus on autonomous vehicle technologies from major industry players: publication dates spanning 2020-2025, granted US patents with complete documentation (title, abstract, claims, description, full text), active legal status, and specific applicant companies including Baidu USA LLC, Ford Global Tech LLC, Amazon Tech INC, Qualcomm INC, Toyota Motor CO LTD, Intel CORP, Google LLC, and Nvidia CORP. CPC classification codes targeted machine learning and neural network technologies (G06N3/08, G06N20/00, G06N3/045) while excluding certain computer vision classifications to maintain focus. These filters yielded a curated subset of 667 patents from hundreds of thousands available.

### 2. Metadata Extraction and API Integration
Initial metadata was exported as lens-export.csv containing essential identifiers, particularly Lens IDs. However, this export lacked critical fields like detailed claims and descriptions. To obtain comprehensive patent data, API access was requested and granted for Lens.org's REST API, enabling automated data retrieval using the collected Lens IDs.

### 3. Automated Data Pipeline Development
A systematic code pipeline was developed to fetch complete patent records via API calls. Data was stored in JSONL format (av_patentdata.jsonl) with each line containing full patent information as delivered by the API, ensuring efficient processing of large datasets while maintaining data integrity.

### 4. Data Preprocessing and Standardization
Raw API data contained extensive nested attributes and irrelevant fields (patent families, legal agents). A preprocessing pipeline was implemented to: remove unnecessary attributes, flatten nested structures to create top-level keys, and ensure consistent attribute availability across all patents. The final standardized schema included nine core attributes: lens_id, date_published, claims, description, earliest_claim_date, applicant_name, cpc_symbols, invention_title_text, and abstract_text.

This structured dataset served as the foundation for subsequent NLP-based clustering and trend analyses, while also providing input for the unstructured-to-structured pipeline feeding downstream ML analyses.

## Methodology for Autonomous Vehicle Patent Technology Clustering

### 1. Data Preprocessing and Corpus Preparation
The analysis begins by loading patent data from the JSONL file and creating a semantic corpus by combining patent titles, abstracts, and claims. Text preprocessing includes cleaning technical references (e.g., "Figure 1" → "figure"), removing excessive whitespace, and truncating documents to 500 words to optimize processing while preserving semantic meaning. Valid documents with sufficient content (>100 characters) are filtered for analysis.

### 2. Semantic Embedding Generation
The Sentence-BERT (SBERT) model transforms patent texts into high-dimensional semantic embeddings that capture contextual meaning beyond simple keyword matching. The 'all-MiniLM-L6-v2' model generates 384-dimensional vectors with L2 normalization, enabling cosine similarity calculations. This approach captures nuanced technological relationships that traditional TF-IDF methods might miss.

### 3. Optimal Clustering Parameter Selection
Multiple clustering quality metrics guide optimal cluster number selection: silhouette scores measure intra-cluster cohesion versus inter-cluster separation, Calinski-Harabasz scores evaluate cluster variance ratios, and the elbow method identifies diminishing returns in inertia reduction. These metrics are visualized to inform decision-making.

### 4. Semantic Clustering and Validation
K-means clustering groups patents based on semantic similarity in the embedding space. Cluster quality is validated through silhouette scoring and coherence analysis, measuring average cosine similarity within clusters. Alternative methods (hierarchical clustering, DBSCAN) provide robustness checks.

### 5. Technology Characterization and Market Analysis
Each cluster is characterized through TF-IDF-based keyword extraction from cluster centroids, identifying representative technological concepts. Cross-cluster similarity analysis reveals technology relationships and potential convergence areas. Patent applicant analysis within clusters identifies market leaders, competitive landscapes, and market concentration using Herfindahl indices.

### 6. Visualization and Reporting
UMAP/t-SNE dimensionality reduction creates interpretable 2D visualizations showing technology landscapes and applicant distributions. Comprehensive reporting includes cluster statistics, technology themes, temporal patterns, leading organizations, and competitive intelligence insights for autonomous vehicle technology domains.

## Methodology for Autonomous Vehicle Patent Innovation Trend Analysis 

### 1. Data Preparation and Preprocessing
The methodology begins by loading patent data from JSONL format and preprocessing textual content from titles, abstracts, and claims. Patent-specific boilerplate language is normalized while preserving technical terminology. Temporal markers are established using the earliest claim dates as the primary timeline reference for trend analysis.

### 2. Meaningful Term Extraction
A multi-layered approach extracts technically relevant terms using both linguistic and domain-specific methods:
- **NLP-based extraction**: Employs spaCy for noun phrase identification and compound term detection while preserving proper grammatical structures
- **Domain-specific pattern matching**: Uses regex patterns to capture AV-specific terminology across domains like perception systems, localization, path planning, V2X communication, and safety standards
- **Technical n-gram analysis**: Identifies 2-3 word combinations with technical relevance based on POS tagging patterns

### 3. Term Filtering and Quality Control
Generic patent language and boilerplate terms are filtered out using comprehensive stopword lists. Terms undergo relevance scoring based on technical keywords, proper phrase structure validation, and awkward phrase detection to ensure meaningful extraction quality.

### 4. Temporal Trend Analysis
Time periods are segmented (yearly/quarterly) with minimum patent thresholds per period. Term frequency normalization by patent count enables fair comparison across periods. Pearson correlation analysis identifies trending (positive correlation) and declining (negative correlation) terms with statistical significance testing.

### 5. Semantic Evolution Analysis
Sentence-BERT embeddings capture semantic relationships between patents within each time period. Cosine similarity measurements between consecutive periods identify significant technological shifts and gradual evolution patterns in the innovation landscape.

### 6. Applicant and Domain Analysis
Top applicants are analyzed for their focus evolution over time using meaningful terms. Domain-specific trend analysis categorizes innovations across key AV technology areas, revealing which domains show strongest growth or decline patterns.

### 7. Visualization and Reporting
Comprehensive visualizations include trending term timelines, semantic evolution plots, applicant activity patterns, and technology shift detection, culminating in detailed reports with statistical insights and strategic implications.

## Methodology for Unstructured to Structured Autonomous Vehicle Patent Data Analysis Pipeline

### **1. Data Preprocessing & Filtering**
The pipeline begins by loading patent data from JSONL format and cross-referencing with existing processed records to identify missing patents for analysis. Text preprocessing involves cleaning figure references, claim numbering, and normalizing whitespace to prepare structured input for the language model.

### **2. Token Management & Content Prioritization**
Given API token limits (3,000 tokens per patent), the system implements intelligent content truncation with hierarchical priority: patent title (always included), abstract (if space permits), and claims (truncated if necessary). This ensures comprehensive coverage while respecting API constraints.

### **3. Structured Analysis via LLM**
Each patent undergoes analysis using Gemini 1.5 Flash API with a carefully crafted prompt that extracts four key components:
- **Core Innovation**: Problem addressed, proposed solution, novelty aspects, and technical approach
- **Conceptual Categories**: Primary and secondary categorizations with confidence scores
- **AV Technology Areas**: Classification into predefined autonomous vehicle domains (perception, localization, control systems, etc.)

### **4. Robust API Integration**
The pipeline implements comprehensive error handling with exponential backoff for server errors, respect for rate limits (429 errors), and automatic retry mechanisms. Conservative delays between requests prevent API exhaustion while maintaining processing continuity.

### **5. Progressive Checkpointing**
To handle large datasets reliably, the system saves progress every 50 patents, creating checkpoint files that enable seamless resumption if processing is interrupted. This ensures no work is lost during extended processing sessions.

### **6. Multi-Format Output Generation**
Final results are exported in multiple formats (CSV, Excel, JSON, Pickle) to support various downstream ML applications. The structured output includes both original patent metadata and extracted analytical insights, creating a comprehensive dataset ready for machine learning model training, clustering analysis, or technology trend identification.

This methodology transforms unstructured patent text into structured, ML-ready data while maintaining processing reliability and scalability.

## Methodology for Autonomous Vehicle Patent Technology Emergence Analysis

### 1. Data Preprocessing and Feature Engineering
The methodology begins with loading patent data from JSON format and extracting key features including publication dates, AV technology areas, CPC symbols, applicant information, and patent claims. The system creates an exploded dataset where each patent-technology combination forms a separate record, enabling granular analysis of technology-specific trends. Time-based features are engineered, including monthly aggregations, filing-to-publication timelines, and text complexity metrics.

### 2. Time Series Construction
Patent data is aggregated into monthly time series for each technology area, creating comprehensive temporal datasets that capture patent counts, unique applicants, innovation quality metrics (token counts, claim complexity), and market concentration indices. The system generates rolling averages and velocity calculations to smooth short-term fluctuations and identify underlying trends.

### 3. Predictive Modeling
Two complementary forecasting approaches are implemented: Prophet models for time series decomposition with seasonality detection, and ensemble machine learning using Random Forest and Gradient Boosting regressors. Features include lagged patent counts, rolling statistics, trend indicators, seasonal components, and competitive landscape metrics. Cross-validation ensures model robustness across different time periods.

### 4. Emergence Score Calculation
A composite emergence score integrates multiple dimensions: growth rate (recent vs. historical patent activity), acceleration (second derivative of patent trends), applicant diversity (market competition level), market concentration (Herfindahl index), innovation quality (average token complexity), and categorization confidence. Scores are normalized and weighted to create a unified ranking system.

### 5. Insight Generation and Visualization
The system produces comprehensive reports identifying top emerging technologies, market dynamics analysis, and competitive landscape insights. Multi-dimensional visualizations include emergence-growth scatter plots, technology portfolio quadrant analysis, and market concentration assessments. The methodology enables identification of breakthrough technologies, market consolidation patterns, and innovation hotspots within the autonomous vehicle patent landscape.

This approach provides stakeholders with data-driven insights for strategic technology investment and competitive intelligence decisions.

## Methodology for Autonomous Vehicle Patent Innovation Outlier Detection

### 1. Data Preprocessing and Preparation
The analysis begins by loading patent data from JSON format and preprocessing key fields including publication dates, abstract text, claims, and descriptions. Missing values are handled through imputation, and temporal features such as patent age and claim-to-publication gaps are calculated to establish baseline characteristics.

### 2. Multi-Dimensional Feature Extraction
Three comprehensive feature categories are extracted:

**Textual Features**: TF-IDF vectorization of abstracts and claims to measure textual uniqueness through cosine similarity analysis. Technical term density and novelty language indicators are quantified to assess innovation vocabulary usage.

**Metadata Features**: Temporal anomalies in publication patterns, CPC classification rarity scores, applicant technology diversity metrics, and cross-technology area concentration are analyzed to identify strategic shifts and unusual filing behaviors.

**Innovation Pattern Features**: Cross-domain innovation scores measuring patents spanning multiple traditional domains (hardware, software, AI/ML, communication, safety), invention intensity calculations, and problem-solution novelty gaps are computed.

### 3. Multi-Method Outlier Detection
Four complementary detection algorithms are employed:
- **Isolation Forest** for general anomaly detection
- **Autoencoder Neural Networks** for reconstruction-based outlier identification
- **DBSCAN Clustering** to identify patents in sparse regions
- **Statistical Methods** using Mahalanobis distance for multivariate outliers

### 4. Ensemble Scoring and Analysis
Results from all detection methods are normalized and combined using weighted averaging to create robust outlier scores. The top 15% of patents are classified as radical innovations. Detailed characterization analyzes outlier patterns across applicants, technology areas, and temporal distributions.

### 5. Strategic Insight Generation
The methodology identifies companies showing strategic pivots through temporal outlier rate analysis and generates comprehensive insights on innovation leaders, emerging technology trends, and novel patent characteristics specific to autonomous vehicle technologies.

This multi-faceted approach ensures robust identification of truly innovative patents while minimizing false positives through ensemble validation.
