from flask import Flask, render_template, request, jsonify, session
import subprocess
import sys
import json
import os
import tempfile
import requests
import re

app = Flask(__name__)
app.secret_key = os.urandom(24)

CURRICULUM = [
    {
        "id": 1, "title": "Hello World", "category": "Basics",
        "icon": "🐍", "xp": 50,
        "theory": """Python is one of the most popular programming languages in the world. It's known for its clean, readable syntax.

Your first Python program is traditionally printing "Hello, World!" to the screen.

The `print()` function displays text (or other values) in the terminal. Text must be wrapped in quotes — either single `'` or double `"` quotes.""",
        "example": 'print("Hello, World!")',
        "challenge": "Write a program that prints your own name.",
        "hint": 'Use print() with your name inside quotes: print("Your Name")',
        "test_keyword": "print",
        "expected_contains": None
    },
    {
        "id": 2, "title": "Variables", "category": "Basics",
        "icon": "📦", "xp": 75,
        "theory": """Variables are containers that store data values. In Python, you create a variable simply by assigning a value to it — no need to declare a type first.

```
name = "Alice"
age = 25
height = 1.75
```

Python automatically figures out the **type** of data:
- `str` — text (strings)
- `int` — whole numbers
- `float` — decimal numbers
- `bool` — True or False""",
        "example": 'name = "Alice"\nage = 25\nprint(name)\nprint(age)',
        "challenge": "Create a variable called `city` with your city name, and a variable `year` with the current year. Print both.",
        "hint": 'city = "Amsterdam"\nyear = 2024\nprint(city)\nprint(year)',
        "test_keyword": "city",
        "expected_contains": None
    },
    {
        "id": 3, "title": "Strings", "category": "Basics",
        "icon": "💬", "xp": 75,
        "theory": """Strings are sequences of characters. You can do many powerful things with them:

**Concatenation** (joining strings):
```
first = "Hello"
second = "World"
result = first + " " + second
```

**f-strings** (modern way to format):
```
name = "Alice"
print(f"Hello, {name}!")
```

**String methods**:
- `.upper()` — converts to uppercase
- `.lower()` — converts to lowercase  
- `.len()` — use `len(string)` for length""",
        "example": 'name = "python"\nprint(name.upper())\nprint(f"I love {name}!")\nprint(len(name))',
        "challenge": "Create a variable `language` with value \"python\". Print it in uppercase, then print an f-string saying 'I am learning Python!'",
        "hint": 'language = "python"\nprint(language.upper())\nprint(f"I am learning {language.title()}!")',
        "test_keyword": "upper",
        "expected_contains": None
    },
    {
        "id": 4, "title": "Numbers & Math", "category": "Basics",
        "icon": "🔢", "xp": 75,
        "theory": """Python can do all kinds of math operations:

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Addition | `5 + 3 = 8` |
| `-` | Subtraction | `5 - 3 = 2` |
| `*` | Multiplication | `5 * 3 = 15` |
| `/` | Division | `10 / 3 = 3.33` |
| `//` | Floor division | `10 // 3 = 3` |
| `%` | Modulo (remainder) | `10 % 3 = 1` |
| `**` | Power | `2 ** 3 = 8` |""",
        "example": 'x = 10\ny = 3\nprint(x + y)\nprint(x ** y)\nprint(x % y)',
        "challenge": "Calculate and print: the area of a rectangle with width=8 and height=5, and check if 17 is odd using modulo.",
        "hint": 'width = 8\nheight = 5\narea = width * height\nprint(area)\nprint(17 % 2)',
        "test_keyword": "print",
        "expected_contains": None
    },
    {
        "id": 5, "title": "If / Else", "category": "Control Flow",
        "icon": "🔀", "xp": 100,
        "theory": """Conditional statements let your program make decisions.

```python
if condition:
    # runs when True
elif other_condition:
    # runs when first is False but this is True
else:
    # runs when all above are False
```

**Comparison operators**:
- `==` equal to
- `!=` not equal
- `>` greater than
- `<` less than
- `>=` greater or equal
- `<=` less or equal

⚠️ Indentation (4 spaces) is **mandatory** in Python!""",
        "example": 'age = 20\nif age >= 18:\n    print("Adult")\nelse:\n    print("Minor")',
        "challenge": "Write a program that checks a `score` variable (set it to any number). Print 'Excellent!' if >= 90, 'Good' if >= 70, otherwise 'Keep practicing!'",
        "hint": 'score = 85\nif score >= 90:\n    print("Excellent!")\nelif score >= 70:\n    print("Good")\nelse:\n    print("Keep practicing!")',
        "test_keyword": "if",
        "expected_contains": None
    },
    {
        "id": 6, "title": "For Loops", "category": "Control Flow",
        "icon": "🔁", "xp": 100,
        "theory": """Loops allow you to repeat code. The `for` loop iterates over a sequence.

**Loop over a list**:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Loop with range()**:
```python
for i in range(5):     # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)
```

`range(start, stop, step)` — step defaults to 1""",
        "example": 'for i in range(1, 6):\n    print(f"{i} x 2 = {i * 2}")',
        "challenge": "Use a for loop to print all even numbers from 2 to 20 (inclusive).",
        "hint": 'for i in range(2, 21, 2):\n    print(i)',
        "test_keyword": "for",
        "expected_contains": None
    },
    {
        "id": 7, "title": "While Loops", "category": "Control Flow",
        "icon": "⏳", "xp": 100,
        "theory": """The `while` loop keeps running **as long as** a condition is True.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

⚠️ Always make sure the condition eventually becomes False, or you'll get an **infinite loop**!

Use `break` to exit early:
```python
while True:
    if some_condition:
        break
```""",
        "example": 'n = 1\nwhile n <= 5:\n    print(n)\n    n += 1\nprint("Done!")',
        "challenge": "Write a while loop that starts at 100 and keeps halving the number (integer division by 2) until it reaches 0 or below. Print each value.",
        "hint": 'n = 100\nwhile n > 0:\n    print(n)\n    n = n // 2',
        "test_keyword": "while",
        "expected_contains": None
    },
    {
        "id": 8, "title": "Lists", "category": "Data Structures",
        "icon": "📋", "xp": 125,
        "theory": """Lists store multiple items in a single variable. They are **ordered**, **mutable** (changeable), and can hold **mixed types**.

```python
fruits = ["apple", "banana", "cherry"]
fruits[0]        # "apple" (index starts at 0)
fruits[-1]       # "cherry" (last item)
fruits[1:3]      # ["banana", "cherry"] (slicing)
```

**Common methods**:
- `append(item)` — add to end
- `remove(item)` — remove first occurrence
- `pop()` — remove and return last item
- `len(list)` — get length
- `sort()` — sort in place""",
        "example": 'scores = [85, 92, 78, 95, 88]\nscores.append(91)\nprint(scores)\nprint(f"Highest: {max(scores)}")\nprint(f"Average: {sum(scores)/len(scores):.1f}")',
        "challenge": "Create a list of 5 of your favourite movies. Sort the list alphabetically and print each movie with its position number (starting from 1).",
        "hint": 'movies = ["Inception", "Matrix", "Interstellar", "Avatar", "Dune"]\nmovies.sort()\nfor i, movie in enumerate(movies, 1):\n    print(f"{i}. {movie}")',
        "test_keyword": "append",
        "expected_contains": None
    },
    {
        "id": 9, "title": "Dictionaries", "category": "Data Structures",
        "icon": "📚", "xp": 125,
        "theory": """Dictionaries store **key-value pairs**. Perfect for structured data.

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "Amsterdam"
}

person["name"]         # "Alice"
person["age"] = 26     # update value
person["job"] = "Dev"  # add new key
```

**Looping over a dict**:
```python
for key, value in person.items():
    print(f"{key}: {value}")
```

**Useful methods**: `.keys()`, `.values()`, `.items()`, `.get(key, default)`""",
        "example": 'student = {"name": "Bob", "grade": "A", "score": 95}\nfor key, value in student.items():\n    print(f"{key}: {value}")',
        "challenge": "Create a dictionary for a product with keys: name, price, stock. Print a formatted summary and then update the price by adding 10% (VAT).",
        "hint": 'product = {"name": "Laptop", "price": 999, "stock": 50}\nproduct["price"] = product["price"] * 1.1\nfor k, v in product.items():\n    print(f"{k}: {v}")',
        "test_keyword": "dict",
        "expected_contains": None
    },
    {
        "id": 10, "title": "Functions", "category": "Functions",
        "icon": "⚡", "xp": 150,
        "theory": """Functions are reusable blocks of code. Define once, use many times.

```python
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)  # Hello, Alice!
```

**Default parameters**:
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

**Multiple return values**:
```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5])
```""",
        "example": 'def calculate_area(width, height):\n    area = width * height\n    return area\n\nresult = calculate_area(5, 8)\nprint(f"Area: {result}")',
        "challenge": "Write a function `is_palindrome(word)` that returns True if the word is a palindrome (reads the same forwards and backwards), False otherwise. Test it with 'racecar' and 'hello'.",
        "hint": 'def is_palindrome(word):\n    return word == word[::-1]\n\nprint(is_palindrome("racecar"))\nprint(is_palindrome("hello"))',
        "test_keyword": "def",
        "expected_contains": None
    },
    {
        "id": 11, "title": "Classes & OOP", "category": "OOP",
        "icon": "🏗️", "xp": 200,
        "theory": """Object-Oriented Programming (OOP) organizes code around **objects** — bundles of data and behavior.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Rex", "Labrador")
print(my_dog.bark())
```

- `class` — defines the blueprint
- `__init__` — constructor, runs when creating an object
- `self` — refers to the current instance
- **Attributes** — data stored on the object
- **Methods** — functions belonging to the class""",
        "example": 'class BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n    \n    def deposit(self, amount):\n        self.balance += amount\n    \n    def __str__(self):\n        return f"{self.owner}: €{self.balance}"\n\nacc = BankAccount("Alice", 1000)\nacc.deposit(500)\nprint(acc)',
        "challenge": "Create a `Rectangle` class with width and height attributes, an `area()` method, and a `perimeter()` method. Create an instance and print both.",
        "hint": 'class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    def area(self):\n        return self.width * self.height\n    def perimeter(self):\n        return 2 * (self.width + self.height)\n\nr = Rectangle(5, 3)\nprint(r.area())\nprint(r.perimeter())',
        "test_keyword": "class",
        "expected_contains": None
    },
    {
        "id": 12, "title": "File I/O", "category": "Advanced",
        "icon": "📁", "xp": 175,
        "theory": """Python can read and write files easily.

**Writing a file**:
```python
with open("file.txt", "w") as f:
    f.write("Hello, file!")
```

**Reading a file**:
```python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
```

**Reading line by line**:
```python
with open("file.txt") as f:
    for line in f:
        print(line.strip())
```

Always use `with` — it automatically closes the file when done. Modes: `"r"` read, `"w"` write, `"a"` append.""",
        "example": 'with open("/tmp/test.txt", "w") as f:\n    for i in range(1, 6):\n        f.write(f"Line {i}\\n")\n\nwith open("/tmp/test.txt", "r") as f:\n    for line in f:\n        print(line.strip())',
        "challenge": "Write a program that creates a file '/tmp/numbers.txt' containing the numbers 1-10 (one per line), then reads it back and prints the sum.",
        "hint": 'with open("/tmp/numbers.txt", "w") as f:\n    for i in range(1, 11):\n        f.write(f"{i}\\n")\n\ntotal = 0\nwith open("/tmp/numbers.txt") as f:\n    for line in f:\n        total += int(line.strip())\nprint(total)',
        "test_keyword": "open",
        "expected_contains": None
    },
    {
        "id": 13, "title": "Error Handling", "category": "Advanced",
        "icon": "🛡️", "xp": 175,
        "theory": """Errors (exceptions) are a normal part of programming. Python lets you handle them gracefully.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError as e:
    print(f"Bad value: {e}")
else:
    print("Success!")
finally:
    print("Always runs")
```

**Common exceptions**:
- `ValueError` — wrong value type
- `TypeError` — wrong data type
- `KeyError` — missing dict key
- `IndexError` — list index out of range
- `FileNotFoundError` — file doesn't exist""",
        "example": 'def safe_divide(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return "Error: division by zero"\n\nprint(safe_divide(10, 2))\nprint(safe_divide(10, 0))',
        "challenge": "Write a function `safe_int(value)` that tries to convert a value to int. If it fails (ValueError), return 0 instead. Test with '42', 'hello', and '3.14'.",
        "hint": 'def safe_int(value):\n    try:\n        return int(value)\n    except ValueError:\n        return 0\n\nprint(safe_int("42"))\nprint(safe_int("hello"))\nprint(safe_int("3.14"))',
        "test_keyword": "try",
        "expected_contains": None
    },
    {
        "id": 14, "title": "List Comprehensions", "category": "Advanced",
        "icon": "✨", "xp": 150,
        "theory": """List comprehensions are a concise, Pythonic way to create lists.

**Basic syntax**:
```python
squares = [x**2 for x in range(10)]
```

**With condition**:
```python
evens = [x for x in range(20) if x % 2 == 0]
```

**Transform strings**:
```python
names = ["alice", "bob", "charlie"]
upper = [name.upper() for name in names]
```

Compare to the traditional loop:
```python
# Traditional
result = []
for x in range(10):
    result.append(x**2)
```
Both produce the same result — comprehensions are just more elegant!""",
        "example": 'numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n\nsquares = [n**2 for n in numbers]\neven_squares = [n**2 for n in numbers if n % 2 == 0]\n\nprint(squares)\nprint(even_squares)',
        "challenge": "Using a list comprehension, create a list of all words longer than 4 characters from this sentence, converted to uppercase: 'the quick brown fox jumps over the lazy dog'",
        "hint": 'words = "the quick brown fox jumps over the lazy dog".split()\nlong_words = [w.upper() for w in words if len(w) > 4]\nprint(long_words)',
        "test_keyword": "for",
        "expected_contains": None
    },
    {
        "id": 15, "title": "Modules & Imports", "category": "Advanced",
        "icon": "📦", "xp": 150,
        "theory": """Python comes with a huge **standard library** of modules. Import them to extend functionality.

```python
import math
import random
import datetime
from os import path
```

**Useful standard modules**:

`math` — mathematical functions:
```python
import math
math.sqrt(16)    # 4.0
math.pi          # 3.14159...
```

`random` — random numbers:
```python
import random
random.randint(1, 10)    # random int 1-10
random.choice(["a","b"]) # random element
```

`datetime` — dates and times:
```python
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d"))
```""",
        "example": 'import random\nimport math\n\nnumbers = [random.randint(1, 100) for _ in range(5)]\nprint(numbers)\nprint(f"Mean: {sum(numbers)/len(numbers):.2f}")\nprint(f"Sqrt of first: {math.sqrt(numbers[0]):.2f}")',
        "challenge": "Use the `random` module to simulate rolling two dice 10 times. Print each roll and count how many times you got a double (both dice the same).",
        "hint": 'import random\ndoubles = 0\nfor i in range(10):\n    d1 = random.randint(1,6)\n    d2 = random.randint(1,6)\n    print(f"Roll {i+1}: {d1} + {d2}")\n    if d1 == d2:\n        doubles += 1\nprint(f"Doubles: {doubles}")',
        "test_keyword": "import",
        "expected_contains": None
    },
]

