from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        future_periods = 5  # Jumlah periode masa depan yang ingin diprediksi
        start_date = datetime.datetime.now().date() + datetime.timedelta(days=1)  # Tanggal awal prediksi (besok)
        date_range = [start_date + datetime.timedelta(days=i) for i in range(future_periods)]

        # Lakukan prediksi dengan model LSTM
        input_data = np.array([[10.0], [20.0], [30.0]])  # Ganti dengan data yang sesuai untuk prediksi
        predicted_values = model.predict(input_data)

        # Format hasil prediksi dalam tabel
        predictions_table = "<table><tr><th>Date</th><th>Predicted Exchange Rate (USD_IDR)</th></tr>"
        for i, pred in enumerate(predicted_values):
            predictions_table += "<tr><td>{}</td><td>{}</td></tr>".format(date_range[i].strftime("%Y-%m-%d"), pred[0])
        predictions_table += "</table>"

        flash('Prediksi berhasil!')
        return render_template('index.html', predictions=predictions_table)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
