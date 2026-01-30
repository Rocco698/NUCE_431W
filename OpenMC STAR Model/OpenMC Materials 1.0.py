# ##############################################
#       MATERIALS
# ##############################################

#Material Initialization
Steel_material = openmc.Material(name='Steel-EUROFER97')
Shielding_material = openmc.Material(name='Shielding-B4C')
Breeder_material = openmc.Material(name='Breeder-PbLi')
Coolant_material = openmc.Material(name='Coolant-He (8MPA)')

#Steel-EUROFER97
Steel_material.mix_materials([Fe,C,Cr,W,Mn,Ta,N2],[0.8924,0.0011,0.09,0.011,0.004,0.0012,0.0003],'wo')
#Shielding-B4C
Shielding_material.add_element('B',4.0,'ao')
Shielding_material.add_element('C',1.0,'ao')
Shielding_material.set_density('g/cm3',2.50)
#Breeder-PbLi/FLiBe/Li/Li4SiO4
    ##PbLi
Breeder_material.add_element('Pb',0.83,'ao')
Breeder_material.add_element('Li',0.17,'ao')
#Breeder_material.add_element('Li',0.17,enrichment=92,enrichment_target='Li6')
Breeder_material.set_density('g/cm3',9.5)
    ##FLiBe
Breeder_material.add_element('F',4.0,'ao')
Breeder_material.add_element('Li',2.0,'ao')
#Breeder_material.add_element('Li',2.0,enrichment=92,enrichment_target='Li6')
Breeder_material.add_element('Be',1.0,'ao')
Breeder_material.set_density('g/cm3',1.94)
    ##Li
Breeder_material.add_element('Li',1.0,'ao')
#Breeder_material.add_element('Li',1.0,enrichment=92,enrichment_target='Li6')
Breeder_material.set_density('g/cm3',0.534)
    ##Li4SiO4
Breeder_material.add_element('Li',4.0,'ao')
#Breeder_material.add_element('Li',4.0,enrichment=92,enrichment_target='Li6')
Breeder_material.add_element('Si',1.0,'ao')
Breeder_material.add_element('O',4.0,'ao')
Breeder_material.set_density('g/cm3',2.35)
#Coolant-He (8MPA)
Coolant_material.add_element('He',1.0,'ao')
Coolant_material.set_density('kg/m3',5.0)


mat_list= openmc.Materials([Steel_material,Shielding_material,Breeder_material,Coolant_material])
mat_list.export_to_xml()

print(mat_list)
mat_list.cross_sections = "/data/endfb-viii.0-hdf5/cross_sections.xml"
