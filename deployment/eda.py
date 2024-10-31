import os
import matplotlib.pyplot as plt
import streamlit as st

def plot_images(path):
    labels = os.listdir(path)
    for label in labels:
        folder_path = os.path.join(path, label)
        fig = plt.figure(figsize=(20, 20))
        columns = 5
        rows = 1
        st.write(f'Class: {label}')
        images = os.listdir(folder_path)
        for index in range(1, columns*rows + 1):
            fig.add_subplot(rows, columns, index)
            image = plt.imread(os.path.join(folder_path, images[index]))
            plt.imshow(image)
            plt.axis("off")
        st.pyplot(fig)

def group_and_count_images(path):
    category_counts = {}
    for category in os.listdir(path):
        category_path = os.path.join(path, category)
        if os.path.isdir(category_path):
            image_files = os.listdir(category_path)
            category_counts[category] = len(image_files)
    return category_counts

def plot_side_by_side_pie_charts(train_data, test_data, valid_data):
    labels_train = list(train_data.keys())
    sizes_train = list(train_data.values())
    
    labels_test = list(test_data.keys())
    sizes_test = list(test_data.values())

    labels_valid = list(valid_data.keys())
    sizes_valid = list(valid_data.values())

    colors = {
        '0': '#FDD20E',  # Yellow for benign (tumor jinak)
        '1': 'r'         # Red for malignant (tumor ganas)
    }

    train_colors = [colors[label] for label in labels_train]
    test_colors = [colors[label] for label in labels_test]
    valid_colors = [colors[label] for label in labels_valid]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    ax1.pie(sizes_train, labels=labels_train, colors=train_colors, autopct='%1.1f%%', startangle=90)
    ax1.set_title('Training Dataset Image Counts')
    ax1.axis('equal')

    ax2.pie(sizes_test, labels=labels_test, colors=test_colors, autopct='%1.1f%%', startangle=90)
    ax2.set_title('Testing Dataset Image Counts')
    ax2.axis('equal')

    ax3.pie(sizes_valid, labels=labels_valid, colors=valid_colors, autopct='%1.1f%%', startangle=90)
    ax3.set_title('Validation Dataset Image Counts')
    ax3.axis('equal')

    plt.legend(labels=['Benign (tumor jinak)', 'Malignant (tumor ganas)'], loc='upper right')
    plt.tight_layout()
    st.pyplot(fig)

def display_eda(train_path, test_path, valid_path):
    st.title("Exploratory Data Analysis (EDA)")
    
    st.header("Visualisasi Gambar dari Setiap Kelas")
    plot_images(train_path)  # Ganti dengan path folder data Anda
    
    st.header("Jumlah Gambar di Setiap Kategori")
    train_image_counts = group_and_count_images(train_path)
    test_image_counts = group_and_count_images(test_path)
    valid_image_counts = group_and_count_images(valid_path)

    plot_side_by_side_pie_charts(train_image_counts, test_image_counts, valid_image_counts)
