import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores.score.rank(method='dense', ascending=False).apply(int)    
    return scores[['score','rank']].sort_values(by='score', ascending=False)




data = [
        (1,3.50),
        (2,3.65),
        (3,4.00),
        (4,3.85),
        (5,4.00),
        (6,3.65)
        ]

scores = pd.DataFrame(columns=['id','score'], data=data)

print(order_scores(scores))