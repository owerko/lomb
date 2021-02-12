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
f = np.linspace(0.01, 6 * 2 * np.pi, 10000)
pgram = signal.lombscargle(t, A, f, normalize=True)

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Radar Data', fontsize=18)
ax1.set_xlabel("Time [s]", fontsize=14)
ax1.set_ylabel("Amplitude [mm]", fontsize=14)
ax1.plot(t, A, linewidth=3, marker='o', markerfacecolor='red', markersize=8)
ax2.plot(f / 2 / np.pi, pgram, linewidth=3)
ax2.annotate('f=1.012 Hz', xy=(1.1, 0.9), xytext=(2, 0.8),
             arrowprops=dict(arrowstyle="simple", color='black', lw=1.5),
             horizontalalignment='center',
             verticalalignment='bottom',
             fontsize=14,
             )
# 1.017
ax2.set_xlabel('Frequency [Hz]', fontsize=14)
ax2.set_ylabel("P(f)", fontsize=14)
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
f_Gk = np.linspace(0.01, 6 * 2 * np.pi, 10000)
pgram_Gk = signal.lombscargle(tGk, AGk, f_Gk, normalize=True)
#

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('TC Data', fontsize=16)
ax1.set_xlabel("Time [s]", fontsize=14)
ax1.set_ylabel("Amplitude [gon]", fontsize=14)

ax1.plot(tGk, AGk, linewidth=3, marker='o', markerfacecolor='red', markersize=8)
ax2.plot(f_Gk / 2 / np.pi, pgram_Gk, linewidth=3)
ax2.set_xlabel('Frequency [Hz]', fontsize=14)
ax2.set_ylabel("P(f)", fontsize=14)
ax2.annotate('f=1.017 Hz', xy=(1.1, 0.85), xytext=(2, 0.8),
             arrowprops=dict(arrowstyle="simple", color='black', lw=1.5),
             horizontalalignment='center',
             verticalalignment='bottom',
             fontsize=14,
             )
plt.show()
