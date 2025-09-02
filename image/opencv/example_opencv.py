# OpenCV quickstart
# עברית: קריאה לתמונה, המרה לאפור ושמירה לקובץ.
import cv2

img = cv2.imread("image/generated.jpg")  # put any image at image/sample.jpg
if img is None:
    # create a dummy image if not found
    import numpy as np
    img = (np.random.rand(240,320,3)*255).astype("uint8")


# צריך להמיר לאפור
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




# שומר לקובץ
cv2.imwrite("image/out_gray.png", gray)
print("Wrote image/out_gray.png")


# Gaussian blur
blur = cv2.GaussianBlur(img, (5,5), 0)

cv2.imwrite("image/out_blur.png", blur)

# Edge detection (Canny)
edges = cv2.Canny(gray, 100, 200)

cv2.imwrite("image/out_edges.png", edges)


img = cv2.imread("generated.png", cv2.IMREAD_COLOR)   # צבע מלא
gray = cv2.imread("generated.png", cv2.IMREAD_GRAYSCALE)  # שחור-לבן
cv2.imwrite("out.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 90])


resized = cv2.resize(img, (200, 200))
cropped = img[50:200, 100:300]      # חיתוך [y1:y2, x1:x2]
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


cv2.rectangle(img, (50,50), (200,200), (0,255,0), 3)
cv2.putText(img, "Hello OpenCV", (60, 250),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)


edges = cv2.Canny(gray, 100, 200)  # זיהוי קצוות
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Contours found:", len(contours))

# זיהיו פנים
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)