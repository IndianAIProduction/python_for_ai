# Python 3.15 — Operators (Quick Reference)

> **Reference only.** Yeh teaching material nahi hai — bas ek quick lookup table. Python ke **saare operators** neeche categories mein diye hain. Har table mein symbol, ek chhota example, aur short note hai. Precedence (kaun pehle chalta hai) sabse neeche diya hai.

---

## 1. Arithmetic Operators

Numbers pe maths. `a = 7`, `b = 2` maan lo.

| Operator | Naam | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `a + b` | `9` |
| `-` | Subtraction | `a - b` | `5` |
| `*` | Multiplication | `a * b` | `14` |
| `/` | True division (hamesha float) | `a / b` | `3.5` |
| `//` | Floor division (neeche round) | `a // b` | `3` |
| `%` | Modulus (remainder) | `a % b` | `1` |
| `**` | Exponent (power) | `a ** b` | `49` |

## 2. Comparison (Relational) Operators

Do values compare karke **`bool`** (`True`/`False`) dete hain.

| Operator | Naam | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `7 == 7` | `True` |
| `!=` | Not equal to | `7 != 2` | `True` |
| `>` | Greater than | `7 > 2` | `True` |
| `<` | Less than | `7 < 2` | `False` |
| `>=` | Greater than or equal | `7 >= 7` | `True` |
| `<=` | Less than or equal | `2 <= 7` | `True` |

> **Chaining allowed:** `0 < x < 10` bilkul valid hai (Python ka feature).

## 3. Logical (Boolean) Operators

Boolean expressions ko jodte/ulate hain. **Short-circuit** karte hain.

| Operator | Naam | Example | Result |
|----------|------|---------|--------|
| `and` | Dono True? | `True and False` | `False` |
| `or` | Koi ek True? | `True or False` | `True` |
| `not` | Ulta karo | `not True` | `False` |

> **Short-circuit:** `and` mein pehla `False` mila toh ruk jaata hai; `or` mein pehla `True` mila toh ruk jaata hai.

## 4. Assignment Operator

| Operator | Naam | Example | Note |
|----------|------|---------|------|
| `=` | Assign (naam ko value se bind karo) | `x = 10` | `==` (compare) se alag hai! |

## 5. Augmented Assignment Operators

"Kaam karke wapas usi variable mein rakho" ka shortcut. `x op= y` ka matlab `x = x op y`.

| Operator | Matlab | Example (`x = 10`) | Baad mein `x` |
|----------|--------|--------------------|----------------|
| `+=` | `x = x + y` | `x += 3` | `13` |
| `-=` | `x = x - y` | `x -= 3` | `7` |
| `*=` | `x = x * y` | `x *= 3` | `30` |
| `/=` | `x = x / y` | `x /= 4` | `2.5` |
| `//=` | `x = x // y` | `x //= 3` | `3` |
| `%=` | `x = x % y` | `x %= 3` | `1` |
| `**=` | `x = x ** y` | `x **= 2` | `100` |
| `&=` | bitwise AND assign | `x &= 6` | `2` |
| `\|=` | bitwise OR assign | `x \|= 1` | `11` |
| `^=` | bitwise XOR assign | `x ^= 3` | `9` |
| `>>=` | right shift assign | `x >>= 1` | `5` |
| `<<=` | left shift assign | `x <<= 1` | `20` |
| `@=` | matrix multiply assign | `M @= N` | (NumPy arrays) |

## 6. Bitwise Operators

`int` ke binary bits pe kaam. `a = 6` (`0b110`), `b = 3` (`0b011`).

| Operator | Naam | Example | Result |
|----------|------|---------|--------|
| `&` | AND (dono bits 1) | `a & b` | `2` (`0b010`) |
| `\|` | OR (koi ek bit 1) | `a \| b` | `7` (`0b111`) |
| `^` | XOR (bits alag) | `a ^ b` | `5` (`0b101`) |
| `~` | NOT (bits ulte) | `~a` | `-7` |
| `<<` | Left shift (×2 per bit) | `a << 1` | `12` |
| `>>` | Right shift (÷2 per bit) | `a >> 1` | `3` |