@app.route('/')
def index():
    if 'progress' not in session:
        session['progress'] = []
    if 'xp' not in session:
        session['xp'] = 0
    return render_template('index.html', curriculum=CURRICULUM, 
                          progress=session.get('progress', []),
                          xp=session.get('xp', 0))

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    lesson_data = next((l for l in CURRICULUM if l['id'] == lesson_id), None)
    if not lesson_data:
        return "Lesson not found", 404
    return render_template('lesson.html', lesson=lesson_data,
                          progress=session.get('progress', []),
                          xp=session.get('xp', 0))

@app.route('/run_code', methods=['POST'])
def run_code():
    data = request.json
    code = data.get('code', '')
    
    # Safety: block dangerous operations
    blocked = ['import os', 'import sys', 'subprocess', '__import__', 'exec(', 'eval(', 'open("/etc', 'open("/usr', 'open("/bin']
    for b in blocked:
        if b in code:
            return jsonify({'output': f'⛔ Blocked: "{b}" is not allowed in the sandbox.', 'error': True})
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        tmpfile = f.name
    
    try:
        result = subprocess.run(
            [sys.executable, tmpfile],
            capture_output=True, text=True, timeout=5
        )
        output = result.stdout
        if result.stderr:
            output += "\n❌ " + result.stderr
        return jsonify({'output': output or '(no output)', 'error': bool(result.returncode)})
    except subprocess.TimeoutExpired:
        return jsonify({'output': '⏱️ Timeout: your code took too long (max 5 seconds)', 'error': True})
    except Exception as e:
        return jsonify({'output': f'Error: {str(e)}', 'error': True})
    finally:
        os.unlink(tmpfile)

