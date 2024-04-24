import pytest
from thala import heat_transfer

def test_heat_conduction_rate():
    # Define input parameters for heat conduction rate calculation
    k_material = 0.5
    area = 2.0
    temperature_difference = 50.0
    thickness = 0.1
    
    expected_heat_conduction_rate = 500.0  # Expected result for the test case
    # Calculate heat conduction rate and assert with expected rate
    assert heat_transfer.heat_conduction_rate(k_material, area, temperature_difference, thickness) == pytest.approx(expected_heat_conduction_rate)

def test_heat_convection_rate():
    # Define input parameters for heat convection rate calculation
    h_coefficient = 10.0
    area = 2.0
    temperature_difference = 50.0
    
    expected_heat_convection_rate = 1000.0  # Expected result for the test case
    # Calculate heat convection rate and assert with expected rate
    assert heat_transfer.heat_convection_rate(h_coefficient, area, temperature_difference) == pytest.approx(expected_heat_convection_rate)

def test_heat_radiation_rate():
    # Define input parameters for heat radiation rate calculation
    sigma_constant = 5.67e-8
    area = 2.0
    surface_temperature = 300.0
    surroundings_temperature = 273.0
    
    expected_heat_radiation_rate = 288.652  # Expected result for the test case
    # Calculate heat radiation rate and assert with expected rate
    assert heat_transfer.heat_radiation_rate(area, surface_temperature, surroundings_temperature) == pytest.approx(expected_heat_radiation_rate, rel=1e-2)
