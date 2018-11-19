"""
----------------------------------------------------
q3.py

----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-02-01"
----------------------------------------------------
"""
from priority_queue_array import PriorityQueue
pq1 = PriorityQueue()
key = 3
pq1.insert(1)
pq1.insert(2)
pq1.insert(3)
pq1.insert(4)

pq2, pq3 = pq1.split(key)
for i in pq2:
    print(i, 'pq2')
for i in pq3:
    print(i, 'pq3')
