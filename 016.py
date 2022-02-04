from functools import reduce
import math
n = int(input())
a = list(map(int,input().split()))
def my_gcd(*numbers):
  return reduce(math.gcd,numbers)
print(my_gcd(*a))