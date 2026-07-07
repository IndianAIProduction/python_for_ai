# WEEK 1 — Data & Variables (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> **Week promise:** *"Is week hum computer ko information YAAD karna sikhayenge (variables), numbers aur text handle karna, aur user se baat karna. Week ke end tak aap ek real interactive program banaoge."*

---

## CLASS 11 — Variables: The Computer's Memory Boxes

*"Pichle week humne fixed text print kiya. Par real programs ko cheezein YAAD rakhni padti hain — aapka name, score, cart total. Aaj hum variables seekhenge — programming ke memory boxes."*

### 🎯 Today's goal
Variables banana, values store karna, change karna, aur print karna.

### 👨‍🏫 Concept — variable kya hai? (easy analogy)

> **📖 Technical definition — Variable:** A variable is a named reference that binds an identifier (its name) to a value stored in the computer's memory. The name lets you read that value later and reassign it to a new value at any time.

*"Ek labelled box socho. Aap usme kuch rakhte ho, aur box par ek naam likh dete ho taaki baad mein dhoondh sako. Bas wahi ek variable hai — ek named box jo value store karta hai."*

```python
name = "Asha"
age = 17
```

*"Ise aise padho: 'name ko Asha banao. age ko 17 banao.' Yeh `=` maths wale 'equal to' jaisa NAHI hai. Yahan `=` ka matlab hai 'right-side ki value ko left-side ke box mein daal do.' Bolo 'gets' → 'name gets Asha'."*

> **Ek choti baat (zaroor dhyaan do):** `"Asha"` quotes ke andar hai kyunki woh **text** hai, par `17` bina quotes ke hai kyunki woh **number** hai. Rule simple: text ko hamesha quotes chahiye, numbers ko nahi. Iski poori detail Class 12 mein aayegi — abhi bas itna yaad rakho.

### 💻 Demo
```python
name = "Asha"
age = 17
city = "Mumbai"

print(name)
print(age)
print(city)
```
Output:
```
Asha
17
Mumbai
```

*"Dhyaan do: `name` (bina quotes) box ke andar ki VALUE print karta hai (Asha). Agar main `print("name")` quotes ke SAATH likhun, toh woh literally 'name' word print karega. Quotes = literal text; bina quotes = variable ki value. Yeh shuru mein sabko confuse karta hai — achhe se yaad rakhna."*

Difference live dikhao:
```python
print("name")   # prints: name
print(name)     # prints: Asha
```

### 👨‍🏫 Variables CHANGE ho sakte hain (isliye "variable" bolte hain)
```python
score = 10
print(score)    # 10
score = 25      # box mein ab nayi value hai
print(score)    # 25
```
*"Purani value replace ho jaati hai. Box mein hamesha sabse latest cheez rehti hai jo aapne daali."*

### 👨‍🏫 Naming rules (industry standard — abhi sahi se seekho)
**Rules (follow karo warna error):**
- Letters, numbers, underscore `_` use kar sakte ho.
- Number se shuru NAHI kar sakte. (`2name` ❌, `name2` ✅)
- Spaces nahi. (`my name` ❌)
- Case-sensitive: `Age` aur `age` ALAG boxes hain.

**Style (professionals aise karte hain — `snake_case`):**
```python
first_name = "Rahul"     # ✅ good: lowercase, words _ se joined
total_marks = 480        # ✅ good
firstName = "Rahul"      # chalega, par Python style nahi
x = 480                  # chalega, par naam meaningless — avoid karo
```
*"Clear names use karo. `total_marks` ek kahaani batata hai; `x` kuch nahi batata. Industry mein readable names ki respect hoti hai."*

### ❌ Common mistakes
```python
1name = "Asha"    # ❌ SyntaxError — number se shuru nahi kar sakte
my name = "Asha"  # ❌ SyntaxError — space allowed nahi
print(Name)       # ❌ NameError agar box ka naam 'name' hai (capital N alag hai)
```

### 🔗 Agentic link
*"Ek AI agent ko user ka goal, chat history, aur har tool ka result yaad rakhna padta hai. YEH SAB variables mein store hota hai. Ise master karo aur aapne agent ki 'memory' master kar li."*

