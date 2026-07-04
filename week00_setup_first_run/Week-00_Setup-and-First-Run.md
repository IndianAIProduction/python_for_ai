# WEEK 0 — Setup & First Run (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> **Class promise:** *"Is week ke end tak aapke paas Python 3.15 chal raha hoga, aap apna pehla program likhoge — code ko DO tareeke se chala paoge (`.py` scripts aur `.ipynb` Jupyter notebooks), red error messages se aap bilkul nahi daroge — aur sabse important, aapke paas wahi **professional toolkit** ready hoga jo asli AI engineers daily use karte hain: **Cursor** (AI code editor), **uv** (environment manager), **Git** + **GitHub Desktop** (apne code ko save aur online portfolio banane ke liye). Hum zero se start kar rahe hain. Agar aapne kabhi coding nahi ki, koi tension nahi!"*

> **Industry note:** *"Yeh course sirf Python sikhane ke liye nahi hai — yeh aapko ek job-ready engineer banane ke liye hai. Isliye Day 1 se hum wahi tools use karte hain jo companies use karti hain. Recruiter aapka GitHub 5 second mein dekh kar bata deta hai ki aap pro ho ya beginner. Hum aapko pro banayenge."*

---

## CLASS 1 — What is Programming & Where We Are Going

*"Good morning everyone! Class 1 mein welcome hai. Aaj hum almost koi code nahi likhenge. Aaj hum DO cheezein samjhenge: (1) Programming actually hai kya? (2) Yeh 'Agentic AI Engineer' ka job kya hai jiske liye hum train kar rahe hain? Ek baar destination pata chal gaya, toh aage ka har din easy lagega."*

### 🎯 Today's goal
Aap apne shabdon mein bata paayenge: code kya hai, Python kya hai, aur ek AI agent kya karta hai.

### 👨‍🏫 Concept 1 — Computer actually hai kya? (easy language)
*"Dekho, computer duniya ka sabse obedient lekin sabse 'stupid' servant hai. Jo bologe, bilkul wahi karega — super fast, millions of times — par uske paas apni koi common sense nahi hai. Agar aap bolo 'paani lao', toh paani layega. Agar aap bhool gaye 'glass mein lao', toh shayad haath mein hi paani le aaye! Isliye hamara kaam hai — bahut clear, step-by-step instructions dena."*

Ek real-life example — **Maggi banana**:
1. 1.5 cup paani boil karo.
2. Masala daalo.
3. Noodles daalo.
4. 2 minute cook karo.
5. Serve karo.

*"Yeh steps ki list hi ek 'program' hai. Jis language mein likhi hai (Hindi/English) woh 'programming language' hai. Aur jo cook in steps ko follow karta hai, woh 'computer' hai."*

### 👨‍🏫 Concept 2 — Programming language & Python kya hai?
- **Programming language** = ek aisi language jo human aur computer dono samajh sakein.
- **Python** = aisi hi ek language hai. Yeh famous isliye hai kyunki yeh almost English jaisi padhi jaati hai.

Yeh code dekho (abhi syntax samajhne ki zaroorat nahi — bas iska 'feel' lo):

```python
if marks >= 33:
    print("Pass")
else:
    print("Fail")
```

*"Dekho — agar aapne kabhi code nahi likha, tab bhi aap ise PADH sakte ho: 'if marks greater-than-equal 33, toh print Pass, else print Fail.' Isiliye hum Python choose karte hain, especially AI ke liye."*

### 👨‍🏫 Concept 3 — 'Interpreter' kya hota hai?
*"Aap Python English-jaise words mein likhte ho. Par computer ka brain (CPU) sirf 0 aur 1 samajhta hai. Toh ek translator chahiye. Us translator ko bolte hain **Python interpreter**. Hum ise Class 3 par install karenge. Yeh aapke Python ko line-by-line padhta hai aur computer ko batata hai kya karna hai."*

### 👨‍🏫 Concept 4 — Hamari destination: Agentic AI Engineer
*"Aap sabne ChatGPT use kiya hoga. Woh questions ke answer deta hai. Par woh khud se aapka train ticket book nahi kar sakta, na aapki file padh sakta hai, na email bhej sakta hai. Ek **AI agent** yeh sab kar sakta hai. Agent ek aisa AI hai jo:*
1. **Think** karta hai — samajhta hai aap kya chahte ho.
2. **Tools use** karta hai — real functions call karta hai (search, calculator, email).
3. **Loop mein act** karta hai — chalta rehta hai: think → act → result check → phir think → jab tak kaam pura na ho."*

Yeh diagram dhyaan se dekho:

```
        ┌─────────────────────────────┐
USER ──▶ │  THINK → USE A TOOL → CHECK │ ──▶ ANSWER
        └──────────▲────────────┬─────┘
                   └── repeat ───┘
```

*"Ek **Agentic AI Engineer** wahi banda hai jo yeh sab BANATA hai. Aur ek secret batata hoon: us loop ka har part — 'tools', 'memory', aur 'loop' khud — sab Python hi hai. Toh agar aap Python master kar lo, aap agents banane ke 90% raaste tay kar chuke ho. Yahi hamari mission hai agle kuch mahino ke liye."*

### 🧠 Aaj ka ek bada idea (yaad rakhna)
> Programming = ek stupid-but-fast servant ko bahut clear step-by-step instructions dena. Python woh easy language hai jo hum use karte hain. AI agent ek program hai jo think karta hai, tools use karta hai, aur loop mein chalta hai jab tak kaam pura na ho — aur yeh sab Python mein bana hota hai.

### ✍️ Homework
1. 5 lines mein (English ya Hindi), **brush karne** ka step-by-step "program" likho. (Yeh aapke brain ko steps mein sochna sikhata hai.)
2. 3 sentences likho: "Main AI engineer kyun banna chahta/chahti hoon?"