> **Note:** yahi `&` `\|` `^` symbols **sets** (Week 4) aur **type unions** (`str \| None`, Week 11) mein bhi aate hain — context alag hai.

## 7. Membership Operators

Kisi sequence/collection mein value hai ya nahi.

| Operator | Naam | Example | Result |
|----------|------|---------|--------|
| `in` | Andar hai? | `"a" in "cat"` | `True` |
| `not in` | Andar nahi hai? | `5 not in [1, 2, 3]` | `True` |

## 8. Identity Operators

Do naam **exact same object** (same memory) hain ya nahi. Value compare NAHI karta.

| Operator | Naam | Example | Note |
|----------|------|---------|------|
| `is` | Same object? | `x is None` | Sirf `None` jaise singletons ke liye use karo |
| `is not` | Alag object? | `x is not None` | `==` value compare karta, `is` identity |

## 9. Conditional Expression (Ternary)

Ek line ka `if/else` jo ek **value** deta hai.

| Form | Example | Result |
|------|---------|--------|
| `a if cond else b` | `"Even" if n % 2 == 0 else "Odd"` | condition pe depend |

## 10. Matrix Multiplication Operator

| Operator | Naam | Example | Note |
|----------|------|---------|------|
| `@` | Matrix / dot product | `a @ b` | NumPy arrays ke liye (Week 14). Plain Python mein nahi. |

## 11. Walrus Operator (Assignment Expression)

Expression ke andar hi variable assign kar deta hai.

| Operator | Naam | Example | Note |
|----------|------|---------|------|
| `:=` | Walrus / assign-expression | `while (line := f.readline()):` | Assign + use ek saath |

---

## Operator Precedence (kaun pehle chalta hai)

Upar wale ka precedence zyada — pehle chalega. Same row = left-to-right (except `**`).

| Level | Operators |
|-------|-----------|
| Highest | `()` grouping |
| | `**` (power) — right-to-left |
| | `~` `+` `-` (unary / sign) |
| | `*` `/` `//` `%` `@` |
| | `+` `-` (binary add/sub) |
| | `<<` `>>` (shifts) |
| | `&` (bitwise AND) |
| | `^` (bitwise XOR) |
| | `\|` (bitwise OR) |
| | `==` `!=` `<` `>` `<=` `>=` `is` `is not` `in` `not in` (comparisons) |
| | `not` |
| | `and` |
| | `or` |
| | `if … else` (ternary) |
| Lowest | `:=` (walrus), `=` and augmented assignments |

> **Rule of thumb:** confusion ho toh **brackets `()`** laga do — code readable rehta hai aur bug nahi aata.

```python
print(2 + 3 * 4)        # 14  (* pehle)
print((2 + 3) * 4)      # 20  (brackets ne order badla)
print(2 ** 3 ** 2)      # 512 (** right-to-left: 2 ** 9)
```

---

## Course scope (kya padhaya, kya nahi)

| Category | Course mein? | Kahan |
|----------|--------------|-------|
| Arithmetic `+ - * / // % **` | ✅ | Week 1 (Class 12) |
| Comparison `== != < > <= >=` | ✅ | Week 1 (Class 14) |
| Logical `and or not` | ✅ | Week 1 (Class 14) |
| Assignment `=` | ✅ | Week 1 |
| Ternary `a if c else b` | ✅ | Week 2 (Class 17) |
| Membership `in` / `not in` | ✅ | Week 2 & 4 |
| Identity `is` / `is not` | ✅ | Week 4 (Class 29) |
| Set operators `\| & - ^` | ✅ (sets ke roop mein) | Week 4 (Class 28) |
| Type-union `\|` | ✅ | Week 11 |
| Matrix `@` | ✅ (NumPy) | Week 14 |
| Augmented assignment (poora set) | ⚠️ sirf `+=` chhua | Week 3 (aside) |
| Bitwise `& \| ^ ~ << >>` (ints pe) | ❌ (reference only) | — |
| Walrus `:=` | ❌ (reference only) | — |

*AI-agent focused beginner course ke liye upar wale ✅ operators kaafi hain. Bitwise aur walrus sirf reference ke liye diye gaye hain — advanced/optional.*
