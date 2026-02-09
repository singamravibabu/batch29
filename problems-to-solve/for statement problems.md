# Python — `for` Loop Practice

### 🔍 Important learning objective for your students

For each problem, force this thinking pattern:

> What exactly is changing every iteration?

and

> What information must I carry from the previous iteration?

That is the real mental model of the `for` loop.

---

- Use only `for` loops (no `while`, no recursion unless stated).
- Avoid built-in shortcuts like `sum()`, `max()`, `min()` unless allowed.

---

## 1️⃣ Sum of only even numbers in a range

Input two integers `start` and `end`.

Find the **sum of all even numbers** between them (inclusive).

---

## 2️⃣ Count how many numbers are divisible by both 3 and 5

Input a number `n`.

From `1` to `n`, count how many numbers are divisible by **both 3 and 5**.

---

## 3️⃣ Reverse a number using only a for loop

Input an integer.

Reverse the number using a `for` loop.

(Hint: first find how many digits, then loop.)

---

## 4️⃣ Find factorial — but skip one number

Input a number `n` and another number `k`.

Compute:

```
n!  but skip multiplying k
```

Example:

```
n = 5, k = 3
Result = 5 × 4 × 2 × 1
```

---

## 5️⃣ Count digits that are odd in a number

Input an integer.

Count how many digits inside it are **odd digits**.

---

## 6️⃣ Find the largest digit in a number

Input a number.

Find the largest digit using a `for` loop only.

(No max(), no converting to list)

---

## 7️⃣ Pattern – centered number pyramid

Input `n`.

Print:

```
   1
  123
 12345
```

(for n = 3)

Use nested `for` loops.

---

## 8️⃣ Check if a number is a perfect number

A number is perfect if:

sum of its proper divisors = the number.

Input `n`.

Use a `for` loop to test and print Yes or No.

---

## 9️⃣ Sum of prime numbers in a range

Input two numbers `a` and `b`.

Find the **sum of all prime numbers** between them.

(You must use nested `for` loops.)

---

## 🔟 Count how many times a character appears

Input a string and a character.

Count how many times the character appears using a `for` loop.

---

## 1️⃣1️⃣ Find first number divisible by 7 and 11 in a range

Input `start` and `end`.

Find and print the **first** number divisible by both 7 and 11.

Stop the loop once found.

---

## 1️⃣2️⃣ Check if a string is a palindrome using a for loop

Input a string.

Check palindrome by comparing characters using a loop.

(No slicing trick allowed.)

---

## 1️⃣3️⃣ Find the sum of digits at even positions

Input a number.

Count positions from the **right side**.

Add only digits at even positions.

Example:

```
Number: 57294
Positions from right: 1 2 3 4 5
Pick position 2 and 4
```

---

## 1️⃣4️⃣ Generate first n Fibonacci numbers

Input `n`.

Print the first `n` Fibonacci numbers using a `for` loop.

---

## 1️⃣5️⃣ Find the second largest number in a list

Input a list of numbers.

Find the **second largest value** using a single `for` loop.

(No sorting, no max twice.)

---

## 1️⃣6️⃣ Count how many words start with a vowel

Input a sentence.

Split it and use a `for` loop.

Count how many words start with:

```
a e i o u (case insensitive)
```

---

## 1️⃣7️⃣ Find all pairs whose sum is a target

Input:

* a list of numbers
* a target sum

Print all unique pairs whose sum equals the target.

Use nested `for` loops.

---

## 1️⃣8️⃣ Check if a number is an Armstrong number

Input a number.

An Armstrong number:

Sum of each digit raised to power of number of digits equals the number.

You must use a `for` loop.

---

## 1️⃣9️⃣ Create a frequency table of characters

Input a string.

Print each character and how many times it appears.

(You may use a dictionary, but counting must be done using a `for` loop.)

---

## 2️⃣0️⃣ Logical challenge – longest consecutive increasing sequence

Input a list of numbers.

Find the length of the **longest continuous increasing sequence**.

Example:

```
[1, 2, 3, 1, 2, 3, 4, 0]
Answer = 4
```

Use only a single `for` loop.

