
############## Snippet (Min Heap) ################
import heapq
A = [1,3,4,2,7]
heapq.heapify(A)	   # Build Min Heap
heapq.heappop(A) # 1   # Pop min
heapq.heappush(A, 0)   # Push 0
############## Snippet END ################










############## Snippet (Max Heap) ################
import heapq
A = [1,3,4,2,7]
A2 = [-x for x in A]
heapq.heapify(A2)
heapq.heappop(A2) * -1  # 7
############## Snippet END ################








############## Snippet (Heap for Object) ################
import heapq
class Person:
    def __init__(self, no, name):
        self.no = no
        self.name = name
A = [
    Person(1, "John"),
    Person(2, "Mary"),
    Person(3, "Ted"),
]
A2 = [(obj.no, obj) for obj in A]
heapq.heapify(A2)
heapq.heappop(A2)  # (1, Person(John))
############## Snippet END ################