number = ['?'] * 1024
look_up = {pow(msg, pow(2,i), N) : i for i in range(0,1024)}
valid_inv = libnum.modular.invmod(valid[0], N)

print '[+] Looking for matches and recovering secret exponent...'

for sig in faulty:
    st = (sig * valid_inv) % N

    if st in look_up:
        number[look_up[st]] = '0'
    st = (libnum.modular.invmod(sig, N) * valid[0]) % N

    if st in look_up:
        number[look_up[st]] = '1'

unknown = number.count('?')

if unknown == 0:
    d = int(''.join(number[::-1]), 2)

    print 'Secret exponent is: {0}'.format(d)
    print 'Check:', valid[0] == pow(msg, d, N)

    return d
else:
    print '[+] Recovered bits'
    print ''.join(number)
    print 'Remaining unknown: {0} / {1}'.format(unknown, len(number))
