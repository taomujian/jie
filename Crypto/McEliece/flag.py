from sage.all import *

ct = load("b5f627007d934190a3dc54bd5e7456e8/ciphertext.sobj")
pk = load("b5f627007d934190a3dc54bd5e7456e8/publickey.sobj")

k, n = pk.dimensions()
F = ct[0].parent()

M = pk.echelon_form()
for c01 in F:
    if c01 == 0:
        continue
    alpha = [None] * n
    # we can set this w.l.o.g
    alpha[0] = 0
    alpha[1] = 1

    # First stage: get alpha[k..n-1]
    good = 1
    for j in range(k, n):
        b01 = M[0, j] / M[1, j]
        if c01 == b01:
            good = 0
            break
        alpha[j] = c01 / (c01 - b01)
    if not good:
        print(c01, ":", "FAIL")
        continue

    # Second stage: get alpha[2..k-1]
    for i in range(2, k):
        p = k
        q = k + 1
        while True:
            bp = M[0, p] / M[i, p]
            bq = M[0, q] / M[i, q]
            A = bp * (alpha[p] - alpha[0])
            A /= bq * (alpha[q] - alpha[0])
            if A == 1:
                p += 1
                q += 1
                if q == n:
                    break
                continue
            alpha[i] = (A * alpha[q] - alpha[p]) / (A - 1)
            break

    # if guessed completely
    if alpha.count(None) == 0:
        print(c01, ":", "Got full alpha.")
        C = codes.GeneralizedReedSolomonCode(alpha, k)
        D = codes.decoders.GRSBerlekampWelchDecoder(C)
        try:
            res = pk.solve_left(D.decode_to_code(ct))
            print("   ", "message vector:", res)
            msg = "".join(map(chr, [v.integer_representation() for v in res]))
            print("  ", "message:", msg)
        except:
            print("no decoding...")
