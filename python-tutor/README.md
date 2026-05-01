# 🐍 Python Zero to Hero

A professional, locally-hosted Python learning app with AI tutor, live code editor and gamification.

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the app
```bash
python app.py
```

### 3. Open in browser
http://localhost:5000

---

## 🎓 What's inside?

**15 Lessons — From beginner to advanced:**

| # | Topic | Category | XP |
|---|-------|----------|----|
| 1 | Hello World | Basics | 50 |
| 2 | Variables | Basics | 75 |
| 3 | Strings | Basics | 75 |
| 4 | Numbers & Math | Basics | 75 |
| 5 | If / Else | Control Flow | 100 |
| 6 | For Loops | Control Flow | 100 |
| 7 | While Loops | Control Flow | 100 |
| 8 | Lists | Data Structures | 125 |
| 9 | Dictionaries | Data Structures | 125 |
| 10 | Functions | Functions | 150 |
| 11 | Classes & OOP | OOP | 200 |
| 12 | File I/O | Advanced | 175 |
| 13 | Error Handling | Advanced | 175 |
| 14 | List Comprehensions | Advanced | 150 |
| 15 | Modules & Imports | Advanced | 150 |

**Total: 1,825 XP to earn**

---

## ✨ Features

- **Live Code Editor** with syntax highlighting (CodeMirror)
- **Instant code execution** in a secure sandbox
- **AI Tutor** — ask questions about any lesson (via Claude API)
- **XP System** — earn points for every completed lesson
- **Progress tracking** — saved across sessions
- **Hints** — available whenever you're stuck
- **Example code** — load directly into the editor

---

## 🔧 Tech Stack

- **Backend**: Python + Flask
- **Frontend**: Vanilla HTML/CSS/JS + CodeMirror
- **AI**: Claude claude-sonnet-4 via Anthropic API
- **Code sandbox**: subprocess with timeout protection
