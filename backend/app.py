from flask_socketio import SocketIO, emit, join_room, leave_room
from flask import Flask, request,jsonify
from flask_cors import CORS

import cv2
import io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#socketio
#from websocket_services.socketio_handler import socketio_handler
from websocket_services.users import add_new_user, remove_user, get_users_count
import websocket_services.users as users

#ai model
import services.main as ai_detector

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


#socketio_handler(socketio)
@socketio.on('connect')
def handle_connect():
    socket_id = request.sid
    add_new_user(socket_id)
    #join_room(socket_id)
    emit("connect",{"data":f"id: {socket_id} is connected"},to=socket_id)
    print(f"======>Client:'{socket_id}' connected. , users count: ",get_users_count())

@socketio.on('disconnect')
def handle_disconnect():
    request_id = request.sid
    remove_user(request_id)
    print("---------->Client disconnected. ",request_id +" , users count: ",get_users_count())

@socketio.on("predict_image")
def handle_image_prediction(data):
    socket_id = request.sid
    
    image,emotion = ai_detector.get_predicted_image_emotion(data)

    #increase emotion detected
    users.increase_user_emotion(socket_id=socket_id,emotion=emotion)
    
    #emit result to user
    emit("result_file",{"image":image}, to = socket_id)
    
    print("predict_image: ", data)
    return True

@socketio.on("get_final_result")
def get_final_result():
    socket_id = request.sid
    emit("get_final_result",users.get_user_emotions(),to=socket_id)
    return True

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
