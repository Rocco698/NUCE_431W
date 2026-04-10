# cSpell:disable

from paraview.simple import *
import glob
import os

# --- configuration ---
# folder containing files
input_folder = '/Users/rocco698/Desktop/Undergrad/Spring_2026/NUCE_431W/NUCE_431W/OpenMC_STAR_Model/CAD_TO_OPENMC/STL_Output'
file_pattern = '*.stl'  # Extension: vtk, vtu, stl, etc.
output_folder = '/Users/rocco698/Desktop/Undergrad/Spring_2026/NUCE_431W/NUCE_431W/OpenMC_STAR_Model/CAD_TO_OPENMC/Scaled_STL_output_2'

# scale down 10x
translation = [10.0, 0.0, 0.0]
rotation = [0.0, 0.0, 0.0]
scale = [0.1, 0.1, 0.1]

# --- Processing ---
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = glob.glob(os.path.join(input_folder, file_pattern))

for file_path in files:
    filename = os.path.basename(file_path)
    print(f"Processing: {filename}")
    
    # 1. Read the file
    reader = OpenDataFile(file_path)
    
    # 2. Apply Transform Filter
    transform = Transform(Input=reader)
    transform.Transform = 'Transform'
    transform.Transform.Translate = translation
    transform.Transform.Rotate = rotation
    transform.Transform.Scale = scale
    
    # 3. update pipeline
    UpdatePipeline(proxy=transform)
    
    # 4. save output (e.g., as STL)
    out_path = os.path.join(output_folder, f"trans_{filename}")
    SaveData(out_path, proxy=transform)
    
    # 5. cleanup memory
    Delete(transform)
    Delete(reader)

print("All files transformed successfully.")
