# CMPS 2200 Assignment 3
## Answers

**Name:**Troy Freed


Place all written answers from `assignment-03.md` here for easier grading.

1a. 
Given an integer N, being the max dollar amount, we need to create a greedy algorithm where when N>0,
find the largest coin d, in a set of coin values, {2^0, 2^1, 2^2... 2^k}. This is equivalent to d = 2^(log2N),
Then update N to N - d. Keep repeating this process until N becomes 0

1b. To prove optimality of an algorithm where the largest coin chosen is 2^(log2N), we need to prove it provides
the greedy choice and optimal substructure properties. This has the greedy choice property because the binary
representation of N is unique, and writing it in binary corresponds to expressing it as a sum of a set of power of 2s.
By subtracting N^(log2N) it subtracts the highest order bit, which is the correct greedy choice. This algorithm 
also provides an optimal substructure because it returns N - 2^(log2N), which is of the same form
and can be solved with the same greedy algorithm. 

1c. For the work you are subtracting 2^(log2N) from N for every iteration which is O(1) work,
the number of iterations corresponds to the number of 1s in the binary representation of N, because
each coin is a power of 2. Because the most amount of 1s in binary representation is log2(n) + 1, 
and each iteration takes O(1) work making the work O(log(N) + O(1), which is dominated by log(n) so the final
work is O(log(n)). The span is the same as the work because each iteration depends on the result of the one before
making it sequential and the span equal to O(log(n))


2a. A simple counterexample to this is if you have coins equal to {1, 3, 5, 8} and you want to make 15$, by 
using a greedy algorithm it would first use 8, 5, 1, and 1 to get to 15. The optimal way to do this would be 
by using 5, 5, and 5 using 1 less coin. 

2b. There is optimal substructure property because given F(n) being the minimum number of
coins to make change for n dollars the first coin chosen is d and the remaining amount is n - d.
This makes F(n) = 1 + min{F(n-d)}, if F(n) is achieved by choosing coin d then the solution for n - d
is optimal. To prove this assume there is an optimal solution S for the amount n that uses coin d first
but the remaining amount n - d is not optimal, then there exists a better solution S' for n - d that uses 
fewer coins than S. This would contradict the assumption that S is optimal, therefore the optimal
solution for n must include an optimal solution for n - d.

2c. By using a bottom up approach,
    - create an array F(0, 1, 2... N) where F(0) = 0
    - for n = 1 to N  set F(N) initially to none
    - Then use recurrence
        - for each n from 1 to N
            - for each coin d where d < N
                - if F(n - d) is not none, update F(n) = min(F(n), F(n-d)+1)
    - Return F(n), which is minimum number of coins needed if F(n) is still none then making change is impossible
The algorithm computes each F(n) by checking at most k denominations making the work O(N*K)
Because it is a bottom up approach each value depends on the previous one making span O(N)
    