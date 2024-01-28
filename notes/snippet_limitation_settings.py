
###### -------------------------------------- ######
###### If face the ERROR: ValueError: Exceeds the limit (4300 digits) for integer string 
###### Or, cannot handle integer that is over 64 bits
import sys
sys.set_int_max_str_digits(500000)   # Set higher if cannot pass



###### -------------------------------------- ######
###### If face the recursion limitation, set below
sys.setrecursionlimit(10000000)