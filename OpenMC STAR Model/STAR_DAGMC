# cSpell:disable

# Necessary imports
import numpy as np # numerical tools
import os
import openmc # openMC
import matplotlib.pyplot as plt # plotting tools

# ##############################################
#       MATERIALS
# ##############################################

mat_list= openmc.Materials([])
mat_list.export_to_xml()

print(mat_list)
mat_list.cross_sections = "/data/endfb-viii.0-hdf5/cross_sections.xml"


# ################################################
#       GEOMETRY DEFINITION
# ################################################

geometry = openmc.Geometry([])
geometry.export_to_xml()

print(geometry)
print(mat_list)

# #################################################
#       TALLIES
# #################################################

###############################################################################
# Define problem settings
###############################################################################

settings = openmc.Settings()
settings.batches = 100
settings.inactive = 10
settings.particles = 1000
settings.export_to_xml()

print(settings)


# ################################
#  Plots Definition
# ################################


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
