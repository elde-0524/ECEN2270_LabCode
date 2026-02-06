import matplotlib.pyplot as plt
import numpy as np

V_channel1 = [0.1799, 1.2059, 3.7884, 4.8611]
V_channel2 = [5.0166, 5.0166, 5.0192, 5.0198]
I = []
R_1 = 330

for i, v in enumerate(V_channel1):
    I.append( (V_channel2[i] - V_channel1[i]) / R_1)

V_channel1_LED = [0.00263, 0.00280, 0.00272, 0.23268, 0.67414, 1.119, 1.58121, 2.0467, 2.5172]
V_channel2_Led = [0.499, 0.99833, 1.497, 1.996, 2.495, 3.024, 3.5237, 4.02, 4.5181]

R = 220

I_Led = []
V_Led = []
for i, v in enumerate(V_channel1_LED):
    V_Led.append(V_channel2_Led[i] - V_channel1_LED[i])
    I_Led.append(v/R)

plt.figure()
plt.plot(V_Led, I_Led)
plt.plot(V_channel1, I, color = "r")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.legend(["LED I-V Characteristic", "Load Line"])

plt.title("Load Line for Z1")


plt.show()

