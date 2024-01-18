
# Problem
https://www.hackerrank.com/challenges/jeanies-route/problem

# Skill
1. DFS

# Challenges
1. The answer fomula

# Solving Mindset
1. Build subtree that includes all letter cities.
2. Get total distance of subtree
3. Get longest distance out of all (u,v) distances of subtree
4. Answer = 2 * total_dis - longest_dis

# Reference
- https://www.youtube.com/watch?v=ph-jcosp05k

# Run
```
export OUTPUT_PATH=./output.txt
python sol.py < ./test_cases/1/input.txt
```