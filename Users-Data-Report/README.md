# Users Data Report

**Portfolio project | Python, Pandas, Google AI Studio (AI-assisted exploration)**

## Overview
This project explores a workflow for converting unclean or unstructured user-provided data into a structured dataset, then presenting data-quality checks, summary KPIs, charts, and explanations.

## Repository contents
- `src/users_data_report.py` — recreated, reusable local analysis script for CSV and Excel files.
- `requirements.txt` — Python dependencies.
- `outputs/` — generated locally when the script is run; not committed by default.

**Transparency:** The original project source code and original working dataset were not available during this repository update. The script in `src/` is a newly recreated starter based on the documented project workflow; it is not represented as the recovered original application. It performs local cleaning and exploratory summaries. A Google AI Studio integration, interactive upload interface, and AI question-answering feature are not included in this script.

## Run locally
1. Install Python 3.10 or newer.
2. From this folder, install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run on your own CSV or Excel file:
   ```bash
   python src/users_data_report.py path/to/your_file.csv
   ```
   For Excel, replace the input with `path/to/your_file.xlsx`.
4. Open the generated `outputs/` folder.

## Outputs
- `cleaned_data.csv` — blank rows and exact duplicate rows removed; surrounding text whitespace trimmed.
- `kpi_summary.csv` — row/column counts, duplicates removed, missing cells, and field counts.
- `missing_values.csv` — missing count and percentage by column.
- `numeric_summary.csv` — descriptive statistics for numeric fields, when present.
- `charts/` — histograms for numeric fields and top-value bar charts for categorical fields.

## Important limitations
- Cleaning is intentionally conservative. It does not guess missing values, remove outliers, or infer business-specific rules.
- Review dates, IDs, currency, ratings, and category labels manually.
- Do not upload private, personal, or confidential data to GitHub.
- AI-generated explanations must be checked against the underlying data before use.
- The script does not create an interactive dashboard or connect to Google AI Studio.

## Next development steps
Add a permitted sample dataset, a notebook with project-specific analysis, verified screenshots of the original AI Studio workflow, and an optional AI Q&A layer with API keys stored outside source control.
