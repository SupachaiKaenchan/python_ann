import numpy as np
import matplotlib.pyplot as plt
mu, sigma = 200, 25
x = mu + sigma*np.random.randn(10000)

print x

n, bins, patches = plt.hist(x)
plt.show()

