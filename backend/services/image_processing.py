
import cv2
import numpy as np 

class image_processing:
     
    def convert_imageArr_to_frame(self,file):
         # read the binary string data
        filedata = file['fileData']

        #print("file data, ",filedata)

        # Decode the binary data using OpenCV
        img_array = np.frombuffer(filedata, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # Create an empty frame with the same dimensions as the image
        frame = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

        # Assign the image to the frame
        frame[:, :, :] = img[:, :, :]
        return frame
     
    def convert_frame_to_bytes(self,frame):
         #print("file: ",file)
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        ret, buffer = cv2.imencode('.jpg', frame_bgr)
        frame = buffer.tobytes()
        return frame
