# WEEK 4 — Mappings & Sets (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> **Week promise:** *"Is week ka hero hai DICTIONARY — key-value data. Yeh sabse important data structure hai AI ke liye, kyunki ek LLM ka har message bilkul ek dictionary hota hai: `{"role": "user", "content": "Hello"}`. Iske baad sets aur ek-line comprehensions seekhenge."*

---

## CLASS 26 — Dictionaries Basics

*"List yaad hai? Woh items ko NUMBER (index) se rakhti hai: item 0, item 1... Par socho phone book — aap number 0,1,2 se nahi dhoondhte, aap NAAM se dhoondhte ho: 'Rahul ka number kya hai?' Iske liye chahiye DICTIONARY — jahan har value ka ek naam (key) hota hai."*

### 🎯 Today's goal
Dictionary banana, key se value nikalna, add/update/delete karna.

### 👨‍🏫 Concept 1 — dictionary kya hai

> **📖 Technical definition — Dictionary:** A dictionary (`dict`) is a mutable collection of key–value pairs. Each unique, hashable key maps to a value, allowing fast lookup, insertion, and deletion of values by key rather than by position.

*"Dictionary curly braces `{ }` se banti hai, aur har entry hoti hai `key: value`."*
```python
student = {
    "name": "Asha",
    "age": 17,
    "city": "Mumbai",
}

print(student["name"])    # Asha   — key se value milti hai
print(student["age"])     # 17
```
*"List index se value deti hai (`list[0]`), dictionary KEY se value deti hai (`dict["name"]`). Key usually ek string hota hai — ek label."*

### 👨‍🏫 Concept 2 — add aur update
```python
student = {"name": "Asha", "age": 17}

student["city"] = "Mumbai"    # nayi key add (exist nahi karti thi)
print(student)                # {'name': 'Asha', 'age': 17, 'city': 'Mumbai'}

student["age"] = 18           # purani key update (already thi)
print(student)                # {'name': 'Asha', 'age': 18, 'city': 'Mumbai'}
```
*"Simple rule: `dict[key] = value`. Agar key nahi hai → add ho jaati hai. Agar hai → uski value badal jaati hai."*

### 👨‍🏫 Concept 3 — delete aur check
```python
student = {"name": "Asha", "age": 18, "city": "Mumbai"}

del student["city"]           # key delete
print(student)                # {'name': 'Asha', 'age': 18}

print("name" in student)      # True   — key exist karti hai?
print("phone" in student)     # False
```

### 👨‍🏫 ⚠️ Concept 4 — KeyError (na-maujood key)
```python
student = {"name": "Asha"}
print(student["age"])         # ❌ KeyError — 'age' key hai hi nahi
```
*"Agar aap aisi key maango jo exist nahi karti, Python KeyError deta hai. Agli class mein hum `.get()` seekhenge jo isse safe tareeke se handle karta hai."*

### 💻 Demo — student record
```python
student = {
    "name": "Rahul",
    "marks": 85,
    "passed": True,
}

print(f"{student['name']} scored {student['marks']}")
# Rahul scored 85
```
*"Dhyaan do: f-string ke andar `{ }` ke beech `student['name']` mein SINGLE quotes use kiye, kyunki bahar already DOUBLE quotes the. Quotes mix karo, warna confusion."*

### ❌ Common mistakes
```python
student = {"name": "Asha"}
print(student[name])      # ❌ NameError — key string hai, quotes chahiye: student["name"]
print(student["Name"])    # ❌ KeyError — keys case-sensitive hain ("name" != "Name")
```

### 🔗 Agentic link
*"Yeh week ka SABSE bada idea: **ek LLM message ek dictionary hai.** Har message aisa dikhta hai:*
```python
message = {"role": "user", "content": "What is AI?"}
```
*Aur poori chat = aisi dictionaries ki ek list. Toh dictionaries master karna = AI ke saath baat karne ki language seekhna. Yeh non-negotiable hai."*

### ✍️ Homework
1. Apna ek dictionary banao: name, age, city, favourite_subject. Sab print karo.
2. Usme ek nayi key `dream_job` add karo aur `age` update karo.
3. `in` se check karo ki `city` key hai ya nahi.

**Answers:**
```python
# 1
me = {"name": "Priya", "age": 17, "city": "Jaipur", "favourite_subject": "CS"}
print(me["name"], me["age"], me["city"], me["favourite_subject"])

# 2
me["dream_job"] = "AI Engineer"
me["age"] = 18
print(me)

# 3
print("city" in me)       # True
```

