#coding=utf8
import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(1000);

n, bin, patches = plt.hist(x, bins=50, normed=True, facecolor='g', alpha=0.3);

plt.xlabel('IQ');
plt.ylabel('Probability');
plt.title('Histogram of IQ');
plt.text(60, 0.025, '$\mu=100, \sigma=15$');
plt.axis([40, 160, 0, 0.03]);
plt.grid(True);

plt.show();
