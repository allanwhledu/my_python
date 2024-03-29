import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

sample_rate = 100.0
nsamples = 400
t = np.arange(nsamples) / sample_rate
x = np.cos(2*np.pi*0.5*t)+np.sin(2*np.pi*20*t)

b1 = signal.firwin(40, 10*2/sample_rate)
b2 = signal.firwin(41, [15*2/sample_rate, 40*2/sample_rate])
w1, h1 = signal.freqz(b1)
w2, h2 = signal.freqz(b2)

filtered_x = signal.filtfilt(b1, 1.0, x)

plt.figure(1)
plt.title('Digital filter frequency response')
plt.plot(w1/np.pi, 20*np.log10(np.abs(h1)), 'b', label='b1')
plt.plot(w2/np.pi, 20*np.log10(np.abs(h2)), 'r', label='b2')
plt.ylabel('Amplitude Response (dB)')
plt.xlabel('Frequency (rad/sample)')

plt.legend(loc='upper right')
plt.grid()
plt.show()

plt.figure(2)

ax1 = plt.subplot(3,1,1)
ax1.plot(t, x, color='blue')
plt.title('filtering result')
plt.ylabel('original signal')

ax2 = plt.subplot(3,1,2)
ax2.plot(t, filtered_x, color='red')
plt.ylabel('passed signal')

ax3 = plt.subplot(3,1,3)
ax3.plot(t, x - filtered_x, color='red')
plt.xlabel('Time (s)')
plt.ylabel('filtered signal')

plt.grid()
plt.show()