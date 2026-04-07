# cSpell:disable

import dagmc_h5m_file_inspector as di
import pydagmc

file = "output.h5m"

print(di.get_bounding_box_from_h5m(file))

print(di.get_volumes_and_materials_from_h5m(file))

print(di.get_volumes_from_h5m_by_cell_id(file))
