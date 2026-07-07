# WEEK 2 — Decisions & Repetition (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> **Week promise:** *"Is week tak aapke programs SOCH-samajh kar decisions lenge (if/else) aur kaam REPEAT karenge (loops). Yeh do cheezein — choose karna aur repeat karna — ek AI agent ke dimaag ka aakaar hain. Week ke end tak aap ek number-guessing game aur menu calculator banaoge."*

---

## CLASS 16 — if / elif / else & Truthiness

*"Pichle week recap: variables (boxes), numbers, strings, booleans (True/False). Aaj hum un booleans ko KAAM par lagayenge. Ab tak hamare programs upar se neeche, har line chalaate the — bina soche. Aaj se program SOCHEGA: 'agar yeh sach hai toh yeh karo, warna woh karo.'"*

### 🎯 Today's goal
`if`, `elif`, `else` se program ko alag-alag raaste choose karwana.

### 👨‍🏫 Concept 1 — `if` ka basic shape

> **📖 Technical definition — `if` / `elif` / `else`:** A conditional statement runs a block of code only when its boolean condition is true. `if` tests the first condition, each `elif` tests a further condition when all previous ones were false, and `else` runs when none of the conditions were true. At most one block executes.

*"Sochiye ghar par rule hai: 'agar baarish ho rahi hai, toh chhata le jao.' Code mein bilkul aise:"*
```python
is_raining = True

if is_raining:
    print("Take an umbrella")
```
*"Padho: 'IF is_raining True hai, toh yeh wali line chalao.' Agar `is_raining` False hota, toh Python woh line skip kar deta."*

**Do cheezein bahut important hain (warna error):**
- `if` ke baad **colon `:`** zaroori hai.
- Andar wali line ko **indent** karna zaroori hai (4 spaces). Yeh Python ka tareeka hai yeh batane ka ki "yeh line `if` ke ANDAR hai".

### 👨‍🏫 Concept 2 — `else` (warna ye karo)
```python
marks = 25

if marks >= 33:
    print("Pass")
else:
    print("Fail")
```
Output:
```
Fail
```
*"`marks` 25 hai, jo 33 se chhota hai, toh `if` False hua → Python `else` wala block chalata hai → 'Fail'. Bas DO mein se EK block chalega, dono kabhi nahi."*

### 👨‍🏫 Concept 3 — `elif` (ek aur chance)
*"Sirf pass/fail nahi, grade bhi chahiye? Tab `elif` (else-if) aata hai. Python upar se neeche check karta hai, JO PEHLA True mile wahi chalata hai, baaki chhod deta hai."*
```python
marks = 72

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```
Output:
```
Grade C
```
*"Dekho: 72 >= 90? Nahi. 72 >= 75? Nahi. 72 >= 60? HAAN → 'Grade C' print, aur baaki sab skip. Order matter karta hai — hamesha bade number se chhote ki taraf jao."*

### 👨‍🏫 Concept 4 — Truthiness (chupa hua superpower)

> **📖 Technical definition — Truthiness:** Truthiness is the boolean value that any object takes on when used in a condition. Empty or zero-like values (`""`, `0`, `0.0`, `[]`, `{}`, `None`) are treated as `False`; all other values are treated as `True`.

*"Python mein har value ko ek 'haan/naa' value maani jaa sakti hai. Khaali cheezein 'False jaisi' hain, bhari cheezein 'True jaisi'."*
```python
name = input("Your name: ")

if name:                       # khaali string = False jaisi
    print(f"Hello, {name}")
else:
    print("You did not type a name!")
```
**Yaad rakhne wali table:**
| False jaisi (empty/zero) | True jaisi (bhari) |
|---|---|
| `""` (empty string) | `"a"` (koi bhi text) |
| `0`, `0.0` | `5`, `-3` (koi bhi non-zero) |
| `[]` (empty list) | `[1]` (bhari list) |
| `None` | almost sab kuch |

