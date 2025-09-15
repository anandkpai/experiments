import pandas as pd

employee = pd.DataFrame(columns=['id','salary'], data=[(1,100),(2,200),(3,300)])


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(subset=['salary'], inplace=True)
    employee.drop(employee.loc[employee.salary == employee.salary.max()].index, inplace=True)
    return pd.DataFrame(columns=['SecondHighestSalary'], data=[employee.salary.max()])

print(second_highest_salary(employee))
