import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

sample_rate = 100.0
n_rate = sample_rate/2
nsamples = 400
t = np.arange(nsamples) / sample_rate
x = np.cos(2*np.pi*1*t)+np.sin(2*np.pi*20*t)+np.sin(2*np.pi*40*t)

b1 = signal.firwin(100, 0.1, fs=2)
# b2 = signal.firwin(101, [0.01, 0.9], fs=2)
b2 = signal.remez(101, (0, 0.05, 0.08, 0.2, 0.22, 0.50), (0.1, 1, 0.1))
w1, h1 = signal.freqz(b1)
w2, h2 = signal.freqz(b2)


filtered_x = signal.filtfilt(b2, 1.0, x)

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
ax2 = plt.subplot(3,1,2)
ax3 = plt.subplot(3,1,3)
ax1.plot(t, x, color='blue')
ax2.plot(t, filtered_x, color='red')
ax3.plot(t, x - filtered_x, color='red')
plt.grid()
plt.show()