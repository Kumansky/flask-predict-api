# Flask Predict API

A simple API service built with Flask that makes a prediction based on two numbers provided via a GET request.

---

## 🔍 Endpoint

```
GET /api/v1.0/predict?x1=<number1>&x2=<number2>
```

### 📌 Logic:
- If the **sum of the two numbers** (`x1 + x2`) is greater than **5.8**, the application returns `prediction: 1`
- Otherwise, it returns `prediction: 0`
- If the numbers are not provided, default values of `0` are used

---

## 🧪 Example request

```
GET http://localhost:5000/api/v1.0/predict?x1=3.5&x2=3.0
```

**Response JSON:**
```json
{
  "prediction": 1,
  "features": {
    "x1": 3.5,
    "x2": 3.0,
    "sum": 6.5
  }
}
```

---

## 🚀 Run locally

### Requirements:
- Python 3.x
- Flask

### Steps:
```bash
pip install -r requirements.txt
python app.py
```

---

## 🐳 Run with Docker

1. Build the image:
```bash
docker build -t flask-predict-api .
```

2. Run the container:
```bash
docker run -p 5000:5000 flask-predict-api
```

3. Open in browser:
```
http://localhost:5000/api/v1.0/predict?x1=2.5&x2=4
```

---

## 📁 Repository contents

- `app.py` – main Flask application file
- `requirements.txt` – project dependencies
- `Dockerfile` – Docker container configuration

---

## 👨‍💻 Author
Project created as part of a homework assignment for the course **Real-Time Data Analysis**.