### 🔗 Agli class
*"Agli class — dictionaries par loop karna, safe `.get()`, aur dictionary ke andar dictionary (nested) — jo bilkul real API data jaisa hota hai."*

---

## CLASS 27 — Dict Methods & Nesting

*"Pichli class mein humne ek key se ek value li. Aaj seekhenge poori dictionary par GHOOMNA, missing keys ko SAFELY handle karna, aur dictionary ke andar dictionary — jaise real AI/web data aata hai."*

### 🎯 Today's goal
`.keys() .values() .items()`, looping, safe `.get()`, aur nested dicts.

### 👨‍🏫 Concept 1 — `.keys() .values() .items()`

> **📖 Technical definition — `keys()`, `values()`, `items()`:** These dictionary methods return dynamic view objects: `.keys()` gives the keys, `.values()` gives the values, and `.items()` gives `(key, value)` pairs. The views reflect any later changes to the dictionary and are commonly used to iterate over it.

```python
student = {"name": "Asha", "age": 17, "city": "Mumbai"}

print(student.keys())     # dict_keys(['name', 'age', 'city'])
print(student.values())   # dict_values(['Asha', 17, 'Mumbai'])
print(student.items())    # dict_items([('name', 'Asha'), ('age', 17), ('city', 'Mumbai')])
```
*"`.keys()` saare labels, `.values()` saari values, `.items()` dono jodi-jodi mein (tuples ke roop mein — yaad hai pichle week tuples?)."*

### 👨‍🏫 Concept 2 — dictionary par loop (sabse common pattern)
```python
student = {"name": "Asha", "age": 17, "city": "Mumbai"}

for key, value in student.items():
    print(f"{key}: {value}")
```
Output:
```
name: Asha
age: 17
city: Mumbai
```
*"`.items()` se hum ek saath key AUR value dono pakad lete hain (tuple unpacking — Class 24!). Yeh dictionary ghoomne ka pro tareeka hai."*

### 👨‍🏫 Concept 3 — `.get()` (safe access, KeyError se bachao)

> **📖 Technical definition — `dict.get()`:** `.get(key, default)` returns the value stored for `key`, or the supplied `default` (or `None` if no default is given) when the key is absent. Unlike square-bracket access, it never raises a `KeyError`.

```python
student = {"name": "Asha", "age": 17}

print(student.get("age"))          # 17
print(student.get("phone"))        # None   — error NAHI, bas None
print(student.get("phone", "N/A")) # N/A    — default value de do
```
*"Difference yaad rakho: `student["phone"]` na mile toh CRASH (KeyError). `student.get("phone")` na mile toh None deta hai (no crash). Jab pakka na ho ki key hai ya nahi, hamesha `.get()` use karo — yeh professional habit hai."*

### 👨‍🏫 Concept 4 — nested dictionary (dict ke andar dict)

> **📖 Technical definition — Nested dictionary:** A nested dictionary is a dictionary whose values are themselves dictionaries (or other collections). Inner values are accessed by chaining keys, for example `data["outer"]["inner"]`, mirroring the structure of real API and JSON data.

```python
users = {
    "u1": {"name": "Asha", "age": 17},
    "u2": {"name": "Rahul", "age": 18},
}

print(users["u1"]["name"])     # Asha   — pehle u1, phir uska name
print(users["u2"]["age"])      # 18

for user_id, info in users.items():
    print(f"{user_id} -> {info['name']}, age {info['age']}")
```
Output:
```
u1 -> Asha, age 17
u2 -> Rahul, age 18
```
*"Do brackets: pehla bahar wali key, doosra andar wali. Bilkul nested list ke `grid[r][c]` jaisa, par yahan index ki jagah keys."*

### 💻 Demo — gradebook
```python
gradebook = {"Asha": 85, "Rahul": 90, "Priya": 78}

# total aur average
total = sum(gradebook.values())
average = total / len(gradebook)
print(f"Class average: {average:.1f}")     # Class average: 84.3

# topper dhoondho
topper = max(gradebook, key=gradebook.get)
print(f"Topper: {topper}")                 # Topper: Rahul
```
*"`max(gradebook, key=gradebook.get)` — Python se bolo 'us key ko do jiski VALUE sabse bdi hai'. Thoda advanced, par bahut useful. Abhi bas concept samjho."*

