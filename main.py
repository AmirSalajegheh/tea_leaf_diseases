from ultralytics import YOLO
import cv2

model = YOLO("Data/best.pt")

image_path = "Data/input.jpg"

results = model.predict(source=image_path, save=False , conf=0.6)

img = cv2.imread(image_path)

class_names = model.names

# پردازش نتایج
for r in results:
    for box in r.boxes:
        cls_id = int(box.cls[0])  
        label = class_names[cls_id]  
        x1, y1, x2, y2 = map(int, box.xyxy[0])  


        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)  


        cv2.putText(img, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

output_path = "Data/result.jpg"
cv2.imwrite(output_path, img)

