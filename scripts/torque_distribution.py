
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "ai4i2020.csv"

ai = pd.read_csv(DATA_PATH)

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
ai = pd.read_csv("ai4i2020.csv")

# Create histogram
fig, ax = plt.subplots(figsize=(9, 5))

ax.hist(
    ai["Torque [Nm]"],
    bins=30,
    edgecolor="black",
    alpha=0.8
)

ax.set_title("Distribution of Torque")
ax.set_xlabel("Torque (Nm)")
ax.set_ylabel("Number of Records")
ax.grid(axis="y", alpha=0.2)

fig.tight_layout()
fig.savefig("torque_histogram.png", dpi=300)

# Separate records
normal = ai.loc[ai["Machine failure"] == 0, "Torque [Nm]"]
failed = ai.loc[ai["Machine failure"] == 1, "Torque [Nm]"]

# Create box plot
fig2, ax2 = plt.subplots(figsize=(8, 5))

ax2.boxplot(
    [normal, failed],
    tick_labels=["No Failure", "Failure"],
    showmeans=True
)

ax2.set_title("Torque Distribution by Machine Failure")
ax2.set_ylabel("Torque (Nm)")
ax2.grid(axis="y", alpha=0.2)

fig2.tight_layout()
fig2.savefig("torque_boxplot.png", dpi=300)

# Display both figures
plt.show()
