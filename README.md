# pizerofacecam

Quick start instructions:
apt install python-opencv python-picamera python-flask
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

You can then start it with:
python facecam.py

Then when you request http://{hostname}:5000/facecam/ it will grab a frame from the raspberry pi camera, send through opencv with the frontal face detection, draw rectangles around any faces found, and then return the image as a png.
