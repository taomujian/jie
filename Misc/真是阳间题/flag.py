
from Crypto.Util.number import long_to_bytes  

# sage
flag_str = 3207357975641587136122466514425152961654613410728337142271750273124995105747053991640817066352343657398947248938255086358418100814441196784643527787764297
flag = long_to_bytes(flag_str).decode()
flag = list(flag)
print(flag)
flag.reverse()
flag = ''.join(flag)
print(flag)