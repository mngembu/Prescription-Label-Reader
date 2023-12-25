import re
import src.outil

class PrescriptionParser():
    def __init__(self, text):
        self.text = text
        
    def parse(self):
        prescription_name = self.get_field('prescription_name')
        dosage = (self.get_field('dosage').replace("GIVE", "TAKE")).lower().replace('\n\n', '')
        refills = self.get_field('refills')
        expirydate = self.get_field('expirydate')
        
        message_text = f'Hello, as prescription for the drug {prescription_name}, {dosage}. It can be refilled {refills} times, on or before {expirydate}.'
        
        speech = src.outil.text2speech(message_text)
        
        return speech
                       
    
    def get_field(self, field_name):
        pattern = ''
        flags = 0
        
        pattern_dict = {
            'prescription_name' : {'pattern': '(.*)Drug', 'flags' : 0},
            'dosage' : {'pattern': 'Netcare[^\n]*(.*)All', 'flags' : re.DOTALL},
            'refills' : {'pattern': 'Refilis:(.*)', 'flags' : 0},
            'expirydate' : {'pattern': 'Refills.Expire:(.*)', 'flags' : 0}
        }
        
        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()
                
            
        
        
      
    
#if __name__ == "__main__":
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
    
    
    #pp = PrescriptionParser(label_text)
    #print(pp.parse())