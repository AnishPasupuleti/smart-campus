
# Smart Campus 🏫📲

**Smart Campus** is a web application designed to streamline campus operations using smart technologies like QR-based attendance, facial verification, and location validation. Built with Flask and OpenCV, it offers a role-based system for students, teachers, and administrators.

## 🚀 Features

- ✅ QR Code-based attendance
- 📷 Facial recognition for identity verification
- 📍 GPS-based location check (within 50m of teacher)
- 👨‍🏫 Teacher dashboard with class control
- 👩‍🎓 Student panel to view attendance and mark presence
- 🛠 Admin portal to manage users and review issues

## 🛠 Tech Stack

- **Python**
- **Flask**
- **OpenCV** (Face detection)
- **HTML/CSS (Jinja Templates)**
- **Geolocation APIs**
- **QR Code Generator**

## 🧪 Setup Instructions

```bash
git clone https://github.com/AnishPasupuleti/smart-campus.git
cd smart-campus
pip install -r requirements.txt
python app.py
```

Open your browser and visit `http://localhost:5000/`

## 👥 User Roles

- **Student**: Scans QR, verifies face, and checks attendance
- **Teacher**: Starts class, generates QR, monitors attendance
- **Admin**: Views all users, manages issues, updates statuses

## 📁 Folder Structure

```
├── app.py                     # Main Flask app
├── static/                    # Static files (CSS, JS)
├── templates/                 # HTML pages
│   ├── login.html
│   ├── dashboard.html
│   └── admin_panel.html
├── data/                      # JSON/DB for users, attendance
├── requirements.txt
```

## 🔮 Future Enhancements

- Enable live face tracking with better models
- Add notification system for issue status updates
- Support offline sync mode for classrooms without Wi-Fi

## 📜 License

MIT License — use, modify, and deploy freely with credit.

---

> Developed by [Anish Pasupuleti](https://github.com/AnishPasupuleti)
