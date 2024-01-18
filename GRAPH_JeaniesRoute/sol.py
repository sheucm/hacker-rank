#!/bin/python3

import os
import sys
sys.setrecursionlimit(1000000)
#
# Complete the jeanisRoute function below.
#
def jeanisRoute(n, cities, edges):
    is_letter_city = [False] * (n+1)
    for c in cities:
        is_letter_city[c] = True 
    
    tree = [set() for _ in range(n+1)]
    for v1, v2, w in edges:
        tree[v1].add((v2, w))
        tree[v2].add((v1, w))
    
    ## -- tree built -- 
    
    
    is_subtree = [False] * (n+1)
    for c in cities:
        is_subtree[c] = True
    def _dfs(v, pa=-1):
        for ch, w in tree[v]:
            if ch == pa:
                continue
            _dfs(ch, v)
            is_subtree[v] = is_subtree[v] or is_subtree[ch]
    _dfs(cities[0])
    ## -- subtree built -- 
    
    
    total_dis = 0
    def _dfs2(v, pa=-1):
        nonlocal total_dis
        for ch, w in tree[v]:
            if ch == pa or not is_subtree[ch]:
                continue
            total_dis += w
            _dfs2(ch, v)
    _dfs2(cities[0])
    ## -- total dis got
    
    
    
    def _get_longest_city_and_dis(start):
        max_city = start
        max_dis = 0
        def _dfs3(v, pa=-1, cur_dis = 0):
            nonlocal max_city
            nonlocal max_dis
            if is_letter_city[v]:
                if cur_dis > max_dis:
                    max_dis = cur_dis
                    max_city = v
            for ch, w in tree[v]:
                if ch == pa or not is_subtree[ch]:
                    continue
                _dfs3(ch, v, cur_dis + w)
        _dfs3(start)
        return max_city, max_dis
                
                
    max_city, max_dis = _get_longest_city_and_dis(cities[0])
    max_city, max_dis = _get_longest_city_and_dis(max_city)
    
    ans = 2 * total_dis - max_dis
    print(ans)
    return ans
    
    
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open(os.getenv('OUTPUT_PATH', './output.txt'), 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    city = list(map(int, input().rstrip().split()))

    roads = []

    for _ in range(n-1):
        roads.append(list(map(int, input().rstrip().split())))

    result = jeanisRoute(n, city, roads)

    fptr.write(str(result) + '\n')

    fptr.close()