### ✍️ Homework
Inhe achhe naam wale variables mein store karke print karo: apna name, age, city, favourite subject, dream job.

**Sample answer:**
```python
student_name = "Priya"
student_age = 17
student_city = "Delhi"
favourite_subject = "Computer Science"
dream_job = "AI Engineer"

print(student_name)
print(student_age)
print(student_city)
print(favourite_subject)
print(dream_job)
```

### 🔗 Agli class
*"Agli class — numbers aur maths. Computer ko apna calculator banayenge."*

---

## CLASS 12 — Numbers & Arithmetic

*"Computers calculate karne ke liye hi bane the. Aaj hum Python ko ek super-calculator ki tarah use karenge aur number types seekhenge."*

### 🎯 Today's goal
`int` aur `float` use karna, saare arithmetic operators, aur operator precedence samajhna.

### 👨‍🏫 Concept — do tarah ke numbers

> **📖 Technical definition — `int` and `float`:** An `int` (integer) is a whole number with no fractional part and unlimited precision in Python. A `float` (floating-point number) represents a real number with a decimal part, stored in a fixed-precision binary format.

- **`int`** = integer = whole number, no decimal. `5`, `100`, `-7`, `0`.
- **`float`** = floating-point = decimal WALA number. `3.14`, `99.5`, `-0.5`.

```python
marks = 95          # int
percentage = 87.5   # float
```
*"Simple rule: cheezein count karna → int (number of students). Cheezein measure karna → float (height, price, average)."*

### 👨‍🏫 Arithmetic operators (ek twist ke saath)

> **📖 Technical definition — Arithmetic operator:** An arithmetic operator is a symbol that performs a mathematical operation on numeric operands and produces a numeric result (for example `+`, `-`, `*`, `/`, `//`, `%`, and `**`).

```python
a = 17
b = 5

print(a + b)    # 22   addition
print(a - b)    # 12   subtraction
print(a * b)    # 85   multiplication
print(a / b)    # 3.4  division (HAMESHA float deta hai)
print(a // b)   # 3    floor division (decimal phenk deta hai)
print(a % b)    # 2    modulus (REMAINDER)
print(a ** b)   # 1419857   power (17 ki power 5)
```

*"Teen special operators jo students ko gehraai se samajhne hain:"*
- `/` → normal division → hamesha float. `10 / 2` is `5.0`, `5` nahi.
- `//` → floor division → sirf whole part rakhta hai. `17 // 5` = `3`.
- `%` → modulus → remainder. `17 % 5` = `2`. **Super useful** — jaise `number % 2 == 0` check karta hai ki number even hai!

### 👨‍🏫 Operator precedence (basically BODMAS)

> **📖 Technical definition — Operator precedence:** Operator precedence is the set of rules that determines the order in which operators are evaluated in an expression when parentheses are not used. Operators with higher precedence are applied before those with lower precedence.

*"Python maths ke rules follow karta hai: Brackets pehle, phir power, phir × ÷, phir + −."*
```python
print(2 + 3 * 4)      # 14, 20 NAHI (× before +)
print((2 + 3) * 4)    # 20 (brackets pehle)
print(2 ** 3 + 1)     # 9 (power pehle: 8 + 1)
```
*"Confusion ho toh BRACKETS USE KARO. Yeh aapka intent clear karte hain aur bugs rokte hain. Industry tip: cleverness se zyada clarity important hai."*

### 💻 Demo — real Indian example
```python
# Ek shopkeeper ka bill
price_per_kg = 40
quantity_kg = 3
total = price_per_kg * quantity_kg
print(total)             # 120

# Restaurant bill dosto mein split karna
bill = 1000
friends = 3
each_pays = bill / friends
print(each_pays)         # 333.33...
```

### ❌ Common mistakes
```python
print(10 / 0)   # ❌ ZeroDivisionError — zero se divide nahi kar sakte
print("5" + 3)  # ❌ TypeError — text + number allowed nahi (kal fix karenge)
```