*"Isiliye hum `if name:` likh sakte hain — `if name != "":` likhne ki zaroorat nahi. Yeh Pythonic (saaf) style hai."*

### ❌ Common mistakes
```python
if marks >= 33          # ❌ colon ':' bhool gaye → SyntaxError
print("Pass")           # ❌ indent nahi kiya → IndentationError

if marks = 33:          # ❌ single '=' (store) use kiya, '==' (compare) chahiye tha
```

### 🔗 Agentic link
*"Ek agent constantly decisions leta hai: 'kya user ne maths poocha? → calculator tool use karo. Kya answer ready hai? → ruk jao.' Yeh saare `if/elif/else` hain. Aaj aapne agent ki decision-making ka asli core seekh liya."*

### ✍️ Homework
1. Ek program: number lo, print karo "Positive", "Negative", ya "Zero".
2. Ek program: age lo. 18+ → "You can vote", warna → "Too young".
3. Marks lo aur upar wala grade A/B/C/D print karo.

**Answers:**
```python
# 1
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2
age = int(input("Your age: "))
if age >= 18:
    print("You can vote")
else:
    print("Too young")

# 3
marks = int(input("Your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

### 🔗 Agli class
*"Agli class — ek decision ke andar doosra decision (nested), aur ek-line wala shortcut if-else (ternary)."*

---

## CLASS 17 — Nested Conditions & Ternary

*"Pichli class mein humne ek decision liya. Par real zindagi mein decisions layered hote hain: 'agar movie ke liye eligible ho... AUR ticket ke paise ho... tabhi jao.' Aaj decisions ko aapas mein jodte hain."*

### 🎯 Today's goal
Nested `if` aur one-line `if/else` (ternary) use karna.

### 👨‍🏫 Concept 1 — Nested if (if ke andar if)

> **📖 Technical definition — Nested conditional:** A nested conditional is an `if` statement placed inside the body of another `if`, `elif`, or `else` block, so that an inner condition is only tested when the outer condition has already been satisfied.

*"Ek `if` ke block ke andar doosra `if` rakh sakte ho. Bas indentation badhati jaati hai."*
```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Enjoy the movie!")
    else:
        print("Please buy a ticket")
else:
    print("Only 18+ allowed")
```
Output:
```
Enjoy the movie!
```
*"Pehle bahar ka `if` check hua (age 20 >= 18 ✅), phir andar ka (has_ticket True ✅). Dono pass → 'Enjoy'."*

### 👨‍🏫 Concept 2 — Aksar `and` zyada saaf hota hai
*"Bahut saari nesting confusing ho jaati hai. Pichle week ka `and` yaad hai? Use karke ek hi line mein:"*
```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Enjoy the movie!")
else:
    print("Sorry, cannot enter")
```
*"Industry tip: jab dono conditions saath honi chahiye, `and` use karo. Nesting tab use karo jab har level par alag message dena ho. Clarity > cleverness."*

### 👨‍🏫 Concept 3 — Ternary (one-line if/else)

> **📖 Technical definition — Ternary (conditional) expression:** A ternary expression is a single-line construct of the form `value_if_true if condition else value_if_false` that evaluates to one of two values depending on whether the condition is true.

*"Jab aap ek value ko do mein se ek choose karke set karna chahte ho, ek line mein likh sakte ho:"*
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)        # Adult
```
*"Padho aise: 'status ko Adult bana do AGAR age>=18, ELSE Minor.' Yeh sirf SHORT cases ke liye hai. Lambi logic ke liye normal if/else hi use karo."*

### 💻 Demo — ticket price by age
```python
age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age < 18:
    price = 100
elif age < 60:
    price = 200
else:
    price = 50          # senior citizen discount

print(f"Ticket price: ₹{price}")
```
*"5 se kam → free, 18 se kam → 100, 60 se kam → 200, warna senior → 50. Dekho `elif` ki chain kitni saaf padhi jaati hai."*