### ❌ Common mistakes
```python
data = {"a": 1}
for x in data:            # dict par seedhe loop sirf KEYS deta hai
    print(x)              # a   (value nahi!)
# value bhi chahiye → data.items() use karo

print(data["b"])          # ❌ KeyError — .get("b") use karo safe rehne ke liye
```

### 🔗 Agentic link
*"Real API responses (aur LLM outputs) gehre nested dicts hote hain, jaise `response["choices"][0]["message"]["content"]`. Aur `.get()` agent ke liye lifesaver hai — kabhi-kabhi koi field missing hota hai, aur `.get()` crash hone se bachata hai. Yeh skill har din kaam aayegi."*

### ✍️ Homework
1. 3 dosto ka phone book banao (naam: number) aur `.items()` se sab print karo.
2. `.get()` se ek na-maujood naam dhoondho, default "Not found" do.
3. 2 users ka nested dict banao aur dono ke naam print karo.

**Answers:**
```python
# 1
phone = {"Amit": "98765", "Sara": "91234", "Ravi": "90000"}
for name, number in phone.items():
    print(f"{name}: {number}")

# 2
print(phone.get("John", "Not found"))     # Not found

# 3
users = {"u1": {"name": "Asha"}, "u2": {"name": "Rahul"}}
print(users["u1"]["name"])                # Asha
print(users["u2"]["name"])                # Rahul
```

### 🔗 Agli class
*"Agli class — sets (unique cheezon ka collection) aur read-only dictionaries (jo galti se badal na sakein)."*

---

## CLASS 28 — Read-only Mappings & Sets

*"Aaj do cheezein: (1) SET — ek aisा collection jisme har cheez UNIQUE hoti hai, duplicates apne aap hat jaate hain. (2) Read-only dictionary — config jo lock ho jaaye taaki galti se na badle."*

### 🎯 Today's goal
Sets + union/intersection/difference, aur read-only mapping (immutable config).

### 👨‍🏫 Concept 1 — set kya hai (unique items)

> **📖 Technical definition — Set:** A set is a mutable, unordered collection of unique, hashable elements. It automatically discards duplicates and supports fast membership testing and mathematical set operations.

*"Set bhi `{ }` use karta hai, par sirf values (keys nahi). Iska superpower: duplicates AUTOMATICALLY hat jaate hain."*
```python
nums = {1, 2, 2, 3, 3, 3}
print(nums)               # {1, 2, 3}   — duplicates gaye!

# list se duplicates hatane ka famous trick:
names = ["Asha", "Rahul", "Asha", "Priya", "Rahul"]
unique = set(names)
print(unique)             # {'Asha', 'Rahul', 'Priya'}  (order fix nahi)
print(len(unique))        # 3
```
*"Dhyaan: set ka ORDER guaranteed nahi hota. Agar order chahiye toh list use karo. Set tab use karo jab sirf 'unique cheezein' chahiye."*

### 👨‍🏫 Concept 2 — set operations (maths jaise)

> **📖 Technical definition — Set operations:** Set operations combine or compare sets: union (`|`) returns all elements from both sets, intersection (`&`) returns elements common to both, and difference (`-`) returns elements in the first set that are not in the second.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)      # {1,2,3,4,5,6}   union — sab milा kar
print(a & b)      # {3, 4}          intersection — dono mein common
print(a - b)      # {1, 2}          difference — a mein hai par b mein nahi
```
*"`|` = sab jodо, `&` = common nikaalो, `-` = ek mein se doosre wale hatao. Yeh do groups compare karne ke liye perfect hai."*

### 👨‍🏫 Concept 3 — read-only dictionary (locked config)

> **📖 Technical definition — Read-only mapping:** A read-only mapping is a wrapper (such as `types.MappingProxyType`) that exposes a dictionary for reading but forbids modification. It provides an immutable, tamper-proof view of configuration or shared data.

*"Kabhi-kabhi humein ek dictionary chahiye jo PADHI jaaye par BADLI na ja sake — jaise app ki settings. Python `types.MappingProxyType` se ek read-only view deta hai:"*
```python
from types import MappingProxyType

config = {"model": "gpt", "max_tokens": 1000}
locked = MappingProxyType(config)      # read-only view

