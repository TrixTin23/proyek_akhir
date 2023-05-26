from flask import Flask, request, jsonify
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import numpy as np

app = Flask(__name__)

# Load model LSTM
model = load_model('model.h5')

# Definisikan endpoint untuk route '/predict' dengan method POST
@app.route('/predict', methods=['GET'])
def predict():
    # Mendapatkan data yang dikirimkan melalui POST request
    data = request.get_json()
    usd_value = data['Price']

    # Normalisasi nilai USD
    max_usd_value = 1000  # Nilai USD maksimum yang digunakan saat melatih model
    normalized_usd_value = usd_value / max_usd_value

    # Lakukan prediksi menggunakan model LSTM
    prediction = model.predict(np.array([[normalized_usd_value]]))
    predicted_rupiah_value = prediction[0][0] * max_usd_value

    # Mengembalikan hasil prediksi dalam format JSON
    return jsonify({'predicted_rupiah_value': predicted_rupiah_value})

if __name__ == '__main__':
    # Menjalankan aplikasi Flask
    app.run(debug=True)