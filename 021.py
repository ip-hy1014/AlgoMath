from operator import mul
from functools import reduce
def combinations_count(n,r):
    r = min(r,n-r)
    numer = reduce(mul,range(n,n-r,-1),1)
    denom = reduce(mul,range(1,r+1),1)
    return numer // denom
n,r = map(int,input().split())
print(combinations_count(n,r))