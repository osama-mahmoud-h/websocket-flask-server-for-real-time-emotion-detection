
import services.image_processing as img_process
import services.emotion_detector as detect
import services.pretrained_model  as ai_model


model = ai_model.pretrained_model()
img_processor = img_process.image_processing()

detector = detect.emotion_detector()

def get_predicted_image_emotion(image_array):
    #print("image arrays: ",image_array)
    
    #pre-trained model parameters
    loadedmodel = model.load_model()
    face_haar_cascade = model.get_face_haar_cascade()

    #image processing 
    result_frame = img_processor.convert_imageArr_to_frame(image_array)

    #get prediected imageframe and emotion
    frame_and_emotion_detected = detector.gen_frame_and_emotion(model=loadedmodel,
                                                                face_haar_cascade=face_haar_cascade,
                                                                frame=result_frame)
    

    predicted_frame, predicted_emotion = frame_and_emotion_detected
    # convert frame to bytes using image processing
    #frame_bytes = img_processor.convert_frame_to_bytes(predicted_frame)


    return predicted_frame, predicted_emotion






