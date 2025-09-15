import pandas as pd

INPUT="""+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+""".splitlines()

def guess_type(s:str):
    try :
        f = float(s)
    except:
        return s
    
    return f if f%1 else int(f)


def convert_to_data(s:str)->list:
    return   [guess_type(s) for s in (filter(None, map(lambda f:f.strip(), s.split('|'))))]


def get_data_frame(input:list)->pd.DataFrame:
    columns = convert_to_data(input[1]) 
    data = list(map(convert_to_data, input[3:-1]))
    return pd.DataFrame(columns=columns, data=data)


if __name__ == "__main__":
    print(get_data_frame(INPUT))


