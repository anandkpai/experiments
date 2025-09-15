from input_parser import get_data_frame

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

employee = get_data_frame(INPUT)

import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    eligible_managers = employee.groupby(by='managerId').filter(lambda g:len(g)>4)['managerId']
    series =  pd.merge(eligible_managers, employee, left_on='managerId', right_on='id', how='inner')['name'].drop_duplicates()
    return pd.DataFrame(columns=['name'], data = series)
    

if __name__=="__main__":
    print(find_managers(employee))