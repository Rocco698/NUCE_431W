# cSpell:disable

# Necessary imports
import numpy as np # numerical tools
import os
import openmc # openMC
import matplotlib.pyplot as plt # plotting tools
from IPython.display import Image
from openmc_plasma_source import tokamak_source # Ring source, make sure to download: pip install openmc_plasma_source
# ##############################################
# IMPORT THE FILE FUNCTION
# ##############################################
import urllib.request

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
onion_rings = tokamak_source(
    elongation=1.557,
    ion_density_centre=1.09e20,
    ion_density_pedestal=1.09e20,
    ion_density_peaking_factor=1,
    ion_density_separatrix=3e19,
    ion_temperature_centre=45.9e3,
    ion_temperature_pedestal=6.09e3,
    ion_temperature_separatrix=0.1e3,
    ion_temperature_peaking_factor=8.06,
    ion_temperature_beta=6,
    major_radius=906,
    minor_radius=292.258,
    pedestal_radius=0.8 * 292.258,
    mode="H",
    shafranov_factor=0.44789,
    triangularity=0.270,
    fuel={"D": 0.5, "T": 0.5},
)


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
settings.source = onion_rings
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
