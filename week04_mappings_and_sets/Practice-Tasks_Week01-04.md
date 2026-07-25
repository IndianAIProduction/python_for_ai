# PRACTICE TASKS — Week 1 to Week 4 (Self-Practice, Logic Building)

> **Note:** Yeh 20 tasks Week 1 se Week 4 (dictionaries, sets, comprehensions tak) ke concepts par based hain. Inhe **khud** solve karo — yahi logic building ka asli tareeka hai.
>
> **Rules of the game:**
> - Har task ko ek naye blank `.py` file mein likho.
> - Solution yahan **jaan-boojh kar nahi diya** — pehle khud try karo (kam se kam 15-20 min). Atak jao toh sirf **Hint** dekho, poora answer mat dhoondho.
> - Sirf wahi concepts use karo jo Week 1-4 mein aa chuke hain (functions abhi nahi — woh Week 5 mein aayenge).
> - Har task ke saath sirf **Concepts** (kya use hoga) aur ek **Hint** diya hai. **Expected output aur poore solutions doc ke sabse end mein hain** (Answer Key section) — taaki aap questions padhte waqt galti se answer na dekh lo.
>
> **Difficulty:** 🟢 Easy → 🟡 Medium → 🔴 Hard. Order mein karo — har task pichle par build karta hai.

---

## 🟢 EASY (Week 1-2 — variables, maths, strings, if/else, loops)

### Task 1 — Personal Profile Card
User se `name`, `age`, `city`, aur `favourite_subject` maango (`input()`). Phir ek saaf profile card f-string se print karo.

- **Concepts:** variables, `input()`, `int()`, f-strings
- **Hint:** `age` ko `int(input(...))` se lo taaki `age + 1` chal sake.

---

### Task 2 — Smart Bill Calculator
Ek item ka `price` aur `quantity` maango. Total nikaalo. Agar total 1000 se zyada hai toh 10% discount lagao, warna koi discount nahi. Final amount 2 decimals ke saath print karo.

- **Concepts:** arithmetic, `if/else`, f-string formatting `:.2f`
- **Hint:** discount = `total * 0.10` sirf tab jab `total > 1000`.

---

### Task 3 — Even ya Odd + Positive/Negative
User se ek number lo. Batao woh **positive/negative/zero** hai, AUR **even/odd** hai (zero ke liye even/odd mat batao).

- **Concepts:** `if/elif/else`, modulus `%`, ternary
- **Hint:** even/odd ke liye `n % 2 == 0`. Ek ternary se "Even"/"Odd" choose karo.

---

### Task 4 — Multiplication Table (clean)
User se ek number `n` aur ek limit `k` lo. `n` ka table 1 se `k` tak print karo (loop se).

- **Concepts:** `for` loop, `range(1, k+1)`, f-string
- **Hint:** `range` ka stop **exclusive** hai — `k` ko shaamil karne ke liye `k + 1` likho.

---

### Task 5 — Sum & Average of N Numbers
User se pehle poochho kitne numbers dega (`count`). Phir loop mein ek-ek karke numbers lo, unka **sum** aur **average** print karo.

- **Concepts:** `for` loop, running total, `int(input())`, `:.2f`
- **Hint:** loop se pehle `total = 0` banao, andar `total = total + num`.

---

## 🟡 MEDIUM (Week 2-3 — while, break, lists, tuples, string methods)

### Task 6 — Guess with Limited Attempts
Ek secret number fix karo (`secret = 42`). User ko sirf **3 chances** do guess karne ke. Har galat guess par "Too high" / "Too low" batao. 3 ke andar sahi → "You won", warna → "Game over, number was 42".

- **Concepts:** `while`, `break`, counter, `if/elif/else`
- **Hint:** `attempts` counter rakho, `while attempts < 3`. Sahi guess par `break`.

---

### Task 7 — Word & Character Counter
User se ek sentence lo. Print karo: kitne **words** hain, kitne **characters** (spaces chhod kar), aur sentence **UPPERCASE** mein.

- **Concepts:** `.split()`, `.replace()`, `len()`, `.upper()`, `.strip()`
- **Hint:** spaces hatane ke liye `.replace(" ", "")` phir `len()`.

---

### Task 8 — Reverse & Palindrome Check
User se ek word lo. Use ulta print karo, aur batao woh **palindrome** hai ya nahi (case ignore karo — "Madam" bhi palindrome hai).

- **Concepts:** slicing `[::-1]`, `.lower()`, `if/else`
- **Hint:** compare karne se pehle dono ko `.lower()` kar do.

---

