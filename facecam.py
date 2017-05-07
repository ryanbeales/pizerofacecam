import cv2
import time
import picamera
import picamera.array
import base64
from flask import Flask, Request, make_response
import numpy as np


def cv2_array_capture():
  with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(1)
    with picamera.array.PiRGBArray(camera) as stream:
      camera.capture(stream, format='bgr')
      image = stream.array
  return image

def detect_face(image_array):
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(5,5), flags=cv2.CASCADE_SCALE_IMAGE)
  print faces, face_cascade.empty()
  for (x,y,w,h) in faces:
    cv2.rectangle(image_array,(x,y),(x+w,y+h),(255,0,0),2)
  return image_array

def capture_and_find():
  image = detect_face(cv2_array_capture())
  cv2.imwrite('test.jpg', image)


app = Flask(__name__)

@app.route('/facecam/')
def facecam():
  image = detect_face(cv2_array_capture())
  ret, buf = cv2.imencode('.png', image)
  response = make_response(buf.tostring())
  response.headers['Content-Type'] = 'image/png'
  return response


if __name__ == '__main__':
  app.run(host='::', debug=False)
