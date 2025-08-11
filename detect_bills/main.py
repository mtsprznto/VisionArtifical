from ultralytics import YOLO
import cv2

model = YOLO("./models/cash_v0.pt")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame= cap.read()

    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("YOLO", annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
