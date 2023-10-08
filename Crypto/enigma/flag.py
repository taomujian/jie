import codecs
from crypto_commons.generic import xor_string


def main():
    cts = []
    for i in range(1, 7):
        with codecs.open("encrypted/" + str(i) + "e", "r") as input_file:
            data = input_file.read()
            cts.append(data)
    xored = [xor_string(chr(ord('&') ^ ord(' ')) * len(data), d) for d in cts]
    print(xored)

main()