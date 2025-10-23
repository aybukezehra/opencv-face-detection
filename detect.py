import cv2
import os

# --- Dosya yolu (Türkçe karakter yok) ---
img_path = r"C:\Users\AhmetD\Desktop\yuzzz\data.png"

# Resmi oku
img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError(f"Resim okunamadı: {img_path}")

# Haar cascade yükle
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
if not os.path.exists(cascade_path):
    raise FileNotFoundError(f"Cascade dosyası bulunamadı: {cascade_path}")

face_cascade = cv2.CascadeClassifier(cascade_path)

# Griye çevir ve yüzleri bul
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 4)

# Dikdörtgen çiz
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Görüntüyü göster
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()