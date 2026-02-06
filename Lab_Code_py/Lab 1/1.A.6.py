import matplotlib.pyplot as plt
import numpy as np

V_channel1_LED = [0.00263, 0.00280, 0.00272, 0.23268, 0.67414, 1.119, 1.58121, 2.0467, 2.5172]
V_channel2_Led = [0.499, 0.99833, 1.497, 1.996, 2.495, 3.024, 3.5237, 4.02, 4.5181]

R = 220


I_Led = []
V_Led = []
for i, v in enumerate(V_channel1_LED):
    V_Led.append(V_channel2_Led[i] - V_channel1_LED[i])
    I_Led.append(v/R)

print("I_LED")
print(I_Led)
print("V_Led")

print(V_Led)



plt.figure()
plt.plot(V_Led, I_Led)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')

plt.title('Voltage vs. Current of the LED')
plt.show()