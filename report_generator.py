import matplotlib.pyplot as plt
from fpdf import FPDF
import datetime
import os

def generate_simulation_report(data, filename="Inducoal_Report_Demo.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Inducoal TCS – Thermal Simulation Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.ln(10)
    for key, value in data.items():
        pdf.cell(200,
