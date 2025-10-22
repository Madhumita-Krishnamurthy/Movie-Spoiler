from flask import Flask, request, jsonify
from flask_cors import CORS  # 🔥 new import
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)
CORS(app)  # 🔥 allow all domains to access the API

# Load model and tokenizer
model = load_model("spoiler_pred_finalcopy.h5")
tokenizer = pickle.load(open("tokenizer_final.pkl", "rb"))

MAX_LEN = 200  # update if different in your training

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=MAX_LEN, padding='post')
    prediction = model.predict(padded)
    is_spoiler = int(prediction[0][0] > 0.5)

    return jsonify({'is_spoiler': bool(is_spoiler)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
