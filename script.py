import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Parameters
VOCAB_SIZE = 10000
MAX_LEN = 250
EMBEDDING_DIM = 16
MODEL_PATH = 'sentiment_analysis_model.h5'

# Load the IMDB dataset
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=VOCAB_SIZE)

# Pad the sequences
train_data = pad_sequences(train_data, maxlen=MAX_LEN, value=VOCAB_SIZE - 1, padding='post')
test_data = pad_sequences(test_data, maxlen=MAX_LEN, value=VOCAB_SIZE - 1, padding='post')

# Check if saved model exists
if os.path.exists(MODEL_PATH):
    print("Loading Saved Model...")
    model = load_model(MODEL_PATH)
else:
    print("Training a New Model...")

    # Define the Model
    model = Sequential([
        Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LEN),
        GlobalAveragePooling1D(),
        Dense(16, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    # Compile the Model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train the Model
    model.fit(train_data, train_labels, epochs=10, batch_size=32, validation_split=0.2)

    # Save the Trained Model
    model.save(MODEL_PATH)

# Evaluate the Model on Test Data
loss, accuracy = model.evaluate(test_data, test_labels)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Interactive loop for Predictions
word_index = imdb.get_word_index()


def encode_text(text):
    tokens = tf.keras.preprocessing.text.text_to_word_sequence(text)
    tokens = [word_index[word] if word in word_index else 0 for word in tokens]
    return pad_sequences([tokens], maxlen=MAX_LEN, padding='post', value=VOCAB_SIZE - 1)


while True:
    user_input = input("Enter a sentence for sentiment analysis (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    encoded_input = encode_text(user_input)
    prediction = model.predict(encoded_input)

    if prediction[0] < 0.5:
        print("Sentiment Negative")
    else:
        print("Sentiment Positive")