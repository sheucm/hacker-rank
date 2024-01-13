# Python list to act a Queue
q = [1,2,3]
q.append(4)
q # [1,2,3,4]
q.insert(0, 100)
q # [100, 1,2,3,4]
q.pop(0)  # 100
q # [1,2,3,4]
q.pop(-1)  # 4
q # [1,2,3]





#  Efficient at removing/adding element on left side (Can use in BFS)
from collections import deque 
     
# Declaring deque 
q = deque([1,2,3,4,5])  
q.append(4)
q.appendleft(6)
pop_v = q.pop()
pop_v = q.popleft()

# index(ele, beg, end)
idx_4 = q.index(4, 2, 5)

# insert(i, a)
# using insert() to insert the value 3 at 5th position
q.insert(4, 3)


# using count() to count the occurrences of 3
cnt = q.count(3) # The count of 3 in deque 


# using remove() to remove the first occurrence of 3
q.remove(3)


# Accessing the front element of the deque
print("Front element of the deque:", q[0])
 
# Accessing the back element of the deque
print("Back element of the deque:", q[-1])


# using extend() to add numbers to right end 
# adds 4,5,6 to right end
q.extend([4,5,6])

# using extendleft() to add numbers to left end 
# adds 7,8,9 to left end
q.extendleft([7,8,9])


# using rotate() to rotate the deque
# rotates by 3 to left
q.rotate(-3)


# using reverse() to reverse the deque
q.reverse()








# Priority Queues?


# (Not sure why use it. Seems like the same as normal dict on Python 3.11.)
from collections import OrderedDict   











