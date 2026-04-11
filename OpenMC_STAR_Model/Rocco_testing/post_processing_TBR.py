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


statepoint = openmc.StatePoint('statepoint.10.h5')

#> MATERIAL TRITIUM PRODUCTION TALLY

breeding_tally = statepoint.get_tally(name = 'TRITIUM')
print(breeding_tally)

breeding_tally.sum

print(breeding_tally.mean.shape)
(breeding_tally.mean, breeding_tally.std_dev)

TBR = breeding_tally.get_slice(scores = ['(n,t)'])

print(f"ESTIMATED TRITIUM-BREEDING-RATIO: {TBR}")