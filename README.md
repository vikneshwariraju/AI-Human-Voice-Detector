# 🎙️ AI vs Human Voice Detection

An AI-powered web application that detects whether a voice sample is **Human-generated** or **AI-generated** using Machine Learning.
The system allows users to record audio directly from their microphone or upload a voice sample and get real-time predictions.

---

## 🚀 Project Overview

With the rapid growth of AI-generated voices and deepfake audio, identifying synthetic speech has become important for security and authenticity. This project demonstrates a practical implementation of voice classification using audio feature extraction and machine learning.

The application consists of:

* 🎧 Modern Web UI for recording/uploading voice
* ⚡ FastAPI backend for prediction
* 🧠 Machine Learning model for classification
* 🔊 Audio feature extraction using MFCC
* ☁️ Deployment-ready architecture (Render)

---

## 🧠 Features

✅ Record voice directly using microphone
✅ Upload audio file for prediction
✅ Detect AI-generated vs Human voice
✅ FastAPI REST API backend
✅ Modern responsive UI
✅ Real-time prediction response
✅ Easy deployment on cloud platforms

---

## 🛠️ Tech Stack

### 👨‍💻 Backend

* FastAPI
* Python
* Uvicorn

### 🤖 Machine Learning

* Scikit-learn
* Librosa
* NumPy
* Pandas

### 🎨 Frontend

* HTML
* CSS
* JavaScript

### 🧰 Tools

* Git & GitHub
* VS Code
* Render (Deployment)

---

## 📂 Project Structure

```
AI-vs-Human-Voice-Detection/
│
├── app/
│   └── main.py
│
├── scripts/
│   └── predict.py
│
├── static/
│   ├── index.html
│
├── model/
│   └── model.pkl
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📸 Output Screenshots

### 🎤 Voice Recording Interface

![Output](screenshot/output%20screenshot.png)

### ✅ Prediction Result

![Output](screenshot/output%20screenshot1.png)

## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/AI-vs-Human-Voice-Detection.git
cd AI-vs-Human-Voice-Detection
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

Open browser:

```
http://127.0.0.1:8000
```

---

## ☁️ Deployment (Render)

1. Push project to GitHub
2. Create new Web Service in Render
3. Connect GitHub repository
4. Add Build Command:

```
pip install -r requirements.txt
```

5. Start Command:

```
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

6. Deploy 🎉

---

## 📈 Future Improvements

* Improve model accuracy with larger datasets
* Real-time streaming prediction
* Deepfake detection enhancement
* User authentication
* Model confidence visualization

---

## 👩‍💻 Author

**Vikneshwari Raju**
B.E Computer Science & Engineering
AI & Full Stack Development Enthusiast

📧 [vikneshwariraju@gmail.com](mailto:vikneshwariraju@gmail.com)
🌐 [Portfolio](https://vikneshwariraju.github.io/vikneshwari/) 
🔗 [LinkedIn](https://www.linkedin.com/in/vikneshwariraju/) 

---

⭐ If you like this project, consider giving it a star on GitHub! And suggestions are always welcome  

