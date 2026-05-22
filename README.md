# Greenwashing-Auditor

I built this project to help make sense of corporate environmental claims; it's pretty common for companies to make big promises about cutting emissions. This tool helps audit those claims.

## Installation

Clone this repository and set up your environment:

```bash
# Create and activate your virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install the required packages
pip install openai pandas pymupdf python-dotenv
```

How to use

1 Prepare Data: Run ⁠python create_data.py⁠ to get your company data ready.

2 Extraction: Use ⁠python extract.py⁠ to pull the relevant information.

3 Run Audit: Execute ⁠python audit.py⁠ to perform the analysis on the company claims.

Important Note
Target Reconciliation Line: Ensure the model compares the target year emission goals against the reported emissions.

Project Structure
 ⁠audit.py⁠: The main script for running the audit.
 ⁠company_data.csv⁠: The dataset containing the corporate claims.
 ⁠create_data.py⁠: Script to generate/clean your data.
 ⁠extract.py⁠: Helper script to extract text/data for the pipeline.
 ⁠final_audit_report.json⁠: The output generated after running the audit.
 ⁠report.pdf⁠: The source document being audited.

Acknowledgements
 Built using LangChain for the RAG pipeline.
