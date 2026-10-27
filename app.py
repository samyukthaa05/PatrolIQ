import streamlit as st
import pandas as pd
from src.data_loader import load_crime_data
from src.preprocessing import preprocess_crime_data
from src.visualization import summary_metrics, crime_type_chart, hourly_chart, map_chart

st.set_page_config(page_title="PatrolIQ | Smart Safety Analytics", page_icon="🚓", layout="wide")
st.title("🚓 PatrolIQ — Smart Safety Analytics Platform")
st.caption("Chicago crime-pattern exploration and unsupervised analytics. Historical patterns are descriptive, not individual risk predictions.")

with st.sidebar:
    st.header("Data")
    uploaded = st.file_uploader("Upload Chicago crime CSV (optional)", type=["csv"])
    use_demo = st.toggle("Use built-in demo data", value=True)
    max_rows = st.slider("Maximum rows to load", 1000, 500000, 50000, step=1000)

@st.cache_data(show_spinner=False)
def get_data(uploaded_bytes, use_demo, max_rows):
    if uploaded_bytes:
        raw = pd.read_csv(uploaded_bytes, low_memory=False, nrows=max_rows)
    elif use_demo:
        from src.data_loader import make_demo_data
        raw = make_demo_data(5000)
    else:
        return pd.DataFrame()
    return preprocess_crime_data(raw)

df = get_data(uploaded.getvalue() if uploaded else None, use_demo, max_rows)

if df.empty:
    st.info("CSV upload pannunga, illa sidebar-la built-in demo data enable pannunga.")
    st.stop()

summary_metrics(df)
st.subheader("Crime categories")
st.plotly_chart(crime_type_chart(df), use_container_width=True)
col1, col2 = st.columns(2)
with col1:
    st.subheader("Incidents by hour")
    st.plotly_chart(hourly_chart(df), use_container_width=True)
with col2:
    st.subheader("Geographic overview")
    st.plotly_chart(map_chart(df), use_container_width=True)

st.subheader("Data preview")
st.dataframe(df.head(100), use_container_width=True)
st.download_button("Download processed sample CSV", df.to_csv(index=False).encode("utf-8"), "patroliq_processed_sample.csv", "text/csv")
st.caption("Demo data is synthetic and must not be interpreted as real Chicago crime statistics.")
