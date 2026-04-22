# cSpell:disable


import numpy as np                                  #> numerical analysis
import os                                           #> path manipulation

import openmc                                       #> openMC
import openmc.cell              
import openmc.stats                                 #> dependency for plasma source
from openmc import IndependentSource                #> plasma source

from typing import Tuple, List, Dict 
import pandas as pd                                 #> data import via excel
import matplotlib.pyplot as plt                     #> plotting
from IPython.display import Image                   #> jupyter
import neutronics_material_maker as nmm             #> does not work don't use

from openmc_plasma_source import fusion_ring_source #> Ring source, make sure to download: pip install openmc_plasma_source
import urllib.request
from openmc_regular_mesh_plotter import plot_mesh_tally

# ##############################################
#       MATERIALS
# ##############################################

all_materials = nmm.AvailableMaterials()
print(all_materials.keys())


#> Steel-EUROFER97
Steel_material = openmc.Material(name='Steel_material')
Steel_material.add_element('Fe', 0.8924, 'wo')
Steel_material.add_element('C', 0.0011, 'wo')
Steel_material.add_element('Cr', 0.09, 'wo')
Steel_material.add_element('W', 0.011, 'wo')
Steel_material.add_element('Mn', 0.004, 'wo')
Steel_material.add_element('Ta', 0.0012, 'wo')
Steel_material.add_element('N', 0.0003, 'wo')


#> Shielding-B4C

Shielding_material = openmc.Material(name='Shielding_material')
Shielding_material.add_element('B',4.0,'ao')
Shielding_material.add_element('C',1.0,'ao')
Shielding_material.set_density('g/cm3',2.50)

'''
Shielding_material = openmc.Material(name = 'Shielding_material')
Shielding_material.add_element('Pb', 1.0, 'ao')
Shielding_material.set_density('g/cm3', 11.3)
'''
#> Copper50Hatelloy50HTS

'''
#> Hastelly C-276
Hastelloy = openmc.Material(name = 'Hastelloy')
Hastelloy.add_element('Ni', 0.6177, 'ao')
Hastelloy.add_element('Cr', 0.1884, 'ao')
Hastelloy.add_element('Mo', 0.1053, 'ao')
Hastelloy.add_element('Fe', 0.0623, 'ao')
Hastelloy.add_element('W', 0.0129, 'ao')
Hastelloy.add_element('Co', 0.0134, 'ao')
Hastelloy.set_density('g/cm3', 8.89)

Copper = openmc.Material(name = 'Copper')
Copper.add_element('Cu', 1.0)
Copper.set_density('g/cm3', 8.96)

Copper_material = openmc.Material.mix_materials([Hastelloy, Copper], [0.5, 0.5], 'vo')
Copper_material.name = 'Copper_material'
'''

#> MULTIPLIER ONLY
Mult_material = openmc.Material(name = 'Mult_material')
Mult_material.add_element('Pb', 1.0)
Mult_material.set_density('g/cm3', 10.5)

#> PbLi (breeder)

Breeder_material = openmc.Material(name='Breeder_material')
Breeder_material.add_element('Pb', 0.83, 'ao')
#Breeder_material.add_element('Li', 0.17, 'ao', enrichment=90.0, enrichment_target='Li6', enrichment_type='ao')
Breeder_material.add_element('Li', 0.17, 'ao')
#Breeder_material.add_element('Li', 1.0, enrichment=90.0, enrichment_target='Li6', enrichment_type='ao')
Breeder_material.set_density('g/cm3', 0.48)


#> definitions for file specific breeder materials

#> FLiBe
'''
Breeder_material = openmc.Material(name = 'Breeder_material')
Breeder_material.add_element('Li', 0.285, 'ao')
Breeder_material.add_element('F', 0.572, 'ao')
Breeder_material.add_element('Be', 0.143, 'ao')
Breeder_material.set_density('g/cm3',2.0)
'''
#> FLiNaK
'''
LiF = openmc.Material()
LiF.add_elements_from_formula('LiF')

NaF = openmc.Material()
NaF.add_elements_from_formula('NaF')

KF = openmc.Material()
KF.add_elements_from_formula('KF')

Breeder_material = openmc.Material.mix_materials([LiF, NaF, KF], [0.29, 0.29, 0.42], 'wo')
Breeder_material.name = 'Breeder_material'
Breeder_material.set_density('g/cm3', 2.0)
'''

#> Li4SiO4
'''
Breeder_material = openmc.Material(name = 'Breeder_material')
Breeder_material.add_elements_from_formula('Li4SiO4', enrichment_target='Li6', enrichment=90.0, enrichment_type='ao')
Breeder_material.set_density('g/cm3', 2.39)
'''

