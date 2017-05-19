#coding=utf8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 400);
y = np.sin(x**2);


plt.close('all');

line = plt.plot(x, y, 'r-');

plt.axis([0, 2*np.pi, 1.5*min(y), 1.5*max(y)]); #设置坐标轴范围

plt.xlabel('$0 \sim \pi$');
plt.ylabel('$sin(x^2)$');
plt.title('$f(x)=sin(x^2)$');
plt.text(0.2, 1.2, '$f(x)=sin(x^2)$');
plt.annotate(xy=((2*np.pi)**0.5/2, 1), xytext=(2.0, 1.3), s='local max', arrowprops=dict(facecolor='black', shrink=0.05));



plt.setp(line, lw=2, color='r', animated=False);

plt.show();
