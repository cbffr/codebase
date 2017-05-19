#coding=utf8

import matplotlib.pyplot as plt
import numpy as np

# Simple data to display in various forms
x = np.linspace(0, 2 * np.pi, 400);
y = np.sin(x ** 2);

# 单个图片
f, ax = plt.subplots(); ax.plot(x, y, 'r-', lw=2);
ax.set_title('Simple demo');

#共享x轴
f, axarr = plt.subplots(2, sharex=True);
axarr[0].plot(x, y, 'r-', lw=2);
axarr[0].set_title('share x');
axarr[1].scatter(x, y);

#共享y轴
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True);
ax1.plot(x, y, 'r-', lw=2);
ax1.set_title('share y');
ax2.scatter(x, y);

#共享x轴和y轴
f, axarr = plt.subplots(3, sharex=True, sharey=True);
plt.yticks([-1, 0, 1]);  #设置y坐标tick位置
axarr[0].set_yticklabels([-1, 0, 1]);  #设置y坐标tick标签
axarr[0].plot(x, y, 'r-', lw=2);
plt.setp(axarr[0].get_xticklabels(), visible=False); #不显示x轴tick，未生效
axarr[0].set_title('share both');
axarr[1].plot(x, y, 'bo');
axarr[2].scatter(x, y);
f.subplots_adjust(hspace=0); #设置图之间的水平距离
plt.setp([a.get_xticklabels() for a in f.axes[:]], visible=False);

#横向共享y轴，纵向共享x轴
f, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2, sharex='col', sharey='row');
ax0.set_title('share x per columns, y per row');
ax0.plot(x, y, 'r-', lw=2);
ax1.plot(x, y, 'bo');
ax2.scatter(x, y);
ax3.plot(x, y, 'ro');

plt.close('all')

#极坐标系
f, axarr = plt.subplots(2, 2, subplot_kw=dict(projection='polar'))
axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('Axis [0,0]')
axarr[0, 1].scatter(x, y)
axarr[0, 1].set_title('Axis [0,1]')
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title('Axis [1,0]')
axarr[1, 1].scatter(x, y ** 2)
axarr[1, 1].set_title('Axis [1,1]')
# Fine-tune figure; make subplots farther from each other.
f.subplots_adjust(hspace=0.3)

plt.show();
