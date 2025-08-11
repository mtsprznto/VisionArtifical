from ultralytics import YOLO


# De esta forma se usan los modelos entrenados
model = YOLO('./model/yolov8n-pose.pt')

images = "./inputs/*.jpg"
result = model(images, conf=0.7)

for res in result:
    res.show()