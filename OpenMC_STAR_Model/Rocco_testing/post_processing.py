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


sp = openmc.StatePoint('statepoint.10.h5')


#> FLUX, TRITIUM PRODUCTION, & ABSORPTION TALLY (FOR VISUAL)
flux_tally = sp.get_tally(scores = ['flux', 'absorption', '(n,t)'])

print(flux_tally)
flux_tally.sum

print(flux_tally.mean.shape)
(flux_tally.mean, flux_tally.std_dev)

flux = flux_tally.get_slice(scores = ['flux'])
absorption = flux_tally.get_slice(scores = ['absorption'])
Breeding = flux_tally.get_slice(scores = ['(n,t)'])
#Total_Breeding = flux_tally.get_slice(scores = ['(n,Xt)'])

flux.std_dev.shape = (1000, 1000)
flux.mean.shape = (1000, 1000)

absorption.std_dev.shape = (1000, 1000)
absorption.mean.shape = (1000, 1000)

Breeding.std_dev.shape = (1000, 1000)
Breeding.mean.shape = (1000, 1000)

#Total_Breeding.std_dev.shape = (1000, 1000)
#Total_Breeding.mean.shape = (1000, 1000)

print(flux)

#> PLOTTING

plt.plot(121)
plt.imshow(flux.mean)
plt.savefig('fluxmap2.png', dpi = 300)

plt.plot(121)
plt.imshow(absorption.mean)
plt.savefig('absorptionmap.png', dpi = 300)

plt.plot(121)
plt.imshow(Breeding.mean)
plt.savefig('Breedingmap.png', dpi = 300)

#plt.plot(121)
#plt.imshow(Total_Breeding.mean)
#plt.savefig('TotalBreedingMap.png', dpi = 300)






