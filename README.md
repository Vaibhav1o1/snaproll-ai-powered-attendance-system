<div align="center">

# 🎯 SnapRoll

### _One photo. One voice clip. Zero roll calls._

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
[![OpenCV](https://img.shields.io/badge/dlib-CC2927?style=for-the-badge&logo=opencv&logoColor=white)](http://dlib.net/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

[![Deployed on Streamlit](https://img.shields.io/badge/Live-snaproll.streamlit.app-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://snaproll.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)]()

<br/>

**SnapRoll** is an AI-powered classroom attendance system that recognizes students by **face and voice** — swapping out manual roll calls for a single classroom photo or audio clip, verified in seconds.

[🚀 Live Demo](https://snaproll.streamlit.app) · [📖 Setup Guide](#setup--installation) · [🐛 Report Bug](https://github.com/Vaibhav1o1/snaproll-ai-powered-attendance-system/issues)

<br/>

</div>

---

## 📋 Table of Contents

- [The Problem](#-the-problem)
- [Our Solution](#-our-solution)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup & Installation](#setup--installation)
- [Environment Variables](#-environment-variables)
- [User Roles & Access](#-user-roles--access)
- [How It Works](#-how-it-works)
- [Future Scope](#-future-scope)
- [Contributors](#-contributors)

---

## 🚨 The Problem

Manual attendance in classrooms is slow, easy to game, and hard to audit:

- 📢 **Roll calls waste class time** — calling out names one by one eats into every session
- ✍️ **Proxy attendance is common** — students can answer for absent classmates
- 📉 **No usable records** — attendance data lives in registers or scattered spreadsheets, never analyzed
- 🔁 **Repetitive teacher effort** — the same manual process repeats for every class, every subject, every day

---

## 💡 Our Solution

SnapRoll turns attendance into a **single photo or audio clip**, verified by AI:

| Role | What They Can Do |
|---|---|
| 👩‍🏫 **Teachers** | Create subjects, take AI-based attendance (face or voice), track records |
| 🎓 **Students** | Log in with Face ID, self-enroll into subjects via link/QR code, view attendance history |

> One classroom photo. One AI scan. Attendance done — no calling names, no registers.

---

## ✨ Features

### 🔐 Authentication
- **Face ID login for students** — no passwords, just look at the camera
- **Username + password login for teachers**, with bcrypt-hashed credentials
- Session-based role routing (`teacher` / `student` / guest home screen)

### 🤳 Face Recognition Attendance
- Upload one or more classroom photos
- `dlib` HOG face detector + 128-d face embeddings per student
- An `SVM` classifier (scikit-learn) trained on enrolled students' embeddings identifies everyone in the frame in one pass
- Automatically cross-checks detected faces against the subject's enrolled roster and marks Present/Absent

### 🎙️ Voice Recognition Attendance
- Record a single classroom audio clip of students saying a short phrase
- `librosa` splits the clip into per-speaker segments; `Resemblyzer` generates 256-d voice embeddings
- Each segment is matched against enrolled students' voice profiles via cosine similarity, with a configurable confidence threshold

### 📚 Subject & Enrollment Management
- Teachers create subjects with a unique subject code and section
- **Shareable join links + auto-generated QR codes** (via `segno`) let students self-enroll instantly
- Students can browse, join, and unenroll from subjects from their own dashboard

### 📊 Attendance Records
- Per-subject and per-student attendance history
- Aggregated present/total counts per session, timestamped and grouped
- Clean tabular views for both teachers (class-wide) and students (personal)

### 🎨 UI/UX
- Fully interactive **Streamlit** web interface — no separate frontend/backend to run
- Role-aware dashboards (Teacher vs. Student) with tabbed navigation
- Live camera and microphone capture built directly into the browser

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     STREAMLIT APPLICATION                   │
│         (Home Screen → Teacher Screen / Student Screen)     │
│      camera_input · audio_input · session_state routing     │
└───────────────────────┬──────────────────────────────────────
                        │
                        ▼
┌────────────────────────────────────────────────────────────────
│                       AI PIPELINE LAYER                       │
│                                                               │
│   Face Pipeline                    Voice Pipeline             │
│   dlib detector + shape predictor  librosa segmentation       │
│   128-d face embeddings            Resemblyzer 256-d embeds   │
│   SVM classifier (scikit-learn)    Cosine similarity matching │
└───────────────────────┬───────────────────────────────────────┘
                        │ Supabase Client
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                        DATA LAYER                           │
│                  Supabase (PostgreSQL)                      │
│   teachers · students · subjects · subject_students ·       │
│   attendance                                                │
└─────────────────────────────────────────────────────────────┘
```

**Data Flow:**
1. A teacher captures a classroom photo (or audio clip) inside the Streamlit UI
2. The relevant pipeline (face or voice) extracts embeddings and matches them against the subject's enrolled students
3. Results are shown as an editable Present/Absent table before being logged
4. Confirmed records are written to Supabase and immediately reflected in both teacher and student dashboards

---

## 🛠 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| App Framework | Streamlit | Full web UI — no separate frontend needed |
| Face Recognition | dlib, face_recognition_models | Face detection + 128-d embeddings |
| Face Classification | scikit-learn (SVM) | Matching detected faces to enrolled students |
| Voice Recognition | Resemblyzer, librosa | Speaker segmentation + 256-d voice embeddings |
| QR Codes | segno | Auto-generated join codes for subjects |
| Auth | bcrypt | Password hashing for teacher accounts |
| Database | Supabase (PostgreSQL) | Students, teachers, subjects, attendance records |
| Data Handling | pandas, numpy | Attendance aggregation and tabular display |
| Language | Python 3.10+ | Core application logic |

---

## 📁 Project Structure

```
snaproll-ai-powered-attendance-system/
├── src/
│   ├── components/                    # Reusable Streamlit UI pieces
│   │   ├── header.py
│   │   ├── footer.py
│   │   ├── subject_card.py
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_auto_enroll.py      # QR/link-based quick enrollment
│   │   ├── dialog_add_photos.py
│   │   ├── dialog_share_subject.py    # QR code + join link generation
│   │   ├── dialog_voice_attendance.py
│   │   └── dialog_attendance_result.py
│   │
│   ├── database/
│   │   ├── config.py                  # Supabase client setup
│   │   └── db.py                      # All CRUD queries (students, teachers, subjects, attendance)
│   │
│   ├── pipelines/
│   │   ├── face_pipeline.py           # dlib embeddings + SVM classifier
│   │   └── voice_pipeline.py          # Resemblyzer embeddings + speaker matching
│   │
│   ├── screens/
│   │   ├── home_screen.py             # Landing / role selection
│   │   ├── teacher_screen.py          # Teacher login, dashboard, attendance, records
│   │   └── student_screen.py          # Face ID login, registration, subject dashboard
│   │
│   └── ui/
│       └── base_layout.py             # Shared page styling
│
├── assets/
│   └── SnapRoll_Logo.ico
│
├── app.py                             # Entry point + routing
├── requirements.txt
└── README.md
```

---

<a id="setup--installation"></a>

## ⚙️ Setup & Installation

> 💡 Want to try it first without installing anything? Head to the live app: **[snaproll.streamlit.app](https://snaproll.streamlit.app)**

### Prerequisites

- [Python](https://www.python.org/) 3.10+
- [Git](https://git-scm.com/)
- A [Supabase](https://supabase.com/) project (free tier works)
- A working microphone and webcam for live attendance capture

---

### 1. Clone the Repository

```bash
git clone https://github.com/Vaibhav1o1/snaproll-ai-powered-attendance-system.git
cd snaproll-ai-powered-attendance-system
```

---

### 2. Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

> ⚠️ `dlib-bin` and `face_recognition_models` are heavier packages — installation can take a few minutes.

---

### 3. Database Setup

1. Create a project at [supabase.com](https://supabase.com)
2. In the **Table Editor**, create the following tables: `teachers`, `students`, `subjects`, `subject_students`, `attendance`
3. Note down your **Project URL** and **API Key** from Project Settings → API

---

### 4. Run the App

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_api_key
```

> ⚠️ **Never commit your `.env` file to GitHub.** It's already listed in `.gitignore`.

---

## 👤 User Roles & Access

| Role | Login Method | Key Capabilities |
|---|---|---|
| **Teacher** | Username + password | Create subjects, run face/voice attendance, view attendance records |
| **Student** | Face ID (camera) | Self-enroll via link/QR, view personal attendance history |

---

## 🔍 How It Works

**Taking Attendance by Face:**
1. Teacher selects a subject and uploads one or more classroom photos
2. Each photo is scanned for faces, and embeddings are matched against the subject's enrolled students
3. A results table shows Present/Absent status with the source photo for each match
4. Teacher confirms, and the records are logged to Supabase

**Taking Attendance by Voice:**
1. Teacher records a single classroom audio clip
2. The clip is auto-segmented into individual speaker turns
3. Each segment is matched against enrolled students' voice profiles
4. Matches above the similarity threshold are marked Present

**Student Onboarding:**
1. New student scans their face on the login screen — if unrecognized, a quick registration form appears
2. Registration requires both a face capture and a short voice recording, creating dual biometric profiles
3. Once registered, students log in with just their face going forward

---

## 🔭 Future Scope

- 📱 **Mobile-friendly capture flow** for teachers taking attendance from their phones
- 📈 **Analytics dashboard** — attendance trends, defaulter lists, subject-wise insights
- 🔔 **Low-attendance alerts** for students and teachers
- 🌐 **Multi-classroom / multi-institution support**
- 🧠 **Improved low-light and multi-angle face recognition**
- 🗣️ **Noise-robust voice matching** for larger classrooms

---

## 🤝 Contributors

| Name | GitHub |
|------|--------|
| Vaibhav Gupta | [Vaibhav1o1](https://github.com/Vaibhav1o1) |

---

<div align="center">

**Built with ❤️ to make attendance effortless**

⭐ If you found this project interesting, consider giving it a star!

</div>
