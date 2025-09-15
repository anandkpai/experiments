import pandas as pd
import re
DIAB_RE = re.compile('(^|\s)DIAB1')

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients.conditions.str.contains(DIAB_RE)]


data = [(1, "Daniel", "YFEV COUGH"), 
        (2, "Alice",""),
        (3, "Bob", "DIAB100 MYOP"),
        (4, "George", "ACNE DIAB100"),
        (5, "Alain", "DIAB201")]

patients = pd.DataFrame(columns=['patient_id','patient_name','conditions'], data=data)

df = find_patients(patients)

print(df)