#> Li8ZrO6
'''
Breeder_material = openmc.Material(name = 'Breeder_material')
Breeder_material.add_elements_from_formula('Li8ZrO6', enrichment_target='Li6', enrichment=90.0, enrichment_type='ao')
Breeder_material.set_density('g/cm3', 2.58)
'''

#> Li2O
'''
Breeder_material = openmc.Material(name = 'Breeder_material')
Breeder_material.add_elements_from_formula('Li2O', enrichment_target='Li6', enrichment=90.0, enrichment_type='ao')
Breeder_material.set_density('g/cm3', 2.013)
'''
#> LiAlO2 
'''
Breeder_material = openmc.Material(name = 'Breeder_material')
Breeder_material.add_elements_from_formula('LiAlO2', enrichment_target='Li6', enrichment=90.0, enrichment_type='ao')
Breeder_material.set_density('g/cm3', 2.62)
'''
#> Li5AlO4
'''
Breeder_material = openmc.Material(name = 'Breeder_material')
Breeder_material.add_elements_from_formula('Li5AlO4', enrichment_target='Li6', enrichment=90.0, enrichment_type='ao')
Breeder_material.set_density('g/cm3', 2.17)
'''
#> Li2ZrO3
'''
Breeder_material = openmc.Material(name = 'Breeder_material')
Breeder_material.add_elements_from_formula('Li2ZrO3', enrichment_target='Li6', enrichment=90.0, enrichment_type='ao')
Breeder_material.set_density('g/cm3', 4.15)
'''
#> Li2TiO3
'''
Breeder_material = openmc.Material(name = 'Breeder_material')
Breeder_material.add_elements_from_formula('Li2TiO3', enrichment_target='Li6', enrichment=90.0, enrichment_type='ao')
Breeder_material.set_density('g/cm3', 3.43)
'''












#> Coolant-He (8MPA)
Coolant_material = openmc.Material(name='Coolant_material')
Coolant_material.add_element('He',1.0,'ao')
Coolant_material.set_density('kg/m3',5.0)


mat_list= openmc.Materials([Breeder_material, Steel_material, Shielding_material, Mult_material])
mat_list.export_to_xml()

mat_list.cross_sections = "/Users/rocco698/Desktop/JENDL5/jendl-5-hdf5/cross_sections.xml"
print('materials export success')


# ################################################
#       GEOMETRY DEFINITION
# ################################################

dag_univ = openmc.DAGMCUniverse('/Users/rocco698/Desktop/Undergrad/Spring_2026/NUCE_431W/NUCE_431W/OpenMC_STAR_Model/CAD_TO_OPENMC/Scaled_STL_output/config4_scaled.h5m', auto_geom_ids = True)

root_cell = openmc.Cell(fill = dag_univ)

boundary = openmc.Sphere(r = 2500.0, boundary_type = 'vacuum')

root_cell.region = -boundary

cell_count = dag_univ.n_cells

print()
print(f"Number of Cells within Model: {cell_count}")
print()

print()
print(f"Path to Model:  {dag_univ.filename}")
print()

print()
print(f"Cells: {dag_univ.get_all_cells}")

# , padding_distance = 30.0



#sim_univ = dag_univ.bounded_universe(bounding_cell_id= 999, boundary_type = 'vacuum')


geometry = openmc.Geometry([root_cell,])
geometry.export_to_xml()

print(geometry)
print(mat_list)

# #################################################
#       SOURCE DEFINITION
# #################################################

#> Heavy use of code from: https://github.com/fusion-energy/openmc-plasma-source/blob/main/examples/ring_source_example.py
def onion_ring_source(radius: float, z_placement: float, activity: float, #> these are the only inputs you should need to change
                      angles: Tuple[float, float] = (0, 2 * np.pi),       #> not these
                      fuel: Dict = {"D": 0.5, "T": 0.5}):                 #> not these

    """Creates a list of openmc.IndependentSource objects in a ring shape.

    Useful for simulations where all the plasma parameters are not known and
    this simplified geometry will suffice. Resulting ring source will have an
    energy distribution according to the fuel composition.
    Args:
        radius: the inner radius of the ring source, in metres
        angles: the start and stop angles of the ring in radians
       z_placement: Location of the ring source (m). Defaults to 0.
        temperature: Temperature of the source (eV). #Unused#
        fuel: Isotopes as keys and atom fractions as values
    Returns:
        A list of one openmc.IndependentSource instance.
    """

    if not isinstance(radius, (int, float)) or radius <= 0:
        raise ValueError("Radius must be a float strictly greater than 0.")

    if not (
        isinstance(angles, tuple)
        and len(angles) == 2
        and all(
            isinstance(angle, (int, float)) and -2 * np.pi <= angle <= 2 * np.pi
            for angle in angles
        )
    ):

        raise ValueError("Angles must be a tuple of floats between zero and 2 * np.pi")
    if not isinstance(z_placement, (int, float)):
        raise TypeError("Z placement must be a float.")

    source = IndependentSource()

    source.space = openmc.stats.CylindricalIndependent(
        r=openmc.stats.Discrete([radius*100], [1]),
        phi=openmc.stats.Uniform(a=angles[0], b=angles[1]),
        z=openmc.stats.Discrete([z_placement*100], [1]),
        origin=(0.0, 0.0, 0.0) )
    source.energy =openmc.stats.Discrete([14.0e6], [1.0]) #> (14 MeV neutrons, 100% distribution)
    source.angle = openmc.stats.Isotropic()
    source.strength = activity
    return source

