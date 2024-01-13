

# - binary insert

############## Snippet (Bisect Insert for Nums) ################
### >>>>>>>> FOR NUMBER (Asc Order) <<<<<<<< ###
import bisect
A = [1,1,2,4,5]  # Must be sorted
bisect.insort(A,3)  # Insert 3
# [1, 1, 2, 3, 4, 5]




### >>>>>>>> FOR NUMBER (Desc Order) <<<<<<<< ###
A = [5,4,2,1,1]  # Must be sorted DESC
reversed(A)
... (Same Approach)




### >>>>>>>> FOR STRING (ASC Order) <<<<<<<< ###
def bisect_dict_insort(A, target):
    def _find(start, end):
        if end < start:
            raise Exception('Invalid index')

        mid = (start + end) // 2
        if mid == start or mid == end:
            if target == A[start]:
                return start + 1
            elif target == A[end]:
                return end + 1
            elif start == 0 and target < A[start]:
                return 0
            elif end == len(A) - 1 and target > A[end]:
                return len(A)
            else:
                return end

        if target > A[mid]:
            return _find(mid, end)
        else:
            return _find(start, mid)
    idx_to_insert = _find(0, len(A)-1)
    A.insert(idx_to_insert, target)
    return A


li = ['bc', 'ba', 'a', 'b1']
li = sorted(li)  # ['a', 'b1', 'ba', 'bc']

# bisect_dict_insort(li, '1')   # ['1', 'a', 'b1', 'ba', 'bc']
# bisect_dict_insort(li, 'a')  	# ['a', 'a', 'b1', 'ba', 'bc']
# bisect_dict_insort(li, 'b2')  # ['a', 'b1', 'b2', 'ba', 'bc']
bisect_dict_insort(li, 'c')  	# ['a', 'b1', 'ba', 'bc', 'c']
print(li)
############## Snippet END ################