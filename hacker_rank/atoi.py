import re

def myAtoi(s: str) -> int:
    if s[0] in('+','-'):
        leadChar = s[0]
        checkstring = s[1:]
        neg_pos_multiplier = -1
    else : 
        neg_pos_multiplier = +1
        leadChar = ''
        checkstring = s

    match = re.search('[^0-9]', checkstring)
    if not match:
        return int(s) 
    else :
        try : 
            val = neg_pos_multiplier *int(checkstring[:match.start()])
        except: 
            print(checkstring[:match.start()])
            return 1

print(myAtoi("   -042"))