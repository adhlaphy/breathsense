import numpy as np
L, D, u = 0.06, 1.1e-5, 0.05        # chamber length (m), diffusivity (m2/s), mean velocity (m/s)
N = 120; dx = L / N
dt = min(0.4 * dx**2 / D, 0.4 * dx / u)   # stable time step
c = np.zeros(N); t = 0; out = []
while t < 10:
    c[0] = 1.0                                   # inlet held at breath concentration
    adv = -u * (c - np.roll(c, 1)) / dx          # upwind advection
    dif = D * (np.roll(c, -1) - 2 * c + np.roll(c, 1)) / dx**2
    c[1:-1] += dt * (adv + dif)[1:-1]; c[-1] = c[-2]
    t += dt; out.append((t, c[int(0.8 * N)]))  # sensor at 80 % of length
t90 = next(tt for tt, cc in out if cc >= 0.9); print("t90 at sensor:", round(t90, 2), "s")
