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


sp = openmc.StatePoint('statepoint.10.h5')

flux_tally = sp.get_tally(scores = ['flux'])

print(flux_tally)

flux_tally.sum

print(flux_tally.mean.shape)
(flux_tally.mean, flux_tally.std_dev)

flux = flux_tally.get_slice(scores = ['flux'])

print(flux)



plt.subplot(121)
plt.imshow(flux.mean)
plt.show()






