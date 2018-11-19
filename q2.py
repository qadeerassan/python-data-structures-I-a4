"""
----------------------------------------------------
q2.py
Tests combine() in priority queue.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-01-31"
----------------------------------------------------
"""
from priority_queue_array import PriorityQueue
pq1 = PriorityQueue()
pq2 = PriorityQueue()

pq1.insert(0)
pq2.insert(1)
pq1.insert(2)
pq2.insert(3)
for i in pq1:
    print(i,"pq1")
for i in pq2:
    print(i,"pq2")

pq3 = pq1.combine(pq2)
for i in pq3:
    print(i, "pq3")