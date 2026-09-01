import csv

with open("Titanic.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

survived = sum(1 for row in rows if row["Survived"] == "1")
total = len(rows)

print(f"Passengers: {total}")
print(f"Survived: {survived} ({survived / total:.1%})")

for sex in ("female", "male"):
    group = [row for row in rows if row["Sex"] == sex]
    n = len(group)
    s = sum(1 for row in group if row["Survived"] == "1")
    print(f"{sex.capitalize()}: {s}/{n} survived ({s / n:.1%})")
