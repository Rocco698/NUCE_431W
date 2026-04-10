# cSpell: Disable

# NOTICE: Run this script in the same directory as the .stl files. 
from stl_to_h5m import stl_to_h5m

stl_to_h5m(
    files_with_tags=[
        ('Breeder97Steel3OB_scaled.stl', 'Breeder_material'),
        ('Breeder97Steel3IB_scaled.stl', 'Breeder_material'),

        ('trans_316SSHTSInner1.stl', 'Steel_material'),
        ('trans_316SSHTSInner2.stl', 'Steel_material'),
        ('trans_316SSHTSInner3.stl', 'Steel_material'),
        ('trans_316SSHTSInner4.stl', 'Steel_material'),
        ('trans_316SSHTSInner5.stl', 'Steel_material'),
        ('trans_316SSHTSInner6.stl', 'Steel_material'),
        ('trans_316SSHTSInner7.stl', 'Steel_material'),
        ('trans_316SSHTSInner8.stl', 'Steel_material'),
        ('trans_316SSHTSInner9.stl', 'Steel_material'),
        ('trans_316SSHTSInner10.stl', 'Steel_material'),
        ('trans_316SSHTSInner11.stl', 'Steel_material'),
        ('trans_316SSHTSInner12.stl', 'Steel_material'),

        ('trans_316SSHTSOuter1.stl', 'Steel_material'),
        ('trans_316SSHTSOuter2.stl', 'Steel_material'),
        ('trans_316SSHTSOuter3.stl', 'Steel_material'),
        ('trans_316SSHTSOuter4.stl', 'Steel_material'),
        ('trans_316SSHTSOuter5.stl', 'Steel_material'),
        ('trans_316SSHTSOuter6.stl', 'Steel_material'),
        ('trans_316SSHTSOuter7.stl', 'Steel_material'),
        ('trans_316SSHTSOuter8.stl', 'Steel_material'),
        ('trans_316SSHTSOuter9.stl', 'Steel_material'),
        ('trans_316SSHTSOuter10.stl', 'Steel_material'),
        ('trans_316SSHTSOuter11.stl', 'Steel_material'),
        ('trans_316SSHTSOuter12.stl', 'Steel_material'),

        ('trans_Shield97Steel3IBOuter.stl', 'Shielding_material'),
        ('trans_Shield97Steel3Inner.stl', 'Shielding_material'),
        ('trans_Shield97Steel3OB.stl', 'Shielding_material'),
        ('trans_Shield97316SS3InsideShield.stl', 'Shielding_material'),
    ],
    h5m_filename='_scaled.h5m',
)