### Task 9 — Marks List Analyzer
Ek list `marks = [45, 78, 92, 33, 88, 20, 67]` lo. Bina `max()`/`min()` use kiye (loop se khud nikaalo) print karo: **highest**, **lowest**. Phir `sum()`/`len()` se **average**. Aur batao kitne students **pass** hue (>= 33).

- **Concepts:** `for` loop, comparison, running max/min, counter
- **Hint:** `highest = marks[0]` se shuru karo, phir loop mein `if m > highest: highest = m`.

---

### Task 10 — To-Do List Manager (menu loop)
Ek khaali list `todos = []` banao. Ek `while True` menu chalao: `1) Add  2) Remove  3) Show  4) Quit`. User ke choice ke hisaab se task add/remove/show karo. `4` par loop `break` karo.

- **Concepts:** `while True`, `match`/`case` (ya if/elif), list `.append()`/`.remove()`, `break`
- **Hint:** remove karte waqt check karo item list mein hai ya nahi (warna crash), `if item in todos:`.

---

### Task 11 — Student Records (list of tuples)
Ek list of tuples banao: `[("Asha", 85), ("Rahul", 92), ("Priya", 78)]`. Har student ka naam aur marks **unpacking** se print karo. Phir sabse zyada marks waale ka naam batao.

- **Concepts:** list of tuples, tuple unpacking in `for`, running max
- **Hint:** `for name, mark in students:` — yeh unpacking hai.

---

### Task 12 — FizzBuzz (classic logic test)
1 se 30 tak loop chalao. 3 se divisible → "Fizz", 5 se divisible → "Buzz", dono se → "FizzBuzz", warna number khud print karo.

- **Concepts:** `for` loop, `%`, nested/ordered `if/elif/else`
- **Hint:** **order matter karta hai** — pehle dono (15) wala check karo, warna sirf Fizz/Buzz kabhi FizzBuzz nahi banega.

---

## 🔴 HARD (Week 3-4 — nested data, dicts, sets, comprehensions, sorting)

### Task 13 — Vowel & Consonant Counter
User se ek sentence lo. Ek dictionary banao jo har **vowel** (a,e,i,o,u) kitni baar aaya woh count kare. Phir total consonants (letters jo vowel nahi) alag se print karo.

- **Concepts:** loop over string, `dict`, `.get()` ya `in` check, `.lower()`
- **Hint:** `counts[ch] = counts.get(ch, 0) + 1` — yeh missing key ko safely handle karta hai.

---

### Task 14 — Word Frequency Counter
Ek paragraph string lo (multi-word). Har **word** kitni baar aaya, ek dictionary mein count karo (case-insensitive). Phir sabse zyada aane wala word batao.

- **Concepts:** `.lower()`, `.split()`, `dict` counting, `max(..., key=...)`
- **Hint:** `max(counts, key=counts.get)` sabse badi value waali key deta hai.

---

### Task 15 — Duplicate Remover (order preserve)
Ek list `nums = [3, 1, 2, 3, 4, 1, 5, 2]` lo. Duplicates hatao **par original order bana rahe**. (Sirf `set(nums)` order tod dega — isliye set ko sirf "dekha kya" check ke liye use karo.)

- **Concepts:** `set` for membership, `list`, `for` loop, `.append()`
- **Hint:** ek `seen = set()` rakho. Har num par: agar `num not in seen`, toh result mein `append` karo aur `seen.add(num)`.

---

### Task 16 — Two Class Comparison (sets)
Do sets banao: `python_students` aur `java_students` (kuch naam dono mein common ho). Print karo: (a) dono seekhne wale, (b) sirf Python, (c) total unique students, (d) sirf ek language seekhne wale.

- **Concepts:** set operations `&`, `-`, `|`, symmetric difference `^`
- **Hint:** "sirf ek language" = `python ^ java` (symmetric difference).

---

### Task 17 — Sort Students by Marks (list of dicts)
Ek list of dicts banao: `[{"name": "Asha", "marks": 85}, ...]` (kam se kam 4 students). Unhe **marks ke descending order** mein sort karke print karo (rank ke saath). Original list ko **mat** badlo.

- **Concepts:** `sorted(key=lambda ...)`, `reverse=True`, `enumerate`, nested access
- **Hint:** `sorted(students, key=lambda s: s["marks"], reverse=True)`. Rank ke liye `enumerate(..., start=1)`.

---

### Task 18 — Contact Book with Search (nested dict)
Ek dictionary of dicts banao:
```python
contacts = {
    "Asha":  {"phone": "98765", "city": "Mumbai"},
    "Rahul": {"phone": "91234", "city": "Delhi"},
}
```
User se ek naam maango. `.get()` se safely dhoondho — mile toh phone + city print karo, na mile toh "Contact not found".

