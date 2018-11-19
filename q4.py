"""
----------------------------------------------------
q4.py
pq_combine
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-02-01"
----------------------------------------------------
"""
from asgn04 import pq_combine
from priority_queue_array import PriorityQueue
pq1 = PriorityQueue()
pq2 = PriorityQueue()
pq1.insert(0)
pq1.insert(2)
pq2.insert(1)
pq2.insert(3)
pq3 = pq_combine(pq1, pq2)

for i in pq3:
    print(i)

