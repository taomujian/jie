import codecs
def enc(s, t):
	if t:
		l = list(map(ord, s))
		return enc(''.join(list(map(chr, [l[i]^l[i+1] for i in range(len(l)-1)]))), t-1)
	else:
		return s

with open('in.txt') as f:
	s = enc(f.read(), 5)
with open('out.txt', 'w') as f:
	f.write(s)