from typing import *

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_keys = dict()
        record_keys = dict()
        for i in range(len(accounts)):
            record = accounts[i]
            email_set = set(record[1:])
            intersection = email_keys.keys() - (email_keys.keys()-email_set)
            record_index = i
            intersection_exists = False
            if intersection  # this exists previously 
                intersection_exists = True                
                if len(intersection) == 1:  # but only once.
                    intersection_email = intersection.pop()
                    record_index = email_keys[intersection_email]
                else :   # we found a more complicated case, we have to re-do the previous records
                    



            for email in email_set:
                email_keys[email] = record_index 
            if intersection_exists:
                record_keys[record_index] = email_set.union(record_keys[record_index])
            else:
                record_keys[record_index] = email_set
            
        mergedAccounts = []
        for index,email_set in record_keys.items():
            record = [accounts[index][0]]
            record.extend(sorted(email_set))
            mergedAccounts.append(record)

        return mergedAccounts 
    
accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]

print(Solution().accountsMerge(accounts))