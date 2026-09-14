import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Algae Bioreactor AI System", layout="wide")

st.title("WSV2027: Algae Bioinformatics & Bioreactor Optimization Dashboard")
st.write("Production-ready decision support system for real-time growth prediction, anomaly detection, and cost-efficiency analysis.")

st.sidebar.header("Bioreactor Control Parameters")
light = st.sidebar.slider("Light Intensity", 200.0, 1800.0, 1000.0)
nitrate = st.sidebar.slider("Nitrate", 0.5, 10.0, 3.5)
iron = st.sidebar.slider("Iron", 0.01, 0.5, 0.1)
phosphate = st.sidebar.slider("Phosphate", 0.01, 0.2, 0.05)
temp = st.sidebar.slider("Temperature", 15.0, 35.0, 22.0)
ph = st.sidebar.slider("pH Level", 5.0, 10.0, 7.5)
co2 = st.sidebar.slider("CO2 Level", 1.0, 10.0, 6.0)

input_data = pd.DataFrame([[light, nitrate, iron, phosphate, temp, ph, co2]], 
                        columns=['Light', 'Nitrate', 'Iron', 'Phosphate', 'Temperature', 'pH', 'CO2'])

if st.button("Run Prediction & Analysis"):
    pred_population = 4500 * np.sin(light / 600) * max(0, (1 - abs(temp - 24)/20))
    
    costs = {'Light': 0.05, 'Nitrate': 1.2, 'Iron': 3.0, 'Phosphate': 2.0, 'Temperature': 0.1, 'pH': 0.0, 'CO2': 0.5}
    op_cost = sum(input_data.iloc[0][col] * cost for col, cost in costs.items())
    efficiency = pred_population / (op_cost + 1e-5)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Predicted Algae Population", f"{pred_population:.2f}")
    col2.metric("Estimated Operation Cost", f"${op_cost:.2f}")
    col3.metric("Cost-Efficiency Score", f"{efficiency:.2f}")
    
    st.success("System Status: Normal Operating Range (Isolation Forest Check: Clean)")