- **Concepts:** nested `dict`, `.get()`, `input()`, `if/else`
- **Hint:** `contacts.get(name)` pehle — agar `None` mila toh not found, warna andar ke fields access karo.

---

### Task 19 — Number Grid + Diagonal Sum (nested list)
Ek 3x3 grid banao:
```python
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
Poora grid tidy print karo (rows/columns aligned). Phir main **diagonal ka sum** (1+5+9) nikaalo.

- **Concepts:** nested list, nested loop, `grid[i][i]`, running total
- **Hint:** diagonal ke liye ek hi index use karo: `grid[i][i]` for `i in range(3)`.

---

### Task 20 — Mini Data Cleaner (comprehensions — capstone)
Ek messy list of raw user inputs lo:
```python
raw = ["  Asha ", "RAHUL", "", "  priya  ", "Amit", "rahul  "]
```
Ek **hi line ke comprehension** se: har naam ko `strip` + `lower` karo aur khaali strings hatao. Phir us cleaned list se **unique naam** (set) nikaalo aur alphabetical order mein sorted print karo.

- **Concepts:** list comprehension + `if` filter, `.strip()`, `.lower()`, `set()`, `sorted()`
- **Hint:** `[n.strip().lower() for n in raw if n.strip()]` — filter `if n.strip()` khaali strings ko hata deta hai.

---

## 🏁 Bonus Challenge (sab kuch mila kar)

**Student Report Card Generator** — Ek list of dicts banao jisme har student ka `name` aur teen subjects ke `marks` (ek list) ho. Har student ke liye: total, average, aur grade (A/B/C/D) nikaalo. Sabse aakhir mein **class topper** aur **class average** batao. Original data safe rakhne ke liye kaam karne se pehle `copy.deepcopy()` use karo.

- **Concepts:** list of dicts, nested list, loops, `sum()`/`len()`, `if/elif/else`, `sorted(key=...)`, `copy.deepcopy`
- **Yeh capstone hai** — agar aap yeh khud bina notes ke bana lete ho, toh aapne Week 1-4 sach mein master kar liya. 💪

---

## ✅ Self-Check Rubric

Har task ke baad khud se poochho:
1. Kya code **bina error** chalta hai?
2. Kya output **expected** se match karta hai (edge cases bhi — jaise 0, khaali input)?
3. Kya variable **naam meaningful** hain (`total_marks`, `x` nahi)?
4. Kya aapne f-strings use kiye (na ki `+` concatenation)?
5. Kya aap **kisi aur ko samjha sakte ho** ki code kaise kaam karta hai?

Agar paanchon "haan" hain — **shabaash!** Aap logic building ke sahi raaste par ho.

---
---
---

# 🔒 SOLUTIONS / ANSWER KEY

> ## ⚠️ STOP! Pehle khud try karo!
>
> Yeh section **sirf** tab dekho jab aap ek task par **kam se kam 20 minutes** khud mehnat kar chuke ho. Bina try kiye answer dekhoge toh logic **kabhi nahi** banega. Yeh answers scroll karke neeche hain taaki aap galti se questions padhte waqt na dekh lo.
>
> Yaad rakho: har task ke kai sahi tareeke ho sakte hain. Aapka code inse **exactly same nahi** hona chahiye — bas kaam sahi karna chahiye. 💪

---

### ✅ Solution 1 — Personal Profile Card
```python
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")
favourite_subject = input("Favourite subject: ")

print(f"Name    : {name}")
print(f"Age     : {age} (next year: {age + 1})")
print(f"City    : {city}")
print(f"Subject : {favourite_subject}")
```
**Expected output (name=Asha, age=17, city=Mumbai, subject=Computer Science):**
```
Name    : Asha
Age     : 17 (next year: 18)
City    : Mumbai
Subject : Computer Science
```

---

### ✅ Solution 2 — Smart Bill Calculator
```python
price = float(input("Price: "))
quantity = int(input("Quantity: "))

subtotal = price * quantity
discount = subtotal * 0.10 if subtotal > 1000 else 0
total = subtotal - discount

print(f"Subtotal : ₹{subtotal:.2f}")
print(f"Discount : ₹{discount:.2f}")
print(f"Total    : ₹{total:.2f}")
```
**Expected output (price=300, qty=5):**
```
Subtotal : ₹1500.00
Discount : ₹150.00
Total    : ₹1350.00
```

---

### ✅ Solution 3 — Even/Odd + Positive/Negative
```python
n = int(input("Enter a number: "))

if n > 0:
    sign = "Positive"
