import numpy as np
from matplotlib import pyplot as plt

x = '7fffffffffffffffffffffffffffffffbffff0e10419dff07fdc3ffdaeab6deffdbfff6ffed7f7aef3febfffb7ff1bfbc675931e33c79fadfdebbae7aeddedb7dafef7dc37df7ef6dbed777beedbedb77b6de24718f260e0e71879fffffffffffffffffffffffffffffffffffffffffff07f87fc7f9ffffffffdbfbbfdbfeffffffffebfdffdfff7ffffff871c33e6fe7bffffffd5aefeed62dcffffffeadf9fb8bb0efffffff56df5db6dbf7ffffffaa0c21e19e3bffffe07ffffffffff9fffffffffffffffffffffffffffffffffffffff'
x = np.array(list(bin(int(x, 16))[2:]), dtype=np.uint8)

n = 23
plt.imshow(x.reshape(n, x.shape[0] // n))