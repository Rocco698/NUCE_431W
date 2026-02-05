# Settings and Tallies for TBR 

# We want a fixed source of plasma
from openmc_plasma_source import tokamak_source
from openmc_plasma_source import fusion_ring_source

# Two options

# Option 1

my_sources = tokamak_source(
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
    fuel={"D": 0.5, "T": 0.5}, # Ask Khodak about all parameters
)

# Option 2

my_source = fusion_ring_source(
    radius=700, # we can modify
    angles=(0.0, 2 * math.pi),  # 360deg source, we can cut down to our size
    temperature=20000.0, # also needs to be modified
    fuel={"D": 0.5, "T": 0.5}, # Ask Khodak
)




settings = openmc.Settings()
settings.run_mode = 'fixed source'
# Add line specifiying which source we are using
settings.particles = 10000
settings.generations_per_batch = 20
settings.batches = 200
settings.inactive = 50

cell_filer = openmc.CellFileter([blanket.id, sheilding.id])
tally.scores['absorption', 'H3-production']
# Tallies must be multiplied by our given source strength
# H3-production/absorption = TBR
