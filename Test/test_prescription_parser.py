

import pytest
import sys

#adding src to the system path because
sys.path.insert(0, 'C:/Users/amari/OneDrive/Documents/Data science internships/Prescription-Label-Reader/backend/src')

from parser_prescription import PrescriptionParser

def test_get_prescription_name():
    pp = PrescriptionParser(label_text)
    assert pp.get_field('prescription_name') == 'Ondansetron 4mg'
    
def test_get_refills():
    pp = PrescriptionParser(label_text)
    assert pp.get_field('refills') == '8'    
    
def test_get_dosage():
    pp = PrescriptionParser(label_text)
    assert pp.get_field('dosage') == 'take 1.5 tablets 3 times dailywhen required'
    
def test_get_expirydate():
    pp = PrescriptionParser(label_text)
    assert pp.get_field('expirydate') == '29-Mar-2024'
    



    

label_text = '''
Gateway Pharmacy . {780). 466- -6337_
942 3803 Calgary Trail, Edmonton, AB Ted 5M8_

Rx: 2016003
Dr. Abobo. Moses ©

“WC 19-Jan-2023
10 TAB Sandoz-Ondansetron ODT 4mq

Ondansetron 4mg Drug Exo: [20
DIN: 02481723 Mfr: SDZ Refilis: 8

Netcare Order #:00HVQBQ1_—_—s Netcare Disp #:0099WPDDOOLHEZKT

GIVE 1.5 TABLETS 3 TIMES DAILY

WHEN REQUIRED
All Refills Expire: 29-Mar-2024
'''