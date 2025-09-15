from datetime import datetime, timezone
from testcases import DATESTRINGS

def time_delta(t1, t2):
    t1_obj = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2_obj = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

    print(abs(int((t1_obj-t2_obj).total_seconds())))

if __name__=="__main__":
    for i in range(0, len(DATESTRINGS), 2):                         
        time_delta(DATESTRINGS[i],DATESTRINGS[i+1])