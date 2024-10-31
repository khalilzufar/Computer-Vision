# Mammogram Tumor Detection 🩺

## Overview 🌟
Proyek ini bertujuan untuk mengembangkan model berbasis Computer Vision yang mampu mendeteksi tanda-tanda tumor pada mammogram. Dengan melakukan klasifikasi gambar, model ini membantu dalam mendeteksi kanker payudara sejak dini, yang penting untuk meningkatkan tingkat kesembuhan.

Analisis ini mencakup:
- 🧑‍💻 Eksplorasi Data
- 🧹 Pembersihan Data
- 🔍 Modelling
- 📊 Evaluasi Model

Proyek ini diharapkan dapat mendukung diagnosis lebih awal dengan deteksi tumor payudara melalui analisis gambar medis. Model ini tersedia melalui demo deployment di Hugging Face, memungkinkan pengguna mengunggah gambar mammogram dan menerima prediksi risiko, yang diharapkan dapat mendukung diagnosis lebih awal dan akurasi deteksi tumor payudara melalui analisis gambar medis.

## Objectives 🎯
- Mengembangkan model Machine Learning yang mampu mengidentifikasi gambar mammogram yang menunjukkan indikasi tumor.

## Dependencies ⚙️
- ![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white)
- ![Jupyter Notebook](https://img.shields.io/badge/-Jupyter%20Notebook-orange?logo=jupyter&logoColor=white)
- ![TensorFlow](https://img.shields.io/badge/-TensorFlow-orange?logo=tensorflow&logoColor=white)


## Libraries 📚
- **Data Manipulasi dan Visualisasi:**
  - Numpy
  - os
  - Pandas
  - Matplotlib
  - Seaborn
- **Modeling dan Evaluasi:**
  - `tensorflow` (dengan `ImageDataGenerator`, `Sequential`, `Conv2D`, `MaxPooling2D`, `Flatten`, `Dense`, `Dropout`, `GlobalAveragePooling2D`)
  - `MobileNetV2` dari `tensorflow.keras.applications` untuk transfer learning
  - `sklearn.metrics` (classification report, confusion matrix)

## Related Project Links 🔗
 - [Dataset](https://www.kaggle.com/datasets/hayder17/breast-cancer-detection)
 - [Demo Deployment on Hugging Face](https://huggingface.co/spaces/khalilzufar/Breast-Tumor-Prediction)

## How to Use 🛠️
1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/khalilzufar/Computer-Vision.git
   
2. Navigasi ke Direktori Proyek: Ubah direktori Anda ke repositori yang telah dikloning:
   ```bash
   cd Computer-Vision

3. Buka Jupyter Notebook: Mulai Jupyter Notebook dengan perintah berikut:
   ```bash
   jupyter notebook
   ```
   Ini akan membuka web di browser Anda.

4. Jalankan Notebook: Buka file notebook yang relevan (misalnya, computer_vision.ipynb) dan ikuti instruksi untuk mengeksplorasi data dan menjalankan analisis.

## Author ✍️
**Khalil Zufar**

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/khalil-zufar/)
