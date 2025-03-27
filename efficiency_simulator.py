
def calculate_efficiency(power_input, core_mass, ambient_temp, target_temp=500):
    specific_heat = 0.46  # J/g°C
    mass_grams = core_mass * 1000
    energy_required = mass_grams * specific_heat * (target_temp - ambient_temp)  # in J
    time_seconds = energy_required / power_input
    return {
        "energy_kJ": round(energy_required / 1000, 2),
        "time_minutes": round(time_seconds / 60, 2)
    }