### 🔗 Agentic link
*"AI mein andar sab kuch numbers hi hai: ek prompt kitne 'tokens' (word-pieces) use karta hai, cost rupees mein, 'temperature' setting, do text ke beech similarity score. Aap yeh maths constantly karoge."*

### ✍️ Homework
1. Radius 7 wale circle ka area nikalo (use `3.14159 * 7 ** 2`).
2. Ek student ne 500 mein se 425 marks paaye. Percentage print karo.
3. `%` use karke check karo ki 2026 ko 4 se divide karne par remainder 0 aata hai ya nahi.

**Answers:**
```python
radius = 7
area = 3.14159 * radius ** 2
print(area)                 # 153.93791

marks = 425
total = 500
percentage = marks / total * 100
print(percentage)           # 85.0

print(2026 % 4)             # 2  (toh 2026, 4 se divisible NAHI hai)
```

### 🔗 Agli class
*"Agli class — text (strings) aur magical f-string. Kyunki AI ko bheje gaye prompts sirf text hain, yeh sabse important classes mein se ek hai."*

---

## CLASS 13 — Strings & f-strings

*"Ek 'string' bas text hai — characters ki ek string. Aapka name, ek message, ChatGPT ko ek prompt — sab strings. Aaj hum text master karenge, aur f-string seekhenge, jo aap apni poori AI career mein har din use karoge."*

### 🎯 Today's goal
Strings banana, join karna, aur f-strings se variables ko text mein daalna.

### 👨‍🏫 Concept — string kya hai?

> **📖 Technical definition — String:** A string (`str`) is an immutable, ordered sequence of characters used to represent text. Once created, its contents cannot be changed in place.

*"Quotes ke andar koi bhi text ek string hai. Single `' '` ya double `" "` quotes dono chalte hain — bas consistent raho."*
```python
name = "Rahul"
message = 'Welcome to class'
```

**Multi-line strings** triple quotes use karte hain:
```python
para = """This is line one.
This is line two."""
print(para)
```

### 👨‍🏫 Strings ko join karna — PURANA tareeka (aur uska dard)
```python
first = "Virat"
last = "Kohli"
full = first + " " + last     # + strings ko jodta hai ("concatenation")
print(full)                   # Virat Kohli
```
*"`+` strings ko glue karta hai. Dhyaan do humne beech mein `" "` (ek space) add kiya, warna 'ViratKohli' aata. Ab problem dekho:"*
```python
age = 35
print("Age is " + age)        # ❌ TypeError! text + number glue nahi hota
print("Age is " + str(age))   # ✅ chalta hai, par ugly — str() number ko text banata hai
```
*"Yeh `+` aur `str()` ka jugglery painful hai. Ab hero ki entry: f-string."*

### 👨‍🏫 ⭐ f-strings — modern, easy tareeka (SABSE IMPORTANT)

> **📖 Technical definition — f-string:** An f-string (formatted string literal) is a string prefixed with `f` in which expressions inside curly braces `{ }` are evaluated at runtime and their results are inserted into the text.

*"Quote se pehle letter `f` lagao. Phir text ke andar kisi bhi variable ko seedhe `{ }` mein daal do. Python khud fill kar dega."*
```python
name = "Virat"
age = 35
print(f"My name is {name} and I am {age} years old")
# My name is Virat and I am 35 years old
```
*"Na `+`, na `str()`, na sirdard. Yeh numbers ko bhi automatically handle karta hai. YEH professionals use karte hain. Aaj se, HAMESHA f-strings use karo."*

**Aap `{ }` ke andar maths bhi kar sakte ho:**
```python
price = 40
qty = 3
print(f"Total bill is {price * qty} rupees")   # Total bill is 120 rupees
```

**Decimals format karna (bahut useful):**
```python
pi = 3.14159265
print(f"Pi rounded is {pi:.2f}")   # Pi rounded is 3.14
```
*"`:.2f` ka matlab 'decimal ke baad 2 digits dikhao'. Money aur percentage ke liye great."*

### 💻 Demo
```python
student = "Asha"
marks = 425
total = 500
percent = marks / total * 100
print(f"{student} scored {marks}/{total} = {percent:.1f}%")
# Asha scored 425/500 = 85.0%
```

