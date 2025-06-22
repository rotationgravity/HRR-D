
# HRR-D v5.2 – Harmonic Rotating Relativistic Dynamics

This repository presents version 5.2 of the HRR-D (Harmonic Rotating Relativistic Dynamics) model — a novel cosmological framework that interprets spacetime as a structured, rotating geometry.

## 🔭 Overview

HRR-D provides a rotation-based alternative to standard ΛCDM cosmology, explaining:
- Redshift-distance relations without expansion
- Galaxy rotation curves without dark matter
- CMB features using wave resonances in rotating space
- Large-scale structure formation and BAO analogs
- Time-delay and lensing effects without modified gravity

## 🧠 What's New in v5.2

- Fully reformulated geodesic model: rotation affects geometry, not particle velocity
- Light and neutrinos now follow same null geodesics — resolves SN 1987A neutrino timing
- Simulations of Apophis asteroid trajectory under HRR-D constraints
- All scripts now Python 3.12 compatible

## 📂 Included Files

- `hrrd_apophis_simulering.py`: Real-world asteroid trajectory simulation
- `README.md`: Project documentation
- `CHANGELOG.txt`: Version history and evolution notes
- `LICENSE`: Open-source license (MIT)

## 🚀 Requirements

- Python ≥ 3.12
- Libraries: `astropy`, `numpy`, `matplotlib`, `datetime`, `requests`

Install them using:
```bash
pip install astropy numpy matplotlib requests
```

## 🛰️ Running the Simulation

To simulate Apophis using HRR-D metrics:
```bash
python hrrd_apophis_simulering.py
```

This script fetches orbital data, applies HRR-D geometric corrections, and plots trajectory shifts vs classical model.

## 🧪 Validation Status

| Test Area                  | Status     |
|---------------------------|------------|
| Redshift z(r)             | ✅ Approved |
| Galaxy Rotation Curves    | ✅ Approved |
| CMB Peaks (ℓ ≈ 220)       | ✅ Approved |
| BAO Structure             | ✅ Approved |
| Gravitational Lensing     | ✅ Approved |
| 21 cm Absorption          | ✅ Approved |
| Supernova Neutrino Delay  | ✅ Approved |
| Asteroid Risk Zones       | ⚙️ In Progress |
| Solar System Tests        | ⚙️ Upcoming |

## 🌐 Related Articles

- Medium: [HRR-D: From Vision to Verification](https://medium.com/@danielssonhendrik/hrr-d-the-next-phase-from-vision-to-verification-15f97cde92ef)
- GitHub Repo: https://github.com/rotationgravity/HRR-D

## 📧 Contact

For collaboration, questions, or testing requests, please reach out via Medium or GitHub issues.

---

**“Why make it harder than it is? Look at what’s in front of us – and understand it.”**
