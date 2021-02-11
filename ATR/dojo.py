import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import statistics

A = 2.
w = 1.
phi = 0.5 * np.pi
nin = 1000
nout = 100000
frac_points = 0.9  # Fraction of points to select

r = np.random.rand(nin)
x = np.linspace(0.01, 10 * np.pi, nin)
x = x[r >= frac_points]

y = A * np.sin(w * x + phi)
f = np.linspace(0.01, 10, nout)
plt.plot(x,y, 'b+')
plt.show()

pgram = signal.lombscargle(x, y, f, normalize=True)

plt.subplot(2, 1, 1)
plt.plot(x, y, 'b+')
plt.subplot(2, 1, 2)
plt.plot(f, pgram)
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
f = np.linspace(0.01, 8, nout)
plt.plot(tGk,AGk, linewidth=3, marker='o', markerfacecolor='red', markersize=8)
plt.show()

pgram2 = signal.lombscargle(tGk, AGk, f, normalize=True)



plt.subplot(2, 1, 1)
plt.plot(tGk, AGk, 'b+')
plt.subplot(2, 1, 2)
plt.plot(f, pgram2)
plt.show()
