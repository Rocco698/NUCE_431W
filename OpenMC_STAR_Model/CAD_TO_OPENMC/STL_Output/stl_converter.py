# cSpell: Disable

# NOTICE: Run this script in the same directory as the .stl files. 
from stl_to_h5m import stl_to_h5m

stl_to_h5m(
    files_with_tags=[
        ('Breeder97Steel3OB_scaled.stl', 'Breeder_material'),
    ],
    h5m_filename='Breeder97Steel3OB_scaled.h5m',
)