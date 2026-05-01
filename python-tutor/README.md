# 🐍 Python Zero to Hero — Interactieve Cursus

Een professionele, lokale Python-leerapplicatie met AI-tutor, live code editor en gamificatie.

## 🚀 Snelstart

### 1. Installeer dependencies
```bash
pip install -r requirements.txt
```

### 2. Start de app
```bash
python app.py
```

### 3. Open in browser
```
http://localhost:5000
```

---

## 🎓 Wat zit er in?

**15 Lessen — Van beginner tot gevorderd:**

| # | Onderwerp | Categorie | XP |
|---|-----------|-----------|-----|
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

**Totaal: 1.825 XP te verdienen**

---

## ✨ Features

- **Live Code Editor** met syntax highlighting (CodeMirror)
- **Directe code uitvoering** in een veilige sandbox
- **AI Tutor** — stel vragen over elke les (via Claude API)
- **XP Systeem** — verdien punten bij elke voltooide les
- **Progressie tracking** — bijgehouden via sessie
- **Hints** — als je vastzit
- **Voorbeeldcode** — laad direct in de editor

---

## 🔧 Technische Details

- **Backend**: Python + Flask
- **Frontend**: Vanilla HTML/CSS/JS + CodeMirror
- **AI**: Claude claude-sonnet-4-20250514 via Anthropic API
- **Code sandbox**: subprocess met timeout-beveiliging
