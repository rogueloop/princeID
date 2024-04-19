from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2


model = YOLO("best.pt")
result = model.predict(source="0",show = True)
print(result)
# camera = cv2.VideoCapture(0)
# img_counter = 0

# while True:
#     ret, frame = camera.read()

#     if not ret:
#         print("failed to grab frame")
#         break
#     cv2.imshow("test", frame)

#     k = cv2.waitKey(1)
#     if k%256 == 27:
#         # ESC pressed
#         print("Escape hit, closing...")
#         break
#     elif k%256 == 32:
#         # SPACE pressed
#         img_path = "opencv_frame_{}.png".format(img_counter)
#         cv2.imwrite(img_path, frame)
#         outs = model.predict(img_path)
#         img_counter += 1

# camera.release()
