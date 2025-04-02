# 🐱 Cat API

A simple Flask-based API that lets users upload and retrieve random cat pictures. This app is great for learning how to build and deploy a basic web service with Python and Flask.

---

## 🚀 Features

- Upload a cat picture via POST request
- Retrieve a random cat picture
- Basic frontend for interacting with the API
- Written in Python using Flask

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cat-api.git
cd cat-api
```

### 2. Set up a virtual environment

```bash
python3 -m venv cat-api-venv
source cat-api-venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app locally

```bash
python app.py
```

The app will be available at `http://localhost:8080`.

---

## 🌐 Deploying to Render

1. Push your code to a GitHub repo
2. Go to [https://dashboard.render.com](https://dashboard.render.com)
3. Click **New > Web Service**
4. Connect your GitHub account and select this repo
5. Set up the service:
   - **Environment:** Python
   - **Build Command:** (leave blank)
   - **Start Command:** `python app.py`
6. Click **Create Web Service** and wait for deployment

Once deployed, visit the URL Render provides — your app will be live!

---

## 📂 Routes

| Method | Endpoint             | Description                  |
|--------|----------------------|------------------------------|
| GET    | `/`                  | Home page with basic UI      |
| POST   | `/uploadCatPicture`  | Upload a new cat image       |
| GET    | `/getCatPicture`     | Get a random cat image       |

---

## 📄 License

MIT License © Kenta Miyahara
