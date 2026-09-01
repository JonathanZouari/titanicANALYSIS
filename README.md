# Titanic Analysis

ניתוח נתונים של נוסעי הטיטאניק — בדיקת הגורמים שהשפיעו על סיכויי ההישרדות.

## נתונים

`Titanic.csv` — 891 נוסעים, 12 עמודות:

| עמודה | תיאור |
|-------|-------|
| PassengerId | מזהה נוסע |
| Survived | 0 = נספה, 1 = שרד |
| Pclass | מחלקת כרטיס (1/2/3) |
| Name | שם מלא |
| Sex | מין |
| Age | גיל (חסרים ערכים) |
| SibSp | אחים/בני זוג על הסיפון |
| Parch | הורים/ילדים על הסיפון |
| Ticket | מספר כרטיס |
| Fare | מחיר הכרטיס |
| Cabin | תא (חסרים ערכים רבים) |
| Embarked | נמל עלייה (C/Q/S) |

## דרישות

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

## הרצה

```bash
jupyter notebook
```

## מבנה הפרויקט

```
titanicANALYSIS/
├── Titanic.csv     # נתוני הגלם
└── README.md
```

## שאלות מחקר

1. האם מין הנוסע השפיע על סיכויי ההישרדות?
2. מה הקשר בין מחלקת הכרטיס להישרדות?
3. כיצד הגיל משפיע על ההישרדות?
4. האם נסיעה עם משפחה שיפרה את הסיכויים?

## מקור

[Kaggle — Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic)
