# 🏦 Django Bank Management System

A full-stack Django-based Bank Management System that allows customers to securely transfer money, view transaction history, and admins to manage users — built with modern design and role-based access.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![Status](https://img.shields.io/badge/Live%20App-Deployed-success)
![License](https://img.shields.io/badge/License-MIT-informational)

---

## 🚀 Live Demo
🌐 [https://yourusername.pythonanywhere.com](https://yourusername.pythonanywhere.com)  

---

## 📸 Screenshots

<img width="1920" height="1080" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/f213c631-480b-40a3-b971-1a9d1a59c076" />
> <img width="1920" height="1080" alt="Screenshot (16)" src="https://github.com/user-attachments/assets/c27d4b09-4bfb-4ce0-a35b-34dc74cbd0f2" />
<img width="1920" height="1080" alt="Screenshot (17)" src="https://github.com/user-attachments/assets/deb20315-068f-4b6b-b9b2-11c61dee0300" />
<img width="1920" height="1080" alt="Screenshot (18)" src="https://github.com/user-attachments/assets/d2b78adc-6fa1-4f89-a880-dc9ff8ed2c3f" />
<img width="1920" height="1080" alt="Screenshot (19)" src="https://github.com/user-attachments/assets/f9bcabdb-1cef-4f51-adf5-62751029ec52" />
<img width="1920" height="1080" alt="Screenshot (20)" src="https://github.com/user-attachments/assets/c9bcc522-6869-4075-a78f-1475e6c9cfa3" />
<img width="1920" height="1080" alt="Screenshot (21)" src="https://github.com/user-attachments/assets/7c627c96-3c58-4ee9-a132-98826bb103cc" />


---

## ✨ Features

### ✅ Core Features
- 🔐 User Authentication (Register / Login / Logout)
- 👤 Admin vs User Role-Based Access Control
- 👥 Customer Management (CRUD)
- 💸 Secure Fund Transfers Between Customers
- 📜 Transaction History Logs
- 📄 PDF Export of Transaction History
- 📊 Dashboard with Chart.js Visualizations
- 🔍 Search & Filter for Transactions
- ⚙️ Responsive Bootstrap 5 UI

---

## 🛠 Tech Stack

- **Backend:** Django, SQLite
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database:** SQLite3 (can upgrade to PostgreSQL)
- **Charts:** Chart.js
- **PDF Generation:** xhtml2pdf

---

## 📁 Folder Structure

```bash
├── bank_pro/              # Django Project Folder
│   ├── settings.py
│   └── urls.py
├── bank_app/              # Main App
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│   └── urls.py
├── templates/             # Base Templates
├── staticfiles/           # Collected Static Files
├── db.sqlite3             # Default Database
├── requirements.txt
├── render.yaml            # Render Deployment Config
├── Procfile               # Gunicorn Entry Point
└── README.md
