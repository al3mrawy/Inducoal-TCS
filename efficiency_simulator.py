import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the app
st.title("Efficiency Simulator")

# Sidebar inputs
st.sidebar.header("Input Parameters")

power_input = st.sidebar.number_input("Input Power (kW)", min_value=0.0, value=10.0)
output_power = st.sidebar.number_input("Output Power (kW)", min_value=0.0, value=8.0)

# Calculate efficiency
def calculate_efficiency(input_power, output_power):
    if input_power == 0:
        return 0
    return (output_power / input_power) * 100

efficiency = calculate_efficiency(power_input, output_power)

# Display result
st.subheader("Results")
st.metric("Efficiency", f"{efficiency:.2f} %")

# Plotting a simple chart
st.subheader("Efficiency Over Time (Example Data)")
time = np.arange(1, 11)
efficiency_over_time = efficiency + np.random.normal(0, 2, size=10)

fig, ax = plt.subplots()
ax.plot(time, efficiency_over_time, marker='o')
ax.set_xlabel("Time")
ax.set_ylabel("Efficiency (%)")
ax.set_title("Simulated Efficiency Over Time")
st.pyplot(fig)
