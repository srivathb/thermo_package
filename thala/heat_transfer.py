
"""
Heat Transfer Module

This module provides functions to calculate heat transfer rates through conduction, convection, and radiation.

This module has three functions as of now:

    - `heat_conduction_rate(k, A, delta_T, d)`: Calculate heat transfer rate through conduction.
    - `heat_convection_rate(h, A, delta_T)`: Calculate heat transfer rate through convection.
    - `heat_radiation_rate(A, T_surface, T_surroundings)`: Calculate heat transfer rate through radiation.
"""

def heat_conduction_rate(k, A, delta_T, d):
    """
    The `heat_conduction_rate` function calculates the rate of heat transfer through a material by conduction, which occurs when heat flows through a solid material due to a temperature gradient.
    
    Applicability:
    This equation applies to scenarios where heat is transferred through a solid material (e.g., walls, pipes) due to a temperature gradient.
    
    Parameters:
        k (float): Thermal conductivity of the material (in W/(m-K)).
        A (float): Cross-sectional area through which heat is transferred (in m²).
        delta_T (float): Temperature difference across the material (in Kelvin).
        d (float): Thickness of the material (in meters).

    Returns:
        float: Heat transfer rate/heat flux (Q) in watts.
        
    Formula:
    Q = k * A * (delta_T / d)
    where:
        Q is the heat transfer rate (in watts).
        k is the thermal conductivity (in W/(m-K)).
        A is the cross-sectional area (in m²).
        delta_T is the temperature difference (in Kelvin).
        d is the thickness of the material (in meters).

    """
    Q = k * A * (delta_T / d)
    return Q

def heat_convection_rate(h, A, delta_T):
    """
    The `heat_convection_rate` function calculates the rate of heat transfer through convection, which occurs between a solid surface and a fluid (liquid or gas) due to forced or natural fluid motion.
    
    Applicability:
    This equation applies to scenarios where heat is exchanged between a solid surface (e.g., radiator, heat exchanger) and a fluid (e.g., air, water) through forced or natural convection.
    
    Parameters:
        h (float): Convective heat transfer coefficient (in W/(m²-K)).
        A (float): Surface area (in m²).
        delta_T (float): Temperature difference between the surface and the fluid (in Kelvin).

    Returns:
        float: Heat transfer rate/heat flux (Q) in watts.
        
    Formula:
    Q = h * A * delta_T
    where:
        Q is the heat transfer rate (in watts).
        h is the convective heat transfer coefficient (in W/(m²-K)).
        A is the surface area (in m²).
        delta_T is the temperature difference (in Kelvin).
    """
    Q = h * A * delta_T
    return Q

def heat_radiation_rate(A, T_surface, T_surroundings):
    """
    The `heat_radiation_rate` function calculates the rate of heat transfer through radiation, which occurs between two surfaces via electromagnetic waves based on their temperatures and surface areas.
    
    Applicability:
    This equation applies to scenarios where heat is exchanged between two surfaces (e.g., spacecraft, buildings) via electromagnetic radiation.
    
    Parameters:
        sigma (float): Stefan-Boltzmann constant (5.67e-8 W/(m²-K⁴)).
        A (float): Surface area (in m²).
        T_surface (float): Surface temperature (in Kelvin).
        T_surroundings (float): Surroundings temperature (in Kelvin).

    Returns:
        float: Heat transfer rate/heat flux (Q) in watts.
        
    Formula:
    Q = sigma * A * ((T_surface ** 4) - (T_surroundings ** 4))
    where:
        Q is the heat transfer rate (in watts).
        sigma is the Stefan-Boltzmann constant (in W/(m²-K⁴)).
        A is the surface area (in m²).
        T_surface is the surface temperature (in Kelvin).
        T_surroundings is the surroundings temperature (in Kelvin).
    """
    sigma = 5.67e-8  # Stefan-Boltzmann constant in W/(m^2-K^4)
    Q = sigma * A * ((T_surface ** 4) - (T_surroundings ** 4))
    return Q
