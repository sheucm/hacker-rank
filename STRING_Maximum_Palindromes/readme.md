
# Problem
https://www.hackerrank.com/challenges/maximum-palindromes/problem

# Skill
(empty)

# Challenges
- Need to handle big integer division problem.

# Solving Mindset
----- Detail Explanation -----
Basic Concept: permutations fomula
For example: What is the combination count of "aaabb"? Ans: 10
Total Combinations without reducing duplicates: factorial(5)
But we have duplicated counts as three 'a' pairs are the same. (Same as 'b'). So we need to deduplicate them.
Final Combinations: factorial(5) / (factorial(3) * factorial(2))
Back to our questions:
For example, the palindromes is "aaabbbbaaa". We take only left part for simple, which is "aaabb".
We said they are 5 pairs (3 for 'a' pairs and 2 for 'b' pairs)
We have 3 pairs of 'a' that are the same, and 2 pairs of 'b' same.
So, we need to deduplicate. 
The answer will be factorial(5) / (factorial(3) * factorial(2)) = 10
If we have single characters (no pair), for example "xyzaaabbbbaaa", "x,y,z" are single characters. We can put one of them in the middle of "aaabbbbaaa" to gain more combinations.
Then, the combination will be 3 * 10 = 30.

# Reference
(empty)

# Run
```
export OUTPUT_PATH=./output.txt
python sol.py < ./test_cases/1/input.txt
```