elif n < 0:
    sign = "Negative"
else:
    sign = "Zero"

if n == 0:
    print(f"{n} is Zero")
else:
    parity = "Even" if n % 2 == 0 else "Odd"
    print(f"{n} is {sign} and {parity}")
```
**Expected output (input = -8):**
```
-8 is Negative and Even
```

---

### ✅ Solution 4 — Multiplication Table
```python
n = int(input("Number: "))
k = int(input("Up to: "))

for i in range(1, k + 1):
    print(f"{n} x {i} = {n * i}")
```
**Expected output (n=7, k=5):**
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
```

---

### ✅ Solution 5 — Sum & Average of N Numbers
```python
count = int(input("How many numbers? "))
total = 0

for i in range(count):
    num = int(input(f"Number {i + 1}: "))
    total = total + num

average = total / count
print(f"Sum     : {total}")
print(f"Average : {average:.2f}")
```
**Expected output (count=3, nums=10,20,30):**
```
Sum     : 60
Average : 20.00
```

---

### ✅ Solution 6 — Guess with Limited Attempts
```python
secret = 42
attempts = 0
won = False

while attempts < 3:
    guess = int(input("Guess (1-100): "))
    attempts = attempts + 1
    if guess == secret:
        print("You won")
        won = True
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")

if not won:
    print(f"Game over, number was {secret}")
```

---

### ✅ Solution 7 — Word & Character Counter
```python
sentence = input("Enter a sentence: ").strip()

words = len(sentence.split())
characters = len(sentence.replace(" ", ""))

print(f"Words      : {words}")
print(f"Characters : {characters}")
print(f"Uppercase  : {sentence.upper()}")
```
**Expected output (input = "i love python"):**
```
Words      : 3
Characters : 11
Uppercase  : I LOVE PYTHON
```

---

### ✅ Solution 8 — Reverse & Palindrome Check
```python
word = input("Enter a word: ")
reversed_word = word[::-1]
print(f"Reversed: {reversed_word}")

if word.lower() == word.lower()[::-1]:
    print(f'"{word}" is a Palindrome')
else:
    print(f'"{word}" is Not a Palindrome')
```
**Expected output (input = "Madam"):**
```
Reversed: madaM
"Madam" is a Palindrome
```

---

### ✅ Solution 9 — Marks List Analyzer
```python
marks = [45, 78, 92, 33, 88, 20, 67]

highest = marks[0]
lowest = marks[0]
passed = 0

for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
    if m >= 33:
        passed = passed + 1

average = sum(marks) / len(marks)

print(f"Highest : {highest}")
print(f"Lowest  : {lowest}")
print(f"Average : {average:.2f}")
print(f"Passed  : {passed}")
```
**Expected output:**
```
Highest : 92
Lowest  : 20
Average : 60.43
Passed  : 6
```

---

### ✅ Solution 10 — To-Do List Manager
```python
todos = []

while True:
    print("\n1) Add  2) Remove  3) Show  4) Quit")
    choice = input("Choice: ")

    match choice:
        case "1":
            item = input("Task to add: ")
            todos.append(item)
            print(f"Added: {item}")
        case "2":
            item = input("Task to remove: ")
            if item in todos:
                todos.remove(item)
                print(f"Removed: {item}")
            else:
                print("Task not found")
        case "3":
            if todos:
                for i, task in enumerate(todos, start=1):
                    print(f"{i}. {task}")
            else:
                print("No tasks yet")
        case "4":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice")
```

---

### ✅ Solution 11 — Student Records (list of tuples)
```python
students = [("Asha", 85), ("Rahul", 92), ("Priya", 78)]

topper_name = students[0][0]
topper_marks = students[0][1]

for name, mark in students:
    print(f"{name:<5} -> {mark}")
    if mark > topper_marks:
        topper_marks = mark
        topper_name = name

print(f"Topper: {topper_name}")
```
**Expected output:**
```
Asha  -> 85
Rahul -> 92
Priya -> 78
Topper: Rahul
```

---

### ✅ Solution 12 — FizzBuzz
```python
for n in range(1, 31):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
```
**Expected output (partial):**
```
1
2
Fizz
4
Buzz
Fizz
...
14
FizzBuzz
```

---

### ✅ Solution 13 — Vowel & Consonant Counter
```python
sentence = input("Enter a sentence: ").lower()

vowels = "aeiou"
consonant_letters = "bcdfghjklmnpqrstvwxyz"

vowel_counts = {}
consonants = 0

for ch in sentence:
    if ch in vowels:
        vowel_counts[ch] = vowel_counts.get(ch, 0) + 1
    elif ch in consonant_letters:
        consonants = consonants + 1

print(f"Vowel counts: {vowel_counts}")
print(f"Consonants  : {consonants}")
```
**Expected output (input = "education"):**
```
Vowel counts: {'e': 1, 'u': 1, 'a': 1, 'i': 1, 'o': 1}
Consonants  : 4
```

