import matplotlib.pyplot as plt

# getting the frequency response of the circuit

V_out = [992.19, 953.75, 862.1, 691.94, 421.13, 252.00]
V_in = [999.9, 999.9, 999.9, 999.9, 999.8, 996.6]
f = [200, 500, 1000, 2000, 5000, 10000]
h = []

# populate list with frequency response
for i, v in enumerate(V_out):
    h.append(v/V_in[i])

for v in h:
    print(v)

plt.plot(f, h, "o-")
plt.title("Frequency Response |H(F)|")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Voltage (V)")
# Set x-axis range
plt.xlim(0, 10000)

# Set tick marks every 1000 Hz
plt.xticks(range(0, 10001, 1000))
plt.yticks([i/10 for i in range(0, 11)])
plt.grid()
plt.show()