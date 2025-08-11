from ultralytics import YOLO
import cv2

image = cv2.imread('./inputs/render.jpg')

model = YOLO('./model/yolov8x-pose.pt')

results = model(image, conf=0.7)

print(results[0])
print(results[0].keypoints)

#x,y,conf=results[0].keypoints.data[0][0]
#cv2.circle(image,(int(x),int(y)), 5,(0,255,0),2)

for person in results[0].keypoints.data:
    for i, (x,y,conf) in enumerate(person):
        color = (255,255,255)
        if conf > 0.5:
            if i <= 4:
                color = (0,255,0)
            elif i == 5:
                color = (0,0,0)
            elif 6 <= i <= 11:
                color = (255,255,0)

            cv2.circle(image,(int(x),int(y)), 5,color,2)

        
        cv2.circle(image,(int(x),int(y)), 5,color,2)



cv2.imshow(f"image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()