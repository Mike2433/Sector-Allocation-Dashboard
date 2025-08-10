
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Sector Allocation Dashboard", layout="wide")

# Sample data
data = {
    "date": ["2024-08-31", "2024-09-30", "2024-10-31", "2024-11-30", "2024-12-31"],
    "XLK": [0.006993, 0.024645, -0.015592, 0.051701, -0.005177],
    "XLF": [0.045725, -0.009182, 0.025596, 0.104561, -0.058629],
    "XLE": [-0.020706, -0.038124, 0.008998, 0.078338, -0.103318],
    "regime": ["Neutral", "Easing", "Easing", "Easing", "Easing"]
}
df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

# Sector descriptions
sector_labels = {
    "XLK": "Technology",
    "XLF": "Financials",
    "XLE": "Energy"
}
sector_description_df = pd.DataFrame.from_dict(sector_labels, orient='index', columns=["Sector Description"])
sector_description_df.index.name = "Ticker"

# KPI Metric - Best Performing Sector
average_returns = df.drop(columns="regime").mean()
average_returns.index = average_returns.index.map(sector_labels)
best_sector = average_returns.idxmax()
best_value = average_returns.max()

# Sidebar
regimes = df["regime"].unique().tolist()
selected_regime = st.sidebar.selectbox("Select Regime", regimes)

# Filter data
filtered_df = df[df["regime"] == selected_regime]
sector_returns = filtered_df.drop(columns=["regime"])

# Main Dashboard
st.title("Sector Returns by Macro Regime")
st.write(f"**Selected Regime:** {selected_regime}")

# KPI Display
st.metric(label="Best Performing Sector", value=best_sector, delta=f"{best_value:.2%}")

# Plot
fig, ax = plt.subplots()
sector_returns.mean().sort_values().plot(kind="barh", ax=ax, color="skyblue")
ax.set_title(f"Average Sector Returns ({selected_regime} Regime)")
ax.set_xlabel("Return")
st.pyplot(fig)

# Sector Descriptions Table
with st.expander("Sector Descriptions"):
    st.dataframe(sector_description_df)

# Optionally show raw data
with st.expander("Show raw data"):
    st.dataframe(filtered_df)
