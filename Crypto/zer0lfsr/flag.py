import z3
import codecs
from Crypto.Util.number import bytes_to_long,long_to_bytes
import hashlib

def solve_3_lfsr(keystream, relevant_bit_indices, length, mask_length):
    len_mask = (2 ** (mask_length + 1) - 1)
    result_bits = map(int, "".join([bin(ord(c))[2:].zfill(8) for c in keystream]))
    s = z3.Solver()
    x = z3.BitVec('x', length)
    y = z3.BitVec('y', length)
    z = z3.BitVec('z', length)
    inits = [x, y, z]
    for result in result_bits:
        combs = []
        new_inits = []
        for index in range(3):
            relevant_bit1 = (inits[index] & (1 << relevant_bit_indices[index][0]))
            bit1_value = z3.LShR(relevant_bit1, relevant_bit_indices[index][0])
            relevant_bit2 = inits[index] & (1 << relevant_bit_indices[index][1])
            bit2_value = z3.LShR(relevant_bit2, relevant_bit_indices[index][1])
            single_lfsr_result = bit1_value ^ bit2_value
            combs.append(single_lfsr_result)
            new_init = ((inits[index] << 1) & len_mask) ^ single_lfsr_result
            new_inits.append(new_init)
        s.add(combine(combs[0], combs[1], combs[2]) == result)
        inits = new_inits
    s.check()
    model = s.model()
    print(model)
    x_res = int(str(model[x]))
    y_res = int(str(model[y]))
    z_res = int(str(model[z]))
    return x_res, y_res, z_res

def combine(x1,x2,x3):
    return (x1*x2)^(x2*x3)^(x1*x3)

def solve():
    with codecs.open("release/keystream", 'rb', 'utf8') as input_file:
        data = input_file.read()
        mask1 = (47, 22)
        mask2 = (47, 13)
        mask3 = (47, 41)
        x, y, z = solve_3_lfsr("".join(map(chr, map(ord, data)))[:48], [mask1, mask2, mask3], 48, 48)
        print(x, y, z)
        init1, init2, init3 = map(long_to_bytes, [x, y, z])
        print("flag{" + hashlib.sha256(init1 + init2 + init3).hexdigest() + "}")

if __name__ == '__main__':
    solve()
