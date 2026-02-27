# cSpell: Disable

# NOTICE: This file will not work unless you move all of the .stl files to the CAD_TO_OPENMC directory! They were only moved to a dedicated folder for cosmetic purposes. If you plan on running this code, move all 74 .stls to CAD_TO_OPENMC first. When finished, put them back!
from stl_to_h5m import stl_to_h5m

stl_to_h5m(
    files_with_tags=[
        ('316SSCoilStructure1.stl', 'Steel_material'), #Applying steel to coils for now (was mat_1)
        ('316SSCoilStructure2.stl', 'Steel_material'),
        ('316SSCoilStructure3.stl', 'Steel_material'),
        ('316SSCoilStructure4.stl', 'Steel_material'),
        ('316SSCoilStructure5.stl', 'Steel_material'),
        ('316SSCoilStructure6.stl', 'Steel_material'),
        ('316SSCoilStructure7.stl', 'Steel_material'),
        ('316SSCoilStructure8.stl', 'Steel_material'),
        ('316SSCoilStructure9.stl', 'Steel_material'),
        ('316SSCoilStructure10.stl', 'Steel_material'),
        ('316SSCoilStructure11.stl', 'Steel_material'),
        ('316SSCoilStructure12.stl', 'Steel_material'),

        ('316SSHTSInner1.stl', 'Steel_material'), #Assuming these are structural supports (was mat_2)
        ('316SSHTSInner2.stl', 'Steel_material'),
        ('316SSHTSInner3.stl', 'Steel_material'),
        ('316SSHTSInner4.stl', 'Steel_material'),
        ('316SSHTSInner5.stl', 'Steel_material'),
        ('316SSHTSInner6.stl', 'Steel_material'),
        ('316SSHTSInner7.stl', 'Steel_material'),
        ('316SSHTSInner8.stl', 'Steel_material'),
        ('316SSHTSInner9.stl', 'Steel_material'),
        ('316SSHTSInner10.stl', 'Steel_material'),
        ('316SSHTSInner11.stl', 'Steel_material'),
        ('316SSHTSInner12.stl', 'Steel_material'),


        ('316SSHTSOuter1.stl', 'Steel_material'),
        ('316SSHTSOuter2.stl', 'Steel_material'),
        ('316SSHTSOuter3.stl', 'Steel_material'),
        ('316SSHTSOuter4.stl', 'Steel_material'),
        ('316SSHTSOuter5.stl', 'Steel_material'),
        ('316SSHTSOuter6.stl', 'Steel_material'),
        ('316SSHTSOuter7.stl', 'Steel_material'),
        ('316SSHTSOuter8.stl', 'Steel_material'),
        ('316SSHTSOuter9.stl', 'Steel_material'),
        ('316SSHTSOuter10.stl', 'Steel_material'),
        ('316SSHTSOuter11.stl', 'Steel_material'),
        ('316SSHTSOuter12.stl', 'Steel_material'),


        ('316SSInnerCoilStructure.stl', 'Steel_material'),


        ('316SSVV.stl', 'Steel_material'),


        ('Breeder97Steel3IB.stl', 'Breeder_material'), #was mat_3
        ('Breeder97Steel3OB.stl', 'Breeder_material'),


        ('Coolant50Steel50IBTop.stl', 'Coolant_material'), #was mat_4
        ('Coolant50Steel50OBBottom.stl', 'Coolant_material'),
        ('Coolant50Steel50OBTop.stl', 'Coolant_material'),
        ('Coolant50Steel50TransitionBottom.stl', 'Coolant_material'),
        ('Coolant50Steel50TransitionTop.stl', 'Coolant_material'),


        ('Coolant88Steel12IB.stl', 'Coolant_material'), #was mat_5
        ('Coolant88Steel12OBInner.stl', 'Coolant_material'),
        ('Coolant88Steel12OBOuter.stl', 'Coolant_material'),


        ('Copper50Hatelloy50HTS1.stl', 'Steel_material'), #might change to copper? (was mat_6)
        ('Copper50Hatelloy50HTS2.stl', 'Steel_material'),
        ('Copper50Hatelloy50HTS3.stl', 'Steel_material'),
        ('Copper50Hatelloy50HTS4.stl', 'Steel_material'),
        ('Copper50Hatelloy50HTS5.stl', 'Steel_material'),
        ('Copper50Hatelloy50HTS6.stl', 'Steel_material'),
        ('Copper50Hatelloy50HTS7.stl', 'Steel_material'),
        ('Copper50Hatelloy50HTS8.stl', 'Steel_material'),
        ('Copper50Hatelloy50HTS9.stl', 'Steel_material'),
        ('Copper50Hatelloy50HTS10.stl', 'Steel_material'),
        ('Copper50Hatelloy50HTS11.stl', 'Steel_material'),
        ('Copper50Hatelloy50HTS12.stl', 'Steel_material'),


        ('PassivePlateBottom.stl', 'Steel_material'), #was mat_7
        ('PassivePlateTop.stl', 'Steel_material'),


        ('Plasma.stl', 'fuel'), #was mat_8 (make uranium material to update here) (made this steel_material for testing. Will change back to proper later - Rocco 02/16)


        ('Shield97Steel3IBOuter.stl', 'Shielding_material'), #was mat_9
        ('Shield97Steel3Inner.stl', 'Shielding_material'),
        ('Shield97Steel3OB.stl', 'Shielding_material'),
        ('Shield97316SS3InsideShield.stl', 'Steel_material'), #was mat_10


        ('SteelIBInner.stl', 'Steel_material'),
        ('SteelIBInnerShieldStructure.stl', 'Steel_material'),
        ('SteelIBOuter.stl', 'Steel_material'),
        ('SteelIBOuterShieldStructure.stl', 'Steel_material'),
        ('SteelOBInner.stl', 'Steel_material'),
        ('SteelOBOuter.stl', 'Steel_material'),
        ('SteelOBShieldStructure.stl', 'Steel_material')
    ],
    h5m_filename='STAR5_Whole.h5m',
)
