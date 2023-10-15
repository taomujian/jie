


def process(a, b, m):
    return "".join(map(chr, map(lambda x: (x * a + b) % 251, bytes.fromhex(m))))

m = "cc90b9054ca67557813694276ab54c67aa93092ec87dd7b539"
for i in range(255):
    for j in range(255):
        if "AES_key{" in process(i, j, m):
            print(process(i, j, m))
