from ordered_set import OrderedSet


def factors(n:int,start=1):
    top = n//2+1
    for i in range(start,top+1):
        if n%i == 0 :
            yield(i)            


def check(s:str,t:str, set_s={}):
    # basic check for length 
    if len(s)%len(t) > 0 :
        return False
    
    # basic check for characters
    set_s = set_s if len(set_s) else OrderedSet(list(s))
    set_t = OrderedSet(list(t))
    if set_s != set_t:
        return False
    
    for start in range(0,len(s),len(t)):
        if s[start:start+len(t):] != t:
            return False
    
    return True 

def findSmallestDivisor(s, t):
    
    if not check(s,t):
        return -1 
        
    # if we didn't return -1, we got a divisor, so it is valid
    # now we have to check if the t string itself can be divided 

    # for efficiency, we create the Ordered set of t once
    set_t = OrderedSet(list(t))
    
    # we know that the minimum length is the number of characters 
    start = len(set_t)
    valid_lengths = factors(len(t), start)

    while l:=next(valid_lengths,None):
        substr = t[:l:]
        if check(t,substr,set_t):
            return l
    
    return len(t)


if __name__ =='__main__':
    s= 'rbrb'
    t ='rb'
    print(findSmallestDivisor(s,t))


