import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("🔥 Inducoal TCS - Thermal Simulation")

# Sidebar Inputs
power = st.sidebar.slider("Power Input (W)", 500, 5000, 2000)
mass = st.sidebar.slider("Core Mass (kg)", 0.5, 5.0, 2.0)
ambient_temp = st.sidebar.slider("Ambient Temperature (°C)", 0, 50, 25)
fin_type = st.sidebar.radio("Fin Type", ["Straight", "Spiral"])

# Calculate Heat Transfer
c = 0.46  # Specific heat capacity of steel (J/g·°C)
Q = mass * 1000 * c * (500 - ambient_temp)  # Total energy needed
time_to_heat = Q / power  # Seconds

# Display Results
st.metric("Energy Required (kJ)", round(Q / 1000, 2))
st.metric("Time to Reach 500°C (min)", round(time_to_heat / 60, 2))

# Plot Heating Curve
time = np.linspace(0, time_to_heat, 100)
temp = ambient_temp + (500 - ambient_temp) * (1 - np.exp(-time / (time_to_heat / 5)))
plt.figure(figsize=(6,4))
plt.plot(time / 60, temp, label="Temperature Over Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Thermal Heating Curve")
plt.legend()
plt.grid()
st.pyplot(plt)

st.success("Simulation Complete! Adjust settings to explore further.")
