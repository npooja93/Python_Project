import re
from datetime import datetime

email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
date_format = '%m/%d/%y %H:%M'
def checkEmail(val):
    if re.search(email_regex, val):
        return True
    else:
        return False
    
    
def date_formatting(date_value,hrs_value):
    combined_value = date_value+" "+hrs_value
    print(combined_value)
    date_obj = datetime.strptime(combined_value, date_format)
    return date_obj


