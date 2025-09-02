NLTK — מדריך קצר

מה זה?
NLTK (Natural Language Toolkit) היא ספרייה ותיקה לעיבוד שפה טבעית (NLP) בפייתון.
מאפשרת לבצע פעולות בסיסיות בטקסט: חלוקה למילים, ניתוח תחבירי, קיצוץ מילים לשורש ועוד.

למה להשתמש?

Tokenization – פירוק טקסט למילים או משפטים.

POS Tagging – זיהוי חלקי דיבר (פועל, שם עצם, תואר).

Stemming – קיצוץ מילים לשורש בסיסי.

Lemmatization – החזרת מילה לצורה בסיסית "חוקית".

שימוש בקורפוסים מובנים ללימוד וניתוח.

התקנה
pip install nltk


בהרצה ראשונה צריך להוריד משאבי נתונים:

import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("wordnet")