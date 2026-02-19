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
# IMPORT THE FILE FUNCTION
# ##############################################


STARmodel_url = 'https://github.com/Rocco698/NUCE_431W/blob/main/OpenMC_STAR_Model/CAD_TO_OPENMC/STAR5_Whole.h5m' # 1.2 MB (Should find the file: STAR5_Whole.h5m)
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

excel_path="HOME/STAR40_Neutonics_Data.xlsx"
# ##############################################
#       MATERIALS
# ##############################################
#Material Initialization
Steel_material = openmc.Material(name='Steel-EUROFER97')
Shielding_material = openmc.Material(name='Shielding-B4C')
Breeder_material = openmc.Material(name='Breeder-PbLi')
Coolant_material = openmc.Material(name='Coolant-He (8MPA)')

#Steel-EUROFER97
Steel_material.mix_materials([Fe,C,Cr,W,Mn,Ta,N2],[0.8924,0.0011,0.09,0.011,0.004,0.0012,0.0003],'wo')
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
Coolant_material.add_element('He2',1.0,'ao')
Coolant_material.set_density('kg/m3',5.0)

mat_list= openmc.Materials([Steel_material, Shielding_material, Breeder_material, Coolant_material])
mat_list.export_to_xml()

mat_list.cross_sections = "/storage/work/irj5023/NUCE403/endfb-viii.0-hdf5/cross_sections.xml"
print('materials export success')


# ################################################
#       GEOMETRY DEFINITION
# ################################################

download(STARmodel_url)
dag_univ = openmc.DAGMCUniverse('dagmc.h5m')
geometry = openmc.Geometry(dag_univ)
geometry.export_to_xml()
print(geometry) #Look into plotting later
print(mat_list)

# #################################################
#       SOURCE DEFINITION
# #################################################
# Heavy use of code from: https://github.com/fusion-energy/openmc-plasma-source/blob/main/examples/tokamak_source_example.py
# Needs proper values still (8 Feb)
def fusion_ring_source(radius: float, z_placement: float, activity: float,
    angles: Tuple[float, float] = (0, 2 * np.pi),
    fuel: Dict = {"D": 0.5, "T": 0.5}):
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
        r=openmc.stats.Discrete([radius], [1]),
        phi=openmc.stats.Uniform(a=angles[0], b=angles[1]),
        z=openmc.stats.Discrete([z_placement], [1]),
        origin=(0.0, 0.0, 0.0) )
    source.energy =openmc.stats.Discrete([14.0e6], [1.0]) # (14 MeV neutrons, 100% distribution)
    source.angle = openmc.stats.Isotropic()
    source.strength = activity
    return [source]

# Create data frame from excel sheet #
df = pd.read_excel(excel_path)
radi_s = df.loc[:,"R [m]"].tolist()
z_pos = df.loc[:,"Z[m]"].tolist()
activ_s = df.loc[:,r"[neutron/s]"].tolist()

iter=0
sources = []
while iter <= 501:
    sources= sources.append(fusion_ring_source(radius=radi_s[iter], z_placement=z_pos[iter], activity=activ_s[iter]))
    iter += 1
# #################################################
#       TALLIES
# #################################################

###############################################################################
# Define problem settings
###############################################################################

settings = openmc.Settings()
settings.run_mode = "fixed source"
settings.dagmc = True
settings.batches = 10
settings.inactive = 2
settings.particles = 5000
settings.source = [sources]   
settings.export_to_xml()

print(settings)

# ################################
#  Plots Definition
# ################################
p = openmc.Plot()
p.basis = 'xz'
p.origin = (0.0, 0.0, 0.0)
p.width = (30.0, 20.0)
p.pixels = (450, 300)
p.color_by = 'material'
p.colors = {shield: 'gray', breed: 'blue'}
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
os.environ["OPENMC_CROSS_SECTIONS"] = "/data/endfb-viii.0-hdf5/cross_sections.xml"

openmc.plot_geometry()
openmc.run()
