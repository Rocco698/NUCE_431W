# cSpell: Disable
from stl_to_h5m import stl_to_h5m

stl_to_h5m(
    files_with_tags=[
        ('starassm - 316SS Coil Structure 12-1.STL', 'mat1'),
        ('starassm - 316SS Coil Structure 12-2.STL', 'mat1'),
        ('starassm - 316SS Coil Structure 12-3.STL', 'mat1'),
        ('starassm - 316SS Coil Structure 12-4.STL', 'mat1'),
        ('starassm - 316SS Coil Structure 12-5.STL', 'mat1'),
        ('starassm - 316SS Coil Structure 12-6.STL', 'mat1'),
        ('starassm - 316SS Coil Structure 12-7.STL', 'mat1'),
        ('starassm - 316SS Coil Structure 12-8.STL', 'mat1'),
        ('starassm - 316SS Coil Structure 12-9.STL', 'mat1'),
        ('starassm - 316SS Coil Structure 12-10.STL', 'mat1'),
        ('starassm - 316SS Coil Structure 12-11.STL', 'mat1'),
        ('starassm - 316SS Coil Structure 12-12.STL', 'mat1'),

        ('starassm - 316SS HTS Inner 3-1.STL', 'mat2'),
        ('starassm - 316SS HTS Inner 3-2.STL', 'mat2'),
        ('starassm - 316SS HTS Inner 3-3.STL', 'mat2'),


        ('starassm - 316SS HTS Inner 8-1.STL', 'mat2'),
        ('starassm - 316SS HTS Inner 8-2.STL', 'mat2'),
        ('starassm - 316SS HTS Inner 8-3.STL', 'mat2'),
        ('starassm - 316SS HTS Inner 8-4.STL', 'mat2'),
        ('starassm - 316SS HTS Inner 8-5.STL', 'mat2'),
        ('starassm - 316SS HTS Inner 8-6.STL', 'mat2'),
        ('starassm - 316SS HTS Inner 8-7.STL', 'mat2'),
        ('starassm - 316SS HTS Inner 8-8.STL', 'mat2'),
        ('starassm - 316SS HTS Inner 8-9.STL', 'mat2'),


        ('starassm - 316SS HTS Outer 4-1.STL', 'mat2'),
        ('starassm - 316SS HTS Outer 4-2.STL', 'mat2'),
        ('starassm - 316SS HTS Outer 4-3.STL', 'mat2'),
        ('starassm - 316SS HTS Outer 4-4.STL', 'mat2'),
        ('starassm - 316SS HTS Outer 4-5.STL', 'mat2'),
        ('starassm - 316SS HTS Outer 4-6.STL', 'mat2'),


        ('starassm - 316SS HTS Outer 9-1.STL', 'mat2'),
        ('starassm - 316SS HTS Outer 9-2.STL', 'mat2'),
        ('starassm - 316SS HTS Outer 9-3.STL', 'mat2'),
        ('starassm - 316SS HTS Outer 9-4.STL', 'mat2'),
        ('starassm - 316SS HTS Outer 9-5.STL', 'mat2'),
        ('starassm - 316SS HTS Outer 9-6.STL', 'mat2'),


        ('starassm - 316SS Inner Coil Structure-1.STL', 'mat2'),


        ('starassm - 316SS VV-1.STL', 'mat2'),


        ('starassm - Breeder 97 Steel 3 IB-1.STL', 'mat3'),
        ('starassm - Breeder 97 Steel 3 OB-1.STL', 'mat3'),


        ('starassm - Coolant 50 Steel 50 IB Top-1.STL', 'mat4'),
        ('starassm - Coolant 50 Steel 50 OB Bottom-1.STL', 'mat4'),
        ('starassm - Coolant 50 Steel 50 OB Top-1.STL', 'mat4'),
        ('starassm - Coolant 50 Steel 50 Transition Bottom-1.STL', 'mat4'),
        ('starassm - Coolant 50 Steel 50 Transition Top-1.STL', 'mat4'),


        ('starassm - Coolant 88 Steel 12 IB-1.STL', 'mat5'),
        ('starassm - Coolant 88 Steel 12 OB Inner-1.STL', 'mat5'),
        ('starassm - Coolant 88 Steel 12 OB Outer-1.STL', 'mat5'),


        ('starassm - Copper 50 Hatelloy 50 HTS 7-1.STL', 'mat6'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-2.STL', 'mat6'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-3.STL', 'mat6'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-4.STL', 'mat6'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-5.STL', 'mat6'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-6.STL', 'mat6'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-7.STL', 'mat6'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-8.STL', 'mat6'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-9.STL', 'mat6'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-10.STL', 'mat6'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-11.STL', 'mat6'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-12.STL', 'mat6'),


        ('starassm - Passive Plate Top-1.STL', 'mat7'),
        ('starassm - Passive Plate Top-2.STL', 'mat7'),


        ('starassm - Plasma-1.STL', 'mat8'),


        ('starassm - Shield 97 Steel 3 IB Outer-1.STL', 'mat9'),
        ('starassm - Shield 97 Steel 3 Inner-1.STL', 'mat9'),
        ('starassm - Shield 97 Steel 3 OB-1.STL', 'mat9'),


        ('starassm - Steel IB Inner Shield Structure-1.STL', 'mat10'),
        ('starassm - Steel IB Inner-1.STL', 'mat10'),
        ('starassm - Steel IB Outer Shield Structure-1.STL', 'mat10'),
        ('starassm - Steel IB Outer-1.STL', 'mat10'),
        ('starassm - Steel OB Inner-1.STL', 'mat10'),
        ('starassm - Steel OB Outer-1.STL', 'mat10'),
        ('starassm - Steel OB Shield Structure-1.STL', 'mat10'),
    ],
    h5m_filename='STAR5_Whole.h5m',
)