### ❌ Common mistakes
```python
# galat order — chhota check pehle, toh bada kabhi nahi chalega
if marks >= 33:
    print("Pass")
elif marks >= 90:    # ❌ yahan kabhi nahi aayega (33 already True ho gaya)
    print("Grade A")
```
*"Yaad rakho: `elif` upar se neeche check hote hain. Hamesha sabse strict/bada condition pehle rakho."*

### 🔗 Agentic link
*"Agent ke decisions ek saath kai cheezein tolte hain: 'kya model confident hai? AUR kya yeh action safe hai? AUR kya budget bacha hai?' Yeh nested/combined conditions hain — exactly aaj wala."*

### ✍️ Homework
1. Teen numbers lo aur sabse bada print karo (`if/elif/else` se).
2. Ek simple login: hardcoded `username` aur `password` check karo. Dono sahi → "Login success", warna "Login failed".
3. Ternary se: ek number even hai ya odd, ek line mein print karo.

**Answers:**
```python
# 1
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a >= b and a >= c:
    print(f"Largest is {a}")
elif b >= c:
    print(f"Largest is {b}")
else:
    print(f"Largest is {c}")

# 2
username = input("Username: ")
password = input("Password: ")
if username == "admin" and password == "1234":
    print("Login success")
else:
    print("Login failed")

# 3
n = int(input("Number: "))
print("Even" if n % 2 == 0 else "Odd")
```

### 🔗 Agli class
*"Agli class — LOOPS! Ek hi kaam baar-baar karna, bina copy-paste kiye. Yahin se programming asli mazedaar hoti hai."*

---

## CLASS 18 — for Loops, range & Helpers

*"Maan lo main bolun '1 se 100 tak print karo'. Kya aap 100 baar `print()` likhoge? Bilkul nahi! Loop ek baar likhte hain, computer 100 baar chalata hai. Yeh programming ka sabse bada time-saver hai."*

### 🎯 Today's goal
`for` loop aur `range()` use karna, plus helpers `enumerate`, `zip`, `reversed`.

### 👨‍🏫 Concept 1 — for loop ek list par

> **📖 Technical definition — `for` loop:** A `for` loop is an iteration statement that executes its body once for each item in an iterable (such as a list, string, or range), binding the current item to a loop variable on each pass.

*"`for` loop kisi bhi collection ke har item par ek-ek karke chalta hai."*
```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
mango
```
*"Padho: 'fruits ke har fruit ke liye, fruit print karo.' `fruit` ek temporary box hai jo har round mein agli value le leta hai. Naam aap kuch bhi rakh sakte ho (`item`, `f`, etc.)."*

### 👨‍🏫 Concept 2 — `range()` — numbers banata hai

> **📖 Technical definition — `range()`:** `range()` produces an immutable sequence of evenly spaced integers, defined by a start (default 0), a stop (exclusive), and a step (default 1). It is memory-efficient because it generates values on demand rather than storing them all.

```python
for i in range(5):
    print(i)
```
Output:
```
0
1
2
3
4
```
*"BAHUT important: `range(5)` aapko `0,1,2,3,4` deta hai — 5 numbers, par 5 SHAMIL NAHI. Yeh 0 se shuru hota hai aur end se EK pehle rukta hai."*

**`range` ke 3 roop:**
```python
range(5)        # 0,1,2,3,4         (stop)
range(1, 6)     # 1,2,3,4,5         (start, stop)
range(2, 11, 2) # 2,4,6,8,10        (start, stop, step)
```

### 👨‍🏫 Concept 3 — `enumerate` (number + item dono)

> **📖 Technical definition — `enumerate()`:** `enumerate()` wraps an iterable and yields pairs of `(index, item)`, providing an automatic counter alongside each element so you do not have to maintain one manually.

