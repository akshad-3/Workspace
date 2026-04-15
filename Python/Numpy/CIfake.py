import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

print("All libraries loaded successfully!")
print("TensorFlow version:", tf.__version__)


IMAGE_SIZE = (32, 32)   
BATCH_SIZE = 32         
EPOCHS = 10     

print("Settings are ready!")



import os

def load_images(folder, label, limit=500):
    images = []
    labels = []

    all_files = os.listdir(folder)
    all_files = all_files[:limit]  
    for filename in all_files:
        img = tf.keras.utils.load_img(
            os.path.join(folder, filename),
            target_size=IMAGE_SIZE
        )

        img_array = tf.keras.utils.img_to_array(img)

        img_array = img_array / 255.0

        images.append(img_array)
        labels.append(label)

    return np.array(images), np.array(labels)



print("Load function is ready! (dataset download needed to run)")




def show_sample_images(X, y):
    plt.figure(figsize=(10, 4))

    real_indices = np.where(y == 1)[0][:5]
    for i, idx in enumerate(real_indices):
        plt.subplot(2, 5, i + 1)
        plt.imshow(X[idx])
        plt.title("REAL", color="green")
        plt.axis("off")

    fake_indices = np.where(y == 0)[0][:5]
    for i, idx in enumerate(fake_indices):
        plt.subplot(2, 5, i + 6)
        plt.imshow(X[idx])
        plt.title("FAKE", color="red")
        plt.axis("off")

    plt.suptitle("Can you tell which ones are AI-generated?")
    plt.savefig("sample_images.png")
    plt.show()

print("Sample image function is ready!")

model = keras.Sequential([

    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),

    keras.layers.MaxPooling2D(2, 2),

    keras.layers.Conv2D(32, (3, 3), activation='relu'),

    keras.layers.MaxPooling2D(2, 2),

    keras.layers.Flatten(),

    keras.layers.Dense(64, activation='relu'),

    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("\nModel Summary:")
model.summary()

print("Train function ready! (needs dataset to run)")


def plot_accuracy(history):
    plt.figure(figsize=(8, 4))

    