# 📸 SnapRoll

### *AI-powered attendance, without the roll call*

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)

**SnapRoll** is an AI-powered attendance management system that replaces manual roll calls with **face recognition** and **voice verification**, giving teachers a fast, tamper-resistant way to mark attendance and giving students a self-serve way to check in.

[🐛 Report Bug](https://github.com/Vaibhav1o1/snaproll-ai-powered-attendance-system/issues) · [✨ Request Feature](https://github.com/Vaibhav1o1/snaproll-ai-powered-attendance-system/issues)

---

## 📋 Table of Contents

- [The Problem](#-the-problem)
- [Our Solution](#-our-solution)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup & Installation](#️-setup--installation)
- [Environment Variables](#-environment-variables)
- [User Roles & Access](#-user-roles--access)
- [How It Works](#-how-it-works)
- [Future Scope](#-future-scope)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚨 The Problem

Manual classroom attendance is slow, easy to game, and eats into teaching time:

- 🙋 **Proxy attendance** — students mark friends present who aren't in the room
- ⏱️ **Wasted class time** — calling out names or passing a sheet takes minutes every session
- 📝 **Paper trails** — attendance registers are hard to search, back up, or analyze
- 🔐 **No verification layer** — traditional systems trust whoever holds the pen (or the login)

## 💡 Our Solution

SnapRoll gives teachers and students a **Streamlit-based portal** where attendance is captured biometrically instead of manually:

| Role | What They Can Do |
|---|---|
| 👩‍🏫 **Teachers** | Create subjects, enroll students, run face/voice attendance sessions, view history |
| 🧑‍🎓 **Students** | Join subjects via a code, enroll their face, mark attendance via voice |

> No more passing a sheet around. No more "I was here, I swear."

---

## ✨ Features

### 🔐 Authentication
- Secure teacher login with **bcrypt password hashing**
- Session-based role routing (`teacher` / `student` / guest home screen)

### 🧑‍🏫 Subject & Class Management
- Teachers create subjects and generate shareable **join codes / QR codes** (via `segno`)
- Students join a subject instantly using the join code — no manual roster entry

### 📷 Face Recognition Attendance
- Face enrollment and detection powered by **dlib** + **face_recognition_models**
- Encodes and matches faces against enrolled student embeddings using **OpenCV**
- Bulk/auto-enroll flow for adding multiple student photos at once

### 🎙️ Voice Verification
- Voice embeddings generated with **Resemblyzer** and **Librosa**
- Adds a second biometric factor on top of face recognition to reduce spoofing

### 📊 Attendance Records
- Attendance results stored and queried via **Supabase (PostgreSQL)**
- Dialog-based UI for reviewing attendance results per session

### 🎨 UI/UX
- Clean, dialog-driven Streamlit interface (add photos, enroll, share subject, view results)
- Reusable header/footer/subject-card components for a consistent look across screens

---

## 🏗 Architecture

```
┌───────────────────────────────────────────────────────────┐
│                      CLIENT / UI LAYER                    │
│                  Streamlit (app.py, screens)               │
│      Home Screen · Teacher Screen · Student Screen          │
└───────────────────────┬───────────────────────────────────┘
                         │
                         ▼
┌───────────────────────────────────────────────────────────┐
│                    AI PIPELINE LAYER                       │
│   face_pipeline.py           voice_pipeline.py              │
│   dlib + OpenCV                Resemblyzer + Librosa        │
│   (face detection & match)     (voice embedding & match)    │
└───────────────────────┬───────────────────────────────────┘
                         │
                         ▼
┌───────────────────────────────────────────────────────────┐
│                       DATA LAYER                           │
│                 Supabase (PostgreSQL)                      │
│      teachers · students · subjects · attendance            │
└───────────────────────────────────────────────────────────┘
```

**Flow:**
1. Teacher logs in and creates a subject, generating a join code / QR
2. Student joins the subject and enrolls their face (and optionally voice)
3. During a session, the teacher (or student) triggers a face/voice capture
4. The captured biometric is embedded and matched against enrolled records
5. A match is written back to Supabase as an attendance entry

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend/UI | Streamlit | Web interface, no separate frontend build needed |
| Face Recognition | dlib, OpenCV, face_recognition_models | Face detection & embedding matching |
| Voice Recognition | Resemblyzer, Librosa | Voice embedding & verification |
| Data Handling | NumPy, Pandas, scikit-learn | Numerical processing & embedding comparison |
| Auth | bcrypt | Password hashing for teacher accounts |
| QR/Join Codes | segno, Pillow | Generating shareable subject join codes |
| Database | Supabase (PostgreSQL) | Users, subjects, attendance storage |
| Language | Python | Core application logic |

---

## 📁 Project Structure

```
snaproll-ai-powered-attendance-system/
├── assets/
│   └── SnapRoll_Logo.ico
│
├── src/
│   ├── components/               # Reusable UI dialogs & widgets
│   │   ├── dialog_add_photos.py
│   │   ├── dialog_attendance_result.py
│   │   ├── dialog_auto_enroll.py
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_share_subject.py
│   │   ├── dialog_voice_attendance.py
│   │   ├── footer.py
│   │   ├── header.py
│   │   └── subject_card.py
│   │
│   ├── database/
│   │   ├── config.py              # Supabase client setup
│   │   └── db.py                  # DB queries (auth, subjects, attendance)
│   │
│   ├── pipelines/
│   │   ├── face_pipeline.py       # Face detection & embedding logic
│   │   └── voice_pipeline.py      # Voice embedding & verification logic
│   │
│   ├── screens/
│   │   ├── home_screen.py
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   │
│   └── ui/
│       └── base_layout.py
│
├── app.py                         # Streamlit entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites

- [Python](https://www.python.org/) 3.10+
- [Git](https://git-scm.com/)
- A [Supabase](https://supabase.com/) project (free tier works)
- `cmake` and build tools installed (required by `dlib`)

---

### 1. Clone the Repository

```bash
git clone https://github.com/Vaibhav1o1/snaproll-ai-powered-attendance-system.git
cd snaproll-ai-powered-attendance-system
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ `dlib-bin` and `face_recognition_models` can take a few minutes to build/download. Make sure you have a stable internet connection and, on Windows, the Visual C++ Build Tools installed.

---

### 4. Configure the Database

1. Create a project at [supabase.com](https://supabase.com)
2. Set up tables for `teachers`, `students`, `subjects`, and `attendance` in the **Table Editor** / **SQL Editor**
3. Copy your project URL and API key for the next step

---

### 5. Run the App

```bash
streamlit run app.py
```

The app will be live at `http://localhost:8501`.

---

## 🔑 Environment Variables

Create a `.env` file (or configure `src/database/config.py`) with your Supabase credentials:

```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_api_key
```

> ⚠️ **Never commit your `.env` file to GitHub.** Add it to `.gitignore` before your first push.

---

## 👤 User Roles & Access

| Role | Entry Point | Key Capabilities |
|---|---|---|
| Teacher | Login via home screen | Create subjects, enroll/manage students, run attendance sessions, view results |
| Student | Join via subject code / QR | Enroll face & voice, mark attendance, view own attendance history |

---

## 🧠 How It Works

1. **Enrollment** — A student's face (and voice, optionally) is captured and converted into a numeric embedding.
2. **Storage** — Embeddings are stored against the student's record in Supabase.
3. **Verification** — On attendance day, a new capture is embedded and compared against stored embeddings using distance/similarity matching.
4. **Marking** — A close-enough match automatically marks that student present for the session.

---

## 🔭 Future Scope

- 📱 **Mobile-friendly capture flow** for face/voice check-in from a phone
- 📊 **Analytics dashboard** — attendance trends, defaulter lists, per-subject reports
- 🔔 **Notifications** — email/SMS alerts for low attendance
- 🌐 **Multi-language UI** support
- 🧪 **Liveness detection** to further reduce spoofing (photo/video replay attacks)
- ☁️ **Cloud deployment guide** (Streamlit Community Cloud / Render)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

**Built with ❤️ to make attendance one less thing to worry about.**

⭐ If you found this project useful, consider giving it a star!
