import numpy as np
import matplotlib.pyplot as plt
import statistics
import scipy.signal as signal

t = []
A = []

with open('416_430_rbin34_45.txt', 'r') as f:
    content = f.readlines()
    for x in content:
        row = x.split('\t')
        t.append(float(row[0]))
        A.append(float(row[1]))

A = [item - statistics.mean(A) for item in A]
sf_ibis = len(t) / (t[-1] - t[0])
print(sf_ibis)
f = np.linspace(0.01, sf_ibis, 10000)
pgram = signal.lombscargle(t, A, f, normalize=True)

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Radar Data')
ax1.plot(t, A, linewidth=3, marker='o', markerfacecolor='red', markersize=8)
ax2.plot(f, pgram)
plt.show()

tGk = []
AGk = []

with open('GeoK_IBIStime_416_430.txt', 'r') as f:
    content = f.readlines()
    for x in content:
        row = x.split()
        tGk.append(float(row[0]))
        AGk.append(float(row[1]))

AGk = [item - statistics.mean(AGk) for item in AGk]
sf_Gk = len(tGk) / (tGk[-1] - tGk[0])
print(sf_Gk)
f_Gk = np.linspace(0.01, 6*2*np.pi, 10000)
pgram_Gk = signal.lombscargle(tGk, AGk, f_Gk, normalize=True)
#

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('TC Data')
ax1.plot(tGk, AGk, linewidth=3, marker='o', markerfacecolor='red', markersize=8)
ax2.plot(f_Gk/2/np.pi, pgram_Gk)
ax2.set_label('Frequency [Hz]')
plt.show()

# fourierTransform = np.fft.fft(AGk) / len(AGk)  # Normalize amplitude
# fourierTransform = fourierTransform[range(int(len(AGk) / 2))]  # Exclude sampling frequency
# tpCount = len(AGk)
# values = np.arange(int(tpCount / 2))
# timePeriod = tpCount / sf_Gk
# frequencies = values / timePeriod
#
# # Frequency domain representation
# fig, ax = plt.subplots()
# ax.set_title('Fourier transform depicting the frequency components')
# ax.plot(frequencies, abs(fourierTransform))
# ax.set_xlabel('Frequency')
# ax.set_ylabel('Amplitude')
# plt.show()

