
users = set()
users_emotions = {}

def add_new_user(socket_id):
    users.add(socket_id)
    users_emotions[socket_id]= {'angry':0, 'disgust':0, 'fear':0, 'happy':0, 'sad':0, 'surprise':0, 'neutral':0}
    return True

def remove_user(socket_id):
    if(socket_id in users):
        users.remove(socket_id)
        del(users_emotions[socket_id])
        return True
    else:
        return False

def get_users_count():
    return len(users)

def increase_user_emotion(socket_id,emotion):
    if(socket_id in users_emotions):
        users_emotions[socket_id][emotion] +=1

def get_user_emotions(socket_id):
    if(socket_id in users_emotions):
        return users_emotions[socket_id]        
