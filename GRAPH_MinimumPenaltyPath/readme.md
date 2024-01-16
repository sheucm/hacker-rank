
# Problem
https://www.hackerrank.com/challenges/beautiful-path/problem

# Skill
1. Dijkstra Algorithm (BFS)

# Challenges
1. Dijkstra Alg. should modify a bit.
    - Bitwise value should not compare directly to determine whether add next node into queue. For example, 
        - Case:   
            ```
            start = 1
            end = 4
            edges = [   # format: (node1, node2, weight)
                [1, 2, 7],   # weight bit: 0111
                [1, 3, 8],   # weight bit: 1000
                [2, 4, 8],   # weight bit: 1000
                [3, 4, 8],   # weight bit: 1000
            ]
            # If you use original Diasktra Alg., then you will choose n1 -> n2 -> n4 for shortest path because `7 < 8`, you will choose n2 for next. 
            # However, actually it's n1 -> n3 -> n4 for answer.

            # The cost of "n1 -> n2 -> n4" is "7 | 8 = 15"
            # The cost of "n1 -> n3 -> n4" is "8 | 8 = 8"
            ```
            


# Run
```
export OUTPUT_PATH=./output.txt
python sol.py < ./test_cases/1/input.txt
```