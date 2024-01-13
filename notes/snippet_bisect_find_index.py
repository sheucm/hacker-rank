# - bisect for Finding Index

############## Snippet (Binary Search for number) ################
### >>>>>>>> FOR NUMBER (ASC Order) <<<<<<<< ###
import bisect
def find_index_first(A, val):
    idx = bisect.bisect_left(A, val)
    return idx if idx != len(A) and A[idx] == val else -1

A = [1,1,2,4,5]  # Must be sorted
find_index_first(A, 0) # -1
find_index_first(A, 1) # 0
find_index_first(A, 2) # 2
find_index_first(A, 3) # -1
find_index_first(A, 6) # -1


def find_index_last(A, val):
    idx = bisect.bisect_right(A, val) - 1
    return idx if idx >= 0 and A[idx] == val else -1

A = [1,1,2,4,5]  # Must be sorted
find_index_last(A, 0) # -1
find_index_last(A, 1) # 1
find_index_last(A, 2) # 2
find_index_last(A, 3) # -1
find_index_last(A, 6) # -1




### >>>>>>>> FOR NUMBER (Desc Order) <<<<<<<< ###
A = [5,4,2,1,1]  # Must be sorted DESC
reversed(A)
... (Same Approach)







### >>>>>>>> FOR STRING (ASC Order) <<<<<<<< ###
def bisect_dict_left(A, target):
    def _find(start, end):
        if end < start:
            raise Exception('Invalid index')

        mid = (start + end) // 2
        if mid == start or mid == end:
            if target == A[start]:
                return start
            elif target == A[end]:
                return end
            else:
                return -1

        if target > A[mid]:
            return _find(mid, end)
        else:
            return _find(start, mid)
    return _find(0, len(A)-1)


li = ['bc', 'ba', 'a', 'b1']
li = sorted(li)  # ['a', 'b1', 'ba', 'bc']
bisect_dict_left(li, 'a')  # 0
bisect_dict_left(li, 'a1')  # -1

############## Snippet END ################



















