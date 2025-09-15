import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    data = []
    for store_no in range(1,4):
        store = f'store{store_no}'
        store_data = [(product_id, store, price) for product_id, price in products[['product_id',store]][~products[store].isnull()].values]
        data.extend(store_data)
        
    print( pd.DataFrame(columns=['product_id','store','price'], data=data))


data = [
    (0, 95, 100, 105),
    (1, 70, None, 80)
    ]


products = pd.DataFrame(columns=['product_id', 'store1', 'store2', 'store3'], data = data)
rearrange_products_table(products)