# Ai-Phone-Detection
This project implements a simple AI tool for real-time detection of phones using YOLOv8. When a phone appears in the camera's view, the system raises an alarm, which continues until the phone is no longer visible.

Features
Real-time Detection: Leverages YOLOv8's object detection capabilities to identify phones.
Alarm Notification: Emits an audio alert when a phone is detected.
Customizable Settings: Modify detection parameters and alarm settings to fit specific needs.
Requirements
Python 3.8 or later
YOLOv8 by Ultralytics
OpenCV
Additional dependencies specified in requirements.txt
Setup Instructions
Clone the repository:

git clone https://github.com/LeighWhoriskey/Ai-Phone-Detection.git
cd Ai-Phone-Detection
Install dependencies:

pip install -r requirements.txt
Download the YOLOv8 model weights from Ultralytics and place them in the appropriate folder.

Usage
Run the script:

python phoneAI.py
Position the camera to monitor the area of interest.

If a phone is detected, an alarm will sound until the phone is removed from the camera's view.

Contributing
Contributions are welcome! Please submit issues or pull requests for bug fixes, features, or improvements.
