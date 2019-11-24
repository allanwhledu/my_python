import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

sample_rate = 100.0
b1 = signal.firwin(40, 10*2/sample_rate)

impulse = np.zeros(1000, dtype=np.float)
impulse[0] = 1

filtered_x = signal.filtfilt(b1, 1.0, impulse)
print(filtered_x[-1])

plt.figure(1)
plt.title('Impulse response by FIR filter')
plt.plot(filtered_x, 'b', label='b1')
# plt.ylabel('Amplitude Response (dB)')
# plt.xlabel('Frequency (rad/sample)')
plt.grid()
plt.show()

