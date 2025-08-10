
This project analyzes sector ETF returns across different macroeconomic regimes and provides an interactive Streamlit dashboard to visualize performance, track KPI metrics, and view sector descriptions.

Features
Polygon API Integration – Pulls historical daily sector ETF prices directly from the Polygon.io API.

Jupyter Notebooks for data cleaning, analysis, and regime classification.

Streamlit Dashboard (Streamlit_Sector_Dashboard_KPIs.py) to interactively:

    Filter by macro regime.

    View best-performing sectors and KPI metrics.

    Display average sector returns in bar chart format.

    View sector descriptions for context.

Data Sources:

Historical price data for sector ETFs (e.g., XLK, XLF, XLE) was retrieved using the Polygon API.
Macroeconomic indicators (CPI, Fed Funds Rate) were sourced from the Federal Reserve Economic Data (FRED) API.

Requirements
To run this project, install dependencies:

Bash
pip install -r requirements.txt

Running the Dashboard
In your terminal:

Bash
cd Regime_Research
streamlit run Streamlit_Sector_Dashboard_KPIs.py



Future Improvements:
Connect to live market data via the Polygon API for continuous updates.

Expand regime detection to more categories.

Deploy the Streamlit app online for public access.