print(locked["model"])                 # gpt   — padhna chalega
locked["model"] = "other"              # ❌ TypeError — badla nahi jaa sakta
```
*"Yeh 'guarantee' deta hai: yeh config program ke beech mein galti se nahi badlegi. Tuple ne list ko lock kiya tha (Class 24) — yeh dictionary ko lock karta hai. Concept ek hi hai: jo data fixed rehna chahiye, use immutable banao."*

> **Teacher accuracy note:** Read-only mapping ka standard, reliable tareeka `MappingProxyType` hi hai (har modern Python mein available). Yeh bilkul wahi 'immutable config' kaam karta hai jiski AI projects mein zaroorat hoti hai.

### 💻 Demo — common students (do classes ke beech)
```python
class_a = {"Asha", "Rahul", "Priya", "Amit"}
class_b = {"Rahul", "Amit", "Sara"}

print(f"In both classes: {class_a & class_b}")     # {'Rahul', 'Amit'}
print(f"Only in A: {class_a - class_b}")           # {'Asha', 'Priya'}
print(f"All students: {class_a | class_b}")
```

### ❌ Common mistakes
```python
empty = {}            # ❌ yeh khaali DICTIONARY hai, set nahi!
empty = set()         # ✅ khaali set aise banta hai

s = {1, 2, 3}
print(s[0])           # ❌ TypeError — set indexable nahi (order hi nahi hota)
```

### 🔗 Agentic link
*"Sets agent mein duplicate documents ya repeated tool-results hatane ke liye use hote hain (ek hi cheez do baar process mat karo). Aur read-only config ek agent ke kai steps ke beech settings ko safe rakhta hai — koi step galti se model ya limits na badal de."*

### ✍️ Homework
1. Ek list `[1,2,2,3,4,4,5]` se duplicates hatao (set use karke).
2. Do sets banao aur unka union, intersection, difference print karo.
3. Ek config dict banao, use `MappingProxyType` se lock karo, padhne ki koshish (chalega) aur badalne ki koshish (error padho).

**Answers:**
```python
# 1
nums = [1, 2, 2, 3, 4, 4, 5]
print(set(nums))          # {1, 2, 3, 4, 5}

# 2
a = {"x", "y", "z"}
b = {"y", "z", "w"}
print(a | b)              # union
print(a & b)              # {'y', 'z'}
print(a - b)              # {'x'}

# 3
from types import MappingProxyType
cfg = MappingProxyType({"theme": "dark"})
print(cfg["theme"])       # dark
# cfg["theme"] = "light"  # TypeError: read-only
```

### 🔗 Agli class
*"Agli class — comprehensions: ek hi line mein poori list/dict banana. Yeh code ko chhota aur Pythonic banata hai."*

---

## CLASS 29 — Comprehensions

*"Aaj ek bahut khoobsurt Python feature: COMPREHENSION. Jo kaam 4 lines ke loop mein hota hai, woh ek saaf line mein. Yeh Python developers ki pehchaan hai."*

### 🎯 Today's goal
List, dict, aur set comprehensions; conditions ke saath.

### 👨‍🏫 Concept 1 — purana tareeka vs comprehension

> **📖 Technical definition — Comprehension:** A comprehension is a concise expression that builds a new list, dictionary, or set by transforming (and optionally filtering) the items of an iterable in a single line, replacing an explicit build-up loop.

*"Pehle dekho hum normally kaise karte the:"*
```python
# Purana tareeka — 1 se 5 tak ke squares
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)        # [1, 4, 9, 16, 25]
```
*"Ab wahi kaam, ek line mein — comprehension:"*
```python
squares = [n ** 2 for n in range(1, 6)]
print(squares)        # [1, 4, 9, 16, 25]
```
*"Padho: '`n ** 2` do, har `n` ke liye `range(1,6)` mein.' Format: `[<kya banao> for <item> in <collection>]`. Yeh exactly upar wale loop jaisा hai, bas chhota."*

### 👨‍🏫 Concept 2 — condition ke saath (filter)
```python
# sirf even numbers ke squares
evens = [n ** 2 for n in range(1, 11) if n % 2 == 0]
print(evens)          # [4, 16, 36, 64, 100]
```
*"Aakhir mein `if` filter lagata hai — sirf woh items jo condition pass karein. Padho: 'n ka square do, har n ke liye 1-10 mein, AGAR n even hai.'"*

### 👨‍🏫 Concept 3 — strings par comprehension
```python
words = ["Apple", "BANANA", "mango"]

