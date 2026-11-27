import numpy as np, matplotlib.pyplot as plt
Q = 200.0                                  # mL/s, slow exhale (0.2 L/s)
t = np.linspace(0, 6, 300)
for V in [50, 100, 250]:                   # chamber volume, mL
    tau = V / Q
    plt.plot(t, 1 - np.exp(-t / tau), label=f"V = {V} mL, tau = {tau:.2f} s")
plt.axhline(0.95, ls="--", c="gray"); plt.xlabel("time (s)"); plt.ylabel("C / C_breath")
plt.legend(); plt.tight_layout(); plt.savefig("../analysis/figures/chamber_tau.png", dpi=200)
print("saved analysis/figures/chamber_tau.png")
