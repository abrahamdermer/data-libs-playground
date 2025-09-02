# OpenCV quickstart (עברית)
import cv2
import numpy as np
from pathlib import Path

# נוודא שהתיקייה image קיימת
Path("image").mkdir(exist_ok=True)

# 1) קריאה של תמונה: ננסה קודם את generated.png שהכנו
img = cv2.imread("image/generated.png", cv2.IMREAD_COLOR)
if img is None:
    # אם אין את הקובץ, ניצור תמונה "דמי" כדי שהקוד יעבוד בכל מקרה
    img = (np.random.rand(240, 320, 3) * 255).astype("uint8")

# 2) המרה לגווני אפור
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3) שמירות בסיס
cv2.imwrite("image/out_gray.png", gray)
blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imwrite("image/out_blur.png", blur)

# 4) קצוות + קונטורים
edges = cv2.Canny(gray, 100, 200)
cv2.imwrite("image/out_edges.png", edges)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Contours found:", len(contours))

# (אופציונלי) לצייר קונטורים על העותק של התמונה
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 1)
cv2.imwrite("image/out_contours.png", img_contours)

# 5) ציור טקסט/מלבן על התמונה
img_annot = img.copy()
cv2.rectangle(img_annot, (50, 50), (200, 200), (0, 255, 0), 3)
cv2.putText(img_annot, "Hello OpenCV", (60, 230),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
cv2.imwrite("image/out_annot.png", img_annot)

# 6) שינוי גודל / חיתוך / סיבוב (דוגמאות)
resized = cv2.resize(img, (200, 200))
cv2.imwrite("image/out_resized.png", resized)

# שים לב: טווחי החיתוך חייבים להיות בתוך גבולות התמונה
h, w = img.shape[:2]
y1, y2, x1, x2 = 0, min(200, h), 0, min(300, w)
cropped = img[y1:y2, x1:x2]
cv2.imwrite("image/out_cropped.png", cropped)

rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite("image/out_rotated.png", rotated)

# 7) שמירה ל-JPEG עם איכות 90
cv2.imwrite("image/out_quality90.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 90])

# 8) זיהוי פנים (כנראה לא ימצא בתמונה מלאכותית - זה תקין)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
print("Faces found:", len(faces))
img_faces = img.copy()
for (x, y, w, h) in faces:
    cv2.rectangle(img_faces, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imwrite("image/out_faces.png", img_faces)

print("✅ Saved outputs in the 'image/' folder.")