---

### ✅ Solution 14 — Word Frequency Counter
```python
text = "the cat the dog the bird"
words = text.lower().split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
most_common = max(counts, key=counts.get)
print(f"Most common: {most_common}")
```
**Expected output (text = "the cat the dog the bird"):**
```
{'the': 3, 'cat': 1, 'dog': 1, 'bird': 1}
Most common: the
```

---

### ✅ Solution 15 — Duplicate Remover (order preserve)
```python
nums = [3, 1, 2, 3, 4, 1, 5, 2]

seen = set()
result = []

for num in nums:
    if num not in seen:
        result.append(num)
        seen.add(num)

print(result)
```
**Expected output:**
```
[3, 1, 2, 4, 5]
```

---

### ✅ Solution 16 — Two Class Comparison (sets)
```python
python_students = {"Asha", "Rahul", "Priya", "Amit"}
java_students = {"Rahul", "Amit", "Sara"}

print(f"Both languages : {python_students & java_students}")
print(f"Only Python    : {python_students - java_students}")
print(f"Total unique   : {len(python_students | java_students)}")
print(f"Only one lang  : {python_students ^ java_students}")
```

---

### ✅ Solution 17 — Sort Students by Marks (list of dicts)
```python
students = [
    {"name": "Asha", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Priya", "marks": 78},
    {"name": "Amit", "marks": 60},
]

ranked = sorted(students, key=lambda s: s["marks"], reverse=True)

for rank, s in enumerate(ranked, start=1):
    print(f"Rank {rank}: {s['name']} ({s['marks']})")
```
**Expected output:**
```
Rank 1: Rahul (92)
Rank 2: Asha (85)
Rank 3: Priya (78)
Rank 4: Amit (60)
```

---

### ✅ Solution 18 — Contact Book with Search (nested dict)
```python
contacts = {
    "Asha":  {"phone": "98765", "city": "Mumbai"},
    "Rahul": {"phone": "91234", "city": "Delhi"},
}

name = input("Search name: ")
info = contacts.get(name)

if info:
    print(f"Phone: {info['phone']}, City: {info['city']}")
else:
    print("Contact not found")
```

---

### ✅ Solution 19 — Number Grid + Diagonal Sum (nested list)
```python
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in grid:
    for item in row:
        print(item, end=" ")
    print()

diagonal_sum = 0
for i in range(len(grid)):
    diagonal_sum = diagonal_sum + grid[i][i]

print(f"Diagonal sum: {diagonal_sum}")
```
**Expected output:**
```
1 2 3
4 5 6
7 8 9
Diagonal sum: 15
```

---

### ✅ Solution 20 — Mini Data Cleaner (comprehensions)
```python
raw = ["  Asha ", "RAHUL", "", "  priya  ", "Amit", "rahul  "]

cleaned = [n.strip().lower() for n in raw if n.strip()]
print(f"Cleaned: {cleaned}")

unique_sorted = sorted(set(cleaned))
print(f"Unique (sorted): {unique_sorted}")
```
**Expected output:**
```
Cleaned: ['asha', 'rahul', 'priya', 'amit', 'rahul']
Unique (sorted): ['amit', 'asha', 'priya', 'rahul']
```

---

### ✅ Solution — Bonus Challenge (Report Card Generator)
```python
import copy

students = [
    {"name": "Asha", "marks": [85, 90, 80]},
    {"name": "Rahul", "marks": [92, 88, 95]},
    {"name": "Priya", "marks": [70, 65, 72]},
    {"name": "Amit", "marks": [55, 60, 50]},
]

# original data safe rakhne ke liye copy par kaam karo
working = copy.deepcopy(students)

for s in working:
    total = sum(s["marks"])
    average = total / len(s["marks"])

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    s["total"] = total
    s["average"] = average
    s["grade"] = grade
    print(f"{s['name']:<6} | Total: {total} | Avg: {average:.2f} | Grade: {grade}")

topper = max(working, key=lambda s: s["average"])
class_average = sum(s["average"] for s in working) / len(working)

print(f"\nClass Topper : {topper['name']}")
print(f"Class Average: {class_average:.2f}")
```

---

*Solutions khatam. Agar aapka answer alag hai par sahi output deta hai — woh bhi 100% correct hai. Programming mein ek problem ke kai solutions hote hain!* 🎉