*"Aksar humein item ke saath uska position number bhi chahiye hota hai. Manually counter mat banao — `enumerate` use karo."*
```python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```
Output:
```
0: apple
1: banana
2: mango
```
*"1 se shuru karna ho? `enumerate(fruits, start=1)` likho."*

### 👨‍🏫 Concept 4 — `zip` (do lists saath-saath)

> **📖 Technical definition — `zip()`:** `zip()` combines two or more iterables element by element, yielding tuples of corresponding items. It stops as soon as the shortest input iterable is exhausted.

```python
names = ["Asha", "Rahul", "Priya"]
marks = [85, 90, 78]

for name, mark in zip(names, marks):
    print(f"{name} scored {mark}")
```
Output:
```
Asha scored 85
Rahul scored 90
Priya scored 78
```
*"`zip` do (ya zyada) lists ko jodi-jodi banakar saath chalata hai. Jab do related lists ho, yeh perfect hai."*

### 👨‍🏫 Concept 5 — `reversed` (ulta chalo)
```python
for i in reversed(range(1, 6)):
    print(i)        # 5, 4, 3, 2, 1
```

### 💻 Demo — multiplication table
```python
num = int(input("Which table? "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```
*"5 daalo → poora 5 ka table print ho jayega, 1 se 10 tak. Ek loop, 10 lines output."*

### ❌ Common mistakes
```python
for i in range(1, 5):
    print(i)        # 1,2,3,4 — yaad rakho, 5 NAHI aata

# indent bhool jaana
for i in range(3):
print(i)            # ❌ IndentationError — loop body indent hona chahiye
```

### 🔗 Agentic link
*"Agent constantly cheezon par loop karta hai: chat ke har message par, search ke har result par, har available tool par. `enumerate` se results number karte hain, `zip` se naam aur scores jodte hain. Aaj aapne agent ka 'har cheez process karna' seekh liya."*

### ✍️ Homework
1. 1 se 100 tak ke saare numbers ka SUM nikalo (loop se).
2. Apni pasand ke number ka table 1–10 print karo.
3. Ek list `["red","green","blue"]` ko `enumerate` se number ke saath print karo.

**Answers:**
```python
# 1
total = 0
for i in range(1, 101):
    total = total + i
print(total)            # 5050

# 2
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 3
colors = ["red", "green", "blue"]
for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")
```

### 🔗 Agli class
*"Agli class — doosra loop: `while`. Yeh tab tak chalta hai JAB TAK koi condition sach hai. Aur yahi loop agent ke dil mein dhadakta hai."*

---

## CLASS 19 — while Loops & Loop Control

*"`for` loop tab use karte hain jab humein pata ho kitni baar chalना hai. Par jab humein nahi pata — 'sahi password aane TAK poochte raho' — tab `while` loop aata hai. Aur dhyaan dena: AGENT KA POORA DIMAAG EK `while` LOOP HAI."*

### 🎯 Today's goal
`while` loop, aur control words `break`, `continue`, `pass`, plus `any`/`all`.

### 👨‍🏫 Concept 1 — while loop

> **📖 Technical definition — `while` loop:** A `while` loop repeatedly executes its body as long as its boolean condition remains true. The condition is checked before each pass, so the body may run zero or more times.

*"`while` ka matlab: 'jab tak yeh condition True hai, yeh block dohraate raho.'"*
```python
count = 1

while count <= 5:
    print(count)
    count = count + 1      # yeh line BAHUT zaroori hai
```
Output:
```
1
2
3
4
5
```
*"Har round ke end mein `count` 1 badhta hai. Jab `count` 6 ho jaata hai, condition False ho jaati hai, loop ruk jaata hai."*

### 👨‍🏫 ⚠️ Concept 2 — infinite loop (sabse bada khatra)
```python
count = 1
while count <= 5:
    print(count)
    # count badhaana BHOOL gaye → count hamesha 1 → loop kabhi nahi rukta!
```
*"Agar condition kabhi False na ho, loop HAMESHA chalta rahega — screen bhar jaayegi. Isे infinite loop bolte hain. Rokne ke liye terminal mein `Ctrl + C` dabao. Hamesha confirm karo ki loop ke andar kuch condition ko False ki taraf le ja raha hai."*

