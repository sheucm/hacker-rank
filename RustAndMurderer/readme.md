
# Problem
https://www.hackerrank.com/challenges/rust-murderer/problem

# Skill
1. N/A

# Challenges
1. Need to find out the algorithm

# Solving Mindset
1. Set distaince to 1 for all nodes except for the S (start node) and its neighbors.
2. If not visited node count < N (total node count), then we can assign the distance. (Max distance + 1)
3. Iterate step2 until no non-visted nodes.

# Reference
(empty)

# Run
```
export OUTPUT_PATH=./output.txt
python sol.py < ./test_cases/1/input.txt
```