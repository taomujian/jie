KEY = "CTF{4BDF4498E4922B88642D4915C528DA8F}" # DO NOT SHARE THIS! 
HOST = '109.233.61.11' 
PORT = 8001

if len(sys.argv)<3: 
    print 'Usage: rfax_man.py add|del file.png' 
    print '\nAdd your pictures to transmission!\nSizes: 800<=width<=3200 and height/width <=2.0.\nUse contrast grayscale pictures.' 
    exit(0)

data = open(sys.argv[2],'rb').read(1000000)

m = hashlib.md5(); 
m.update(KEY); 
KEYH=m.hexdigest().upper() 
m=hashlib.md5();
m.update(data); 
h=m.hexdigest().upper() 
print 'File hash',h

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
print 'Connected.'

if sys.argv[1]=='add': 
    s.sendall(KEYH+':ADD:'+data) 
    s.shutdown(socket.SHUT_WR)
    print s.recv(1024) 
elif sys.argv[1]=='del': 
    s.sendall(KEYH+':DEL:'+h) 
    print s.recv(1024)

s.close() 
print 'Done.'