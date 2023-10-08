import time, os
TEST_COUNT = 2
LEN = 16
CHOICES = "0123456789abcdef"

def check(prefix):
    mxtime = -1
    res = ''
    for c in CHOICES:
        cur = prefix + c + '0'*(LEN-len(prefix)-1)
        foo = 0
        for _ in range(TEST_COUNT):
            start = time.time()
            os.system(f"echo '{cur}' | ./task > /dev/null")
            foo += (time.time()-start)
        avgtime = foo/TEST_COUNT
        if avgtime > mxtime:
            mxtime = avgtime
            res = c
    return res


def main():
  prefix = ''
  for i in range(15):
    c = check(prefix)
    prefix += c
    print(c)
    
  for c in CHOICES:
    cur = prefix + c
    print(f"------ trying {cur} --------")
    os.system(f"echo '{cur}' | ./task")

main()