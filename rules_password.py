import re

def min_size(string: str, value: int) -> bool:
        
    if len(string) < value:
        return False
    return True

def min_upper_case(string: str, value: int) -> bool:
    
    countUpperCaseChars = sum(1 for c in string if c.isupper())
    
    if countUpperCaseChars < value:
        return False
    return True

def min_lower_case(string: str, value: int) -> bool:
    
    countLowerCaseChars = sum(1 for c in string if c.islower())
    
    if countLowerCaseChars < value:
        return False
    return True

def min_digit(string: str, value: int) -> bool:
        
    countDigits = sum(1 for c in string if c.isdigit())
    
    if countDigits < value:
        return False
    return True

def min_special_chars(string: str, value: int) -> bool:
    
    specialChars = r'!@#$%^&*()-+\/{}[]'    
    countSpecialChars = sum(string.count(c) for c in list(specialChars))
    
    if countSpecialChars < value:
        return False
    return True

def no_repeted(string: str, value=None) -> bool:
    
    # https://stackoverflow.com/a/28007115    
    if re.search(r'(.)\1', string):
        return False
    return True