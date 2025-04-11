from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    x1 = float(request.args.get('x1', 0))
    x2 = float(request.args.get('x2', 0))
    suma = x1 + x2
    prediction = 1 if suma > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "x1": x1,
            "x2": x2,
            "sum": suma
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)