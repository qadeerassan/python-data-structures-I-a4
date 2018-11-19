"""
----------------------------------------------------
asgn04.py
Holds functions for assignment 4.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-02-01"
----------------------------------------------------
"""
from priority_queue_array import PriorityQueue
from utilities import array_to_queue, queue_to_array
def pq_combine(pq1, pq2):
    """
    -------------------------------------------------------
    Combines contents of two priority queues into a new 
    priority queue. Alternate the values from pq1 and pq2.
    Use: q3 = pq_combine(pq1, pq2)
    -------------------------------------------------------
    Preconditions:
        pq1 - a priority queue (PriorityQueue)
        pq2 - a priority queue (PriorityQueue)
    Postconditions:
        returns
        pq3 - Contents of pq1 and pq2 are moved 
            into pq3 (PriorityQueue)
    -------------------------------------------------------
    """
    pq3 = PriorityQueue()
    while len(pq1) > 0 or len(pq2) > 0:
        if len(pq1) > 0:
            pq3.insert(pq1.remove())
        if len(pq2) > 0:
            pq3.insert(pq2.remove())
    return pq3

def identical(q1, q2):
    """
    ----------------
    Determines whether two given queues are identical.
    Entries of q1 and q2 are compared and if all contents are identical
    and in the same order, returns True, otherwise returns False.
    Use: b = identical(q1, q2)
    ---------------
    Preconditions:
        q1 - a queue (Queue)
        q2 - a queue (Queue)
    Postconditions:
        returns
        is_identical - True if q1 and q2 are identical, False otherwise. 
            Queues are unchanged. (boolean)
    ---------------
    """
    is_identical = True
    if len(q1) == len(q2):
        q1_a = []
        queue_to_array(q1, q1_a)
        q2_a = []
        queue_to_array(q2, q2_a)
        if q1_a == q2_a:
            is_identical = True
        else:
            is_identical = False
        array_to_queue(q1, q1_a)
        array_to_queue(q2, q2_a)
    else:
        is_identical = False
    return is_identical