# Python-Zero-to-Hero
Learn Python from zero to hero. Interactive lessons, live code editor, AI tutor &amp; XP system. Runs locally in your browser.


Learn Python from absolute beginner to confident developer — interactively, locally, and at your own pace.


## What is this?

Python Zero to Hero is a locally-hosted learning app that teaches you Python through 15 hands-on lessons. Every lesson has a theory section, a real coding challenge, and a built-in AI tutor you can ask anything. You write code, run it instantly, and earn XP as you progress.

No accounts. No subscriptions. Runs entirely on your own machine.



## Features

- **15 structured lessons** covering everything from Hello World to OOP and File I/O
- **Live code editor** with Python syntax highlighting powered by CodeMirror
- **Run code instantly** — press Ctrl+Enter and see output in real time
- **AI Tutor** — ask questions about the lesson or your own code, powered by Claude
- **XP system** — earn points as you complete lessons and track your progress
- **Hints** — available on every challenge when you're stuck
- **Clean dark UI** — designed to feel like a real developer environment

---

## Quick Start

### Requirements
- Python 3.8 or higher
- pip

### Install & Run

```bash
git clone https://github.com/JOUW-USERNAME/python-zero-to-hero.git
cd python-tutor
pip install -r requirements.txt
python app.py
```

Then open your browser and go to **http://localhost:5000**

That's it. No config needed.

---

## Curriculum — 15 Lessons, 1825 XP

| # | Lesson | Category | XP |
|---|--------|----------|----|
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

---

## How It Works

Each lesson is split into three sections:

**📖 Theory** — A clear explanation of the concept with examples you can load directly into the editor.

**🎯 Challenge** — A coding task you have to solve yourself. A hint is available if you need it. Mark it complete to earn your XP.

**🤖 AI Tutor** — A chat interface connected to Claude. Ask it why your code isn't working, what a concept means, or how to approach the challenge. It sees your current code and the lesson context.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python + Flask |
| Frontend | HTML, CSS, JavaScript |
| Code Editor | CodeMirror 5 |
| AI Tutor | Anthropic Claude API |
| Code Execution | Sandboxed subprocess (5s timeout) |

---

## AI Tutor Note

The AI tutor uses the Anthropic Claude API. The app works fine without it — the tutor tab will simply show an error if no API key is configured on the server side. If you want to enable it, add your Anthropic API key to the environment before starting:

```bash
export ANTHROPIC_API_KEY=your_key_here
python app.py
```

---

## Contributing

Pull requests are welcome. Ideas for contributions:

- Add more lessons (recursion, generators, decorators, async)
- Add a quiz/multiple choice mode
- Add a leaderboard or user profiles
- Improve the AI tutor prompt
- Add dark/light theme toggle

---

## License

MIT — free to use, modify, and share.
