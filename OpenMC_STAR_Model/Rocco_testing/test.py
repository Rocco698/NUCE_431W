# cSpell:disable

# Necessary imports
import numpy as np # numerical tools
import os
import openmc # openMC
import openmc.cell
import openmc.stats # For Plasma source
from openmc import IndependentSource # For Plasma source
from typing import Tuple, List, Dict # For Plasma source
import pandas as pd # For Excel
import os # For Excel
import matplotlib.pyplot as plt # plotting tools
from IPython.display import Image
from openmc_plasma_source import fusion_ring_source # Ring source, make sure to download: pip install openmc_plasma_source
import urllib.request

# ##############################################
#       MATERIALS
# ##############################################
#Material Initialization
Steel_material = openmc.Material(name='Steel_material')
Shielding_material = openmc.Material(name='Shielding_material')
Breeder_material = openmc.Material(name='Breeder_material')
Coolant_material = openmc.Material(name='Coolant_material')
plasma_material = openmc.Material(name = 'Plasma_Material')
fuel = openmc.Material(name = 'fuel')

# plasma_material (void)
plasma_material.add_element('Ar', 1.0)
plasma_material.set_density('g/cm3', 1.00)

# fuel?
fuel.add_nuclide('H3', 0.5, 'wo')
fuel.add_nuclide('H2', 0.5, 'wo')

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

mat_list= openmc.Materials([Steel_material, Shielding_material, Breeder_material, Coolant_material, plasma_material, fuel])
mat_list.export_to_xml()

mat_list.cross_sections = "/Users/rocco698/Desktop/JENDL5/jendl-5-hdf5/cross_sections.xml"
print('materials export success')


# ################################################
#       GEOMETRY DEFINITION
# ################################################

dag_univ = openmc.DAGMCUniverse('/Users/rocco698/Desktop/Undergrad/Spring_2026/NUCE_431W/NUCE_431W/OpenMC_STAR_Model/CAD_TO_OPENMC/STAR5_Whole.h5m')

sim_univ = dag_univ.bounded_universe(boundary_type = 'reflective', padding_distance = 30.0)

plasma_cell = openmc.Cell(cell_id = 63, name = 'Plasma Region')


geometry = openmc.Geometry(sim_univ)
geometry.export_to_xml()
print(geometry) #Look into plotting later
print(mat_list)

# #################################################
#       SOURCE DEFINITION
# #################################################

plasma_source = fusion_ring_source(
    radius = 700,
    angles = (0.0, 2 * np.pi),
    temperature = 20000.0,
    fuel={"D": 0.5, "T": 0.5},
)


# Create data frame from excel sheet #
df = pd.read_excel('/Users/rocco698/Desktop/Undergrad/Spring_2026/NUCE_431W/NUCE_431W/OpenMC_STAR_Model/STAR40_Neutonics_Data.xlsx')
radi_s = df.loc[:,"R [m]"].tolist()
z_pos = df.loc[:,"Z[m]"].tolist()
norm_activ = df.loc[:,"norm"].tolist()


# #################################################
#       TALLIES
# #################################################

###############################################################################
# Define problem settings
###############################################################################

settings = openmc.Settings()
settings.run_mode = 'fixed source'
settings.dagmc = True
settings.batches = 10
settings.particles = 5000
settings.source = plasma_source
settings.export_to_xml()

print(settings)

# ################################
#  Plots Definition
# ################################

ww = 15000
plot1 = openmc.Plot()
plot1.width = (ww,ww)
plot1.basis = 'yz'
plot1.color_by = 'material'
plot1.filename = 'TestImg'
plot1.pixels = (900,900)
plots = openmc.Plots([plot1])
plots.export_to_xml()

# Set the environment variable for cross sections
os.environ["OPENMC_CROSS_SECTIONS"] = "/Users/rocco698/Desktop/JENDL5/jendl-5-hdf5/cross_sections.xml"

openmc.plot_geometry()
openmc.run()