#> create data frame from excel sheet
excel_path = "/Users/rocco698/Desktop/Undergrad/Spring_2026/NUCE_431W/NUCE_431W/OpenMC_STAR_Model/STAR40_Neutonics_Data.xlsx"
df = pd.read_excel(excel_path)
radi_s = df.loc[:,"R [m]"].tolist()
z_pos = df.loc[:,"Z[m]"].tolist()
norm_activ = df.loc[:,"norm"].tolist()

#> sources = onion_ring_source(radius= radi_s[0], z_placement= z_pos[0], activity= norm_activ[0])

iter=0
sources = []
while iter <= 501:
    sources.append(onion_ring_source(radius=radi_s[iter], z_placement=z_pos[iter], activity=norm_activ[iter]))
    iter += 1
print('> Sources array:', sources)


#> create data frame from excel sheet
df = pd.read_excel('/Users/rocco698/Desktop/Undergrad/Spring_2026/NUCE_431W/NUCE_431W/OpenMC_STAR_Model/STAR40_Neutonics_Data.xlsx')
radi_s = df.loc[:,"R [m]"].tolist()
z_pos = df.loc[:,"Z[m]"].tolist()
norm_activ = df.loc[:,"norm"].tolist()


# #################################################
#       TALLIES
# #################################################

tallies_file = openmc.Tallies()

#> mesh for visualization
mesh = openmc.RegularMesh()
mesh.dimension = [1, 1000, 1000]
mesh.lower_left = [-1000.0, -1000.0, -1000.0]
mesh.upper_right = [1000.0, 1000.0, 1000.0]

mesh_filter = openmc.MeshFilter(mesh)

#> filter for TBR only
breeding_filter = openmc.MaterialFilter(bins = Breeder_material)

#> tallies for pictures
tally_f = openmc.Tally(name = 'flux')
tally_f.filters = [mesh_filter]
tally_f.scores = ['flux', 'absorption', '(n,t)', '(n,Xt)']

#> TBR tally
tally_breeding = openmc.Tally(name = 'Tritium')
tally_breeding.filters = [breeding_filter]
tally_breeding.scores = ['(n,t)', '(n,Xt)']

#> current / leakage tally
energy_bins = np.logspace(1, 8, 700)  # eV (from thermal → fast)
energy_filter = openmc.EnergyFilter(energy_bins)

tallies_file.append(tally_f)
tallies_file.append(tally_breeding)


tallies_file.export_to_xml()

###############################################################################
# Define problem settings
###############################################################################

settings = openmc.Settings()
settings.run_mode = 'fixed source'
settings.dagmc = True
settings.batches = 10
settings.particles = 10000
settings.source = sources
settings.source_rejection_fraction = 0.01
settings.export_to_xml()

print(settings)

# ################################
#  Plots Definition
# ################################

ww = 1500
plot1 = openmc.Plot()
plot1.width = (ww,ww)
plot1.basis = 'yz'
plot1.pixels = [1920, 1080]
plot1.color_by = 'material'
plot1.colors = {
    Breeder_material: 'deeppink',
    Shielding_material: 'black',
    Steel_material: 'blue',
    Mult_material: 'green',
}
plot1.filename = 'TESTIMG_config4'
plot1.pixels = (900,900)
plots = openmc.Plots([plot1])
plots.export_to_xml()

# Set the environment variable for cross sections
os.environ["OPENMC_CROSS_SECTIONS"] = "/Users/rocco698/Desktop/JENDL5/jendl-5-hdf5/cross_sections.xml"

openmc.plot_geometry()
openmc.run()










