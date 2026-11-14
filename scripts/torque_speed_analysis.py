
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "ai4i2020.csv"

ai = pd.read_csv(DATA_PATH)

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. Load dataset
# ==========================================

ai = pd.read_csv("ai4i2020.csv")

# ==========================================
# 2. Separate failure and non-failure records
# ==========================================

normal = ai[ai["Machine failure"] == 0]
failed = ai[ai["Machine failure"] == 1]

print("=== DATASET SUMMARY ===")
print(f"Total records: {len(ai)}")
print(f"No failure: {len(normal)}")
print(f"Failure: {len(failed)}")
print(f"Failure rate: {len(failed) / len(ai) * 100:.2f}%")

# ==========================================
# 3. Statistical comparison
# ==========================================

summary = ai.groupby("Machine failure")[
    ["Rotational speed [rpm]", "Torque [Nm]"]
].agg(["mean", "median", "std"])

print("\n=== TORQUE AND SPEED STATISTICS ===")
print(summary.round(2))

# ==========================================
# 4. Scatter plot - all records
# ==========================================

fig1, ax1 = plt.subplots(figsize=(9, 6))

ax1.scatter(
    ai["Rotational speed [rpm]"],
    ai["Torque [Nm]"],
    alpha=0.4,
    s=12
)

ax1.set_xlabel("Rotational Speed (rpm)")
ax1.set_ylabel("Torque (Nm)")
ax1.set_title("Torque vs Rotational Speed")
ax1.grid(True, alpha=0.2)

fig1.tight_layout()
fig1.savefig("torque_vs_speed.png", dpi=300)

# ==========================================
# 5. Scatter plot - failure comparison
# ==========================================

fig2, ax2 = plt.subplots(figsize=(9, 6))

ax2.scatter(
    normal["Rotational speed [rpm]"],
    normal["Torque [Nm]"],
    alpha=0.15,
    s=10,
    label="No Failure"
)

ax2.scatter(
    failed["Rotational speed [rpm]"],
    failed["Torque [Nm]"],
    alpha=0.8,
    s=24,
    label="Failure"
)

ax2.set_xlabel("Rotational Speed (rpm)")
ax2.set_ylabel("Torque (Nm)")
ax2.set_title("Machine Failures by Torque and Rotational Speed")
ax2.legend()
ax2.grid(True, alpha=0.2)

fig2.tight_layout()
fig2.savefig("machine_failure_torque_speed.png", dpi=300)

# ==========================================
# 6. Show both figures
# ==========================================

failure_types = ["TWF", "HDF", "PWF", "OSF", "RNF"]

failure_counts = ai[failure_types].sum()

print("\n=== FAILURE TYPES ===")
print(failure_counts)

fig3, ax3 = plt.subplots(figsize=(9, 5))

bars = ax3.bar(failure_counts.index, failure_counts.values)

ax3.set_xlabel("Failure Type")
ax3.set_ylabel("Number of Records")
ax3.set_title("Distribution of Machine Failure Types")

ax3.bar_label(bars)

fig3.tight_layout()
fig3.savefig("failure_types.png", dpi=300)
failure_types = ["TWF", "HDF", "PWF", "OSF", "RNF"]

# Number of failure labels assigned to each record
ai["Failure type count"] = ai[failure_types].sum(axis=1)

print("=== FAILURE LABEL CHECK ===")

print("Records with machine failure:")
print((ai["Machine failure"] == 1).sum())

print("Records with at least one failure type:")
print((ai["Failure type count"] > 0).sum())

print("Records with multiple failure types:")
print((ai["Failure type count"] > 1).sum())

print("Machine failure without a failure type:")
print(
    ((ai["Machine failure"] == 1) &
     (ai["Failure type count"] == 0)).sum()
)

print("Failure type without machine failure:")
print(
    ((ai["Machine failure"] == 0) &
     (ai["Failure type count"] > 0)).sum()
)
plt.show()
