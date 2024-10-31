import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

class BreastCancerModel:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def predict(self, img_path):
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

        prediction = self.model.predict(img_array)
        probability = prediction[0][0]

        if probability >= 0.3:
            predicted_class = '1 - Tumor Ganas (Malignant)'
            patient_status = 'Pasien memiliki tumor ganas.'
        else:
            predicted_class = '0 - Tumor Jinak (Benign)'
            patient_status = 'Pasien memiliki tumor jinak.'

        return {'class': predicted_class, 'probability': probability, 'status': patient_status}
