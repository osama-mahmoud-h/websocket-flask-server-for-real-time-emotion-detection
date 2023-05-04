import cv2
from tensorflow.keras.models import model_from_json

class pretrained_model:
    def load_model():
       #load model  
      model = model_from_json(open("./model_parameters/fer.json", "r").read())  

      #load weights  
      model.load_weights('./model_parameters/fer.h5')
      return model

    def get_face_haar_cascade():
       return cv2.CascadeClassifier('haarcascade_frontalface_default.xml')    
