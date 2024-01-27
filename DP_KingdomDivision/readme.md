
# Problem
https://www.hackerrank.com/challenges/kingdom-division/problem

# Skill
(empty)

# Challenges
(empty)

# Solving Mindset
Let `dp[0][v]` safe variations where `v` and it's parent `p` has the same color
Let `dp[1][v]` safe variations where `v` and it's parent `p` has different colors
If v is the leaf, no matter whether `v` and `p` are ally or not, leaf `v` must be the ally with `p`.
So `dp[0][leaf] = 1`, `dp[1][leaf] = 0`.
We build dp arrays from leaf to root by using DFS.
(Traverse the tree from bottom up (processing leaves first and then removing those leaves from the tree) until there is only the root left)


# Reference
- https://unknown-coder-here.blogspot.com/2023/04/kingdom-division-problem-solution-in.html

# Run
```
export OUTPUT_PATH=./output.txt
python sol.py < ./test_cases/1/input.txt
```