import pandas as pd 

brewerEvents = pd.read_json('BrewerEvents.json')
customer = pd.read_csv('Customer.csv')

brewerEventsWithCustomerDetails = brewerEvents.join(customer.set_index())
customer.rename(columns={'device-sequence-number':'device-seq-id'})

brewerEventsWithCustomerDetails = brewerEvents.join(customer.set_index('device-seq-id'),on='device-sequence-number', lsuffix='',rsuffix='_cust', how='inner')

len(brewerEventsWithCustomerDetails)

a = [1,3,5]
sorted(a,)

from datetime import datetime
from dateutil.relativedelta import relativedelta

year_ago = datetime.now() - relativedelta(years=1)