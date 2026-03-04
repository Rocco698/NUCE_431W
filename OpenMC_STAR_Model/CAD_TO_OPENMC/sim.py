# cSpell:disable

import CAD_to_OpenMC.assembly as ab
from pathlib import Path
import os

'''
A=ab.Assembly(['STAR5_214.STEP'])
ab.mesher_config['threads']=1
ab.mesher_config['tolerance']=1e-2
ab.mesher_config['angular_tolerance']=1e-2
A.set_tag_delim("\s_@")
A.run(h5m_filename='output.h5m', backend='stl2')
'''

# NOTE: As of 03/03/2026. This code does not work. Please do not run this.

# path to "input" directory
input_path = Path("/Users/rocco698/Desktop/Undergrad/Spring_2026/OpenMC_x86_Conda/CAD_To_DAGMC/Input")

# path to intermediate directory
intermediate_path = Path("/Users/rocco698/Desktop/Undergrad/Spring_2026/NUCE_431W/NUCE_431W/OpenMC_STAR_Model/CAD_TO_OPENMC/intermediate_h5m_path")

# initialize empty whole array & show initial status
STEPArray = []
print()
print("Initial Whole Array: ", STEPArray)
print()

# initalize empty .h5m intermediate array & show initial status
INTERArray = []
print()
print("Initial .h5m Intermediate Array: ", INTERArray)
print()

# initialize dictionary for storing <index> and its associated <.h5m> file
h5m_dict = {}
print()
print("Initial .h5m Dictionary: ", h5m_dict)
print()

# initalize empty list for storing .h5m files post-meshing
h5mList = list()
print()
print(f"Initial .h5m filename list: {h5mList}")
print()




def MeshAndStore(input_path, h5m_dict, h5mList):
    for index, value in enumerate(input_path.iterdir()):

        print()
        print("Current File: ", value, "Current Index: ", index)
        print()

        print(f"Assigning key: {index}")
        key_name = f"volume_{index}"

        print()
        print(f"{key_name} has value: {value}")
        print()

        A=ab.Assembly([str(value)])
        ab.mesher_config['threads']=1
        ab.mesher_config['tolerance']=1e-4
        ab.mesher_config['angular_tolerance']=1e-4
        A.set_tag_delim("\s_@")

        h5m_filename = intermediate_path / f"volume_{index}.h5m"

        print()
        print(f".h5m intermediary for {key_name} has filename: {h5m_filename}")
        print()

        print(f"Begin Meshing Process")
        print()
        print()

        A.run(h5m_filename=h5m_filename, backend='stl2')

        print()
        print(f"Meshing Complete. Setting {key_name}")
        print()

        h5m_dict[key_name] = A

        print()
        print(f"{key_name} now has value: {h5m_dict[key_name]}")
        print()

        print()
        print(f"Process End. Moving to Next File...")
        print()

    print()
    print(f"Meshing of Input Directory Complete")
    print()

    print(f"Final .h5m Dictionary: {h5m_dict}")

    print()
    print(f"Beginning Merge Process")
    print()

    for index, value in enumerate(h5m_dict):

        print()
        print(f"Appending .h5m file to list")
        print()

        print()
        print(f"Appending {index} ({value})")

        h5mList.append(value)

        print()
        print(h5mList[index])
        print()

    print()
    print(f"Merging")
    print()

    ab.merge2h5m(h5mList, h5m_file='output_sim.h5m')


    print()
    print(f"Complete. Ending")
    print()














if __name__ == "__main__":

    MeshAndStore(input_path, h5m_dict, h5mList)

