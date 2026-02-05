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
my_sources = openmc.IndependentSource()

# Option 2

my_source = fusion_ring_source(
    radius=700, # we can modify
    angles=(0.0, 2 * math.pi),  # 360deg source, we can cut down to our size
    temperature=20000.0, # also needs to be modified
    fuel={"D": 0.5, "T": 0.5}, # Ask Khodak
)
my_source = openmc.IndependentSource()



settings = openmc.Settings()
settings.run_mode = 'fixed source'
settings.source = my_source or my_sources # pick one
settings.particles = 10000
settings.generations_per_batch = 20
settings.batches = 200
settings.inactive = 50
settings.output = {'tallies':True, 'path': 'results'}

cell_filter = openmc.CellFilter([blanket.id])
tbr1_tally = openmc.Tally
tbr1_tally.scores['absorption', 'H3-production']
tbr1_tally.filters = [cell_filter]

# Tallies must be multiplied by our given source strength
# H3-production/absorption = TBR

# Second method, may be more accurate

# creates a mesh that covers the geometry
mesh = openmc.RegularMesh()
mesh.dimension = [100, 100, 100]
mesh.lower_left = [0, 0, -350]  # x,y,z coordinates start at 0 as this is a sector model
mesh.upper_right = [650, 650, 350]
mesh_filter = openmc.MeshFilter(mesh) # creating a mesh

# adds a tally to record the total TBR
tbr_cell_tally = openmc.Tally(name="tbr")
tbr_cell_tally.scores = ["(n,Xt)"]

# makes a mesh tally using the previously created mesh and records TBR on the mesh
tbr_mesh_tally = openmc.Tally(name="tbr_on_mesh")
tbr_mesh_tally.filters = [mesh_filter]
tbr_mesh_tally.scores = ["(n,Xt)"]

tallies = openmc.Tallies([tbr_cell_tally, tbr_mesh_tally, tbr1_tally]) 

my_model = openmc.Model(materials=materials, geometry=geometry, settings=settings, tallies=tallies)
my_model.run()

