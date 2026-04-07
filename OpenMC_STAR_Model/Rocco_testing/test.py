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

from openmc_plasma_source import fusion_ring_source #> Ring source, make sure to download: pip install openmc_plasma_source
import urllib.request
from openmc_regular_mesh_plotter import plot_mesh_tally

# ##############################################
#       MATERIALS
# ##############################################

#> plasma_material (void)
plasma_material = openmc.Material(name = 'Plasma_Material')
plasma_material.add_element('Ar', 1.0)
plasma_material.set_density('g/cm3', 0.00000000000000001)


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


#> PbLi (breeder)
Breeder_material = openmc.Material(name='Breeder_material')
Breeder_material.add_element('Pb',0.83,'ao')
Breeder_material.add_element('Li',0.17,'ao')
Breeder_material.set_density('g/cm3',9.5)

#> definitions for file specific breeder materials
Breeder97Steel3IB = openmc.Material(name = "Breeder97Steel3IB")
Breeder97Steel3IB.add_element('Pb',0.83,'ao')
Breeder97Steel3IB.add_element('Li',0.17,'ao')
Breeder97Steel3IB.set_density('g/cm3',9.5)

Breeder97Steel3OB = openmc.Material(name = "Breeder97Steel3OB")
Breeder97Steel3OB.add_element('Pb',0.83,'ao')
Breeder97Steel3OB.add_element('Li',0.17,'ao')
Breeder97Steel3OB.set_density('g/cm3',9.5)


#> Coolant-He (8MPA)
Coolant_material = openmc.Material(name='Coolant_material')
Coolant_material.add_element('He',1.0,'ao')
Coolant_material.set_density('kg/m3',5.0)


mat_list= openmc.Materials([Breeder97Steel3OB, Breeder97Steel3IB])
mat_list.export_to_xml()

mat_list.cross_sections = "/Users/rocco698/Desktop/JENDL5/jendl-5-hdf5/cross_sections.xml"
print('materials export success')


# ################################################
#       GEOMETRY DEFINITION
# ################################################

dag_univ = openmc.DAGMCUniverse('/Users/rocco698/Desktop/Undergrad/Spring_2026/NUCE_431W/NUCE_431W/OpenMC_STAR_Model/Rocco_testing/Breeder_Outer_Only.h5m', auto_geom_ids = True)

root_cell = openmc.Cell(fill = dag_univ)

root_cell.region = -openmc.Sphere(r = 17000.0, boundary_type = 'vacuum')

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
        r=openmc.stats.Discrete([radius], [1]),
        phi=openmc.stats.Uniform(a=angles[0], b=angles[1]),
        z=openmc.stats.Discrete([z_placement], [1]),
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

tallies_file = openmc.Tallies()                 #? create a tallies.out file


breeder_mesh = openmc.RegularMesh()
breeder_mesh.dimension = [100,100]
breeder_mesh.lower_left = [-15000.0, -15000.0]
breeder_mesh.upper_right = [15000.0, 15000.0]

breeder_mesh_filter = openmc.MeshFilter(breeder_mesh)

breeder_universe_filter = openmc.UniverseFilter(dag_univ)

flux_tally = openmc.Tally(name = 'flux')
flux_tally.filters = [breeder_mesh]
flux_tally.scores = ['flux']
tallies_file.append(flux_tally)


tallies_file.export_to_xml()

###############################################################################
# Define problem settings
###############################################################################

settings = openmc.Settings()
settings.run_mode = 'fixed source'
settings.dagmc = True
settings.batches = 10
settings.particles = 1000
settings.source = sources
settings.source_rejection_fraction = 0.05
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
plot1.colors = {
    Breeder97Steel3OB: 'black',
    Breeder97Steel3IB: 'deeppink',
    Breeder_material: 'blue',
}
plot1.filename = 'TESTIMG'
plot1.pixels = (900,900)
plots = openmc.Plots([plot1])
plots.export_to_xml()

# Set the environment variable for cross sections
os.environ["OPENMC_CROSS_SECTIONS"] = "/Users/rocco698/Desktop/JENDL5/jendl-5-hdf5/cross_sections.xml"

openmc.plot_geometry()
openmc.run()










