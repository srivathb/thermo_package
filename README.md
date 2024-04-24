THALA: Thermodynamics Helper and Analysis Library for Applications
===============

THALA is a Python package designed to assist users with thermodynamic calculations and heat transfer analysis. It provides a set of functions to compute various thermodynamic properties, perform heat transfer calculations, and facilitate scientific analysis related to thermodynamics.

## Installation
You can install THALA using pip. Clone this git repository, then install everything in it:

```python
%%bash 
git clone https://github.com/srivathb/thermo_package.git
```

```python
!cd thermo_package && pip install .
```

## Usage

To use THALA, import the package and its submodules as follows:

```python
from thala import thermodynamics
from thala import heat_transfer
```

## Features

- Thermodynamics Module: This module has two functions - one to calculate enthalpy change and one to calculate the thermodynamic work.
  - `enthalpy_of_reaction(standard_enthalpies, reactants, products)`: Calculate the enthalpy change (∆H) for a chemical reaction.
  - `work_done(pressure, volume_change, constant_pressure=False, constant_volume=False)`: Calculate the work done (W) in a thermodynamic process.
    
- Heat Transfer Module: This module has functions that calculate the heat transfer rate for conduction, convection and radiation settings. 
  - `heat_conduction_rate(k, A, delta_T, d)`: Calculate heat transfer rate through conduction.
  - `heat_convection_rate(h, A, delta_T)`: Calculate heat transfer rate through convection.
  - `heat_radiation_rate(A, T_surface, T_surroundings)`: Calculate heat transfer rate through radiation.
    
Ensure that the necessary thermodynamic and heat transfer properties are provided as inputs to the respective functions.

### Note
THALA is designed to handle basic thermodynamic and heat transfer calculations. For more complex analyses, consider using specialized libraries or tools.

For additional details and examples, please refer to the documentation and usage guide.

Thanks for using THALA! If you have any feedback or suggestions, feel free to contribute or reach out to the project maintainer.
