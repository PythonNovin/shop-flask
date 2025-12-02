def isvalid_phone(phone):
    if len(phone) != 11:
        return False
    
    if not phone.startswith("09"):
        return False
    
    if not phone.isdigit():
        return False
    
    
def isvalid_password(password):
    return not 6 < len(password) < 32