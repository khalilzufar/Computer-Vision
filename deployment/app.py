import streamlit as st
from model import BreastCancerModel
import matplotlib.pyplot as plt
from PIL import Image
import eda

# Memuat model
model = BreastCancerModel('model.h5')  # Ganti dengan path model Anda

# Judul aplikasi
st.title("Deteksi Kanker Payudara")
st.write("Aplikasi ini untuk memprediksi apakah gambar mammogram menunjukkan tanda-tanda kanker payudara.")

# Navigasi Menu
page = st.sidebar.selectbox("Pilih Halaman:", ("Home", "EDA", "Prediksi"))

if page == "Home":
    st.write("Selamat datang di aplikasi deteksi kanker payudara. Anda dapat memprediksi gambar mammogram dan melihat hasilnya.")
    
    # Upload gambar
    uploaded_file = st.file_uploader("Upload gambar mammogram", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption='Gambar yang diunggah', use_column_width=True)

        temp_file_path = "temp_image.jpg"
        img.save(temp_file_path)

        # Melakukan prediksi
        result = model.predict(temp_file_path)

        # Menampilkan hasil prediksi
        st.subheader("Hasil Prediksi")
        st.write(f"Prediksi: {result['class']}")
        st.write(f"Probabilitas: {result['probability']:.2f}")
        st.write(result['status'])

elif page == "EDA":
    # Ganti dengan path ke dataset Anda
    train_path = 'path/to/train_data'  
    test_path = 'path/to/test_data'  
    valid_path = 'path/to/valid_data'  

    eda.display_eda(train_path, test_path, valid_path)
