def get_true_key(msg_data, cip_data):
    xs = ''
    i, t = 0, 0
    for m, c in zip(msg_data, cip_data):
        x = (c - m - i*i) & 0xff
        x ^= t
        t = m
        i += 1
        xs += chr(x)

    return xs[:(xs[1:].find(xs[0]) + 1)]

def solve():
    with open('491476abacd445d19e7dd9dfa474f9d1/msg001', 'rb') as f:
        msg_data = f.read().strip()
        
    with open('491476abacd445d19e7dd9dfa474f9d1/msg001.enc', 'rb') as f:
        cip_data = f.read().strip()
        
    with open('491476abacd445d19e7dd9dfa474f9d1/msg002.enc', 'rb') as f:
        data = f.read().strip()
        
    k = get_true_key(msg_data, cip_data)
    
    print('the true key is:', k)
    
    o_k = [ord(c) for c in k]

    t = 0
    msg = ''
    for i, c in enumerate(data):
        p = (c - i*i - (o_k[i%28] ^ t)) & 0xff
        t = p
        msg += chr(p)
        
    with open('msg002', 'w') as f:
        f.write(msg)
        
    return msg

if __name__ == '__main__':
    print(solve().strip())
