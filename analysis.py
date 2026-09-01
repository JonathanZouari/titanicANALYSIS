import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic.csv")

print(df.info())
print(df.describe())
print("\nMissing values:\n", df.isnull().sum())

print("\nOverall survival rate:", df["Survived"].mean().round(3))
print("\nSurvival rate by sex:\n", df.groupby("Sex")["Survived"].mean())
print("\nSurvival rate by class:\n", df.groupby("Pclass")["Survived"].mean())

sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

df.groupby("Sex")["Survived"].mean().plot(kind="bar", ax=axes[0], title="Survival rate by sex")
df.groupby("Pclass")["Survived"].mean().plot(kind="bar", ax=axes[1], title="Survival rate by class")
sns.histplot(df, x="Age", hue="Survived", multiple="stack", bins=30, ax=axes[2])
axes[2].set_title("Age distribution by survival")

plt.tight_layout()
plt.savefig("survival_overview.png", dpi=150)
print("\nSaved chart to survival_overview.png")
