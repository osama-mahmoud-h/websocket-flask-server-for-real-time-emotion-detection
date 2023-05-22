# socketio_handler.py
"""
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask import Flask, request,jsonify

from websocket_services.users  import add_new_user, remove_user


def socketio_handler(socketio):
   @socketio.on("connect")
   def connected():
        #get user socket_id
        socket_id = request.sid
        #join room
        #join_room(socket_id)
    
        #add to users list
        add_new_user(socket_id)
        print("socket_id: ",socket_id)
        print("=========> client has connected , user count: ")
        emit("connect",{"data":f"id: {socket_id} is connected"},to=socket_id)

   @socketio.on('data')
   def handle_message(data):
        print("data from the front end: ",str(data))
        emit("data",{'data':data,'id':request.sid},broadcast=True)
        return True

    @socketio.on("disconnect")
      def disconnected():
     #get user socket_id
     #socket_id = request.sid
     print("-------> user disconnected : ")
     emit("disconnect",f"user {request.sid} disconnected",broadcast=True)
     return True
    
    @socketio.on('join')
    def on_join():
     #get user socket_id
     socket_id = request.sid
     #join room
     join_room(socket_id)
     print("-----------> joined to room ")

    @socketio.on('leave')
    def on_leave():
      #get user socket_id
     socket_id = request.sid
     #join room
     leave_room(socket_id)
     print("##########> leave room")
   
"""