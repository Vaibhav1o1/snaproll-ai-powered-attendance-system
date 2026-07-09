<div align="center">

# 📸 SnapRoll

### _An Intelligent AI-Powered Attendance Management System_

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)

[![Deployed on Streamlit](https://img.shields.io/badge/Deployed-Streamlit_Cloud-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://snaproll.streamlit.app)
[![Database](https://img.shields.io/badge/Database-Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)](https://supabase.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

<br/>

**SnapRoll** is a modern attendance tracking platform that eliminates manual roll calls by utilizing dual-layer biometric verification (Face ID and Voice Recognition) to create a seamless experience for educators and students.

[🚀 Live Demo](https://snaproll.streamlit.app) · [📖 Setup Guide](#️-setup--installation) · [🐛 Report Bug](https://github.com/Vaibhav1o1/snaproll-ai-powered-attendance-system/issues)

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
- [Setup & Installation](#️-setup--installation)
- [Environment Variables](#-environment-variables)
- [User Roles & Access](#-user-roles--access)
- [Screenshots](#-screenshots)
- [Deployment](#-deployment)
- [Future Scope](#-future-scope)
- [Contributors](#-contributors)

---

## 🚨 The Problem

Traditional educational environments face several challenges with daily attendance tracking:

- ⏱️ **Time Consuming:** Manual roll calls eat into valuable lecture time, especially in large classes.
- 🧑‍🤝‍🧑 **Proxy Attendance:** Paper registers and simple digital clicks are easily manipulated by students covering for absent peers.
- 📉 **Data Management:** Teachers struggle to compile, manage, and analyze attendance records across multiple subjects without tedious spreadsheet work.
- 🖥️ **Poor UX:** Existing digital solutions often have outdated, clunky interfaces that are frustrating for both students and faculty to navigate.

---

## 💡 Our Solution

SnapRoll replaces outdated roll calls with a **unified biometric intelligence platform**. 

| Role | What They Can Do |
|---|---|
| 👨‍🏫 **Teachers** | Create subjects, generate enrollment QR codes, and trigger AI attendance scans |
| 🎓 **Students** | Quick-enroll via links, and log attendance simply by showing their face and speaking |

> No more proxy attendance. No more wasted lecture time. 

---

## ✨ Features

### 🔐 Dual-Layer Biometric Authentication
- **Face Recognition:** High-accuracy facial mapping using `face_recognition` and OpenCV.
- **Voice Verification:** Secondary audio-based identity confirmation using Speech Recognition.

### 👥 User Roles & Workflows
- **Teacher Portal** — Create new classes, share join links, manage enrolled students, and view detailed attendance analytics.
- **Student Portal** — Manage enrolled subjects, view personal attendance percentages, and authenticate securely.

### ⚡ Smart Interactions
- **QR Code Enrollment** — Teachers generate unique QR codes for instant student onboarding.
- **Interactive Modals** — Clean, modern overlay screens for confirmations and data review without page reloads.

### 🎨 UI/UX Excellence
- Custom CSS injected Streamlit interface that breaks the standard "dashboard" mold.
- Smooth state transitions via `st.session_state` for a Single Page Application (SPA) feel.
- Keyboard shortcuts (e.g., `⌘ + Backspace` to logout) for power users.

---

## 🏗 Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                       CLIENT LAYER                          │
│               Streamlit + Custom CSS Injection              │
│       (Session State Routing · Multi-Step Workflows)        │
└───────────────────────┬─────────────────────────────────────┘
                        │ API & Media Streams
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                       PROCESSING LAYER                      │
│                       Python Backend                        │
│                                                             │
│   [ OpenCV / face_recognition ]      [ SpeechRecognition ]  │
│        (Visual Encoding)              (Audio Processing)    │
└───────────────────────┬─────────────────────────────────────┘
                        │ Supabase Python Client
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                       DATA LAYER                            │
│                 Supabase (PostgreSQL)                       │
│      users · subjects · enrollments · attendance_logs       │
└─────────────────────────────────────────────────────────────┘