**Q1 ka sample answer:**
```
1. Brush uthao.
2. Usme toothpaste lagao.
3. Upar ke teeth 1 minute brush karo.
4. Neeche ke teeth 1 minute brush karo.
5. Paani se mooh saaf karo.
```
*(Agar aap "toothpaste ka cap kholo" bhool gaye — yahi lesson hai! Computer ko HAR step chahiye.)*

### 🔗 Agli class
*"Agli class mein hum Python ko bina kuch install kiye, sirf browser mein chalayenge — Google Colab se. Yeh un sabke liye hai jinke paas abhi laptop nahi hai (phone, tablet ya school computer se bhi chal jaayega)."*

---

## CLASS 2 — Google Colab: Python Without Installing Anything (No Laptop? No Problem!)

*"Ruko — agar aapke paas abhi laptop nahi hai, ya install karne mein dikkat aa rahi hai, toh bhi aap aaj se hi Python chala sakte ho! **Google Colab** ek free website hai jahan aapka Python code Google ke computer par chalta hai — aapko sirf ek browser aur ek Google account (Gmail) chahiye. Phone, tablet ya kisi bhi computer se. Isliye yeh hamara **pehla setup** hai — taaki koi peeche na rahe."*

### 🎯 Today's goal
Bina kuch install kiye, browser mein apna pehla Python code chalana — Google Colab se.

### 👨‍🏫 Concept — Google Colab kya hai? (easy language)
*"Normally Python chalane ke liye use apne computer par install karna padta hai (woh hum agli class mein karenge). Par **Colab** ek alag tareeka hai: aapka code Google ke powerful computers par chalta hai, aur result aapke browser mein dikhta hai. Kuch install nahi, kuch setup nahi — bas login karo aur likho."*

| | Google Colab | Laptop install (agli class) |
|---|---|---|
| Kya chahiye | Browser + Google account | Apna laptop/PC (Windows/Mac) |
| Install karna padta hai? | **Nahi** (sab online) | Haan (Python, Cursor) |
| Best kab | No laptop / phone / quick test | Poora course, real projects, jobs |

> **Honest baat:** Colab beginning ke liye perfect hai. Par aage course mein hum `uv`, `Git` aur `Cursor` jaise pro tools laptop par use karenge (Class 8–10). Toh agar laptop hai, toh Colab try karke **agli class se laptop setup zaroor karo**. Laptop nahi hai? Tension nahi — Colab se aap Python ke saare concepts seekh sakte ho.

### 👨‍🏫 Step 1 — Google account ready karo
*"Aapko ek Google account (Gmail) chahiye. Agar pehle se hai (jo zyadatar logon ke paas hota hai), toh perfect. Nahi hai toh [accounts.google.com](https://accounts.google.com/signup) par 2 minute mein free bana lo."*

