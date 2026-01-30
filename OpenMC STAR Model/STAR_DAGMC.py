# cSpell:disable

# Necessary imports
import numpy as np # numerical tools
import os
import openmc # openMC
import matplotlib.pyplot as plt # plotting tools
from IPython.display import Image
# ##############################################
# IMPORT THE FILE FUNCTION
# ##############################################
import urllib.request

blanket_shielding_url = 'https://tinyurl.com/mur2cnn2' # 1.2 MB
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


LiPb={'Li':{'percent': 17, #atomic percent
            'enrichment': 100,
            'enrichment_target': 'Li6'},
      'Pb':{'percent': 83}
B4C={'B':{'percent': 80},
     'C':{'percent': 20}
breed=openmc.Material(LiPb)
shield=openmc.Materal(B4C)

mat_list= openmc.Materials([])
mat_list.export_to_xml()

print(mat_list)
mat_list.cross_sections = "/storage/work/irj5023/NUCE403/endfb-viii.0-hdf5/cross_sections.xml"


# ################################################
#       GEOMETRY DEFINITION
# ################################################

download(blanket_shielding_url)
print(geometry)
print(mat_list)

# #################################################
#       TALLIES
# #################################################

###############################################################################
# Define problem settings
###############################################################################

settings = openmc.Settings()
settings.dagmc = True
settings.batches = 10
settings.inactive = 2
settings.particles = 5000
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
p.colors = {iron: 'gray', water: 'blue'}
openmc.plot_inline(p)

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
