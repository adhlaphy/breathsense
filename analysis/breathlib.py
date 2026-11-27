import numpy as np, pandas as pd

def load(path):
    df = pd.read_csv(path)
    df["t"] = (df.time_ms - df.time_ms.iloc[0]) / 1000.0     # seconds
    return df

def breaths(df, pre=30, post=120):
    """Cut a window around every marker press. Returns list of DataFrames."""
    starts = df.index[(df.marker == 1) & (df.marker.shift(1, fill_value=0) == 0)]
    return [df[(df.t >= df.t[i] - pre) & (df.t <= df.t[i] + post)].copy() for i in starts]

def metrics(w, col="gas_ohm"):
    t0 = w.t[w.marker == 1].iloc[0]
    base = w[w.t < t0][col]
    R0, noise = base.mean(), base.std()
    after = w[w.t >= t0]
    Rmin = after[col].min(); tmin = after.t[after[col].idxmin()]
    target = R0 - 0.9 * (R0 - Rmin)                          # 90 % of the change
    t90 = after.t[after[col] <= target].iloc[0] - t0
    rec = after[(after.t > tmin) & (after[col] >= R0 - 0.1 * (R0 - Rmin))]
    trec = (rec.t.iloc[0] - tmin) if len(rec) else np.nan
    return dict(R0=R0, noise=noise, Rmin=Rmin, S=R0 / Rmin, t90=t90, t_rec=trec,
                RH_peak=after.RH_sht.max())

def humidity_fit(RH, R):
    """Fit ln(R) = a + b*RH from humid-air control data. Returns (a, b)."""
    b, a = np.polyfit(RH, np.log(R), 1)
    return a, b

def corrected_S(Rmeas, RH, a, b):
    """Response left after removing the water-only part."""
    R_water = np.exp(a + b * RH)
    return R_water / Rmeas

def lod(slope, noise_S):
    return 3 * noise_S / slope
