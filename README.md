# BreathSense

**Aim:** Low-cost home monitoring of breath gases linked to health, starting with acetone.

**Approach:** Commercial metal-oxide sensors first (BME688, SHT31, then Figaro TGS1820), with our own calibration, humidity correction and analysis in Python.

**Status:** Phase 0 started 24 Nov 2026. Phase 1 runs 14 Dec 2026 to 24 Jan 2027.

*Research prototype. Self-testing only. Not a medical device.*

## Folders
| Folder | Contents |
|---|---|
| literature | papers.csv and reading notes |
| protocol | sampling protocol |
| model | chamber models (Python / COMSOL) |
| data | raw CSV logs, one file per session (never edited) |
| analysis | notebooks, breathlib.py, figures |
| hardware | ESP32 sketches, logger.py, parts list |
| reports | phase reports and summaries |

## Quick start
```
pip install -r requirements.txt
python hardware/logger.py COM5 baseline
```