### 👨‍🏫 Concept 3 — break aur continue

> **📖 Technical definition — `break` and `continue`:** `break` immediately terminates the innermost enclosing loop. `continue` skips the rest of the current iteration and proceeds to the next pass of the loop.

- **`break`** = loop turant CHHOD do.
- **`continue`** = yeh round CHHOD do, agle par chalo.
```python
# break example — 3 par ruk jao
for i in range(1, 10):
    if i == 4:
        break
    print(i)            # 1, 2, 3
```
```python
# continue example — even numbers skip karo
for i in range(1, 7):
    if i % 2 == 0:
        continue
    print(i)            # 1, 3, 5
```

### 👨‍🏫 Concept 4 — `pass` (kuch mat karo, placeholder)
```python
for i in range(3):
    pass        # "abhi kuch nahi karna, baad mein bharoonga" — error se bachata hai
```
*"`pass` ek khaali jagah-bharne wala word hai. Jab Python ko ek block chahiye par aapke paas abhi code nahi, `pass` likh do."*

### 👨‍🏫 Concept 5 — `any` aur `all`

> **📖 Technical definition — `any()` and `all()`:** `any()` returns `True` if at least one element of an iterable is truthy; `all()` returns `True` only if every element is truthy (and `True` for an empty iterable).

```python
marks = [45, 67, 88, 30]

print(all(m >= 33 for m in marks))   # False — sab pass nahi (30 fail)
print(any(m >= 80 for m in marks))   # True  — kam se kam ek 80+ (88)
```
*"`all` = sabhi True? `any` = koi ek True? Quick checks ke liye super handy."*

### 💻 Demo — password with limited attempts
```python
correct_password = "python123"
attempts = 0

while attempts < 3:
    guess = input("Enter password: ")
    if guess == correct_password:
        print("Access granted ✅")
        break
    else:
        attempts = attempts + 1
        print(f"Wrong! {3 - attempts} attempts left")

if attempts == 3:
    print("Account locked 🔒")
```
*"Dekho yahan dono cheezein hain: `while` (3 baar tak try), aur `break` (sahi password par turant nikal jao). Yeh real software jaisa pattern hai."*

### ❌ Common mistakes
```python
# 1) counter badhaana bhool jaana → infinite loop
# 2) galat comparison
count = 1
while count = 5:        # ❌ single '=' — '==' ya '<=' chahiye
    ...
```

### 🔗 Agentic link
*"Yeh sabse bada idea hai is week ka: **agent ka loop ek `while` loop hai.** 'JAB TAK kaam pura na ho: socho → tool use karo → result dekho.' Aur `break` tab lagta hai jab goal achieve ho jaaye, ya max attempts khatam ho. Aaj aapne agent ki dhadkan likhi hai."*

### ✍️ Homework
1. 10 se 1 tak ulta countdown print karo (`while` se), aur end mein "Blast off!".
2. User se numbers maangte raho jab tak woh "stop" na likhe; phir total sum print karo.
3. `break` use karke: 1 se loop chalao, jaise hi koi number 50 ke paar jaaye, ruk jao.

**Answers:**
```python
# 1
count = 10
while count >= 1:
    print(count)
    count = count - 1
print("Blast off!")

# 2
total = 0
while True:
    entry = input("Enter a number (or 'stop'): ")
    if entry == "stop":
        break
    total = total + int(entry)
print(f"Total: {total}")

# 3
num = 10
while True:
    print(num)
    if num > 50:
        break
    num = num + 15
```

### 🔗 Agli class
*"Agli class — loops ke andar loops (patterns banayenge!), aur ek naya saaf tareeka decisions ka: `match`/`case`. Phir do mini-projects."*

