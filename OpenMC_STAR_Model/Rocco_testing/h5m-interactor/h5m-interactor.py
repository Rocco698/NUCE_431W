# cSpell:disable

import pydagmc as pyd

model = pyd.Model("/Users/rocco698/Desktop/Undergrad/Spring_2026/NUCE_431W/NUCE_431W/OpenMC_STAR_Model/CAD_TO_OPENMC/STAR5_Whole.h5m")

group_dictionary = model.groups_by_name

print()
print(group_dictionary)
print()

steel_group = pyd.Group.create(model, name = "steel_group", group_id = 1)

print()
print(steel_group)
print()

breeder_group = pyd.Group.create(model, name = "breeder_group", group_id = 2)

print()
print(breeder_group)
print()

coolant_group = pyd.Group.create(model, name = "coolant_group", group_id = 3)

print()
print(coolant_group)
print()

plasma_group = pyd.Group.create(model, name = "plasma_group", group_id = 4)

print()
print(plasma_group)
print()

shielding_group = pyd.Group.create(model, name = "shielding_group", group_id = 5)

print()
print(shielding_group)
print()