import matplotlib.pyplot as plt
import numpy as np



# given data points
Vdc_plus = np.array([1.55, 1.98, 2.36, 2.68, 3.36, 3.80, 3.97, 4.49, 4.94, 5.26, 5.67, 6.14])
Vdc_minus = np.array([0.043, 0.049, 0.047, 0.052, 0.052, 0.055, 0.058, 0.059, 0.064, 0.067, 0.070, 0.071])
f_enc = np.array([198, 305, 386, 526, 667, 806, 917, 1025, 1150, 1310, 1380, 1490])


R_m = 2.97
Req = 1/6

V_emf = []
Omega = []
k = []

for f in f_enc:
    Omega.append(((2*np.pi)/960) * f)


for i, v in enumerate(Vdc_plus):
    V_emf.append(Vdc_plus[i] - (R_m * (Vdc_minus[i]/Req)) - Vdc_minus[i])
    k.append(V_emf[i]/Omega[i])

print("Vemf:")
for v in V_emf:
    print(v)

print("Omega:")
for o in Omega:
    print(o)

Omega = np.array(Omega)
K = np.array(k)

plt.figure()
plt.scatter(Omega,K, color = 'r', marker = 'o')
plt.title('Finding k value')
plt.xlabel("omega (rad/s)")
plt.ylabel("k")
plt.ylim(0, 1)

sum = 0

for i, k in enumerate(K):
    sum += k

avg = sum/len(K)


equation_text = f'average = {avg:.3f}'

plt.hlines(avg, 0, 10, linestyles='dashed')

plt.annotate(equation_text, xy=(0.05, 0.90), xycoords='axes fraction', fontsize=12,
             bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.5))
plt.legend(["Data points", "Linear regression"])
plt.show()


# code for finding T and B
plt.figure()
Idc = []

for v in Vdc_minus:
    Idc.append(v/Req)


T = []
for i in (Idc):
    T.append(i * avg )

T = np.array(T)
plt.scatter(Omega, T, color = 'r', marker = 'o'),


B,T_int = np.polyfit(Omega, T, 1)

plt.plot(Omega, B * Omega + T_int, color ='g')
plt.title('Finding B and T values')

equation_text = f'y = {B:.3f}x + {T_int:.3f}'

print("m * b")
print(f"{B} = B ")
print(f"{T_int} = T_int")


print("Idc")
for i in Idc:
    print(i)

plt.annotate(equation_text, xy=(0.05, 0.90), xycoords='axes fraction', fontsize=12,
             bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.5))

plt.xlabel("omega (rad/s)")
plt.ylabel("Torque")
plt.legend(["Data points", "Average Value"])
plt.show()


# Code to solve for J

f_enc_max = 1490
omega_max = ((2 * np.pi) / 960 ) * f_enc_max
tau = 3.4

# remember m = B and b = T_int
J = (B * tau) / np.log((B * omega_max + T_int) / T_int)

print(f" J = {J}")








