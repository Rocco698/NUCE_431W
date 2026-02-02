# cSpell:disable

import CAD_to_OpenMC.assembly as ab

A=ab.Assembly(['STAR5_Checked242.STP'])
ab.mesher_config['threads']=1
ab.mesher_config['tolerance']=1e-2
ab.mesher_config['angular_tolerance']=1e-2
A.set_tag_delim("\s_@")
A.run(h5m_filename='output.h5m', backend='stl2')
