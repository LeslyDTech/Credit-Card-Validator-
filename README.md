# 💳 Credit Card Validator

A Python program that checks whether a credit card number is valid
using the Luhn Algorithm.

---

## How It Works

The program takes a card number, strips out dashes and spaces, reverses
it, then runs the Luhn Algorithm — adding odd position digits, doubling
even position digits, and checking if the total is divisible by 10.

---

## What I Learned

- How to use `.replace()` to clean up user input
- How string slicing works — `[::-1]` to reverse, `[::2]` to grab every other character
- How to loop through specific positions in a string using slice steps
- How the **modulus operator** `%` checks divisibility
- How a real algorithm (Luhn Algorithm) can be broken down into simple steps

---

## Usage

```bash
python credit_card_validator.py
```
