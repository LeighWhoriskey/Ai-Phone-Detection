from ultralytics import YOLO
import cv2
from playsound import playsound
import os

current_working_directory = os.getcwd()
print(current_working_directory)

model = YOLO('C:/Users/Sham/Desktop/THE_BIG_ONE/master/model/best.pt')

cameraIn = cv2.VideoCapture(0)


while cameraIn.isOpened():

    imageCaptured, frame = cameraIn.read()

    if imageCaptured:
        results = model.track(source=frame, persist=True, conf=0.5)
        #results[0].boxes.cls do if statement like if(0 in results[0].boxes.cls) to find phone, 1 to find phone call

        if 0 in results[0].boxes.cls:
            print("found phone or making phone call")
            playsound("C:/Users/Sham/Desktop/THE_BIG_ONE/master/src/sounds/alertSound.mp3")
            playsound("C:/Users/Sham/Desktop/THE_BIG_ONE/master//src/sounds/mobilePhone.mp3")
        elif 1 in results[0].boxes.cls:
            playsound("C:/Users/Sham/Desktop/THE_BIG_ONE/master/src/sounds/alertSound.mp3")
            playsound("C:/Users/Sham/Desktop/THE_BIG_ONE/master//src/sounds/phonecall.mp3")

        annotated_frame = results[0].plot()

        cv2.imshow('YOLO V8 Detection', annotated_frame)

        if cv2.waitKey(2) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reachedq
        break

# Release the video capture object and close the display window
cameraIn.release()
cv2.destroyAllWindows()