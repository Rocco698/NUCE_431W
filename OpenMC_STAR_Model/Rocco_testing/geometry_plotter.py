# cSpell:disable

# Necessary imports
import numpy as np # numerical tools
import os
import openmc # openMC
import openmc.stats # For Plasma source
from openmc import IndependentSource # For Plasma source
from typing import Tuple, List, Dict # For Plasma source
import pandas as pd # For Excel
import os # For Excel
import matplotlib.pyplot as plt # plotting tools
from IPython.display import Image
from openmc_plasma_source import tokamak_source # Ring source, make sure to download: pip install openmc_plasma_source
import urllib.request

# ##############################################
#       MATERIALS
# ##############################################
#Material Initialization
Steel_material = openmc.Material(name='Steel_material')
Shielding_material = openmc.Material(name='Shielding_material')
Breeder_material = openmc.Material(name='Breeder_material')
Coolant_material = openmc.Material(name='Coolant_material')

# fuel temporary
fuel = openmc.Material(name="fuel")
fuel.add_nuclide('U238', 0.97, 'wo')
fuel.add_nuclide('U235', 0.03, 'wo')

# complement air
air = openmc.Material(name="air")
air.set_density('g/cc', 0.001225)
air.add_element('N', 0.784431, 'wo')
air.add_element('O', 0.215569, 'wo')

#Steel-EUROFER97
Steel_material.add_element('Fe', 0.8924, 'wo')
Steel_material.add_element('C', 0.0011, 'wo')
Steel_material.add_element('Cr', 0.09, 'wo')
Steel_material.add_element('W', 0.011, 'wo')
Steel_material.add_element('Mn', 0.004, 'wo')
Steel_material.add_element('Ta', 0.0012, 'wo')
Steel_material.add_element('N', 0.0003, 'wo')
#Shielding-B4C
Shielding_material.add_element('B',4.0,'ao')
Shielding_material.add_element('C',1.0,'ao')
Shielding_material.set_density('g/cm3',2.50)
#List of Breeders-PbLi/FLiBe/Li/Li4SiO4
    ##PbLi
Breeder_material.add_element('Pb',0.83,'ao')
Breeder_material.add_element('Li',0.17,'ao')
#Breeder_material.add_element('Li',0.17,enrichment=92,enrichment_target='Li6')
Breeder_material.set_density('g/cm3',9.5)
    ##FLiBe
Breeder_material.add_element('F',4.0,'ao')
Breeder_material.add_element('Li',2.0,'ao')
#Breeder_material.add_element('Li',2.0,enrichment=92,enrichment_target='Li6')
Breeder_material.add_element('Be',1.0,'ao')
Breeder_material.set_density('g/cm3',1.94)
    ##Li
Breeder_material.add_element('Li',1.0,'ao')
#Breeder_material.add_element('Li',1.0,enrichment=92,enrichment_target='Li6')
Breeder_material.set_density('g/cm3',0.534)
    ##Li4SiO4
Breeder_material.add_element('Li',4.0,'ao')
#Breeder_material.add_element('Li',4.0,enrichment=92,enrichment_target='Li6')
Breeder_material.add_element('Si',1.0,'ao')
Breeder_material.add_element('O',4.0,'ao')
Breeder_material.set_density('g/cm3',2.35)
#Coolant-He (8MPA)
Coolant_material.add_element('He',1.0,'ao')
Coolant_material.set_density('kg/m3',5.0)

mat_list= openmc.Materials([Steel_material, Shielding_material, Breeder_material, Coolant_material, fuel, air])
mat_list.export_to_xml()

mat_list.cross_sections = "/Users/rocco698/Desktop/JENDL5/jendl-5-hdf5/cross_sections.xml"
print('materials export success')


# ################################################
#       GEOMETRY DEFINITION
# ################################################

dag_univ = openmc.DAGMCUniverse('/Users/rocco698/Desktop/Undergrad/Spring_2026/NUCE_431W/NUCE_431W/OpenMC_STAR_Model/CAD_TO_OPENMC/STAR5_Whole.h5m')

sim_univ = dag_univ.bounded_universe(boundary_type = 'reflective', padding_distance = 30.0)



geometry = openmc.Geometry(sim_univ)
geometry.export_to_xml()
print(geometry) #Look into plotting later
print(mat_list)


# ################################
#  Plots Definition
# ################################

ww = 15000
plot1 = openmc.Plot()
plot1.width = (ww,ww)
plot1.basis = 'yz'
plot1.pixels = (900,900)
plot1.color_by = 'material'
plot1.filename = 'RadialView'
plots = openmc.Plots([plot1])
plots.export_to_xml()

# Set the environment variable for cross sections
os.environ["OPENMC_CROSS_SECTIONS"] = "/Users/rocco698/Desktop/JENDL5/jendl-5-hdf5/cross_sections.xml"

openmc.plot_geometry()
