# cSpell: Disable

# NOTICE: This file will not work unless you move all of the .stl files to the CAD_TO_OPENMC directory! They were only moved to a dedicated folder for cosmetic purposes. If you plan on running this code, move all 74 .stls to CAD_TO_OPENMC first. When finished, put them back!
from stl_to_h5m import stl_to_h5m

stl_to_h5m(
    files_with_tags=[
        ('starassm - 316SS Coil Structure 12-1.STL', 'Steel_material'), #Applying steel to coils for now (was mat_1)
        ('starassm - 316SS Coil Structure 12-2.STL', 'Steel_material'),
        ('starassm - 316SS Coil Structure 12-3.STL', 'Steel_material'),
        ('starassm - 316SS Coil Structure 12-4.STL', 'Steel_material'),
        ('starassm - 316SS Coil Structure 12-5.STL', 'Steel_material'),
        ('starassm - 316SS Coil Structure 12-6.STL', 'Steel_material'),
        ('starassm - 316SS Coil Structure 12-7.STL', 'Steel_material'),
        ('starassm - 316SS Coil Structure 12-8.STL', 'Steel_material'),
        ('starassm - 316SS Coil Structure 12-9.STL', 'Steel_material'),
        ('starassm - 316SS Coil Structure 12-10.STL', 'Steel_material'),
        ('starassm - 316SS Coil Structure 12-11.STL', 'Steel_material'),
        ('starassm - 316SS Coil Structure 12-12.STL', 'Steel_material'),

        ('starassm - 316SS HTS Inner 3-1.STL', 'Steel_material'), #Assuming these are structural supports (was mat_2)
        ('starassm - 316SS HTS Inner 3-2.STL', 'Steel_material'),
        ('starassm - 316SS HTS Inner 3-3.STL', 'Steel_material'),


        ('starassm - 316SS HTS Inner 8-1.STL', 'Steel_material'),
        ('starassm - 316SS HTS Inner 8-2.STL', 'Steel_material'),
        ('starassm - 316SS HTS Inner 8-3.STL', 'Steel_material'),
        ('starassm - 316SS HTS Inner 8-4.STL', 'Steel_material'),
        ('starassm - 316SS HTS Inner 8-5.STL', 'Steel_material'),
        ('starassm - 316SS HTS Inner 8-6.STL', 'Steel_material'),
        ('starassm - 316SS HTS Inner 8-7.STL', 'Steel_material'),
        ('starassm - 316SS HTS Inner 8-8.STL', 'Steel_material'),
        ('starassm - 316SS HTS Inner 8-9.STL', 'Steel_material'),


        ('starassm - 316SS HTS Outer 4-1.STL', 'Steel_material'),
        ('starassm - 316SS HTS Outer 4-2.STL', 'Steel_material'),
        ('starassm - 316SS HTS Outer 4-3.STL', 'Steel_material'),
        ('starassm - 316SS HTS Outer 4-4.STL', 'Steel_material'),
        ('starassm - 316SS HTS Outer 4-5.STL', 'Steel_material'),
        ('starassm - 316SS HTS Outer 4-6.STL', 'Steel_material'),


        ('starassm - 316SS HTS Outer 9-1.STL', 'Steel_material'),
        ('starassm - 316SS HTS Outer 9-2.STL', 'Steel_material'),
        ('starassm - 316SS HTS Outer 9-3.STL', 'Steel_material'),
        ('starassm - 316SS HTS Outer 9-4.STL', 'Steel_material'),
        ('starassm - 316SS HTS Outer 9-5.STL', 'Steel_material'),
        ('starassm - 316SS HTS Outer 9-6.STL', 'Steel_material'),


        ('starassm - 316SS Inner Coil Structure-1.STL', 'Steel_material'),


        ('starassm - 316SS VV-1.STL', 'Steel_material'),


        ('starassm - Breeder 97 Steel 3 IB-1.STL', 'Breeder_material'), #was mat_3
        ('starassm - Breeder 97 Steel 3 OB-1.STL', 'Breeder_material'),


        ('starassm - Coolant 50 Steel 50 IB Top-1.STL', 'Coolant_material'), #was mat_4
        ('starassm - Coolant 50 Steel 50 OB Bottom-1.STL', 'Coolant_material'),
        ('starassm - Coolant 50 Steel 50 OB Top-1.STL', 'Coolant_material'),
        ('starassm - Coolant 50 Steel 50 Transition Bottom-1.STL', 'Coolant_material'),
        ('starassm - Coolant 50 Steel 50 Transition Top-1.STL', 'Coolant_material'),


        ('starassm - Coolant 88 Steel 12 IB-1.STL', 'Coolant_material'), #was mat_5
        ('starassm - Coolant 88 Steel 12 OB Inner-1.STL', 'Coolant_material'),
        ('starassm - Coolant 88 Steel 12 OB Outer-1.STL', 'Coolant_material'),


        ('starassm - Copper 50 Hatelloy 50 HTS 7-1.STL', 'Steel_material'), #might change to copper? (was mat_6)
        ('starassm - Copper 50 Hatelloy 50 HTS 7-2.STL', 'Steel_material'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-3.STL', 'Steel_material'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-4.STL', 'Steel_material'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-5.STL', 'Steel_material'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-6.STL', 'Steel_material'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-7.STL', 'Steel_material'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-8.STL', 'Steel_material'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-9.STL', 'Steel_material'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-10.STL', 'Steel_material'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-11.STL', 'Steel_material'),
        ('starassm - Copper 50 Hatelloy 50 HTS 7-12.STL', 'Steel_material'),


        ('starassm - Passive Plate Top-1.STL', 'Steel_material'), #was mat_7
        ('starassm - Passive Plate Top-2.STL', 'Steel_material'),


        ('starassm - Plasma-1.STL', 'fuel'), #was mat_8 (make uranium material to update here) (made this steel_material for testing. Will change back to proper later - Rocco 02/16)


        ('starassm - Shield 97 Steel 3 IB Outer-1.STL', 'Shielding_material'), #was mat_9
        ('starassm - Shield 97 Steel 3 Inner-1.STL', 'Shielding_material'),
        ('starassm - Shield 97 Steel 3 OB-1.STL', 'Shielding_material'),


        ('starassm - Steel IB Inner Shield Structure-1.STL', 'Steel_material'), #was mat_10
        ('starassm - Steel IB Inner-1.STL', 'Steel_material'),
        ('starassm - Steel IB Outer Shield Structure-1.STL', 'Steel_material'),
        ('starassm - Steel IB Outer-1.STL', 'Steel_material'),
        ('starassm - Steel OB Inner-1.STL', 'Steel_material'),
        ('starassm - Steel OB Outer-1.STL', 'Steel_material'),
        ('starassm - Steel OB Shield Structure-1.STL', 'Steel_material'),
    ],
    h5m_filename='STAR5_Whole.h5m',
)
