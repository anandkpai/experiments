from input_parser import get_data_frame

Candidates="""+--------------+---------+--------------+--------------+
| candidate_id | name    | years_of_exp | interview_id |
+--------------+---------+--------------+--------------+
| 11           | Atticus | 1            | 101          |
| 9            | Ruben   | 6            | 104          |
| 6            | Aliza   | 10           | 109          |
| 8            | Alfredo | 0            | 107          |
+--------------+---------+--------------+--------------+"""
# candidate_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name of a candidate, their number of years of experience, and their interview ID.
 

Rounds="""+--------------+----------+-------+
| interview_id | round_id | score |
+--------------+----------+-------+
| 109          | 3        | 4     |
| 101          | 2        | 8     |
| 109          | 4        | 1     |
| 107          | 1        | 3     |
| 104          | 3        | 6     |
| 109          | 1        | 4     |
| 104          | 4        | 7     |
| 104          | 1        | 2     |
| 109          | 2        | 1     |
| 104          | 2        | 7     |
| 107          | 2        | 3     |
| 101          | 1        | 8     |
+--------------+----------+-------+"""

candidates = get_data_frame(Candidates.splitlines())
rounds = get_data_frame(Rounds.splitlines())


import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:

    rplus = rounds.merge(candidates[candidates.years_of_exp >= 2], how='inner')
    selected = rplus.groupby(by='candidate_id').filter(lambda g:g['score'].sum()>15)['candidate_id'].drop_duplicates()
    return pd.DataFrame(columns=['candidate_id'], data = selected)
    




if __name__=="__main__":
    accepted_candidates(candidates, rounds)