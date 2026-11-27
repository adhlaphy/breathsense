RHO, M, VM = 0.791, 58.08, 24450        # g/mL, g/mol, mL/mol at 25 C, 1 atm

def stock_ppm(uL_acetone, bag_mL=10000):
    vapour_mL = uL_acetone * 1e-3 * RHO / M * VM
    return vapour_mL / (bag_mL + vapour_mL) * 1e6

def stock_volume_for(target_ppm, stock, bag_mL=10000):
    """mL of stock to add to bag_mL of clean air to get target_ppm."""
    return target_ppm * bag_mL / (stock - target_ppm)

c0 = stock_ppm(1.0); print(f"stock = {c0:.1f} ppm")
for c in [0.5, 1, 2, 3, 5]:
    print(c, "ppm ->", round(stock_volume_for(c, c0)), "mL of stock into 10 L")
