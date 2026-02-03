# Python – `if` Statement Practice

---

### Tips for solving

While solving, force yourself to think in this order:

1. What condition must be checked first?
2. Which conditions depend on previous checks?
3. Which cases must never overlap?

Do **not** use loops or functions unless stated.

---

## 1️⃣ Pass, Fail or Distinction

Input a student’s mark.

Rules:

* 75 and above → `"Distinction"`
* 50 to 74 → `"Pass"`
* Below 50 → `"Fail"`

👉 Print the result.

---

## 2️⃣ Positive, Negative or Zero — but also Even or Odd

Input a number.

If the number is zero → print `"Zero"`

Otherwise:

* Print whether it is **positive or negative**
* AND whether it is **even or odd**

Example output:

```
Positive and Even
```

---

## 3️⃣ Can the person vote and contest an election?

Input age.

Rules:

* Age ≥ 18 → can vote
* Age ≥ 25 → can contest

Print one of:

* `"Can vote and contest"`
* `"Can vote only"`
* `"Cannot vote"`

---

## 4️⃣ Find the largest of three numbers (no max() allowed)

Input three numbers.

Print the largest.

You must use only `if` statements.

---

## 5️⃣ Salary bonus system

Input salary and years of experience.

Rules:

* If experience ≥ 10 and salary < 50000 → bonus 20%
* If experience ≥ 5 → bonus 10%
* Otherwise → bonus 5%

Print the bonus amount.

---

## 6️⃣ Valid triangle or not

Input three sides.

A triangle is valid if:

```
a + b > c
a + c > b
b + c > a
```

Print `"Valid triangle"` or `"Invalid triangle"`.

---

## 7️⃣ Check leap year (correct rules)

Input a year.

Rules:

* Divisible by 400 → leap year
* Divisible by 100 → not leap year
* Divisible by 4 → leap year
* Else → not leap year

---

## 8️⃣ Online exam eligibility

Input:

* attendance percentage
* medical certificate (`yes` or `no`)

Rules:

* If attendance ≥ 75 → eligible
* If attendance < 75 but medical = yes → eligible
* Otherwise → not eligible

---

## 9️⃣ Electricity bill slab

Input number of units.

Rules:

* First 100 units → ₹1 per unit
* Next 100 units → ₹2 per unit
* Remaining units → ₹5 per unit

Calculate and print the bill.

Use only `if` (no loops).

---

## 🔟 Check if a number is a 3-digit number AND divisible by 5

Input a number.

Print `"Yes"` or `"No"`.

(3-digit means from 100 to 999 or -100 to -999)

---

## 1️⃣1️⃣ Login system (simple)

Input:

* username
* password

Rules:

* If username is `"admin"` and password is `"1234"` → `"Login successful"`
* If username is correct but password wrong → `"Wrong password"`
* Else → `"Invalid user"`

---

## 1️⃣2️⃣ Find the middle number among three numbers

Input three numbers.

Print the number which is **neither smallest nor largest**.

Example:

```
Input: 4 9 6
Output: 6
```

(No sorting allowed)

---

## 1️⃣3️⃣ Character classification

Input a single character.

Print whether it is:

* uppercase letter
* lowercase letter
* digit
* special character

Use comparisons only (`'a' <= ch <= 'z'` style).

---

## 1️⃣4️⃣ Discount logic with priority

Input total bill amount.

Rules:

* If bill ≥ 5000 → 30% discount
* Else if bill ≥ 3000 → 20%
* Else if bill ≥ 1000 → 10%
* Else → no discount

Print final payable amount.

---

## 1️⃣5️⃣ Driving license rule

Input:

* age
* eyesight test result (`pass` or `fail`)

Rules:

* age ≥ 18 AND eyesight = pass → eligible
* Otherwise → not eligible

---

## 1️⃣6️⃣ Grade with plus levels

Input marks.

Rules:

* 90–100 → A+
* 80–89 → A
* 70–79 → B
* 60–69 → C
* Below 60 → F

Make sure 100 is handled properly.

---

## 1️⃣7️⃣ Smart door system

Input:

* is_face_recognized (`yes` / `no`)
* is_pin_correct (`yes` / `no`)

Rules:

* If both yes → `"Door opened"`
* If face recognized but pin wrong → `"Enter correct PIN"`
* If face not recognized but pin correct → `"Face verification required"`
* Else → `"Access denied"`

---

## 1️⃣8️⃣ Check if a point lies on X-axis, Y-axis or origin

Input x and y.

Print one of:

* `"Origin"`
* `"On X-axis"`
* `"On Y-axis"`
* `"Neither"`

---

## 1️⃣9️⃣ Determine triangle type

First check if it is a valid triangle.

Then print:

* `"Equilateral"`
* `"Isosceles"`
* `"Scalene"`

---

## 2️⃣0️⃣ Scholarship decision (logical challenge)

Input:

* marks
* family_income
* sports_certificate (`yes` / `no`)

Rules:

A student gets scholarship if:

* marks ≥ 85 and income ≤ 300000
  OR
* sports_certificate is yes and marks ≥ 70

Print `"Scholarship approved"` or `"Not approved"`.
