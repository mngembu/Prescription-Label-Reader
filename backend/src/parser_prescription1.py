import re

class PrescriptionParser():
    def __init__(self, text):
        self.text = text
        
    def parse(self):
        prescription_name = self.get_prescription_name()
        dosage = self.get_dosage()
        refills = self.get_refills()
        expirydate = self.get_expirydate()
        
        message_text = f'Hello, as prescription for the drug {prescription_name}, {dosage}. It can be refilled {refills} times, on or before {expirydate}.'
        return message_text
    
    
    def get_prescription_name(self):
        pattern = '(.*)Drug'
        matches = re.findall(pattern, self.text)
        if len(matches)>0:
            return matches[0].strip()
        
    def get_dosage(self):
        pattern = 'Netcare[^\n]*(.*)All'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches)>0:
            return (matches[0].replace("GIVE", "TAKE")).strip().lower().replace('\n\n', ' ')
    
    def get_refills(self):
        pattern = 'Refilis:(.*)'
        matches = re.findall(pattern, self.text)
        if len(matches)>0:
            return matches[0].strip()
    
    def get_expirydate(self):
        pattern = 'Refills.Expire:(.*)'
        matches = re.findall(pattern, self.text)
        if len(matches)>0:
            return matches[0].strip()
    
    
    
if __name__ == "__main__":
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
    
    
    pp = PrescriptionParser(label_text)
    print(pp.parse())