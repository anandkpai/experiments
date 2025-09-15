from itertools import groupby
if __name__== "__main__":
    string = "1222311"
    
    for key, group  in groupby(list(string)):
        print(f'({len(list(group))}, {key})', end=' ')
    

