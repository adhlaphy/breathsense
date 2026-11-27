# Usage: python logger.py COM5 breath      (Linux/Mac: /dev/ttyUSB0)
import serial, sys, datetime, pathlib

port, condition = sys.argv[1], sys.argv[2]
day = datetime.date.today().isoformat()
folder = pathlib.Path("data"); folder.mkdir(exist_ok=True)
n = len(list(folder.glob(day + "_s*.csv"))) + 1
path = folder / f"{day}_s{n:02d}_{condition}.csv"

with serial.Serial(port, 115200, timeout=2) as ser, open(path, "w") as f:
    print("Logging to", path, " (Ctrl+C to stop)")
    try:
        while True:
            line = ser.readline().decode(errors="ignore").strip()
            if not line or line.startswith("#"):
                if line: print(line)
                continue
            f.write(line + "\n"); f.flush()
            print(line)
    except KeyboardInterrupt:
        print("Stopped. Saved", path)
