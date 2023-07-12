import streamlit as st

# Define the correct username and password
USERNAME = "gelanaabdisa"
PASSWORD = "galoo"

# Ask the user to enter the username and password
username = st.sidebar.text_input("Enter your username")
password = st.sidebar.text_input("Enter your password", type="password")

# Check if the entered username and password are correct
if username == USERNAME and password == PASSWORD:
        st.write("Welcome!")
    
    # Streamlit code 
    
        import streamlit as st
        import tensorflow as tf
        from keras.applications.imagenet_utils import decode_predictions
        import cv2
        from PIL import Image, ImageOps
        import numpy as np
        from keras.applications.imagenet_utils import preprocess_input

        st.title('This is my love_vs_shyness face recognition dashboard')


        @st.cache_resource()
        def load_model():
            model = tf.keras.models.load_model('lsmodel_1.h5')  
            return model

        def decode_custom_predictions(prediction, class_labels, top=1):
            top_predictions = np.argsort(-prediction, axis=1)[:, :top]
            decoded_predictions = [[(class_labels[i], prediction[j, i]) for i in top_predictions[j]] for j in range(top_predictions.shape[0])]
            return decoded_predictions

        def upload_predict(upload_image, model):
            size = (150, 150)
            image = ImageOps.fit(upload_image, size, Image.ANTIALIAS)
            image = np.asarray(image)
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            img_resize = cv2.resize(img, dsize=size, interpolation=cv2.INTER_CUBIC)
            img_reshape = img_resize[np.newaxis, ...]
            img_preprocessed = preprocess_input(img_reshape)
            prediction = model.predict(img_preprocessed)
            class_labels = ["love", "shayness"]  
            pred_class_indices = np.argmax(prediction, axis=1)
            pred_class = [class_labels[idx] for idx in pred_class_indices]
            return pred_class

            

        def main():
            st.title("Image Classification")

            file = st.file_uploader("Upload the image to be classified as either love or shyness", type=["jpg", "png"])
            st.set_option('deprecation.showfileUploaderEncoding', False)

            if file is None:
                st.text("Please upload an image file")
            else:
                model = load_model()
                image = Image.open(file)
                st.image(image, use_column_width=True)
                predictions = upload_predict(image, model)
                image_class = str(predictions[0])
                st.write("The image is classified as:", image_class)

        if __name__ == '__main__':
            main()
else:
    st.write("Sorry, the password you entered is incorrect.")




