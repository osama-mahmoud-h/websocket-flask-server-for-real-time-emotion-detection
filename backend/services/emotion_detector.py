import cv2
import numpy as np
from tensorflow.keras.preprocessing import image 

class emotion_detector:
    def gen_frame_and_emotion(model,face_haar_cascade,frame):  # generate frame by frame from camera
        # Capture frame by frame
            gray_img= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        
            faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)  
            
        
            for (x,y,w,h) in faces_detected:
                print('WORKING')
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),thickness=5)  
                roi_gray=gray_img[y:y+w,x:x+h]          #cropping region of interest i.e. face area from  image  
                roi_gray=cv2.resize(roi_gray,(48,48))  
                img_pixels = image.img_to_array(roi_gray)  
                img_pixels = np.expand_dims(img_pixels, axis = 0)  
                img_pixels /= 255  
        
                print(img_pixels.shape)
                
                predictions = model.predict(img_pixels)  
        
                #find max indexed array  
                
                max_index = np.argmax(predictions[0])  
        
                emotions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']  
                predicted_emotion = emotions[max_index]  
                print(predicted_emotion)
                cv2.putText(frame, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)  
        
            resized_img = cv2.resize(frame, (1000, 700))  
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            return frame, predicted_emotion


