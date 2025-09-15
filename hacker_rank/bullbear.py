import pandas as pd
import re
from collections import Counter
bullBearRe = re.compile(r'(?<=\s)bull(?=\s)|(?<=\s)bear(?=\s)')


df = pd.DataFrame(columns=['file_name','content'], 
                  data=[('draf1.txt','The stock exchange predicts a bull market which would make many investors happy.'),
                        ('draf2.txt','The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market'),
                        ('draf3.txt','The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market. As always predicting the future market is an uncertain game and all investors should follow their instincts and best practices.'),
                        ])


def bulls_bears(s:str)->tuple[int,int]:
    c = Counter(s.findall(bullBearRe,s))
    return (c.get('bull',0),c.get('bear',0))


def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:    
    results = files.content.apply(bulls_bears).to_list()
    print(pd.DataFrame(results, columns=['bull','bear']))

if __name__=="__main__":
    df2 = count_occurrences(df)
    # print(df2)



