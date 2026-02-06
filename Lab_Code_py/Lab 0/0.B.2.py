import matplotlib.pyplot as plt
import numpy as np
Vdc_plus= np.array([0.57, 1.50, 2.12, 3.06, 4.12, 4.92, 6.43])
Vi = np.array([0.040, 0.101, 0.136, 0.195, 0.250, 0.289, 0.344])



R = 1/6
Vdc = []
Idc = []
for i,v in enumerate(Vdc_plus):
    Vdc.append(v - Vi[i])

for v in Vi:
    Idc.append(v/R)

Vdc = np.array(Vdc)
Idc = np.array(Idc)


m, b = np.polyfit(Idc, Vdc, 1)

print(m)

plt.scatter(Idc, Vdc, color='g', marker='o')

plt.plot(Idc, m*Idc + b, color='r')

plt.xlabel("Idc (A)")
plt.ylabel("Vdc (V)")
plt.title("Idc vs Vdc")
# Format the equation string
equation_text = f'y = {m:.2f}x + {b:.2f}'

# Add the equation to the plot as an annotation
# xy specifies the location in data coordinates, xytext in relative display coordinates
plt.annotate(equation_text, xy=(0.05, 0.90), xycoords='axes fraction', fontsize=12,
             bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.5))

plt.legend(["data points", "linear regression"])
plt.show()