### ❌ Common mistakes
```python
print("Hello {name}")    # ❌ f bhool gaye → literally print hoga: Hello {name}
print(f"Hello {name")    # ❌ } band karna bhool gaye
```

### 🔗 Agentic link
*"Ek 'prompt' (AI ko bheji gayi instruction) bas ek bada string hai. Hum prompts f-strings se banate hain — usme user ka question, data, rules daalte hain. Ek example jo aap jaldi likhoge:"*
```python
user_question = "What is the capital of France?"
prompt = f"Answer this question clearly: {user_question}"
```

### ✍️ Homework
1. Apna name aur city store karke f-string se print karo "Hi, I am ___ from ___."
2. `cost = 250` aur `qty = 4` store karke total f-string se print karo.
3. `marks = 367` store karo, 450 mein se percentage 2 decimals ke saath print karo.

**Answers:**
```python
name = "Priya"
city = "Jaipur"
print(f"Hi, I am {name} from {city}.")

cost = 250
qty = 4
print(f"Total is {cost * qty} rupees")

marks = 367
print(f"Percentage: {marks / 450 * 100:.2f}%")
```

### 🔗 Agli class
*"Agli class — True/False (booleans), data types check karna, aur types ke beech convert karna."*

---

## CLASS 14 — Booleans, Types & Type Conversion

*"Aaj hum seekhenge computer YES/NO questions ka answer kaise deta hai (booleans), data ka TYPE kaise check karte hain, aur ek type ko doosre mein kaise convert karte hain. Yeh decision-making ke building blocks hain."*

### 🎯 Today's goal
`bool`, `type()`, conversion functions, comparison/logical operators, Python data types ka map, aur reserved keywords samajhna.

### 👨‍🏫 Concept 1 — Booleans (True / False)

> **📖 Technical definition — Boolean:** A boolean (`bool`) is a data type with exactly two possible values, `True` and `False`, used to represent the truth value of a condition.

*"Ek boolean ki sirf do values ho sakti hain: `True` ya `False`. Capital T aur F, bina quotes. Yeh computer ke haan/naa bolne ka tareeka hai."*
```python
is_raining = True
is_holiday = False
print(is_raining)    # True
```

### 👨‍🏫 Concept 2 — Comparison operators booleans BANATE hain

> **📖 Technical definition — Comparison operator:** A comparison (relational) operator compares two values and returns a boolean result (`True` or `False`). Examples include `==`, `!=`, `<`, `>`, `<=`, and `>=`.

*"Jab aap do cheezein compare karte ho, answer hamesha True ya False hota hai."*
```python
print(10 > 5)      # True
print(10 < 5)      # False
print(10 == 10)    # True   (== matlab 'equal hai?' — DO equals!)
print(10 != 5)     # True   (!= matlab 'not equal')
print(10 >= 10)    # True
print(7 <= 3)      # False
```
*"⚠️ BAHUT bada point: `=` (ek) box mein value daalta hai. `==` (do) POOCHTA hai 'kya yeh equal hain?'. Inhe mix karna #1 beginner bug hai. Bolo: 'single equals = store, double equals = compare.'"*

### 👨‍🏫 Concept 3 — Logical operators (and / or / not)

> **📖 Technical definition — Logical operator:** A logical operator combines or negates boolean expressions. `and` is true only when both operands are true, `or` is true when at least one operand is true, and `not` inverts a boolean value.

*"Haan/naa questions ko combine karo:"*
```python
age = 20
has_id = True

print(age >= 18 and has_id)   # True  — DONO true hone chahiye
print(age >= 18 or has_id)    # True  — kam se kam EK true
print(not has_id)             # False — ulta kar deta hai
```
*"`and` = strict (saari conditions true). `or` = lenient (koi ek true). `not` = opposite."*

### 👨‍🏫 Concept 4 — Data types ka poora parivaar (family map)

> **📖 Technical definition — Data type:** A data type is a category that defines the kind of value an object holds and the operations allowed on it. Python's core built-in types include numbers (`int`, `float`), text (`str`), truth values (`bool`), collections (`list`, `tuple`, `dict`, `set`), and the special "no value" type (`NoneType`).

