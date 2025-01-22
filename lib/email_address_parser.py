import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    
    def parse(self):
        
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        
        
        addresses = re.split(r'[,\s]+', self.email_addresses.strip())
        
        
        valid_addresses = [email for email in addresses if re.match(email_pattern, email)]
        
        unique_addresses = sorted(set(valid_addresses))
        
        return unique_addresses