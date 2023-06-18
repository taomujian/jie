for _ in range(3):
    p = random_prime(2^1024)
    q = random_prime(2^1024)
    n = p*q
    p1=p>>724
    ct=n * inverse_mod(q % (2 ** 265), 2^265) % 2^265
    print('p1=',p1)
    print('ct=',ct)
    print("n=",n)
    e = 65537
    alarm(80)
    m = randint(2,n-1)
    c=pow(m,e,n)
    print('c=', c)
    print('---------------------------------------------')
    m1 = int(input("m="))
    print('---------------------------------------------')
    print()
    if m1!=m:
        print("Nope")
        exit()

print(open("flag.txt","r").read())