*"Ab tak humne 4 types dekhe: `int`, `float`, `str`, `bool`. Par Python mein aur bhi hain. Ek nazar ka MAP le lo — abhi sirf pehchaan banao, detail baad mein aayegi."*

| Type | Kya store karta hai | Example | Kab detail aayega |
|------|---------------------|---------|-------------------|
| `int` | Poore numbers | `17`, `-4` | ✅ pata hai (Class 12) |
| `float` | Decimal numbers | `3.14`, `5.0` | ✅ pata hai (Class 12) |
| `str` | Text | `"Asha"` | ✅ pata hai (Class 13) |
| `bool` | `True` / `False` | `True` | ✅ aaj |
| `list` | Cheezon ki changeable line | `[1, 2, 3]` | Week 3 |
| `tuple` | Cheezon ki fixed line | `(1, 2)` | Week 3 |
| `dict` | Naam→value pairs | `{"age": 17}` | Week 4 |
| `set` | Unique cheezein | `{1, 2, 3}` | Week 4 |
| `NoneType` | "Koi value nahi" | `None` | Week 5 |

*"Yeh table ratna nahi hai — bas itna samajh lo ki data ke alag-alag 'shapes' hote hain. Numbers, text, haan/naa, aur cheezon ke groups. Har type ke apne kaam aur apne rules hote hain. Neeche wale `type()` se hum kisi bhi value ka type LIVE check kar sakte hain."*

### 👨‍🏫 Concept 5 — `type()` se type check karna

> **📖 Technical definition — Data type and `type()`:** A data type defines the kind of value an object holds and the operations allowed on it. The built-in `type()` function returns the type (class) of the object passed to it.

```python
print(type(5))         # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
```
*"`type()` batata hai box mein kis KIND ka data hai. Bahut useful jab data bahar se aata hai aur aapko pakka nahi pata woh kya hai."*

### 👨‍🏫 Concept 6 — Type conversion (casting)

> **📖 Technical definition — Type conversion (casting):** Type conversion is the process of changing a value from one data type to another, using functions such as `int()`, `float()`, and `str()`. Converting to `int` truncates any decimal part rather than rounding.

*"Kabhi-kabhi data galat type ka hota hai aur hum convert karte hain."*
```python
age_text = "17"          # yeh ek STRING hai (quotes dekho)
age_number = int(age_text)   # string → int convert
print(age_number + 3)    # 20  ✅ ab maths chalta hai

print(str(100))   # "100"  → number to string
print(float(5))   # 5.0    → int to float
print(int(3.9))   # 3      → float to int (decimal KAAT deta hai, round NAHI karta!)
```
*"⚠️ `int(3.9)` `3` deta hai, `4` nahi. Yeh kaatta hai, round nahi karta. Yaad rakho."*

### 👨‍🏫 Concept 7 — Reserved keywords (jo naam ke roop mein use NAHI kar sakte)

> **📖 Technical definition — Keyword:** A keyword (reserved word) is a word that Python reserves for its own syntax, such as `if`, `for`, or `def`. Because the language already gives these words a special meaning, you cannot use them as variable, function, or class names.

*"Class 11 mein humne naming rules dekhe the — spaces nahi, number se shuru nahi. Ek aur rule reh gaya tha: Python ke apne KUCH SPECIAL words hote hain (jaise `if`, `for`, `True`), jo usne khud ke liye reserve kar rakhe hain. Inhe aap apne box ka naam nahi bana sakte."*

Poori list Python khud dikha deta hai:
```python
import keyword
print(keyword.kwlist)       # saari reserved words ki list
print(len(keyword.kwlist))  # kitni hain (~35)
```

Sabse common wale jo aap is course mein baar-baar dekhoge:

| | | | |
|---|---|---|---|
| `if` | `elif` | `else` | `for` |
| `while` | `def` | `return` | `class` |
| `import` | `from` | `and` | `or` |
| `not` | `in` | `is` | `None` |
| `True` | `False` | `try` | `except` |

*"Inhe abhi ratna zaroori nahi — jaise-jaise course chalega, yeh khud yaad ho jayenge. Bas itna samajh lo: agar koi word 'special kaam' karta hai, toh woh variable ka naam nahi ban sakta."*

