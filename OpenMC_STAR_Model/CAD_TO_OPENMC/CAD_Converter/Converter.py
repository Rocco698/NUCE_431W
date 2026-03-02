# cSpell:disable

# This script imports a .STEP file or list of .STEP files and exports them to .h5m & .vtkhdf & .stl format. 

# NOTE: For the use of <"assembly_names">, each .STEP file must be an assembly! Otherwise specify material names manually (or .stem filename and append as material tag).
# NOTE: It is highly recommended that the geometry is checked through ParaView or similar software. 
# NOTE: This script, when ran with direct cadquery meshing, will take a lot of time and a lot of energy. Be weary of how many inputs you are giving this file! 

# author: Rocco Lombardo, 02/27/2026 


import cadquery as cq                 # for cadquery importing
import dagmc_h5m_file_inspector as di # for diagnositcs
from cad_to_dagmc import CadToDagmc   # for format conversion
from pathlib import Path              # for properly dealing with pathnames
import os                             # for making directories 

# path to "input" directory
input_path = Path("<path>")

# path to ".STL Output" directory
output_stl_path = Path("<path>")


# initialize empty whole array & show initial status
STEPArray = []
print()
print("Initial Whole Array: ", STEPArray)
print()

# initialize empty filename array & show initial status
filenameArray = []
print("Initial Filename Array: ", filenameArray)
print()

# initialize empty material tag array & show initial status
materialArray = []
print("Initial Material Array: ", materialArray)
print()

# initialize empty .STL array & show initial status
stlArray = []
print("Initial .STL Array: ", stlArray)
print()

# initialize Cad_To_DAGMC model
model = CadToDagmc()

# generates array with form [<filename>, <material>]
def generateMasterArray(STEPArray):
    # append only files to array
    for item in input_path.iterdir():

        # check if file
        if input_path.is_file:

            # show name and path
            print(item.name)
            print()
            print(item)
            print()

            # append .STEP to array as filepath (even indices)
            STEPArray.append(item)

            # append stripped filename to adjacent element, for material_tag (odd indices)
            STEPArray.append(item.stem.replace(" ", ""))

        # error message for non-file items
        else:
            print("ERROR: Object not recognized within input directory. Check input, ensure only files present.")
            print()
    
    # print full array
    print("Combined Name and Material Array: ", STEPArray)
    print()

# generates material and filename array
def generateSeperatedArray(STEPArray):
    for index, value in enumerate(STEPArray):
        # if even, append filename name to filenameArray
        if index % 2 == 0:
            filenameArray.append(value)
        
        # if odd, append material to material array
        else:
            materialArray.append(value)
    
    # check if both arrays are the same size
    if len(filenameArray) == len(materialArray):
        print("Array Size Equality Test Passed")
        print()
    else:
        print("ERROR: Arrays are not the same size!")
        print()
    # show both arrays
    print("Processed Filename Array: ", filenameArray)
    print()
    print("Processed Material Array: ", materialArray)
    print()



# adds each .STEP file to model
def addToModel(model, filenameArray, materialArray):

    # iterate over inicdes (does not matter if filename or material arrays are used, both same size)
    for i in range(len(filenameArray)):
        model.add_stp_file(
            # append .STEP to model
            filename = filenameArray[i],

            # append material to model
            material_tags = [materialArray[i],]
        )
    

# export to .h5m and vtkhdf
def exportModel(model):
    model.export_dagmc_h5m_file(filename="output.h5m")
    di.convert_h5m_to_vtkhdf(h5m_filename='output.h5m', vtkhdf_filename='output.vtkhdf')


# convert .STEP to .STL function
def STEPtoSTL(filenameArray, stlArray, materialArray, output_stl_path):
    for index, value in enumerate(filenameArray):

        # Specify filename and location for .STL
        stl_filename = output_stl_path / f"{materialArray[index]}.stl"

        # convert path to string for CadQuery
        step_file = str(filenameArray[index])
        stl_file = str(stl_filename)

        # import .STEP file for CadQuery
        step_model = cq.importers.importStep(step_file)

        # get path from filename Array and convert to .STL
        cq.exporters.export(step_model, stl_file, cq.exporters.ExportTypes.STL, tolerance = 0.1)

        # append to STL Array
        stlArray.append(stl_filename)

        # show array after each iteration
        print(f"STL Array Element {index} has name {stl_filename}")
        print()
    
    # show full array
    print(f"Exporting complete. Full STL Array:")
    print()
    print(stlArray)






if __name__ == "__main__":
    # Generate Combined Array
    generateMasterArray(STEPArray)

    # Generate Material nad Filename Array
    generateSeperatedArray(STEPArray)

    # Generate .STL's from .STEP's
    STEPtoSTL(filenameArray, stlArray, materialArray, output_stl_path)

    # Add Filename and Material to Model
    #addToModel(model, filenameArray, materialArray)

    # Export Model
    #exportModel(model)
