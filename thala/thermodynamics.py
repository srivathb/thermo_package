"""
Thermodynamics Module

This module provides functions to calculate thermodynamic properties and changes for chemical reactions.

This module has two functions as of now:

    - `enthalpy_of_reaction(standard_enthalpies, reactants, products)`: Calculate the enthalpy change (∆H) for a chemical reaction.
    - `work_done(pressure, volume_change)`: Calculate the work done (W) in a thermodynamic process.
"""


def enthalpy_of_reaction(standard_enthalpies, reactants, products):
    """
    Calculate enthalpy change (∆H) for a chemical reaction. This function calculates enthalpy of reaction using standard enthalpies of formation.

    Parameters:
        standard_enthalpies (dict): Dictionary of standard enthalpies of formation (in kJ/mol) for reactants and products.
        reactants (dict): Dictionary of reactants and their stoichiometric coefficients.
        products (dict): Dictionary of products and their stoichiometric coefficients.

    Returns:
        float: Enthalpy change (∆H) in kJ/mol.

    Formula:
        ∆H = Σ(products[species] * standard_enthalpies[species]) - Σ(reactants[species] * standard_enthalpies[species])
    """
    delta_H = sum(
        products[species] * standard_enthalpies[species] for species in products
    ) - sum(reactants[species] * standard_enthalpies[species] for species in reactants)
    return delta_H


def work_done(pressure, volume_change, constant_pressure=False, constant_volume=False):
    """
    Calculate the work done (W) in a thermodynamic process. This functions deals only with isobaric and isochoric processes as of now.

    Parameters:
        pressure (float): Pressure in Pascals (Pa).
        volume_change (float): Volume change (ΔV) in cubic meters (m³).
        constant_pressure (bool): Flag indicating constant pressure process.
        constant_volume (bool): Flag indicating constant volume process.

    Returns:
        float: Work done (W) in Joules.

    Formula:
        - If constant pressure process: W = P * ΔV
        - If constant volume process: W = 0
        - Otherwise: W = None (Invalid process type)
    """
    if constant_pressure:
        work_done = pressure * volume_change
    elif constant_volume:
        work_done = 0.0  # No work done at constant volume
    else:
        work_done = None  # Invalid process type

    return work_done
