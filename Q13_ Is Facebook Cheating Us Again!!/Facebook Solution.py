'''
This problem is the smallest to code of all problems I have created till date. The difficulty lies in visualising the
situation well and then using the appropriate representation for the same.
The solution can be described as follows:
    1. Assume each of the U users to be a node in a graph
    2. So new N users will be new nodes in this graph
    3. Now a friend request can be modelled as an edge
    4. As all friend requests are accepted, the direction of the friend request will not matter. So the friend request can
       be considered an undirected edge
    5. Now every request has at least 1 new user. This will help us find total number of friend requests given that N and         U
       are authentic
    6. To verify N we must find a bound on the value of N
    7. As the number of friend requests is always correct, we must derive a bound on N in terms of F and U
    8. It is much easier to calculate a bound on F in terms of U and N. So we will convert the bound on F to a bound on N
    9. Now we start dwelling in the math and PnC behind the problem.
   10. Number of friend requests is same as number of edges having at least 1 new vertex
   11. Fmax = Emax(new to new)+Emax(new to old or vice versa)
   12. Fmax = E(new vertices fully connected) + E(all old vertices connected to new vertices)
   13. Fmax = N(N-1)/2 + NU
   14. F <= N(N-1)/2 + NU
   15. Equation: N^2+(2U-1)N-2Fmax=0
   16. Solution given in code. We have also considered only 1 solution of the quadratic equation as the other one is
       always negative. Ceil operation is applied so that N is big enough to support the value of Fmax.
   17. Now we have a solution for the values of N given that F=Fmax
   18. But as N increases Fmax increases
   19. So if Fmax is fixed at F then there exists a lower bound on N in terms of Fmax (Note that the graphs need not be
       fully connected, we have considered maximum number of edges)
   20. So the value obtained from the quadratic equation will be a lower bound on N
   21. So all values above it can be authentic
   22. Any value below the bound is unauthentic and the difference of the value with the bound would be the minimum error
       in the value provided and the actual number of users
   23. The only exceptional condition is when the input is 0 0 0 which should be considered as it is in the bounds of the
       problem
'''

from math import ceil
U, F, N = [int(i) for i in input().split(' ')]
if U == 0 and F == 0 and N == 0:
    print('Y')
else:
    x = ceil((((2 * U - 1) ** 2 + 8 * F) ** 0.5 - 2 * U + 1) / 2)
    if N >= x:
        print('Y')
    else:
        print('N ' + str(x - N))

