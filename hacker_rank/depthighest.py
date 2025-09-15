import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    groups = employee.groupby(by='departmentId')
    data = []
    for g in groups: 
        data.extend(g[1][g[1].salary == g[1].salary.max()].values.tolist())

    department.rename(columns={'id':'departmentId','name':'Department'},  inplace=True)
    
    maxSals = pd.DataFrame(columns=employee.columns, data=data)\
                    .merge(department, on="departmentId")\
                    .rename(columns={'name':'Employee','salary':'Salary'})\
                    [['Department', 'Employee','Salary']]


    return maxSals




data = [ 
    (1, 'Joe', 70000, 1),
    (2, 'Jim', 90000, 1),
    (3, 'Henry', 80000, 2),
    (4, 'Sam', 60000, 2),
    (5, 'Max', 90000, 1)
]


employee=pd.DataFrame(columns=['id','name','salary','departmentId'], data = data)
department = pd.DataFrame(columns=['id','name'], data=[(1,'IT'),(2,'Sales')])

print(department_highest_salary(employee, department))