---

## CLASS 20 — Nested Loops & match/case (Mini Projects)

*"Aaj week ka finale: loop ke andar loop (powerful patterns), `match`/`case` (lambe if/elif ka saaf version), aur do real games/tools. Belt baandh lo!"*

### 🎯 Today's goal
Nested loops samajhna, `match`/`case` se routing, aur 2 mini-projects banana.

### 👨‍🏫 Concept 1 — Nested loop (loop ke andar loop)

> **📖 Technical definition — Nested loop:** A nested loop is a loop placed inside the body of another loop. For every single pass of the outer loop, the inner loop runs through all of its iterations completely.

*"Bahar wala loop ek baar chalega, par har baar andar wala loop POORA chalega."*
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}-{j}", end="  ")
    print()             # har row ke baad nayi line
```
Output:
```
1-1  1-2  1-3  
2-1  2-2  2-3  
3-1  3-2  3-3  
```
*"`print(end="  ")` ka matlab — nayi line mat daalo, do space daalo. Isse cheezein ek hi row mein rehti hain. Khaali `print()` row khatam karta hai."*

**Star pattern (classic):**
```python
for i in range(1, 5):
    print("*" * i)
```
Output:
```
*
**
***
****
```
*"Yaad hai `"*" * i`? String ko repeat karta hai — pichle week dekha tha. Ab loop ke saath pattern ban gaya."*

### 👨‍🏫 Concept 2 — `match` / `case` (saaf routing)

> **📖 Technical definition — `match` / `case`:** Structural pattern matching compares a subject value against a series of `case` patterns and runs the block of the first pattern that matches. The wildcard pattern `_` matches anything and acts as a default.

*"Jab ek hi cheez ki kai possible values check karni ho, lamba `if/elif/elif` ki jagah `match` zyada saaf lagta hai."*
```python
command = input("Enter command (start/stop/pause): ")

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case _:
        print("Unknown command")
```
*"`case _:` woh 'baaki sab' wala case hai (jaise `else`). Padho: 'command ko match karo: agar "start" → ..., agar "stop" → ..., warna → unknown.'"*

### 💻 Mini Project 1 — Menu Calculator (match se route)
```python
print("=== Simple Calculator ===")
a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operation (+ - * /): ")

match op:
    case "+":
        print(f"Result: {a + b}")
    case "-":
        print(f"Result: {a - b}")
    case "*":
        print(f"Result: {a * b}")
    case "/":
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print(f"Result: {a / b}")
    case _:
        print("Unknown operation")
```
*"Dekho — humne is week ka sab kuch use kiya: input, conversion, match, aur ek nested if (divide-by-zero check). Yeh ek real tool hai!"*

### 💻 Mini Project 2 — Number Guessing Game
```python
import random

secret = random.randint(1, 100)     # 1 se 100 ke beech random number
attempts = 0

print("=== Guess the number (1-100) ===")

while True:
    guess = int(input("Your guess: "))
    attempts = attempts + 1

    if guess < secret:
        print("Too low! ⬆️")
    elif guess > secret:
        print("Too high! ⬇️")
    else:
        print(f"Correct! 🎉 You got it in {attempts} attempts")
        break
```
*"`import random` ek ready-made tool laata hai. `random.randint(1, 100)` ek secret number choose karta hai. Phir `while True` + `break` se hum tab tak khelte hain jab tak sahi guess na ho. Yeh sabse mazedaar program hai jo aapne ab tak banaya!"*

### ❌ Common mistakes
```python
# match mein colon aur indentation zaroori
match x:
    case 1
        print("one")    # ❌ case ke baad ':' bhool gaye

