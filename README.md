# Titanic Analysis

Exploratory analysis of the classic [Titanic passenger dataset](https://www.kaggle.com/c/titanic) — who survived the 1912 sinking, and what factors correlated with survival.

## Dataset

[`Titanic.csv`](Titanic.csv) contains 891 passenger records with the following columns:

| Column | Description |
|---|---|
| `PassengerId` | Unique passenger identifier |
| `Survived` | 0 = died, 1 = survived |
| `Pclass` | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd) |
| `Name` | Passenger name |
| `Sex` | Passenger sex |
| `Age` | Age in years (177 missing) |
| `SibSp` | # of siblings/spouses aboard |
| `Parch` | # of parents/children aboard |
| `Ticket` | Ticket number |
| `Fare` | Passenger fare |
| `Cabin` | Cabin number (687 missing) |
| `Embarked` | Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton; 2 missing) |

## Quick findings

- **Overall survival rate: 38.4%** (342 of 891 passengers)
- **Sex was the strongest predictor**: women survived at 74.2% vs. 18.9% for men
- **Class mattered**: 1st class 63.0% survival, 2nd class 47.3%, 3rd class 24.2%
- **Data quality**: `Age` is missing for ~20% of passengers and `Cabin` for ~77%, so both need imputation or exclusion depending on the analysis

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Run the exploratory script, which prints summary statistics and saves a chart to `survival_overview.png`:

```bash
python analysis.py
```

## Project structure

```
.
├── Titanic.csv          # raw dataset
├── analysis.py          # exploratory analysis script
├── requirements.txt      # Python dependencies
└── README.md
```
