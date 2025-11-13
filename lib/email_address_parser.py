# your code goes here!

import re

class EmailAddressParser:
    EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    def __init__(self, text):
        self.text = text

    def parse(self):
        emails = re.findall(self.EMAIL_REGEX, self.text)
        
        unique_emails = list(set(emails))
        
        unique_emails.sort()
        
        return unique_emails