lower = [w.lower() for w in words]
print(lower)          # ['apple', 'banana', 'mango']

lengths = [len(w) for w in words]
print(lengths)        # [5, 6, 5]
```

### 👨‍🏫 Concept 4 — dict aur set comprehension
```python
# dict comprehension
nums = [1, 2, 3, 4]
squares_map = {n: n ** 2 for n in nums}
print(squares_map)    # {1: 1, 2: 4, 3: 9, 4: 16}

# do lists ko dict banao (zip yaad hai?)
names = ["Asha", "Rahul"]
marks = [85, 90]
report = {name: mark for name, mark in zip(names, marks)}
print(report)         # {'Asha': 85, 'Rahul': 90}

# set comprehension
unique_lengths = {len(w) for w in ["hi", "bye", "ok"]}
print(unique_lengths) # {2, 3}
```

### 💻 Demo — clean a list of user inputs
```python
raw = ["  Asha ", "RAHUL", " priya  ", ""]

# strip + lowercase + khaali hatao, sab ek line mein
cleaned = [name.strip().lower() for name in raw if name.strip()]
print(cleaned)        # ['asha', 'rahul', 'priya']
```
*"Dekho — strip, lower, aur empty filter, sab ek line mein. Yeh exactly AI inputs clean karne wala kaam hai."*

### ❌ Common mistakes
```python
# bahut zyada ghusa dena — padhna mushkil ho jaata hai
result = [x*2 for x in range(100) if x % 2 == 0 if x > 10 if x < 90]
# ❌ agar samajh na aaye, toh normal loop hi behtar hai. Clarity > smartness.

# comprehension mein {} list ke liye galat
squares = {n**2 for n in range(3)}   # yeh SET banega, list nahi! list ke liye []
```

### 🔗 Agentic link
*"Comprehensions agent code mein har jagah hain: tool results ko transform karna `[r.strip() for r in results]`, messages ki content nikalna `[m["content"] for m in messages]`, scores filter karna. Ek line mein saaf data-transform — yeh aap roz likhoge."*

### ✍️ Homework
1. 1–20 ke saare numbers ka comprehension banao, sirf woh jo 3 se divisible hain.
2. Words ki list ko uppercase mein convert karo comprehension se.
3. `{1,2,3,4}` ke har number ka cube ek dict comprehension se banao `{num: cube}`.

**Answers:**
```python
# 1
div3 = [n for n in range(1, 21) if n % 3 == 0]
print(div3)           # [3, 6, 9, 12, 15, 18]

# 2
words = ["hi", "bye", "ok"]
print([w.upper() for w in words])    # ['HI', 'BYE', 'OK']

