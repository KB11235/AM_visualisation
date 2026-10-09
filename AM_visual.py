import numpy as np 
import matplotlib.pyplot as plt

L1 = 1
N1 = 10000
tau_n = np.linspace(0,L1,N1)
m_t = []
r1 = 4
r2 = 2
phi_1 = -np.pi/9
phi_2 = 0

for i in range(len(tau_n)):
    m_t.append(r1*np.cos(2*np.pi*tau_n[i] + phi_1) + r2*np.sin(4*np.pi*tau_n[i] + phi_2))

plt.title("Plot of the message signal in the time domain with length 1")
plt.xlabel("Normalised time tau_n")
plt.ylabel("Message signal m_t")

plt.plot(tau_n, m_t)
plt.grid()

plt.show()
plt.close()

min_val = 9999999
corresponding_tau = 0
index = 0

for i in range(len(m_t)):
    if m_t[i] < min_val:
        min_val = m_t[i]
        index = i
        corresponding_tau = tau_n[i]

print(f'Min value is {min_val:.2f}')
print(f'Min value occurs when tau is {corresponding_tau:.2f}')

Y = r1/abs(min_val)
Z = r2/abs(min_val)

m_nt = []
for i in range(len(tau_n)):
    m_nt.append(Y*np.cos(2*np.pi*tau_n[i] + phi_1) + Z*np.sin(4*np.pi*tau_n[i] + phi_2))

plt.title("Plot of the normalised message signal in the time domain")
plt.xlabel("Normalised time tau_n")
plt.ylabel("Normalised message signal m_nt")

plt.plot(tau_n, m_nt)
plt.grid()

plt.show()
plt.close()

min_norm_val = 9999999
for i in range(len(m_nt)):
    if m_t[i] < min_norm_val:
        min_norm_val = m_nt[i]

if min_norm_val + 1 >= 0:
    print("Condition is held for all t")
else:
    print("Condition is not held")

# Ycos(2*pi*f_m*t - pi/9) + Zsin(4*pi*f_m*t) = Ycos(pi/9)cos(2*pi*f_m*t) + Ysin(pi/9)sin(2*pi*f_m*t) + Zsin(4*pi*f_m*t)
# Therefore, A1 = Ycos(pi/9), B1 = Ysin(pi/9), B2 = Z and all other A_n and B_n = 0 for all natural numbers n
P1 = 1/2 * ((Y*np.cos(np.pi/9))**2 + (Y*np.sin(np.pi/9))**2 + Z**2)
print(P1)

a1 = 0.5
efficiency = (a1**2)*P1/(1+(a1**2)*P1) * 100

a2 = np.linspace(0,10,N1)
eff = []
for i in range(len(a2)):
    eff.append((a2[i]**2)*P1/(1+(a2[i]**2)*P1) * 100)

plt.title("Plot of efficiency variation as a function of modulation index")
plt.xlabel("Modulation index a")
plt.ylabel("Efficiency as a percentage")

plt.plot(a2, eff)
plt.grid()

plt.show()
plt.close()

P = 50
Ac = np.sqrt(2*P)

k = 5
a = 0.5
x_ct = []
for i in range(len(tau_n)):
    x_ct.append(Ac*(1 + a*m_nt[i])*np.cos(2*np.pi*tau_n[i]*k))

envU = []
for i in range(len(tau_n)):
    envU.append(Ac*(1 + a*m_nt[i]))

envL = []
for i in range(len(tau_n)):
    envL.append(-Ac*(1 + a*m_nt[i]))

plt.title("AM signal")
plt.xlabel("Normalised Time")
plt.ylabel("Amplitude")

plt.plot(tau_n, x_ct)
plt.plot(tau_n, envU, linestyle = "--")
plt.plot(tau_n, envL, linestyle = "--")
plt.grid()

plt.show()
plt.close()

L2 = 100
N2 = 2**18
tau_n2 = np.linspace(0,L2,N2)
m_nt2 = []
for i in range(len(tau_n2)):
  m_nt2.append(Y*np.cos(2*np.pi*tau_n2[i] + phi_1) + Z*np.sin(4*np.pi*tau_n2[i] + phi_2))


k = 5
a = 0.5
x_ct2 = []
for i in range(len(tau_n2)):
    x_ct2.append(Ac*(1 + a*m_nt2[i])*np.cos(2*np.pi*tau_n2[i]*k))

fig, axs = plt.subplots(2, 1, figsize = (10, 8))

axs[0].plot(tau_n2, m_nt2)
axs[0].set_title("Plot of the normalised message signal in the time domain with length 100")
axs[0].set_xlabel("Normalised time tau_n")
axs[0].set_ylabel("Message signal m_nt")
axs[0].grid()

axs[1].plot(tau_n2, x_ct2)
axs[1].set_title("AM signal")
axs[1].set_xlabel("Normalised Time")
axs[1].set_ylabel("Amplitude")
axs[1].grid()

plt.tight_layout()
plt.show()
plt.close()

from scipy.fft import fft, fftshift 

fourier = np.abs(fft(x_ct2))
fourier = fftshift(fourier)
fourier = fourier/max(fourier) * Ac
w = np.linspace(-N2/(2*L2),N2/(2*L2),N2)

plt.title("Spectrum of AM signal")
plt.xlabel("Frequency f/f_m (Hz)")
plt.ylabel("Amplitude, |X(omega)|")
plt.xlim(-10, 10)
plt.ylim(0,10)
T
plt.plot(w, fourier)

plt.show()
plt.close()

x_am_1 = (a*r1*Ac)/(2*np.abs(min_val))
x_am_2 = (a*r2*Ac)/(2*np.abs(min_val))
print(x_am_1, x_am_2)
