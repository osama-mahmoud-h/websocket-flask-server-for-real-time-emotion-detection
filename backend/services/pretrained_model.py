import cv2
from tensorflow.keras.models import model_from_json
import services.model_parameters as paramerters
import os

absolute_path = os.path.dirname(__file__)


class pretrained_model:
    def load_model(self):
       #load model  
      full_path1 = os.path.join(absolute_path, "fer.json")
      model = model_from_json(open(full_path1, "r").read())  

      #load weights
      full_path2 = os.path.join(absolute_path, "fer.h5")  
      model.load_weights(full_path2)
      return model

    def get_face_haar_cascade(self):
       full_path3 = os.path.join(absolute_path, "haarcascade_frontalface_default.xml")
       return cv2.CascadeClassifier(full_path3)    