@app.route('/complete_lesson', methods=['POST'])
def complete_lesson():
    data = request.json
    lesson_id = data.get('lesson_id')
    xp_earned = data.get('xp', 0)
    
    progress = session.get('progress', [])
    if lesson_id not in progress:
        progress.append(lesson_id)
        session['xp'] = session.get('xp', 0) + xp_earned
    session['progress'] = progress
    session.modified = True
    
    return jsonify({'success': True, 'total_xp': session['xp'], 'progress': progress})

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    data = request.json
    question = data.get('question', '')
    lesson_title = data.get('lesson_title', '')
    code = data.get('code', '')
    
    prompt = f"""You are a friendly Python tutor helping a beginner learn Python.
Current lesson: {lesson_title}
Student's code:
```python
{code}
```
Student's question: {question}

Give a helpful, encouraging, concise answer (max 150 words). Use simple language. If relevant, show a short code example."""

    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={"Content-Type": "application/json"},
            json={
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 400,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=15
        )
        result = response.json()
        answer = result['content'][0]['text']
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'answer': f'Could not reach AI tutor: {str(e)}'})

@app.route('/reset_progress', methods=['POST'])
def reset_progress():
    session['progress'] = []
    session['xp'] = 0
    session.modified = True
    return jsonify({'success': True})

if __name__ == '__main__':
    print("\n🐍 Python Zero to Hero Tutor")
    print("================================")
    print("Open your browser at: http://localhost:5000")
    print("Press Ctrl+C to stop\n")
    app.run(debug=True, port=5000)
