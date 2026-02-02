# cSpell:disable

import CAD_to_OpenMC.assembly as ab

A=ab.Assembly(['STAR5_00_1.STEP'])
ab.mesher_config['threads']=1
ab.mesher_config['tolerance']=1e-2
ab.mesher_config['angular_tolerance']=1e-2
A.run(h5m_filename='STAR5_00_1.h5m', backend='stl2')
