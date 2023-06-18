import gmpy2
import libnum
from itertools import combinations
from functools import reduce
from operator import mul

def calculate_products(numbers):
    result = []
    n = len(numbers)
    for r in range(1, n + 1):
        combinations_r = combinations(numbers, r)
        for comb in combinations_r:
            remaining_nums = [num for num in numbers if num not in comb]
            if remaining_nums:
                product1 = reduce(lambda x, y: x*y, comb)
                product2 = reduce(lambda x, y: x*y, remaining_nums)
                result.append((product1, product2))
    return result


n = 175797137276517400024170861198192089021253920489351812147043687817076482376379806063372376015921
c = 144009221781172353636339988896910912047726260759108847257566019412382083853598735817869933202168

p1 = 9401433281508038261
p2 = 10252499084912054759
p3 = 11215197893925590897
p4 = 11855687732085186571
p5 = 13716847112310466417

e = 65537
phi = (p1-1) * (p2-1) * (p3-1) * (p4-1) * (p5-1)
d = gmpy2.invert(e, phi)
m = gmpy2.powmod(c, d, n)
flag = libnum.n2s(int(m))
print(flag)
    