Kya hota hai jab aap koshish karte ho:
```python
class = 5      # ❌ SyntaxError — 'class' reserved word hai
for = "Asha"   # ❌ SyntaxError — 'for' reserved word hai
if = 10        # ❌ SyntaxError — 'if' reserved word hai
```
*"💡 Chhota trick: achhe code editors mein reserved keywords ka RANG alag dikhta hai (aksar blue/purple). Agar aapke variable ke naam ka rang badal jaaye, samajh jao woh reserved word hai — koi aur naam chuno, jaise `class_name` ya `for_loop`."*

### ❌ Common mistakes
```python
if age = 18:        # ❌ == ki jagah single = use kiya
print(int("abc"))   # ❌ ValueError — "abc" number nahi hai
class = "A"         # ❌ SyntaxError — reserved keyword ko naam banaya
```

### 🔗 Agentic link
*"Jab koi AI tool data return karta hai, ya user kuch type karta hai, woh usually STRING ke roop mein aata hai. Maths ya logic karne se pehle hum uska type check karke convert karte hain. Aur agent ke decisions ('tool call karu? kaam ho gaya?') booleans hain — bilkul jo aaj seekha."*

### ✍️ Homework
1. Do boolean variables banao aur unpar `and`, `or`, `not` ka result print karo.
2. String `"45"` ko number mein convert karke 5 add karo.
3. Predict phir check karo: `10 == 10.0` → True ya False? `int(7.8)` → ?
4. `import keyword` karke saari reserved words print karo, aur unme se koi 3 words apni copy mein likho.

**Answers:**
```python
is_sunny = True
is_weekend = False
print(is_sunny and is_weekend)   # False
print(is_sunny or is_weekend)    # True
print(not is_weekend)            # True

num = int("45")
print(num + 5)                   # 50

print(10 == 10.0)                # True (same value)
print(int(7.8))                  # 7 (.8 kaat diya)

import keyword
print(keyword.kwlist)            # e.g. ['False', 'None', 'True', 'and', ...]
# 3 words: if, for, def
```

### 🔗 Agli class
*"Agli class — hum programs ko user se BAAT karwayenge input() se, aur apna pehla real interactive project banayenge!"*

---

## CLASS 15 — Input/Output, String Methods & Mini Project

*"Ab tak HUMNE saari values likhi. Aaj PROGRAM, USER se input maangega — yahi software ko interactive banata hai. Phir hum ek real project banayenge."*

### 🎯 Today's goal
`input()` use karna, string methods se text clean karna, aur ek interactive program banana.

### 👨‍🏫 Concept 1 — `input()` user se poochta hai