### 👨‍🏫 Step 2 — Colab kholo aur naya notebook banao
1. Browser mein [colab.research.google.com](https://colab.research.google.com/) par jao.
2. Apne Google account se **Sign in** karo.
3. Menu se **File → New notebook** dabao (ya "New notebook" button). Ek khaali notebook khul jaayega.

*"Notebook ek aisi file hai jisme aap code chhote-chhote dibbon ('cells') mein likhte ho aur har cell ko alag se chala sakte ho."*

### 👨‍🏫 Step 3 — Apna pehla code chalao
*"Notebook ke pehle cell (grey box) mein yeh type karo:"*

```python
print("Hello, World!")
print("I am learning Python on Colab")
```

*"Ab cell ke left side **▶ (play) button** dabao — ya keyboard se **Shift + Enter**. Pehli baar Colab thoda time lega (woh aapke liye ek computer 'connect' kar raha hai). Phir neeche output dikhega:"*

```text
Hello, World!
I am learning Python on Colab
```

*"Bas! Aapne bina kuch install kiye Python chala liya. 🎉"*

### 👨‍🏫 Step 4 — Apna kaam save karo
*"Colab aapka notebook automatically aapke **Google Drive** mein save karta hai (File → Save). Toh kaam kabhi khoyega nahi. Baad mein aap ise GitHub par bhi daal sakte ho — **File → Save a copy in GitHub** (Class 10 mein GitHub account banane ke baad)."*

> **Phone/tablet tip:** Colab mobile browser mein bhi chal jaata hai, par code likhne ke liye chhoti screen thodi mushkil hoti hai. Ho sake toh ek bluetooth keyboard ya tablet use karo. Aur jaise hi laptop mile, agli class se proper setup kar lena.

### 🔗 Agentic link
*"Bahut saari AI experiments (jaise free GPU par models chalana) industry mein Colab par hote hain. Toh yeh tool aapko aage bhi kaam aayega — yeh sirf 'beginner' tool nahi hai."*

### ✍️ Homework
1. Colab par ek naya notebook banao aur 3 lines print karo (apna naam, city, dream job).
2. Notebook ko ek naam do (upar title par click karke) aur Google Drive mein save karo.
3. (Optional) Ek naya cell banao aur `5 + 3` likh kar chalao — kya output aata hai?

### 🔗 Agli class
*"Agli class laptop walon ke liye hai — hum Python aur Cursor ko apne computer par install karenge (real engineers aise hi kaam karte hain). Colab-only students yeh padh sakte ho, par install ke steps tab karna jab laptop mile."*

---

## CLASS 3 — Installing Python 3.15 & the Editor (Laptop Setup)

*"Aaj asli laptop setup class hai. Class ke end tak Python aapke computer ke andar live ho jayega. Mere saath step-by-step chalo — aage mat bhaago. (Sirf Colab use kar rahe ho? Toh yeh aur aage ke install steps tab karna jab laptop mile — concepts padhte raho.)"*

### 🎯 Today's goal
Python **3.15** install + verify, aur ek code editor (VS Code ya Cursor) ready.

### 👨‍🏫 Step 1 — Python 3.15 download karo
*"Browser kholo aur **python.org** par jao → Downloads. Apne system (Windows/Mac) ke liye latest Python 3.15 version download karo."*

> **Teacher accuracy note:** Abhi Python 3.15 apne final stages mein hai (stable release October 2026). Agar aapke machine par sirf 3.15 beta available hai, toh learning ke liye woh bilkul theek hai — jo sabse naya 3.15 mile, woh install karo.

**Windows students — BAHUT IMPORTANT:**
*"Pehli install screen par, sabse neeche ek checkbox dikhega: ✅ **'Add python.exe to PATH'**. Use TICK karo. Yeh ek tick aapko aage 100 errors se bachata hai. Phir 'Install Now' dabao."*

*"'PATH' ka matlab simple hai: yeh Windows ko batata hai 'bhai, Python yahan rehta hai, toh jab koi kahin bhi `python` type kare, tujhe pata ho use kahan dhoondhna hai.'"*

### 👨‍🏫 Step 2 — Installation verify karo
*"Ab check karte hain ki chala ki nahi. Apna terminal kholo."*
- **Windows:** `Start` dabao, `PowerShell` type karo, kholo.
- **Mac:** `Terminal` app kholo.

Yeh type karo aur Enter dabao:

```powershell
python --version
```

*"Aapko kuch aisa dikhna chahiye `Python 3.15.0`. Agar yeh dikha — CONGRATULATIONS, Python aapke machine mein zinda hai! 🎉"*

> **Agar likhe 'python is not recognized'** (Windows): aap PATH wala tick bhool gaye. Uninstall karo, dobara install karo, aur "Add to PATH" tick karo. (Yeh Class-3 ki sabse common problem hai — bilkul normal hai.)

### 👨‍🏫 Step 3 — Code editor install karo (**Cursor** — hamara main editor)
*"Hum code Notepad mein bhi likh sakte hain, par professionals proper editor use karte hain. Is course mein hum **Cursor** use karenge — yeh ek AI-powered code editor hai (VS Code ke upar bana hua), jo aapke saath baith kar code likhne mein madad karta hai. AI engineers ke liye yeh aaj ki industry ka favourite tool hai."*

**Cursor install karne ke steps:**
1. Browser kholo aur [cursor.com/download](https://cursor.com/download) par jao.
2. Apne system (Windows/Mac) ka button dabao → installer download hoga.
3. Downloaded file par double-click karo → **Next → Next → Install** (default settings bilkul theek hain).
4. Install hone ke baad Cursor kholo. Pehli baar woh aapko theme aur sign-in ke liye poochega — abhi **"Continue"** ya **skip** kar sakte ho, baad mein set kar lenge.

> **Python extension (auto-complete + error highlighting):** Cursor kholne ke baad left side **Extensions** icon par click karo (4 squares jaisa) → **'Python'** search karo → Microsoft wala official install karo. Yeh humein colors, auto-complete aur error highlighting deta hai — code ke liye spell-check jaisa.

> **Built-in terminal:** Cursor ke andar hi ek terminal hai — upar menu se **View → Terminal** (ya `` Ctrl+` ``). Hum saare commands yahin se chala sakte hain, alag se PowerShell kholne ki zaroorat nahi.

> **Prefer VS Code?** Agar aap pehle se **VS Code** ([code.visualstudio.com](https://code.visualstudio.com/)) use karte ho toh woh bhi chalega — sab steps same hain. Par course ke AI features dikhane ke liye main Cursor use karunga.

### 👨‍🏫 Version kyun matter karta hai (agentic link)
*"AI jobs mein #1 bewakoofi wala bug hota hai: 'mere laptop par chalta hai, tumhare par nahi.' Usually yeh version mismatch hota hai. Hum sab Python 3.15 use karke Class 1 se hi yeh problem avoid karte hain. Yeh ek industry habit hai, jo aap abhi seekh rahe ho."*

### ✍️ Homework
1. `python --version` run karo aur `3.15` dikhata hua screenshot lo.
2. VS Code + Python extension install karo.
3. (Optional) Terminal mein akela `python` run karo — `>>>` dikhega. `2 + 2` type karke Enter dabao. Nikalne ke liye `exit()` type karo. (Is `>>>` ko kal explore karenge.)

### 🔗 Agli class
*"Agli class mein hum terminal seekhenge — aapka control panel — aur ek real Python file run karenge."*

---

## CLASS 4 — The Terminal (Your Control Panel)

*"Movies mein hackers ek black screen mein type karte hain. Woh black screen terminal hai. Darne wali baat nahi hai — yeh sirf computer se text se baat karne ka tareeka hai, click ke bajaye. Aaj hum isse comfortable ho jayenge."*

### 🎯 Today's goal
Folders ke beech move karna aur terminal se Python file run karna.

### 👨‍🏫 Concept — files, folders & "current location"
*"Aapke computer mein folders (jinhe 'directories' bhi bolte hain) hote hain, folder ke andar folder. Terminal hamesha ek time par EK folder ke andar 'khada' hota hai. Ise bolte hain 'current working directory'. Soch lo jaise ek building mein aap hamesha ek room mein khade ho. Kuch bhi karne ke liye, pehle sahi room mein chalna padta hai."*

### 👨‍🏫 Aaj ke 3 commands

**1) Dekho aap kahan khade ho:**
```powershell
pwd
```
*(pwd = "print working directory" → current folder ka path dikhata hai.)*

**2) Dekho is room mein kya hai (files list karo):**
```powershell
dir
```
*(Mac/Linux par `ls` use karo. Windows PowerShell par `dir` aur `ls` dono chalte hain.)*

**3) Doosre room mein chalo (change directory):**
```powershell
cd Desktop
```
*(cd = "change directory". `cd ..` aapko BAHAR, parent folder mein le jaata hai.)*

### 💻 Chalo apna class folder banate hain
*"Mere saath type karo."*

```powershell
cd Desktop
mkdir python_class
cd python_class
pwd
```

*"`mkdir` = 'make directory' (naya folder banao). Humne `python_class` naam ka folder banaya, uske andar gaye, aur `pwd` se confirm kiya. Yahin hamara saara code rahega."*

### 👨‍🏫 Spaces wale paths ko quotes mein likhna (pro tip)
*"Agar folder ke naam mein space hai, jaise `My Documents`, toh use quotes mein wrap karna ZAROORI hai:"*
```powershell
cd "My Documents"
```
*"Quotes ke bina computer confuse ho jaata hai. Yeh yaad rakhna — yeh sabko ek baar zaroor pareshaan karta hai."*

### 🔗 Agentic link
*"Jab aap agents banaoge, aap unhe terminal se RUN karoge, terminal se DEPLOY karoge, aur terminal se DEBUG karoge. Yeh black screen aapka best friend ban jayegi."*

### ✍️ Homework
1. `python_class` ke andar 3 folders banao: `class3`, `practice`, `notes`.
2. Har ek mein `cd` karke `pwd` se confirm karo.
3. Har baar `cd ..` se wapas bahar aao.

**Answer (commands):**
```powershell
cd Desktop\python_class
mkdir class3
mkdir practice
mkdir notes
cd class3
pwd
cd ..
cd practice
pwd
cd ..
```

### 🔗 Agli class
*"Agli class mein — aapka PEHLA real Python program. Famous 'Hello, World!'"*

---

## CLASS 5 — REPL vs Files & Your First Program

*"Aaj aap officially programmer ban jaoge. Hum apna pehla program likhenge aur run karenge. Python run karne ke DO tareeke hain — dono seekhte hain aur kab kya use karna hai."*

### 🎯 Today's goal
REPL vs `.py` file samajhna, aur `print()` run karna.

### 👨‍🏫 Way 1 — REPL (instant testing)
*"Terminal mein akela `python` type karo. `>>>` dikhega. Yeh **REPL** hai — yeh code ko turant chalata hai, ek line at a time. Quick experiments ke liye best."*

```python
>>> print("Hello, World!")
Hello, World!
>>> 5 + 3
8
```

*"R-E-P-L = Read, Evaluate, Print, Loop. Aapki line ko Read karta hai, Evaluate (run) karta hai, result Print karta hai, aur agli line ke liye Loop karta hai. Nikalne ke liye `exit()` type karo."*

### 👨‍🏫 Way 2 — `.py` file (real programs)
*"REPL band karte hi sab bhool jaata hai. Real programs ke liye hum code ko ek file mein save karte hain jiska end `.py` se hota hai."*

**Chalo karke dekhte hain:**
1. VS Code kholo → File → Open Folder → `python_class` choose karo.
2. New File → naam do `hello.py`.
3. Type karo:

```python
print("Hello, World!")
print("My name is Asha")
print("I am learning Python to become an AI engineer")
```

4. Save karo (`Ctrl+S`).
5. Terminal mein (`python_class` ke andar):

```powershell
python hello.py
```

*"Output aa gaya! Aapne abhi ek real program likha aur run kiya. Ek minute ruko — aap AB programmer ho!"*

### 👨‍🏫 `print()` ko line-by-line samajhte hain
```python
print("Hello, World!")
```
- `print` → woh **command** (technically ek *function*) jiska matlab hai "yeh screen par dikhao".
- `( )` → brackets jo hold karte hain jo hum dikhana chahte hain.
- `"Hello, World!"` → text. Programming mein text ko **string** bolte hain, aur strings quotes `" "` ke andar aate hain.

*"Toh `print("...")` = 'yeh text screen par daal do'. Simple."*

### 👨‍🏫 Kab kya use karein?
| REPL (`>>>`) | File (`.py`) |
|---|---|
| Quick 1-line test | Real, saved programs |
| Band karte hi bhool jaata hai | Hamesha rehta hai |
| "Bas ek baar check karu..." | "Yeh banana hai..." |

### 🔗 Agentic link
*"Agents banate waqt, main ek chhota idea (jaise ek prompt) REPL mein test karta hoon, aur jab chal jaaye toh use proper `.py` file mein daal deta hoon. Aap bhi bilkul yahi karoge."*

### ✍️ Homework
1. `aboutme.py` banao jo aapke baare mein 5 lines print kare (name, city, hobby, dream job, favourite subject).
2. Use `python aboutme.py` se run karo.

**Sample answer:**
```python
print("Name: Rahul Sharma")
print("City: Pune")
print("Hobby: Cricket")
print("Dream job: Agentic AI Engineer")
print("Favourite subject: Maths")
```

### 🔗 Agli class
*"Agli class mein hum code chalane ka ek aur tareeka seekhenge — **Jupyter Notebook (.ipynb)** — wahi cheez jo aapne Colab mein dekhi thi, par ab apne laptop par. Phir uske baad errors se dosti karenge."*

---

## CLASS 6 — Jupyter Notebook (.ipynb): Code + Notes in One Place

*"Yaad hai Class 2 mein Colab par humne code chhote dibbon ('cells') mein chalaya tha? Woh actually ek **Jupyter Notebook** tha — Colab usi ko online chalata hai. Aaj hum wahi notebook apne laptop par, Cursor ke andar chalayenge. Iske baad aap code DO tareeke se likh paoge: `.py` files aur `.ipynb` notebooks — dono industry mein use hote hain."*

### 🎯 Today's goal
`.py` aur `.ipynb` ka farak samajhna, aur Cursor mein apna pehla notebook banakar chalana.

### 👨‍🏫 Concept — Notebook (.ipynb) kya hai? (easy language)
*"Ek `.py` file pura program ek saath, upar se neeche chalta hai. Ek **notebook** alag hai: aap code ko chhote-chhote dibbon (**cells**) mein todte ho, aur har cell ko alag se chala kar uska output turant uske neeche dekhte ho. Beech mein aap **notes (text)** bhi likh sakte ho. Isliye yeh seekhne, experiments, aur AI/data ke kaam ke liye perfect hai."*

| `.py` file | `.ipynb` notebook |
|---|---|
| Pura program, upar se neeche | Cell-by-cell (tukdon mein) |
| Real apps, scripts, agents ke liye best | Seekhne, experiment, AI/data ke liye best |
| Run: `python file.py` ya `uv run file.py` | Run: har cell ka **▶** button (ya `Shift + Enter`) |
| Output terminal mein | Output cell ke neeche, inline |

> **Colab connection:** Colab (Class 2) = Jupyter Notebook jo Google ke computer par online chalta hai. Yeh class = wahi notebook aapke apne laptop par. Concept bilkul same — `.ipynb`.

### 👨‍🏫 Step 1 — Jupyter extension install karo (ek baar)
*"Cursor kholo → left side **Extensions** icon (4 squares) → **'Jupyter'** search karo → Microsoft wala official install karo. (Python extension toh aap Class 3 mein laga hi chuke ho — woh bhi chahiye.)"*

### 👨‍🏫 Step 2 — Naya notebook banao
1. Cursor mein apna folder kholo (**File → Open Folder → `python_class`**).
2. **New File** banao aur naam do `first_notebook.ipynb` (extension `.ipynb` zaroori hai).
3. File khulte hi woh ek notebook ki tarah dikhega — code cells ke saath, normal text nahi.

> **Aasaan tareeka:** `Ctrl+Shift+P` dabao → **"Create: New Jupyter Notebook"** type karke choose karo.

### 👨‍🏫 Step 3 — Kernel choose karo aur code chalao
*"Notebook ko chalane ke liye ek Python 'engine' chahiye — use **kernel** bolte hain."*
1. Upar-right **"Select Kernel"** par click karo → apna **Python 3.15** choose karo.
2. Agar Cursor `ipykernel` install karne ko kahe → **Install** dabao (yeh notebook chalane wala chhota package hai).
3. Pehle cell mein yeh likho:

```python
print("Hello from a notebook!")
2 + 3
```

4. Cell ke left **▶** button dabao (ya **`Shift + Enter`**). Output cell ke neeche turant dikhega:

```text
Hello from a notebook!
5
```
*"Dekha? `print(...)` ka output bhi aaya, aur aakhri line `2 + 3` ki value `5` bhi — bilkul REPL jaise. Yahi notebook ki khaasiyat hai."*

### 👨‍🏫 Step 4 — Notes ke liye markdown cell
*"Code ke saath notes likhne ke liye **markdown cell** add karo: cell ke upar **+ Markdown** dabao, phir likho (jaise `# My First Notebook`) aur `Shift + Enter`. Yeh ek heading ki tarah dikhega. Isiliye notebooks padhne mein itne aasaan hote hain — code + explanation ek saath."*

### 👨‍🏫 Kab `.py` aur kab `.ipynb`?
| Kaam | Behtar choice |
|---|---|
| Quick experiment, ek idea try karna | `.ipynb` notebook |
| Seekhna / step-by-step samajhna | `.ipynb` notebook |
| Real, reusable program ya AI agent | `.py` file |
| Code dusron ko deploy/share karna | `.py` file |

*"Pro workflow: pehle notebook mein try karo, jab chal jaaye toh stable code `.py` file mein daal do. Aap pure course mein dono use karoge."*

### 🔗 Agentic link
*"AI engineers prompts aur models ko pehle **notebook** mein test karte hain (turant feedback milta hai), phir jo chize kaam karti hain unhe `.py` modules mein daal kar real agent banate hain. Aaj aapne wahi dual-skill seekha."*

### ✍️ Homework
1. Cursor mein `first_notebook.ipynb` banao aur 2 code cells chalao.
2. Ek markdown cell add karke ek heading + ek line note likho.
3. Wahi code ek `.py` file mein likh kar `python` se chalao — dono ka output compare karo.

### 🔗 Agli class
*"Ab hum ek mazedaar cheez karenge — apna code jaan-boojh kar TODENGE, taaki red errors se hamesha ke liye darr khatam ho jaaye."*

---

## CLASS 7 — Reading Errors Calmly (Mini Project)

*"Aaj pure week ka sabse important lesson: errors FAILURE nahi hain. Errors toh computer ki MADAD hai — woh exactly bata raha hai kya galat hai. Har expert engineer poora din errors padhta hai. Chalo inse dosti karte hain."*

### 🎯 Today's goal
Python 3.15 ka error message padhna, samajhna, aur fix karna.

### 👨‍🏫 Concept — error ('traceback') kya hota hai?
*"Jab Python aapka code run nahi kar paata, toh woh ruk jaata hai aur ek message print karta hai jise **traceback** bolte hain. Sabse useful line usually LAST line hoti hai — woh problem ka naam batati hai. Python 3.15 ne in messages ko specially improve kiya hai, yeh fix tak suggest karta hai. Dekhte hain."*

### 💻 Chalo jaan-boojh kar cheezein todte hain

**Mistake 1 — ek typo:**
```python
prnt("Hello")
```
Run karo. Python 3.15 kuch aisa bolega:
```
NameError: name 'prnt' is not defined. Did you mean: 'print'?
```
*"Dekha? Yeh literally pooch raha hai 'Did you mean print?' Spelling fix karo → chal gaya. Lesson: LAST line padho."*

**Mistake 2 — quote bhool gaye:**
```python
print("Hello)
```
Error:
```
SyntaxError: unterminated string literal
```
*"'Unterminated string' = aapne quote khola par band nahi kiya. Closing `"` add karo → fixed."*

**Mistake 3 — galat indentation (spacing):**
```python
print("A")
   print("B")
```
Error:
```
IndentationError: unexpected indent
```
*"Python line ke shuru ki spacing ke baare mein strict hai. WHY, woh next week seekhenge — abhi ke liye, lines ko left edge se shuru rakho jab tak na bola jaaye."*

### 🧠 "3-step error-fixing recipe" (likh lo)
1. **Panic mat karo.** Errors normal hain — experts ke liye bhi.
2. **LAST line padho.** Woh problem ka naam batati hai.
3. **Line number dekho** jo Python batata hai, use fix karo, dobara run karo.

### 🛠️ Mini Project — "About Me" card (todo aur fix karo)
*"Yeh program banao, phir main aapko 3 tareeke se todne ko bolunga aur har ek fix karna hai."*

```python
print("====================")
print("     ABOUT ME       ")
print("====================")
print("Name   : Priya")
print("Class  : 12th")
print("Goal   : AI Engineer")
print("====================")
```

**Aapka task:**
1. Run karo — neat card dikhega.
2. Use todo (`print` mein typo, ek quote hatao, ek space add karo). Har error padho.
3. Har ek fix karo. Ho gaya!

### 🔗 Agentic link
*"AI agents bahut baar fail hote hain — ek tool time-out ho jaata hai, API key galat hoti hai, internet chala jaata hai. Jo engineer errors ko calmly padhta hai aur fast fix karta hai, wahi succeed karta hai. Aapne abhi yeh superpower banana shuru kiya hai."*

### ✍️ Homework
1. "About Me" card project complete karo.
2. Upar wale 3 errors jaan-boojh kar banao, message ka screenshot lo, aur ek line likho ki kaise fix kiya.

### 🔗 Agli class
*"Ab basic Python ho gaya. Agli 3 classes mein hum wahi professional tools install karenge jo asli AI engineers use karte hain — taaki aapka setup bilkul industry jaisa ho. Pehla: `uv`."*

---

## CLASS 8 — uv: The Professional's Environment Manager

*"Ab tak humne files banayi aur run ki. Par jab aap real projects banaoge, har project ko apne alag packages (ready-made code ke boxes) chahiye honge. Inhe manage karne ka pro tareeka hai **`uv`** — ek modern, bahut fast tool. Aaj hum ise install karke ek asli project banayenge."*

### 🎯 Today's goal
`uv` install karna, ek project banana, aur usme pehla package add karna.

### 👨‍🏫 Concept — virtual environment kya hai? (easy language)
*"Socho aapke paas 2 projects hain. Project A ko ek package ka purana version chahiye, Project B ko naya. Agar dono ek hi jagah install ho, toh ladai ho jaayegi! Solution: har project ko apna alag chhota 'package ka dabba' do. Is dabbe ko bolte hain **virtual environment** (short mein `venv`). `uv` yeh dabba aapke liye automatically banata aur manage karta hai."*

| Tool | Yeh kya hai | Hum kyun use karte hain |
|---|---|---|
| **`uv`** | Package + environment manager | Modern aur *bahut* fast (purane pip+venv ka jhanjhat khatam) |
| **virtual environment** (`venv`) | Har project ka private package box | Har project ke packages alag rakhta hai (no global mess) |

### 👨‍🏫 Step 1 — uv install karo
*"Sabse aasaan tareeka — Cursor ke terminal mein (`View → Terminal`) yeh command chalao:"*

```powershell
pip install uv
```

> **Recommended (standalone install — kisi ek Python/pip se nahi judta):** official [uv install docs](https://docs.astral.sh/uv/getting-started/installation/). Windows PowerShell par:
> ```powershell
> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
> ```

**Verify karo:**
```powershell
uv --version
```
*"Agar version number dikha (jaise `uv 0.x.x`), toh uv zinda hai! 🎉"*

### 👨‍🏫 Step 2 — Pehla uv project banao
*"Chalo ek project folder banate hain aur uv se ise setup karte hain. Mere saath 4 commands order mein chalao:"*

```powershell
cd Desktop\python_class
mkdir my_first_project
cd my_first_project
uv init          # 1. project banao (pyproject.toml + .python-version)
uv sync          # 2. virtual env (.venv) banao
.\.venv\Scripts\activate   # 3. (Windows) venv "on" karo
uv add requests  # 4. ek package add karo
```
*(Mac/Linux par venv on karne ka command: `source .venv/bin/activate`)*

**Har command ka matlab:**
| Command | Yeh kya karta hai |
|---|---|
| `uv init` | Project files banata hai (`pyproject.toml` — `requirements.txt` ka modern replacement) |
| `uv sync` | `.venv` (package dabba) banata hai aur project ke packages install karta hai |
| `.\.venv\Scripts\activate` | venv ko "on" karta hai — ab terminal project ka apna Python use karega |
| `uv add <pkgs>` | Packages add karta hai (**spaces** se, comma se NAHI) aur install karta hai |

> **Common beginner mistakes:** `uv inti` (typo — sahi hai `uv init`) aur commas: `uv add requests, rich` ❌ — **spaces** use karo: `uv add requests rich` ✅

### 👨‍🏫 Step 3 — Code uv se run karo
*"Project ke andar ek file `hello.py` banao (Cursor mein), usme `print("uv se hello!")` likho, save karo, phir:"*

```powershell
uv run hello.py
```
*"`uv run` automatically sahi venv use karke aapki file chalata hai. Yahi pro tareeka hai."*

### 🔗 Agentic link
*"Course mein aage hum AI libraries (`langchain` waghairah) isi tarah `uv add` se install karenge. Har project ka apna saaf environment — yahi industry standard hai."*

### ✍️ Homework
1. `my_first_project` naam ka uv project banao.
2. `uv add rich` se ek package add karo.
3. Ek file banao jo kuch print kare, aur `uv run` se chalao.

### 🔗 Agli class
*"Agli class mein — **Git**. Apne code ke 'save points' banana aur kabhi kaam na khona."*

---

## CLASS 9 — Git: Save Points for Your Code

*"Imagine karo aap 3 ghante kaam karte ho, phir kuch change karte ho aur sab kuch tut jaata hai. Kaash ek 'undo button' hota jo poore project ke liye kaam kare! Woh button hai **Git**. Aaj hum ise install aur use karna seekhenge."*

### 🎯 Today's goal
Git install karna, apni identity set karna, aur pehla 'save point' (commit) banana.

### 👨‍🏫 Concept — Git kya hai? (easy language)
- **Git** = *version control*. Yeh aapke code ke snapshots ("commits") leta hai, taaki aap galti undo kar sako, dekho kya badla, aur kabhi kaam na kho. Soch lo jaise game ke **"checkpoints"** — par poore project ke liye.
- **`.gitignore`** = ek chhoti text file jisme un files ke naam hote hain jinhe Git **ignore** kare (kabhi save/upload na kare) — jaise secret keys waali files.

### 👨‍🏫 Step 1 — Git install karo
*"Browser mein [git-scm.com/downloads](https://git-scm.com/downloads) par jao (Windows: [git-scm.com/install/windows](https://git-scm.com/install/windows)). Installer download karo. Windows par installer bahut saare options poochega — **beginner ke liye sab default rakho, bas Next → Next → Install dabate jao.** Default settings bilkul safe hain."*

**Verify karo** (Cursor terminal mein):
```powershell
git --version
```
*"Kuch aisa dikhega `git version 2.45.0`. Mil gaya? Shabaash! 🎉"*

> **Agar `git is not recognized` aaye (Windows):** Cursor ko poori tarah band karke dobara kholo (taaki woh naya PATH padh sake), phir command dobara chalao.

### 👨‍🏫 Step 2 — Git ko batao aap kaun ho (ek baar)
*"Har save point par Git aapka naam aur email stamp karta hai. Yeh ek baar set karna hota hai. (Email wahi use karo jo aap GitHub par use karoge — agli class mein.)"*

```powershell
git config --global user.name "Your Name"
git config --global user.email "your_email@gmail.com"
```

### 👨‍🏫 Step 3 — Pehla save point (commit) banao
*"Apne project folder ke andar (`my_first_project`) yeh commands chalao:"*

```powershell
git init                       # 1. is folder ko Git se track karna shuru karo (ek baar)
git status                     # 2. dekho kya-kya badla (bahut use karo!)
git add .                      # 3. saare changes stage karo (save ke liye mark karo)
git commit -m "first commit"   # 4. ek snapshot save karo, ek message ke saath
```

**Har command ka matlab:**
| Command | Yeh kya karta hai |
|---|---|
| `git init` | Folder ko Git se track karna shuru karta hai |
| `git status` | Batata hai kya badla / kya stage hua hai |
| `git add .` | Saare changes ko "save ke liye taiyaar" mark karta hai |
| `git commit -m "..."` | Ek save point (snapshot) banata hai message ke saath |

> **Pro habit:** har commit se **pehle** `git status` chalao — yeh confirm karta hai ki sirf wahi files save ho rahi hain jo aap chahte ho. Yeh ek choti aadat bade accidents bachati hai.

### 🔗 Agentic link
*"AI agents banate waqt code roz badalta hai. Git ke bina aap purani working version par wapas nahi ja sakte. Har serious engineer Git use karta hai — exception nahi."*

### ✍️ Homework
1. `git --version` ka screenshot lo.
2. Apne uv project mein `git init` → `git add .` → `git commit -m "first commit"` karo.
3. `git status` chala kar dekho output kya kehta hai.

### 🔗 Agli class
*"Agli class mein — **GitHub** par account banayenge aur **GitHub Desktop** se apna code online daalenge. Yahi aapka portfolio banega jo recruiters dekhte hain."*

---

## CLASS 10 — GitHub & GitHub Desktop: Your Online Portfolio

*"Git aapke computer par save points banata hai. Par agar laptop kho jaaye? Aur recruiter aapka code kaise dekhega? Iska answer hai **GitHub** — ek website jahan aapka code online safe rehta hai. Aur ise aasaan banane ke liye buttons-waali app hai **GitHub Desktop**. Aaj sab set karte hain."*

### 🎯 Today's goal
GitHub account banana, GitHub Desktop install karna, aur apna project online (push) karna — **buttons se (GitHub Desktop)** aur **command line se (`git push`)**, dono tareeke.

### 👨‍🏫 Concept — GitHub kya hai?
- **GitHub** = ek *website* jo aapke Git projects online store karti hai. Yahin recruiters dekhte hain — aapka GitHub aapka **portfolio** hai. (Is course ke saare projects yahin push honge.)
- **GitHub Desktop** = ek point-and-click app jisse aap commit aur push **buttons** se kar sakte ho (commands yaad rakhne ki zaroorat nahi).

### 👨‍🏫 Step 1 — GitHub account banao (free, 2 minute)
1. [github.com](https://github.com) par jao → **Sign up** dabao.
2. Apna **email**, ek **password**, aur ek **username** daalo. *(Username aapke profile URL ka hissa banta hai `github.com/<username>` — kuch professional choose karo, recruiters yeh dekhte hain.)*
3. GitHub email par ek code/link bhejega — verify karo, phir log in karo. Ho gaya — ab aapka GitHub account hai! 🎉

> **Wahi email yaad rakho** jo aapne Class 9 ke `git config` mein use kiya — taaki aapke commits aapke GitHub profile se link ho jaayein.

### 👨‍🏫 Step 2 — GitHub Desktop install karo
1. [desktop.github.com/download](https://desktop.github.com/download/) par jao → apne system ka installer download karo.
2. Install karke kholo → **"Sign in to GitHub.com"** dabao → browser mein apne account se log in karo → **Authorize** dabao.
3. Wapas aane par yeh aapka naam/email confirm karega — **Finish** dabao.

### 👨‍🏫 Step 3 — Apna project online daalo (push)
*"Ab buttons se kaam karenge — bilkul aasaan:"*
1. GitHub Desktop mein: **File → Add Local Repository** → apna `my_first_project` folder choose karo. *(Yeh wahi folder hai jahan aapne Class 9 mein `git init` kiya tha.)*
2. Agar koi change pending hai, neeche-left **Summary** box mein ek message likho (jaise `update`) → **Commit to main** dabao.
3. Upar **Publish repository** dabao → naam confirm karo → *(beginner ke liye **"Keep this code private"** ka tick hata sakte ho taaki recruiters dekh sakein)* → **Publish repository** dabao.
4. Bas! Browser mein `github.com/<aapka-username>/my_first_project` kholo — aapka code online aa gaya! 🎉

### 👨‍🏫 Step 4 — (Pro) Command line se `git push` karo
*"GitHub Desktop buttons aasaan hain, par job par engineers zyadatar **command line** se push karte hain. Chalo wahi tareeka bhi seekh lo — yeh wahi kaam karta hai jo upar wala 'Publish' button, bas commands se."*

> **Note:** Yeh **Step 3 ka alternative** hai. Agar aap GitHub Desktop se already publish kar chuke ho, toh ise dobara karne ki zaroorat nahi — ise apne agle project par try karna.

**Pehle GitHub website par ek khaali repo banao:**
1. [github.com](https://github.com) (logged in) → top-right **+** → **New repository**.
2. Ek **naam** do (jaise `my_first_project`), use **bilkul khaali rakho** (README ya .gitignore **add mat karo** — aapke local project mein pehle se hain), phir **Create repository** dabao.
3. Agle page par dikhaya gaya repo URL copy karo (aisa dikhta hai `https://github.com/<you>/<repo>.git`).

**Phir apne project folder ke andar yeh commands chalao** (URL apna paste karo):
```powershell
git remote add origin https://github.com/<you>/<repo>.git   # 1. GitHub repo ko local project se jodo
git branch -M main                                           # 2. apni branch ka naam "main" set karo
git push -u origin main                                      # 3. apne commits online upload karo
```

**Har command ka matlab:**
| Command | Yeh kya karta hai |
|---|---|
| `git remote add origin <url>` | Aapke local project ko GitHub repo se jodta hai (`origin` = us repo ka short naam) |
| `git branch -M main` | Branch ka naam `main` rakhta hai (GitHub yahi expect karta hai) |
| `git push -u origin main` | Aapke commits GitHub par bhejta hai. `-u` se agli baar sirf `git push` likhna kaafi hoga |

> **Pehli push par browser khulega — sign in karo:** GitHub command line par account password accept nahi karta, isliye ek browser window khul kar login + **Authorize** maangega. Yeh bilkul normal aur expected hai.

> **Security habit (bahut important):** push se **pehle** hamesha `git status` chalao aur confirm karo ki koi secret file (jaise `.env`, API keys) list mein **nahi** hai. Aise files ko `.gitignore` mein daalo taaki woh kabhi GitHub par na jaayein — leaked keys = surprise bills + data theft.

> **Aage badalne par (roz ka flow):** jab bhi code change karo →
> - **GitHub Desktop:** **Commit to main** → upar **Push origin**.
> - **Command line:** `git add .` → `git commit -m "message"` → `git push`.
> Dono ek hi kaam karte hain — apni pasand ka use karo.

### 🔗 Agentic link
*"Is course ka har project aap GitHub par push karoge. Mahine ke ant tak aapke paas ek bharaa-poora portfolio hoga jo aap interviews mein dikha sakte ho. Yeh ek student aur ek job-ready engineer ka farak hai."*

### ✍️ Homework
1. GitHub account banao aur apna profile URL note karo (`github.com/<username>`).
2. GitHub Desktop install karo aur sign in karo.
3. Apna `my_first_project` GitHub par publish karo, aur browser mein khol kar screenshot lo.
4. (Pro) Ek naya chhota project banao aur use **command line** se push karo: `git init` → `git add .` → `git commit -m "first commit"` → `git remote add origin <url>` → `git push -u origin main`.

### 🏁 Week 0 wrap-up
*"Chalo dekhte hain is week aapne kya ACHIEVE kiya:*
- *Programming & agent goal samjha (Class 1)*
- *Google Colab se bina install ke pehla code chalaya (Class 2)*
- *Python 3.15 + Cursor (AI editor) install kiya (Class 3)*
- *Terminal seekha (Class 4)*
- *Apna pehla `.py` program likha (Class 5)*
- *Jupyter Notebook (`.ipynb`) mein code + notes chalaya (Class 6)*
- *Errors se dosti ki (Class 7)*
- *`uv` se professional project + environment banaya (Class 8)*
- *Git se code ke save points banaye (Class 9)*
- *GitHub par apna code push kiya — GitHub Desktop aur `git push` dono se — online portfolio banaya (Class 10)*

*"Yaad rakho — aapke paas ab wahi setup hai jo ek asli AI engineer ke laptop par hota hai: Python, Cursor, uv, Git aur GitHub. Yeh ek bahut bada milestone hai. Next week se asli mazaa shuru — hum computer ko variables se cheezein YAAD karna sikhayenge. Shabaash, Monday ko milte hain!"*
