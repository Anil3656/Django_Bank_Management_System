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

> _Add screenshots in `/screenshots` folder and embed below if needed_

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