> **📖 Technical definition — `input()`:** `input()` is a built-in function that pauses the program, reads a line of text typed by the user, and returns it as a string (always a string, even when the user types digits).

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```
*"`input()` aapka question dikhata hai, user ke type karke Enter dabane ka wait karta hai, aur jo type kiya use variable mein store karta hai."*

### 👨‍🏫 ⚠️ input() ka #1 trap — yeh HAMESHA string deta hai!
```python
age = input("Your age: ")    # user 17 type karta hai
print(age + 1)               # ❌ ERROR! age "17" (text) hai, 17 nahi
```
*"User number type kare tab bhi, `input()` use STRING ke roop mein deta hai. Maths ke liye convert karo:"*
```python
age = int(input("Your age: "))    # turant convert
print(f"Next year you'll be {age + 1}")   # ✅ chalta hai
```
*"Yeh pattern yaad rakho: whole numbers ke liye `int(input(...))`, decimals ke liye `float(input(...))`. Yeh single trap har beginner ko pakadta hai — par aapko nahi, kyunki ab aap jaante ho."*

### 👨‍🏫 Concept 2 — kaam ke string methods (user text clean karna)

> **📖 Technical definition — String method:** A string method is a built-in function attached to a string object that returns a new, transformed string (for example `.strip()`, `.upper()`, `.lower()`, `.split()`, and `.replace()`). Because strings are immutable, the original string is never changed.

*"Users messy type karte hain — extra spaces, galat case. Yeh methods use karte hain clean karne ke liye:"*
```python
text = "  Hello World  "
print(text.strip())        # "Hello World"  — bahar ke spaces hatata hai
print(text.upper())        # "  HELLO WORLD  "
print(text.lower())        # "  hello world  "
print("apple,banana,mango".split(","))   # ['apple', 'banana', 'mango']
print("I like tea".replace("tea", "coffee"))  # I like coffee
```
*"`.split(",")` text ko list mein todta hai jahan comma dikhe — lists hum next week use karenge. `.strip()` input clean karne ke liye lifesaver hai."*

### 👨‍🏫 Concept 3 — UTF-8 by default (Python 3.15)
*"Achhi khabar: Python 3.15 saari languages aur emojis ko by default perfectly handle karta hai. Toh yeh seedha chalta hai:"*
```python
greeting = "नमस्ते 🙏 Hello"
print(greeting)
```
*"Purane Python mein yeh kabhi-kabhi error deta tha. 3.15 mein smooth hai — important kyunki AI prompts mein aksar Hindi, emojis, aur kai languages hoti hain."*

### 💻 Mini Project 1 — Temperature Converter
```python
print("=== Celsius to Fahrenheit Converter ===")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
```
*"Run karo, 37 type karo, aur convert hote dekho. Aapne ek real tool bana diya!"*

### 💻 Mini Project 2 — Token-Cost Estimator (ek AI-flavoured project!)
*"AI models per 'token' (roughly ek word-piece) charge karte hain. Cost estimate karte hain — yeh us cheez ka baby version hai jo real engineers calculate karte hain."*
```python
print("=== AI Token Cost Estimator ===")
tokens = int(input("How many tokens? "))
price_per_1000 = float(input("Price per 1000 tokens (in rupees)? "))
cost = (tokens / 1000) * price_per_1000
print(f"Estimated cost: ₹{cost:.2f}")
```

### ❌ Common mistakes
```python
age = input("Age: ")
print(age * 2)      # agar user 5 type kare → "55" print hoga (string repeat!), 10 nahi
```
*"Bina `int()` ke, `"5" * 2` `"55"` ban jaata hai. Hamesha convert karo."*

### 🔗 Agentic link
*"Ek chatbot literally ek loop hai `input()` (user bolta hai) → process → `print()` (bot reply karta hai). Next week hum loop add karenge. Aur `.strip()`/`.lower()` se user text clean karna — exactly aise hum messages tidy karte hain AI model ko bhejne se pehle."*

### ✍️ Homework
1. Ek program banao jo name aur birth year poochhe, phir age print kare.
2. Ek simple bill calculator: item price aur quantity poochho, total ₹ aur 2 decimals ke saath print karo.
3. User se ek messy sentence maango, phir use stripped aur uppercase mein print karo.

**Answers:**
```python
# 1
name = input("Name: ")
birth_year = int(input("Birth year: "))
print(f"{name}, you are about {2026 - birth_year} years old")

# 2
price = float(input("Price: "))
qty = int(input("Quantity: "))
print(f"Total: ₹{price * qty:.2f}")

# 3
msg = input("Type a sentence: ")
print(msg.strip().upper())
```

### 🏁 Week 1 wrap-up*"Dekho is week aap kitna aage aa gaye:*
- *Variables — computer ki memory (Class 11)*
- *Numbers & maths (Class 12)*
- *Strings & f-strings — AI prompts ki language (Class 13)*
- *Booleans, types & conversion (Class 14)*
- *Input + aapke pehle interactive projects (Class 15)*

*Ab aap data store kar sakte ho, calculate kar sakte ho, aur user se baat kar sakte ho. Next week hum program ko DECISIONS lena aur actions REPEAT karna sikhayenge — aur tab yeh sach mein powerful lagne lagega. Bahut badhiya, agli class mein milte hain!"*

### 📝 Weekend revision task
**Token-Cost Estimator** ko ek blank file se dobara banao, BINA notes dekhe. Agar aap yeh kar lete ho, toh aapne sach mein Week 1 seekh liya.
