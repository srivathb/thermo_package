import pytest
from thala import thermodynamics

def test_enthalpy_change():
    # Define input parameters for enthalpy change calculation
    standard_enthalpies = {'A': -100.0, 'B': 50.0, 'C': 30.0}
    reactants = {'A': 2, 'B': 1}
    products = {'C': 1}
    
    expected_enthalpy_change = 180.0  # Expected result for the test case
    # Calculate enthalpy change for the reaction and assert with expected change
    assert thermodynamics.enthalpy_of_reaction(standard_enthalpies, reactants, products) == pytest.approx(expected_enthalpy_change)
    
def test_work_done_constant_pressure():
    # Define input parameters for constant pressure process
    pressure = 100000.0  # 100 kPa
    volume_change = 1   # 1000 L = 1 m³
    
    expected_work_done = 100000.0  # W = PΔV = 100 kPa * 0.001 m³ = 100 J
    # Calculate work done at constant pressure and assert with expected work
    assert thermodynamics.work_done(pressure, volume_change, constant_pressure=True) == pytest.approx(expected_work_done)

def test_work_done_constant_volume():
    # Define input parameters for constant volume process
    pressure = 100000.0  # 100 kPa
    volume_change = 0  # No volume change
    
    expected_work_done = 0.0
    # Calculate work done at constant volume and assert with expected work (should be zero)
    assert thermodynamics.work_done(pressure, volume_change, constant_volume=True) == pytest.approx(expected_work_done)
