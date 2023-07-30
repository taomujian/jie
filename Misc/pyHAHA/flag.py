f = open('PyHaHa2.pyc','wb')
with open('PyHaHa.pyc','rb') as g:
	f.write(g.read()[::-1])
f.close()