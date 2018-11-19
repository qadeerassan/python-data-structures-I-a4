"""
----------------------------------------------------
q5.py
Tests identical function.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-02-01"
----------------------------------------------------
"""
from queue_array import Queue
from asgn04 import identical
q1 = Queue()
q2 = Queue()
q1.insert(0)
q1.insert(2)
q2.insert(0)
q2.insert(2)
b = identical(q1, q2)
print("q1==q2: ", b)

q3 = Queue()
q4 = Queue()
q3.insert(0)
q3.insert(2)
q4.insert(1)
q4.insert(3)
c = identical(q3, q4)
print("q3==q4: ", c)