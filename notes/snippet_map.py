
# Default Map
from collections import defaultdict

d = defaultdict(int)
d['x']   # 0

d = defaultdict(list)
d['x']   # []

d = defaultdict(lambda _: "Not Implemented")
d['x']   # "Not Implemented"



# Order Dict (Map)
from collections import OrderedDict


