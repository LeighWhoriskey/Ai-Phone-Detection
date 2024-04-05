import cv2
import dlib

# Load the detector and predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:/Users/Sham/Desktop/THE_BIG_ONE/master/src/shape_predictor_68_face_landmarks.dat")

# Load an image using OpenCV
camera = cv2.VideoCapture(0)
capture, image = camera.read()

# Convert to grayscale (dlib expects grayscale images)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = detector(gray)


def lookingDown(landmarks):
    # the range 42,48 is the values dlib places around the right eye
    rightEyeAvg = sum([landmarks.part(i) for i in range(42,48)]) / 6
    
# Loop over each face found in the image
for face in faces:
    # Predict facial landmarks
    landmarks = predictor(gray, face)
    
    # Draw circles on the eye landmarks
    for n in range(36, 42):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(image, (x, y), 4, (255, 0, 0), -1)  # Blue circles for right eye

    for n in range(42, 48):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(image, (x, y), 4, (0, 255, 0), -1)  # Green circles for left eye

# Display the output image with the eyes highlighted
cv2.imshow("Eyes detected", image)
cv2.waitKey(0)
cv2.destroyAllWindows()