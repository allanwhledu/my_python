from scipy import signal
from numpy import cos, sin, pi, absolute, arange
from pylab import figure, clf, plot, subplot, xlabel, ylabel, xlim, ylim, title, grid, axes, show

sample_rate = 100.0
nsamples = 400
t = arange(nsamples) / sample_rate
x = cos(2*pi*0.5*t)+ 0.2*sin(2*pi*15.3*t)

b, a = signal.butter(8, 0.1, 'lowpass')  # 配置滤波器 8 表示滤波器的阶数
# c, d = signal.butter(8, 0.8, 'highpass')
filtedData_l = signal.filtfilt(b, a, x)  # data为要过滤的信号
# filtedData_h = signal.filtfilt(c, d, x)

fig = figure()
ax1 = subplot(3,1,1)
ax2 = subplot(3,1,2)
ax3 = subplot(3,1,3)
ax1.plot(t, x, color='blue')
ax2.plot(t, filtedData_l, color='red')
ax3.plot(t, x - filtedData_l, color='red')
show()