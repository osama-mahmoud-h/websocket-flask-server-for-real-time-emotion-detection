from flask_socketio import SocketIO, emit
from flask import Flask, request,jsonify
from flask_cors import CORS

import cv2
import io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route("/")
def home():
    data = {'data':'hello world'}
    return jsonify(data)

@app.route("/http-call")
def http_call():
    """return JSON with string data as the value"""
    data = {'data':'This text was fetched using an HTTP call to server on render'}
    return jsonify(data)

@socketio.on("connect")
def connected():
    """event listener when client connects to the server"""
    print("socket_id: ",request.sid)
    print("client has connected")
    emit("connect",{"data":f"id: {request.sid} is connected"})

@socketio.on('data')
def handle_message(data):
    """event listener when client types a message"""
    print("data from the front end: ",str(data))
    emit("data",{'data':data,'id':request.sid},broadcast=True)

@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("user disconnected")
    emit("disconnect",f"user {request.sid} disconnected",broadcast=True)
   


@socketio.on("file")
def readfile(file):
   # read the binary string data
   filedata = file['fileData']

  # Decode the binary data using OpenCV
   img_array = np.frombuffer(filedata, np.uint8)
   img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

   # Create an empty frame with the same dimensions as the image
   frame = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

   # Assign the image to the frame
   frame[:, :, :] = img[:, :, :]
   #print("file: ",file)
   ret, buffer = cv2.imencode('.jpg', frame)
   frame = buffer.tobytes()
   print("file processed sucsuflly.............................")
   emit("result_file",{"image":frame})


if __name__ == '__main__':
    socketio.run(app, debug=True,port=5050)
    
""" https://medium.com/@adrianhuber17/how-to-build-a-simple-real-time-application-using-flask-react-and-socket-io-7ec2ce2da977 """