# nested loop mein galat indentation se logic badal jaata hai — dhyaan se indent karo
```

### 🔗 Agentic link
*"`match`/`case` agent ke liye perfect hai: model bolta hai kaunsa tool chahiye ('calculator' / 'search' / 'weather'), aur hum `match tool_name:` se sahi function par route karte hain — lambe `if/elif` se kahin saaf. Aur nested loops? Agent har document ke har chunk par loop karta hai. Aaj sab connect ho gaya."*

### ✍️ Homework
1. Nested loop se 1–5 ka right-angle star triangle banao.
2. Menu calculator ko run karke saare 4 operations test karo.
3. Number guessing game khelo aur jeeto!

**Answers:**
```python
# 1
for i in range(1, 6):
    print("*" * i)
# Output:
# *
# **
# ***
# ****
# *****

# 2 aur 3 — upar wale projects run karo
```

### 🏁 Week 2 wrap-up*"Dekho is week aapne kya power haasil ki:*
- *`if/elif/else` — program ab SOCHTA hai (Class 16)*
- *Nested + ternary — layered decisions (Class 17)*
- *`for` + range + enumerate/zip — cheezein process karna (Class 18)*
- *`while` + break/continue — agent ka loop (Class 19)*
- *Nested loops + match + 2 real projects (Class 20)*

*Ab aapke programs decisions le sakte hain aur kaam repeat kar sakte hain — yahi ek agent ka basic dimaag hai. Next week hum bahut saara data ek saath rakhna sikhenge (lists). Shabaash, agli class mein milte hain!"*

### 📝 Weekend revision task
**Number Guessing Game** ko ek blank file se, bina notes dekhe, dobara banao. Agar ho gaya — aapne Week 2 sach mein master kar liya.

---

## 🎤 Industry Interview Questions — Week 2

> Real interview-style questions covering this week's topics, with model answers (in English). Try to answer them yourself first, then read the solution.

**Q1. Which values are "falsy" in Python?**

The following evaluate to `False` in a boolean context: `False`, `None`, any zero number (`0`, `0.0`), and any empty collection or string (`""`, `[]`, `{}`, `()`, `set()`). Everything else is "truthy". This lets you write `if items:` instead of `if len(items) > 0:`. Be careful: `0` and `""` are valid values that are also falsy, so `if not value:` will treat a real `0` the same as a missing value — use `if value is None:` when you specifically mean "not provided".

**Q2. Explain the difference between `break`, `continue`, and `pass`.**

`break` exits the innermost loop immediately. `continue` skips the rest of the current iteration and jumps to the next one. `pass` does nothing at all — it is a syntactic placeholder used where a statement is required (an empty function or branch you'll fill in later). They are often confused, but only `break` and `continue` change control flow.

**Q3. When would you use a `for` loop versus a `while` loop?**

Use `for` when you are iterating over a known collection or a fixed range — you know (or the iterable knows) how many times to go around. Use `while` when you loop until a *condition* changes and you don't know the count in advance, such as retrying until success, or an agent loop that runs "until the task is done". The main risk with `while` is forgetting to update the condition, causing an infinite loop, so always include a guaranteed exit (or a `max_steps` safety counter).

**Q4. Why prefer `enumerate()` and `zip()` over indexing with `range(len(...))`?**

`enumerate(items)` gives you `(index, item)` pairs directly, which is cleaner and less error-prone than `for i in range(len(items)): item = items[i]`. `zip(a, b)` iterates two (or more) sequences in lockstep, giving paired elements without manual indexing, and it stops at the shortest one. Both make the intent obvious and avoid off-by-one and IndexError bugs — this is considered idiomatic ("Pythonic") code.

**Q5. What does `match`/`case` offer over a long `if/elif` chain?**

`match`/`case` (structural pattern matching, Python 3.10+) is cleaner for routing on a single value or on the *shape* of data — it can destructure tuples, dicts, and objects, and bind variables in the pattern. For simple value routing it reads better than a long `elif` chain. For range checks or complex boolean logic, `if/elif` is still the right tool. In agent code it's handy for dispatching on a command name or an action type.