# 3
cubes = {n: n ** 3 for n in {1, 2, 3, 4}}
print(cubes)          # {1: 1, 2: 8, 3: 27, 4: 64}
```

### 🔗 Agli class
*"Agli class — week ka finale: cheezon ko custom tareeke se sort karna, aur ek CHUPA hua bug jo har programmer ko pakadta hai — copy vs reference. Phir Contact Book project."*

---

## CLASS 30 — Sorting & References (Mini Project)

*"Aaj do important cheezein, phir ek real project. Pehla: cheezon ko apne tareeke se sort karna (jaise students ko marks se). Doosra: ek bahut common bug jo do variables ko galti se jod deta hai. Yeh bug agents mein bahut takleef deta hai — aaj hi pakad lo."*

### 🎯 Today's goal
`sorted(key=...)`, `is` vs `==`, aur `copy` vs `deepcopy`.

### 👨‍🏫 Concept 1 — custom sorting `sorted(key=...)`

> **📖 Technical definition — Sort key:** A sort key is a function passed as the `key` argument to `sorted()` or `.sort()`. It is called on each element to produce a value that is used for comparison, allowing items to be ordered by a derived property rather than their raw value.

*"Normally `sorted` chhote-bade ke hisaab se sort karta hai. Par dicts/tuples ko KIS cheez se sort karein? `key=` batata hai."*
```python
students = [
    {"name": "Asha", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Priya", "marks": 78},
]

# marks ke hisaab se sort (chhote se bade)
by_marks = sorted(students, key=lambda s: s["marks"])
for s in by_marks:
    print(s["name"], s["marks"])
```
Output:
```
Priya 78
Asha 85
Rahul 92
```
*"`key=lambda s: s["marks"]` ka matlab: 'har student `s` ko uske marks se compare karo.' `lambda` ek mini-function hai (next week detail mein). Topper pehle chahiye? `reverse=True` add karo."*

```python
top_first = sorted(students, key=lambda s: s["marks"], reverse=True)
print(top_first[0]["name"])     # Rahul (highest)
```

### 👨‍🏫 Concept 2 — `is` vs `==`

> **📖 Technical definition — Identity vs equality:** The `==` operator tests value equality (do two objects hold equal data?), while the `is` operator tests identity (are two names bound to the exact same object in memory?). Use `is` mainly for comparisons with `None`.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)     # True   — values same hain?
print(a is b)     # False  — ek hi object hai? (NAHI, do alag lists)
```
*"`==` poochta hai 'values barabar hain?'. `is` poochta hai 'yeh bilkul EK HI cheez hai (same memory)?'. 99% time aap `==` chahte ho. `is` sirf `None` check ke liye use karo: `if x is None:`."*

### 👨‍🏫 ⚠️ Concept 3 — the copy/reference bug (BAHUT important)

> **📖 Technical definition — Reference vs copy:** Assigning one variable to another (`b = a`) binds both names to the same underlying object, so changes through one name are visible through the other. A copy creates a separate object; a shallow copy duplicates only the top level, while a deep copy (`copy.deepcopy`) recursively duplicates all nested objects.

```python
list1 = [1, 2, 3]
list2 = list1            # yeh COPY nahi hai! dono ek hi list ko point karte hain

list2.append(4)
print(list1)             # [1, 2, 3, 4]  😱 list1 bhi badal gayi!
print(list2)             # [1, 2, 3, 4]
```
*"Yeh sabse chaunkane wala beginner bug hai. `list2 = list1` ek NAYI list nahi banata — yeh sirf ek aur naam deta hai SAME list ko. Ek ko badlo, dono badalte hain (kyunki woh ek hi hain)."*

**Fix — asli copy banao:**
```python
list1 = [1, 2, 3]
list2 = list1.copy()     # ✅ ab yeh alag list hai

list2.append(4)
print(list1)             # [1, 2, 3]      (safe!)
print(list2)             # [1, 2, 3, 4]
```

### 👨‍🏫 Concept 4 — `deepcopy` (nested data ke liye)
*"`.copy()` ek 'shallow' copy hai — top level toh alag, par andar nested cheezein abhi bhi shared. Nested data (list of dicts) ke liye `deepcopy` chahiye:"*
```python
import copy

original = [{"name": "Asha", "marks": [85, 90]}]
shallow = original.copy()
shallow[0]["name"] = "CHANGED"
print(original[0]["name"])     # CHANGED  😱 (andar wala dict abhi bhi shared)

# sahi tareeka:
original = [{"name": "Asha", "marks": [85, 90]}]
deep = copy.deepcopy(original)
deep[0]["name"] = "CHANGED"
print(original[0]["name"])     # Asha  ✅ (poori tarah alag)
```
*"Rule yaad rakho: simple flat list → `.copy()` theek. Nested (list of dicts) → `copy.deepcopy()` use karo. Yeh ek agent bug se bachata hai jahan ek agent ka data galti se doosre ka badal deta hai."*

### 🛠️ Mini Project — Contact Book
```python
import copy

contacts = []

def add_contact(name, phone):
    contacts.append({"name": name, "phone": phone})

# kuch contacts add karo
add_contact("Asha", "98765")
add_contact("Rahul", "91234")
add_contact("Priya", "90000")

# naam ke hisaab se sorted dikhao (original safe rehe)
for c in sorted(contacts, key=lambda c: c["name"]):
    print(f"{c['name']}: {c['phone']}")

# ek safe copy par kaam karo (original ko mat chhuо)
backup = copy.deepcopy(contacts)
backup[0]["phone"] = "00000"
print(f"Original first phone still: {contacts[0]['phone']}")   # 98765 (safe!)
```
*"Yeh project is week ka sab use karta hai: list of dicts (agent message-history ki shakal!), sorting by key, aur deepcopy se safe editing. Yeh agent memory manager ka baby version hai."*

### ❌ Common mistakes
```python
# reference bug nested data mein
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print(a)              # [[1, 2, 99], [3, 4]] 😱 — deepcopy chahiye tha

# is ka galat use
if name is "Asha":    # ❌ strings ke liye 'is' use mat karo — '==' use karo
    ...
```

### 🔗 Agentic link
*"Yeh week ka sabse practical agent-bug hai: ek agent ki message-history doosre agent ke saath galti se share ho jaaye. Solution: edit karne se pehle `deepcopy`. Aur sorting by key se hum search results ko relevance-score se rank karte hain. Dono skills real agents mein roz chahiye."*

### ✍️ Homework
1. 3 dicts ki list banao (naam, age) aur age ke hisaab se sort karke print karo.
2. Reference bug khud banaо: `b = a` karke `b` badlo, dikhao `a` bhi badla.
3. Phir `.copy()` se theek karke dikhao `a` safe raha.

**Answers:**
```python
# 1
people = [{"name": "A", "age": 30}, {"name": "B", "age": 20}, {"name": "C", "age": 25}]
for p in sorted(people, key=lambda p: p["age"]):
    print(p["name"], p["age"])
# B 20 / C 25 / A 30

# 2
a = [1, 2, 3]
b = a
b.append(4)
print(a)          # [1, 2, 3, 4]  (bug dikha)

# 3
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)          # [1, 2, 3]  (safe)
```

### 🏁 Week 4 wrap-up*"Yeh week aapne data ko organize karna master kiya:*
- *Dictionaries — key-value, LLM message ki shakal (Class 26)*
- *Dict methods, .get(), nesting — real API data (Class 27)*
- *Sets + read-only config (Class 28)*
- *Comprehensions — one-line transforms (Class 29)*
- *Sorting by key + copy/reference bug + Contact Book (Class 30)*

*Ab aap har tarah ka data store, transform, aur safely handle kar sakte ho. Yeh agent memory ka foundation hai. Next week — FUNCTIONS, jahan se asli engineering shuru hoti hai (har tool ek function hoga!). Shabaash!"*

### 📝 Weekend revision task
Contact Book ko blank file se dobara banao, bina notes ke. Bonus: ek `.get()`-based search add karo jo naam dhoondhe aur na mile toh "Not found" bole.

---

## 🎤 Industry Interview Questions — Week 4

> Real interview-style questions covering this week's topics, with model answers (in English). Try to answer them yourself first, then read the solution.

**Q1. What is the difference between `d[key]` and `d.get(key)`?**

`d[key]` raises a `KeyError` if the key is missing, which is what you want when the key *must* exist. `d.get(key)` returns `None` (or a supplied default, `d.get(key, default)`) instead of raising, which is safer for optional keys and avoids wrapping the access in a try/except. When parsing external/API data where fields may be absent, `.get()` with a default is the defensive choice.

**Q2. What kinds of objects can be used as dictionary keys (or set members), and why?**

Only *hashable* objects — objects with a stable `__hash__`, which in practice means immutable ones: strings, numbers, booleans, and tuples of hashables. Lists, dicts, and sets are mutable and therefore unhashable, so they can't be keys. The reason is that dicts and sets locate items by hash value; if a key's contents (and thus its hash) could change after insertion, the container could never find it again.

**Q3. Why is a set faster than a list for membership tests and deduplication?**

A set is backed by a hash table, so `x in my_set` is on average O(1). Checking `x in my_list` scans the list, which is O(n). So for repeated "have I seen this?" checks or removing duplicates, a set is dramatically faster on large data. The trade-offs: sets are unordered and can only hold hashable elements. Deduplicating is as simple as `set(my_list)`.

**Q4. What is a comprehension, and when does it become the wrong choice?**

A comprehension builds a list/dict/set in one expression, e.g. `[x*2 for x in nums if x > 0]`, which is concise and often faster than an equivalent loop with `.append()`. It becomes the wrong choice when it grows complex — nested loops plus multiple conditions become unreadable, and any comprehension used purely for side effects (not to build a collection) should just be a normal `for` loop. Readability wins over cleverness.

**Q5. Explain the aliasing bug with `b = a` for mutable objects, and how to avoid it.**

For a mutable object, `b = a` does not copy — both names point to the *same* object, so `b.append(4)` also changes `a`. This causes subtle shared-state bugs (e.g. one agent accidentally mutating another's history). Avoid it by making an explicit copy: `b = a.copy()` for a shallow copy, or `copy.deepcopy(a)` when the object contains nested mutable structures.
