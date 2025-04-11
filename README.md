# Flask Predict API

Prosty serwis API zbudowany przy użyciu Flask, który wykonuje predykcję na podstawie dwóch liczb przekazanych w zapytaniu GET.

---

## 🔍 Endpoint

```
GET /api/v1.0/predict?x1=<liczba1>&x2=<liczba2>
```

### 📌 Zasady działania:
- Jeśli **suma dwóch liczb** (`x1 + x2`) > **5.8**, aplikacja zwraca `prediction: 1`
- W przeciwnym razie zwraca `prediction: 0`
- Jeśli liczby nie są podane – domyślnie przyjmuje `0`

---

## 🧪 Przykład zapytania

```
GET http://localhost:5000/api/v1.0/predict?x1=3.5&x2=3.0
```

**Odpowiedź JSON:**
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

## 🚀 Uruchomienie lokalnie

### Wymagania:
- Python 3.x
- Flask

### Krok po kroku:
```bash
pip install -r requirements.txt
python app.py
```

---

## 🐳 Uruchomienie z użyciem Dockera

1. Zbuduj obraz:
```bash
docker build -t flask-predict-api .
```

2. Uruchom kontener:
```bash
docker run -p 5000:5000 flask-predict-api
```

3. Otwórz przeglądarkę:
```
http://localhost:5000/api/v1.0/predict?x1=2.5&x2=4
```

---

## 📁 Zawartość repozytorium

- `app.py` – główny plik aplikacji Flask
- `requirements.txt` – zależności projektu
- `Dockerfile` – konfiguracja dla konteneryzacji w Dockerze

---

## 👨‍💻 Autor
Projekt wykonany w ramach zadania domowego z przedmiotu **Analiza danych w czasie rzeczywistym**.