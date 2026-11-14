from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "ai4i2020.csv"

ai = pd.read_csv(DATA_PATH)


import pandas as pd
import matplotlib.pyplot as plt


ai = pd.read_csv("ai4i2020.csv")

failed_machine = (ai["Machine failure"] == 1).sum()

working_machine = (ai["Machine failure"] == 0).sum()

Total_machine = failed_machine+working_machine

failure_percent = failed_machine/Total_machine * 100

ai["Wear_group"] = pd.cut(ai["Tool wear [min]"], bins=[
                          0, 60, 120, 180, 240, 300], include_lowest=True)

failure_rate = (ai.groupby("Wear_group", observed=True)
                ["Machine failure"].mean()*100)

failure_compare = ai.groupby("Wear_group", observed=True)[
    "Machine failure"].agg(["count", "sum"])

failure_compare["Failure rate (%)"] = (
    failure_compare["sum"] / failure_compare["count"] * 100
)

failure_compare = failure_compare.rename(
    columns={
        "count": "Total records",
        "sum": "Failed records"
    }
)


labels = ["0–60", "60–120", "120–180", "180–240", "240–300"]

rates = failure_compare["Failure rate (%)"]
counts = failure_compare["Total records"]

fig, ax = plt.subplots(figsize=(9, 5))

bars = ax.bar(labels, rates)

ax.set_xlabel("Tool Wear (min)")
ax.set_ylabel("Failure Rate (%)")
ax.set_title("Machine Failure Rate by Tool Wear")

ax.set_ylim(0, max(rates) * 1.2)

for bar, rate, count in zip(bars, rates, counts):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.5,
        f"{rate:.1f}%\nn={count}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()
plt.savefig("machine_failure_by_tool_wear.png", dpi=300)

plt.show()
plt.hist(ai["Torque [Nm]"], bins=30, edgecolor="black")

plt.xlabel("Torque (Nm)")
plt.ylabel("Frequency")
plt.title("Distribution of Torque")

plt.show()

print(failed_machine)

print(working_machine)

print(failure_percent)

print(ai["Type"].value_counts())

print(ai.groupby("Machine failure")["Torque [Nm]"].mean())

print(ai.groupby("Machine failure")["Tool wear [min]"].mean())

print(ai["Wear_group"])

print(failure_rate)

print(failure_compare)

print(failure_compare.round(2))
