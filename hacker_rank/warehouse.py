from input_parser import get_data_frame

Inventory="""+---------+----------------+---------------+----------------+
| item_id | item_type      | item_category | square_footage | 
+---------+----------------+---------------+----------------+
| 1374    | prime_eligible | Watches       | 68.00          | 
| 4245    | not_prime      | Art           | 26.40          | 
| 5743    | prime_eligible | Software      | 325.00         | 
| 8543    | not_prime      | Clothing      | 64.50          |  
| 2556    | not_prime      | Shoes         | 15.00          |
| 2452    | prime_eligible | Scientific    | 85.00          |
| 3255    | not_prime      | Furniture     | 22.60          | 
| 1672    | prime_eligible | Beauty        | 8.50           |  
| 4256    | prime_eligible | Furniture     | 55.50          |
| 6325    | prime_eligible | Food          | 13.20          | 
+---------+----------------+---------------+----------------+"""

inventory = get_data_frame(Inventory.splitlines())

import pandas as pd

def maximize_items(inventory: pd.DataFrame) -> pd.DataFrame:
    SQ_FEET_WAREHOUSE=500_000
    prime_eligible = inventory[inventory.item_type=='prime_eligible'].square_footage
    prime_sum = prime_eligible.sum()
    item_count = len(prime_eligible)
    combos_count = SQ_FEET_WAREHOUSE//prime_sum
    combos_space = prime_sum * combos_count
    prime_items_total_count = combos_count * item_count
    
    remaining_space = max(SQ_FEET_WAREHOUSE - combos_space,0)
    print(remaining_space)
    nprime = inventory[inventory.item_type=='not_prime'].square_footage
    nprime_sum = nprime.sum()
    nitem_count = len(nprime)
    ncombos_count = remaining_space//nprime_sum
    nprime_items_total_count = ncombos_count * nitem_count

    data = [
            ('prime_eligible',  prime_items_total_count),
            ('not_prime', nprime_items_total_count)
            ]
    return pd.DataFrame(columns=['item_type','item_count'], data=data)


print(maximize_items(inventory))

    




if __name__=="__main__":
    maximize_items(inventory)