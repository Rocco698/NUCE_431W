"""
Code name (purpose): Capstone STAR openmc code
by Rocco L., Sean D., Vasil I., and Issac J.
This is an abomination any you know it

import matplotlib.pyplot as plt
import numpy as np
"""

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
#from openmc_plasma_source import tokamak_source # Ring source, make sure to download: pip install openmc_plasma_source
import urllib.request
# ##############################################
# IMPORT THE FILE FUNCTION
# ##############################################


STARmodel_url = 'https://github.com/Rocco698/NUCE_431W/raw/refs/heads/main/OpenMC_STAR_Model/Rocco_testing/output.h5m' # 1.2 MB (Should find the file: .h5m star file) (needs the url from right-clicking the 'raw button on github)
excel_path="/storage/work/irj5023/Capstone/STAR40_Neutonics_Data.xlsx"

def download(url):
    """
    Helper function for retrieving dagmc models
    """
    u = urllib.request.urlopen(url)
    
    if u.status != 200:
        raise RuntimeError("Failed to download file.")
    
    # save file as dagmc.h5m
    with open("dagmc.h5m", 'wb') as f:
        f.write(u.read())

download(STARmodel_url)

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

mat_list.cross_sections = "/storage/work/irj5023/Capstone/jendl-5-hdf5/cross_sections.xml"
print('> Materials Export Success')


# ################################################
#       GEOMETRY DEFINITION
# ################################################

dag_univ = openmc.DAGMCUniverse("dagmc.h5m", auto_geom_ids = True)
root_cell = openmc.Cell(fill = dag_univ)
root_cell.region = -openmc.Sphere(r = 2500.0, boundary_type = 'vacuum')
cell_count = dag_univ.n_cells
print(f"Number of Cells within Model: {cell_count}")
print(f"Path to Model:  {dag_univ.filename}")
print(f"Cells: {dag_univ.get_all_cells}")
# , padding_distance = 30.0
#sim_univ = dag_univ.bounded_universe(bounding_cell_id= 999, boundary_type = 'vacuum')
geometry = openmc.Geometry([root_cell,])
geometry.export_to_xml()
print('> Geometry Export Success')

# #################################################
#       SOURCE DEFINITION
# #################################################
# Heavy use of code from: https://github.com/fusion-energy/openmc-plasma-source/blob/main/examples/ring_source_example.py
def onion_ring_source(radius: float, z_placement: float, activity: float, #these are the only inputs you should need to change
                      angles: Tuple[float, float] = (0, 2 * np.pi),       #not these
                      fuel: Dict = {"D": 0.5, "T": 0.5}):                 #not these
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
    #if not (isinstance(temperature, (int, float)) and temperature > 0): #Temp not used, assumed 14 MeV
        #raise ValueError("Temperature must be a float strictly greater than 0.")
    source = IndependentSource()
    source.space = openmc.stats.CylindricalIndependent(
        r=openmc.stats.Discrete([radius]*100, [1]),
        phi=openmc.stats.Uniform(a=angles[0], b=angles[1]),
        z=openmc.stats.Discrete([z_placement]*100, [1]),
        origin=(0.0, 0.0, 0.0) )
    source.energy =openmc.stats.Discrete([14.0e6], [1.0]) # (14 MeV neutrons, 100% distribution)
    source.angle = openmc.stats.Isotropic()
    source.strength = activity
    return source

# Create data frame from excel sheet #
df = pd.read_excel(excel_path)
radi_s = df.loc[:,"R [m]"].tolist()
z_pos = df.loc[:,"Z[m]"].tolist()
norm_activ = df.loc[:,"norm"].tolist()

#sources = onion_ring_source(radius= radi_s[0], z_placement= z_pos[0], activity= norm_activ[0])

iter=0
sources = []
while iter <= 501:
    sources.append(onion_ring_source(radius=radi_s[iter], z_placement=z_pos[iter], activity=norm_activ[iter]))
    iter += 1
print('> Sources Success')
# #################################################
#       TALLIES
# #################################################

external_mesh = openmc.SphericalMesh(
r_grid = (0,10,1000) #(mid, outer, subdivide the radial direction)
)
energy_filter_thermal = openmc.EnergyFilter([0.0, 1.0e6]) # eV
energy_filter_fast = openmc.EnergyFilter([1.0e6, 14.0e6]) # eV

mesh_filter = openmc.MeshFilter(external_mesh)
tally_leak = openmc.Tally(name='neutron_leakage')
tally_leak.filters = [energy_filter_fast, energy_filter_thermal, mesh_filter]
tally_leak.scores= ['flux']

tallies = openmc.Tallies([tally_leak])
tallies.export_to_xml()

###############################################################################
# Define problem settings
###############################################################################

settings = openmc.Settings()
settings.run_mode = "fixed source"
settings.dagmc = True
settings.batches = 10
settings.inactive = 2
settings.particles = 5000
settings.source = sources   
settings.export_to_xml()

print(settings)


# ################################
#  Plots Definition
# ################################
material_colors = {
    Shielding_material: 'black',
    Breeder_material: 'red',
    Steel_material: 'grey',
    Coolant_material: 'blue'
}

p = openmc.Plot()
p.basis = 'xz'
p.origin = (0.0, 0.0, 0.0)
p.width = (30.0, 20.0)
p.pixels = (450, 300)
p.colors = material_colors
p.color_by = 'material'
plots = openmc.Plots([p])
plots.export_to_xml()
openmc.plot_geometry()

#ww = 15
#plot1 = openmc.Plot()
#plot1.width = (ww,ww)
#plot1.basis = 'xy'
#plot1.color_by = 'material'
#plot1.filename = 'RadialView'
#plots = openmc.Plots([plot1])
#plots.export_to_xml()

# Set the environment variable for cross sections
os.environ["OPENMC_CROSS_SECTIONS"] = "/storage/work/irj5023/Capstone/jendl-5-hdf5/cross_sections.xml"

openmc.plot_geometry()
openmc.run()
