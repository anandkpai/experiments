from input_parser import get_data_frame


Employee="""+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+"""

Department="""+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+"""

employee = get_data_frame(Employee.splitlines())
department = get_data_frame(Department.splitlines())

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # first drop the duplicate salaries by department
    unique_salaries_by_department = employee[['departmentId', 'salary']].drop_duplicates()
    # then sort 
    unique_salaries_by_department.sort_values(axis=0, by=['departmentId','salary'], ascending=[True, False], inplace=True)
    # now find the third salary, if there  isn't a third, then all salaries qualify
    groups = unique_salaries_by_department.groupby(by='departmentId')
    third_sals_by_department = [(dept_id, groupdata['salary'].iloc[2] if len(groupdata)>2 else 0) for dept_id, groupdata in groups]
    department_cutoff = pd.DataFrame(columns=['departmentId','salary_cut_off'], data = third_sals_by_department)

    with_cutoff = employee.join(department_cutoff.set_index('departmentId'), how='inner', on='departmentId')
    highly_paid = with_cutoff[with_cutoff['salary']>=with_cutoff['salary_cut_off']] [['departmentId','name','salary']]
    print(highly_paid)

    department.rename(columns={'id':'departmentId'}, inplace=True)

    hp_with_department = highly_paid.join(department.set_index('departmentId'), how= 'inner', on='departmentId', lsuffix='', rsuffix='_r')[['name_r','name', 'salary']]
    hp_with_department.rename(columns={'name_r':'Deparment','name':'Employee', 'salary':'Salary'}, inplace=True)
    
    return hp_with_department


    




top_three_salaries(employee, department)
