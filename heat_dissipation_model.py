def fin_efficiency(fin_type: str):
    """
    Return the thermal efficiency multiplier based on fin type.
    """
    if fin_type.lower() == "spiral":
        return 1.25  # Spiral fins increase surface contact
    elif fin_type.lower() == "straight":
        return 1.0
    else:
        return 1.0  # default fallback

def estimate_surface_temp(core_temp, ambient_temp, efficiency_factor):
    """
    Estimate the surface temperature for convection simulation.
    """
    return ambient_temp + (core_temp - ambient_temp) * efficiency_factor
